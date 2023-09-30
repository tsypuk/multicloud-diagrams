import json
import xml.etree.ElementTree as Et
import logging
import os.path
import pkgutil
import re
import yaml
import hashlib


def update_style_by_key(style_str: str, key: str, value: str):
    pattern = r'{}=([^;]+)'.format(key)
    if re.search(pattern, style_str) is None:
        return f"{style_str}{key}={value};"
    else:
        return re.sub(pattern, f'{key}={value}', style_str)


def customize(node_template: dict, style: dict = None):
    for (key, value) in style.items():
        node_template['style'] = update_style_by_key(style_str=node_template['style'], key=key, value=value)


def stringify_dict(metadata: dict) -> str:
    if metadata:
        # return '<BR>-----------<BR>' + '<BR>'.join([f'<b>{k.capitalize()}</b>: {v}' for k, v in metadata.items()])
        return '<BR>'.join([f'<b>{k}</b>: {v}' for k, v in metadata.items()])
    else:
        return ''


def build_vertex_id(vertex_details, edge, src_dst_marker: str):
    resource = {}
    if f'{src_dst_marker}_id' in edge:
        resource["type"] = edge[f"{src_dst_marker}_type"]
        resource["id"] = edge[f'{src_dst_marker}_id']
    elif src_dst_marker in edge:
        resource = [vertex for vertex in vertex_details if vertex['name'] == edge[src_dst_marker]][0]
    return f'{resource["type"]}:{resource["id"]}'


def stringify_labels(labels: []) -> str:
    if len(labels) > 0:
        return '<BR>'.join([f'{k}' for k in labels])
    else:
        return ''


class Distribution:
    algorithm: str
    element_width: int
    element_height: int
    vertical_spacing: int = 5
    horizontal_spacing: int = 5
    start_x: int = 0
    start_y: int = 0
    columns: int = 1


def starts_with_any(string, actors, participants):
    if any(string.startswith(prefix) for prefix in actors):
        return 'actor'
    elif any(string.startswith(prefix) for prefix in participants):
        return 'participant'


def generate_hash(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()[:8]


def extract_actors_and_participants(sequence_diagram):
    actors = []
    participants = []
    lines = sequence_diagram.split('\n')
    for line in lines:
        strip = line.strip()
        if strip.startswith('actor'):
            entity = line.strip().split()[1]
            actors.append(entity)
        elif strip.startswith('participant'):
            entity = line.strip().split()[1]
            participants.append(entity)
    return actors, participants


# [Actor][Arrow][Actor]:Message text

# Type	Description
# ->	Solid line without arrow
# -->	Dotted line without arrow
# ->>	Solid line with arrowhead
# -->>	Dotted line with arrowhead
# -x	Solid line with a cross at the end
# --x	Dotted line with a cross at the end.
# -)	Solid line with an open arrow at the end (async)
# --)	Dotted line with a open arrow at the end (async)
def extract_info(input_string):
    pattern = r'(.*?)(?:-->|->>)(.*?):(.*)'
    match = re.match(pattern, input_string)

    if match:
        actor1 = match.group(1).strip()
        actor2 = match.group(2).strip()
        message = match.group(3).lstrip()
        return actor1, actor2, message
    else:
        return None


class MultiCloudDiagrams:
    def __init__(self, debug_mode=False, shadow=True, layer_name=''):
        self.actors_to_nodes = {}
        self.mx_file = Et.Element('mxfile',
                                  host="multicloud-diagrams",
                                  agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.",
                                  type="MultiCloud")

        diagram = Et.SubElement(self.mx_file, 'diagram', id="diagram_1", name="AWS components")
        mx_graph_model = Et.SubElement(diagram, 'mxGraphModel', dx="1015", dy="661", grid="1", gridSize="10",
                                       guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                       pageScale="1", pageWidth="850", pageHeight="1100", math="0")
        if shadow:
            mx_graph_model.attrib['shadow'] = '1'
        else:
            mx_graph_model.attrib['shadow'] = '0'

        self.root = Et.SubElement(mx_graph_model, 'root')

        self.layers = {}
        Et.SubElement(self.root, 'mxCell', id="0")
        self.add_layer(layer_name)

        self.debug_mode = debug_mode

    def add_layer(self, layer_name: str = ''):
        if self.get_layer_id_by_name(layer_name) is None:
            self.layers[self.get_current_layer_count() + 1] = layer_name
            layer_cell = Et.SubElement(self.root, 'mxCell', id=f"{self.get_current_layer_count()}", parent="0")
            if layer_name != '':
                layer_cell.attrib['value'] = layer_name

    def get_current_layer_count(self):
        return len(self.layers)

    def get_layer_id_by_name(self, layer_name):
        for key, val in self.layers.items():
            if val == layer_name:
                return key
        return None

    def get_layer_id(self, layer_name=None, layer_id=None):
        if layer_name is not None:
            layer_id = self.get_layer_id_by_name(layer_name)
            if layer_id is not None:
                return layer_id
            else:
                raise AttributeError(f'Layer name: {layer_name} not exist')
        elif layer_id is not None:
            # check
            current_layers = self.get_current_layer_count()
            if layer_id > current_layers:
                raise AttributeError(f'Layer ID: {layer_id} more than current layers ({current_layers})')
            return layer_id
        else:
            return 1

    prev_coords = {}

    supported_vertex = {}
    provider_services = {}

    def assemble_node_name(self, node_name, node_id, metadata, node_type):
        metadata = f"<BR>-----------<BR>{stringify_dict(metadata)}" if metadata else ""
        identifier = 'ID'
        if 'aws' == self.get_provider_by_service_name(node_type):
            identifier = 'ARN'
        return f'<b>Name</b>: {node_name}<BR><b>{identifier}</b>: {node_id}{metadata}'

    def get_provider_by_service_name(self, node_type) -> str:
        for provider, value in self.provider_services.items():
            if node_type in value:
                return provider
        return 'fallback'

    # Load supported vertexes for registered Cloud Providers
    providers = ['aws', 'azure', 'gcp', 'onprem', 'fallback', 'core']
    for provider in providers:
        path = pkgutil.get_data(__package__, f'providers/{provider}.json')
        json_data = json.loads(path.decode("utf-8"))
        supported_vertex.update(json_data)
        provider_services[provider] = list(json_data.keys())

    def get_node_template(self, node_type: str) -> dict:
        if node_type in self.supported_vertex:
            return self.supported_vertex[node_type].copy()
        else:
            logging.warning(
                f'No such nodeType: {node_type} in the Library (using default fallback icon Info). Please contact maintainer to add it, or provide MergeRequest')
            return self.supported_vertex['fallback_vertex'].copy()

    def add_snapshot(self, table_id='', table_name='', style: dict = None, snapshot: str = '', width=300):
        if not table_id:
            table_id = table_name
        self.prepare_table(table_id=table_id, table_name=table_name, style=style, rows_count=1, width=width)
        self.prepare_row(1, snapshot, table_id, width)

    def create_table(self, rows, table_id='', table_name='', style: dict = None, width=300, layer_name: str = None, layer_id: str = None,
                     x: int = None, y: int = None):
        parent_id = str(self.get_layer_id(layer_name, layer_id))
        if not table_id:
            table_id = table_name
        self.prepare_table(table_id=table_id, table_name=table_name, style=style, rows_count=len(rows),
                           width=width, parent_id=parent_id, x=x, y=y)

        y = 0
        for index, item in enumerate(rows):
            y = y + 30
            self.prepare_row(index, item, table_id, width, y=y)

    def add_map(self, table_id='', table_name='', style: dict = None, key_value_pairs: dict = None, width=300, layer_name: str = None, layer_id: str = None,
                x: int = None, y: int = None):
        rows = []
        if key_value_pairs is not None:
            rows = [f'<b>{name}</b>: {value}' for name, value in key_value_pairs.items()]
        self.create_table(rows=rows, table_id=table_id, table_name=table_name, style=style, width=width, layer_name=layer_name, layer_id=layer_id,
                          x=x, y=y)

    # add_table
    def add_list(self, table_id='', table_name='', style: dict = None, rows=None, width=300, layer_name: str = None, layer_id: str = None,
                 x: int = None, y: int = None):
        if rows is None:
            rows = []
        self.create_table(rows=rows, table_id=table_id, table_name=table_name, style=style, width=width, layer_name=layer_name, layer_id=layer_id,
                          x=x, y=y)

    def prepare_row(self, index, snapshot, table_id='', width=300, y=30):
        mx_cell = Et.SubElement(self.root,
                                'mxCell',
                                id=f'vertex:{table_id}:row:{index}',
                                value=snapshot,
                                style=self.get_node_template('row')['style'],
                                parent=f'vertex:{table_id}:list',
                                vertex="1")

        mx_geometry = Et.SubElement(mx_cell, 'mxGeometry', width=str(width), height="30", y=str(y))
        mx_geometry.set('as', 'geometry')
        # Position Vertex based on X,Y cords
        self.update_vertex_coords_width_height_from_prev_version(mx_geometry, f'vertex:{table_id}:row:{index}')

    def prepare_table(self, table_id='', table_name='', style: dict = None, rows_count=0, width=300, parent_id: str = "1",
                      x: int = None, y: int = None):

        if style is None:
            style = {}

        node_template = self.get_node_template('list')

        # Customization
        customize(node_template=node_template, style=style)

        mx_cell = Et.SubElement(self.root,
                                'mxCell',
                                id=f'vertex:{table_id}:list',
                                value=f'<b>{table_name}</b>',
                                style=f"{node_template['style']}",
                                parent=parent_id,
                                vertex="1")

        mx_geometry = Et.SubElement(mx_cell, 'mxGeometry', width=str(width),
                                    height=str(30 * (1 + rows_count)))
        mx_geometry.set('as', 'geometry')

        # X,Y were passed
        if x:
            mx_geometry.set('x', str(x))
        if y:
            mx_geometry.set('y', str(y))

        # Position Vertex based on X,Y cords
        self.update_vertex_coords_width_height_from_prev_version(mx_geometry, f'vertex:{table_id}:list')

    def add_vertex(self, node_id: str, node_name: str, metadata: dict = None, node_type: str = '', layer_name: str = None, layer_id: str = None, style: dict = None,
                   x: int = None, y: int = None) -> str:
        if metadata is None:
            metadata = {}
        if style is None:
            style = {}
        # check that there is no such vertex already
        exist = False
        for mx_cell in self.root:
            # print(mxCell.attrib['id'])
            if mx_cell.attrib['id'] == f'vertex:{node_type}:{node_id}':
                logging.warning(f'Already exists: vertex:{node_type}:{node_id} name:{node_name}')
                exist = True
                break

        if not exist:
            node_template = self.get_node_template(node_type)

            # Customization
            customize(node_template=node_template, style=style)

            parent_id = str(self.get_layer_id(layer_name, layer_id))
            mx_cell = Et.SubElement(self.root,
                                    'mxCell',
                                    id=f'vertex:{node_type}:{node_id}',
                                    value=self.assemble_node_name(node_name, node_id, metadata, node_type),
                                    style=f"{node_template['style']}",
                                    parent=parent_id,
                                    vertex="1")
            if self.debug_mode:
                mx_cell.insert(0, Et.Comment(f'vertex:{node_name}'))
            mx_geometry = Et.SubElement(mx_cell, 'mxGeometry', width=node_template['width'],
                                        height=node_template['height'])
            mx_geometry.set('as', 'geometry')

            # Position Vertex based on X,Y cords
            self.update_vertex_coords_width_height_from_prev_version(mx_geometry, f'vertex:{node_type}:{node_id}')

            # X,Y were passed
            if x:
                mx_geometry.set('x', str(x))
            if y:
                mx_geometry.set('y', str(y))
        return f'{node_type}:{node_id}'

    def update_vertex_coords_width_height_from_prev_version(self, mx_geometry, vertex_id):
        self.update_vertex_coords_from_prev_version(mx_geometry, vertex_id)
        if vertex_id in self.prev_coords:
            if 'height' in self.prev_coords[vertex_id]:
                mx_geometry.set('height', self.prev_coords[vertex_id]['height'])
            if 'width' in self.prev_coords[vertex_id]:
                mx_geometry.set('width', self.prev_coords[vertex_id]['width'])

    def update_vertex_coords_from_prev_version(self, mx_geometry, vertex_id):
        if vertex_id in self.prev_coords:
            if 'x' in self.prev_coords[vertex_id]:
                mx_geometry.set('x', self.prev_coords[vertex_id]['x'])
            if 'y' in self.prev_coords[vertex_id]:
                mx_geometry.set('y', self.prev_coords[vertex_id]['y'])

    def add_vertex_list(self, vertexes, distribution: Distribution = None):
        algo = getattr(distribution, 'algorithm', None)
        if 'Table' == algo:
            if distribution.algorithm == 'Table':
                r = (len(vertexes) + distribution.columns - 1) // distribution.columns
                current_row = 0
                current_column = 0

                for index, vertex in enumerate(vertexes):
                    row_index = current_row % r
                    column_index = current_column % distribution.columns
                    x_position = column_index * distribution.element_width + distribution.start_x
                    y_position = row_index * distribution.element_height + distribution.start_y
                    vertex['x'] = x_position
                    vertex['y'] = y_position
                    self.add_vertex(**vertex)

                    current_column += 1
                    if current_column >= distribution.columns:
                        current_column = 0
                        current_row += 1
        elif algo is None:
            for vertex in vertexes:
                self.add_vertex(**vertex)

    def add_connection(self, src_node_id, dst_node_id, edge_style=None, labels=None, label_style=None, layer_name=None, layer_id=None, prefix=None):
        if labels is None:
            labels = []
        if edge_style is None:
            edge_style = {}
        if label_style is None:
            label_style = {}

        # Check that both source and destination exist, before creating edge
        found = 0
        for mx_cell in self.root:
            # print(mxCell.attrib['id'])
            if mx_cell.attrib['id'] == f'vertex:{src_node_id}':
                found += 1
            if mx_cell.attrib['id'] == f'vertex:{dst_node_id}':
                found += 1
            if found == 2:
                break

        edge_id = f'edge:{src_node_id}:to:{dst_node_id}'
        label_id = f'label:{src_node_id}:to:{dst_node_id}'
        parent_edge_id = f'edge:{src_node_id}:to:{dst_node_id}'

        if prefix is not None:
            edge_id = f'edge_{prefix}:{src_node_id}:to:{dst_node_id}'
            label_id = f'label_{prefix}:{src_node_id}:to:{dst_node_id}'
            parent_edge_id = f'edge_{prefix}:{src_node_id}:to:{dst_node_id}'

        if found == 2:
            # check that Edge does not exist
            edge_exist = False
            for mx_cell in self.root:
                if mx_cell.attrib['id'] == edge_id:
                    edge_exist = True
                    # update the labels
                    for mxLabel in self.root:
                        if mxLabel.attrib['id'] == f'label_{prefix}:{src_node_id}:to:{dst_node_id}':
                            if 'value' in mxLabel.attrib:

                                for label in labels:
                                    old_label = mxLabel.attrib['value']
                                    if label in old_label:
                                        print('skip label exists')
                                    else:
                                        mxLabel.attrib['value'] = old_label + '<BR><BR>' + stringify_labels([label])

                                break
                    break
            if not edge_exist:
                node_template = self.get_node_template('edge')
                customize(node_template=node_template, style=edge_style)

                parent_id = str(self.get_layer_id(layer_name, layer_id))
                mx_cell = Et.SubElement(self.root,
                                        'mxCell',
                                        id=edge_id,
                                        style=node_template['style'],
                                        parent=parent_id,
                                        source=f'vertex:{src_node_id}',
                                        target=f'vertex:{dst_node_id}',
                                        edge="2")

                if self.debug_mode:
                    mx_cell.insert(0, Et.Comment(f'edge:{src_node_id}:to:{dst_node_id}'))
                mx_geometry = Et.SubElement(mx_cell, 'mxGeometry')
                mx_geometry.set('as', 'geometry')

                # Add label to edge
                if len(labels) > 0:
                    node_template = self.get_node_template('label')
                    customize(node_template=node_template, style=label_style)
                    mx_cell = Et.SubElement(self.root,
                                            'mxCell',
                                            id=label_id,
                                            value=stringify_labels(labels),
                                            style=node_template['style'],
                                            parent=parent_edge_id,
                                            vertex="1",
                                            connectable="0")
                    # <mxGeometry relative="1" as="geometry">
                    mx_geometry = Et.SubElement(mx_cell,
                                                'mxGeometry',
                                                relative="1"
                                                )
                    mx_geometry.set('as', 'geometry')
                    # <mxPoint as="offset"/>
                    mx_geometry = Et.SubElement(mx_geometry, 'mxPoint')
                    mx_geometry.set('as', 'offset')

                    self.update_vertex_coords_from_prev_version(mx_geometry, f'label:{src_node_id}:to:{dst_node_id}')

                    # </mxGeometry>
                    # </mxCell>
            else:
                logging.warning(
                    f'Already exist edge:{src_node_id}:to:{dst_node_id}')
        else:
            logging.error(
                f'Not both vertexes present to build Edge between them (expected vertex:{src_node_id} & vertex:{dst_node_id})')

    def add_link(self, src_node_id, dst_node_id, action=None, layer_name=None, layer_id=None):

        style = {
            'startArrow': 'none',
            'endArrow': 'none'
        }
        self.add_connection(src_node_id=src_node_id, dst_node_id=dst_node_id, labels=action, edge_style=style, layer_name=layer_name, layer_id=layer_id)

    def add_link_uml(self, src_node_id, dst_node_id, action=None, layer_name=None, layer_id=None, edge_style=None, label_style=None):
        self.add_connection(src_node_id=src_node_id, dst_node_id=dst_node_id, labels=action, edge_style=edge_style, label_style=label_style, layer_name=layer_name, layer_id=layer_id,
                            prefix=layer_name)

    def add_bidirectional_link(self, src_node_id, dst_node_id, action=None):
        style = {
            'startArrow': 'classic',
            'endArrow': 'classic'
        }
        self.add_connection(src_node_id=src_node_id, dst_node_id=dst_node_id, edge_style=style, labels=action)

    def add_unidirectional_link(self, src_node_id, dst_node_id, action=None):
        style = {
            'startArrow': 'none',
            'endArrow': 'classic'
        }
        self.add_connection(src_node_id=src_node_id, dst_node_id=dst_node_id, edge_style=style, labels=action)

    def add_unidirectional_reverse_link(self, src_node_id, dst_node_id, action=None):
        style = {
            'startArrow': 'classic',
            'endArrow': 'none'
        }
        self.add_connection(src_node_id=src_node_id, dst_node_id=dst_node_id, edge_style=style, labels=action)

    def add_link_list(self, links):
        for link in links:
            self.add_link(src_node_id=link['sourceNodeID'], dst_node_id=link['destinationNodeID'])
        return

    def augment_from_yaml(self, yaml_name: str):
        with open(yaml_name, 'r') as file:
            data = yaml.safe_load(file)
            for vertex in data['vertices']:
                self.add_vertex(
                    node_id=vertex['id'],
                    node_name=vertex['name'],
                    node_type=vertex['type'],
                )
            for edge in data['edges']:
                self.add_link(
                    src_node_id=build_vertex_id(data['vertices'], edge, 'src'),
                    dst_node_id=build_vertex_id(data['vertices'], edge, 'dst'),
                    action=[edge['label']]
                )

    def read_nodes_from_file(self, file_name: str):
        print(file_name)
        if os.path.isfile(file_name):
            tree = Et.parse(file_name)
            root = tree.getroot()
            self.root = tree.findall("./*/*/")[0]
            self.mx_file = root

            # Layers
            mx_cells = tree.findall("./*/*/*/")
            for layer in mx_cells:
                if ('parent' in layer.attrib) and layer.attrib['parent'].isdigit() and (int(layer.attrib['parent']) == 0):
                    layer_id = int(layer.attrib['id'])
                    if layer_id > 1:
                        self.layers[layer_id] = layer.attrib['value']

    def read_coords_from_file(self, file_name: str):
        if os.path.isfile(file_name):
            tree = Et.parse(file_name)
            root = tree.getroot()

            for neighbor in root.iter('mxCell'):
                if neighbor.get('id').startswith("vertex:"):
                    data = neighbor.find('mxGeometry')
                    cords = {}
                    if data.get('x') is not None:
                        cords['x'] = data.get('x')
                    if data.get('y') is not None:
                        cords['y'] = data.get('y')
                    if data.get('height') is not None:
                        cords['height'] = data.get('height')
                    if data.get('width') is not None:
                        cords['width'] = data.get('width')
                    self.prev_coords[neighbor.get('id')] = cords

                elif neighbor.get('id').startswith("label:"):
                    data = neighbor.find('mxGeometry')
                    mx_point = data.find('mxPoint')
                    cords = {}
                    if mx_point.get('x') is not None:
                        cords['x'] = mx_point.get('x')
                    if mx_point.get('y') is not None:
                        cords['y'] = mx_point.get('y')
                    self.prev_coords[neighbor.get('id')] = cords

    def dump(self):
        from xml.dom import minidom
        rough_string = Et.tostring(self.mx_file, 'utf-8')
        parsed = minidom.parseString(rough_string)
        print(parsed.toprettyxml(indent="  "))

    def export_to_file(self, file_path):
        # tree = Et.ElementTree(self.mx_file)
        # removed for older Python versions compatibility
        # Et.indent(tree, space="\t", level=0)
        # tree.write(file, encoding='utf-8')
        # Convert ElementTree to string
        xml_string = Et.tostring(self.mx_file, encoding='utf-8')

        # Parse the XML string and prettify with indentation
        import xml.dom.minidom
        parsed = xml.dom.minidom.parseString(xml_string)
        pretty_xml = parsed.toprettyxml(indent="\t")

        # Remove the first line containing the XML declaration
        pretty_lines = pretty_xml.splitlines()
        if pretty_lines and '<?xml' in pretty_lines[0].strip():
            pretty_lines.pop(0)
        non_empty_lines = [line for line in pretty_lines if line.strip()]
        resulting_xml = '\n'.join(non_empty_lines)

        # Write the prettified XML to a file
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(resulting_xml)

    def read_uml_from_file(self, file_name, edge_style=None, label_style=None):
        with open(file_name, 'r') as file:
            sequence_diagram = file.read()

        actors, participants = extract_actors_and_participants(sequence_diagram)

        print("Actors:")
        for actor in actors:
            print(actor)

        # create Layer with UML file name
        base_name = os.path.splitext(os.path.basename(file_name))[0]
        self.add_layer(base_name)
        self.extract_messages_from_uml(sequence_diagram, actors=actors, participants=participants, layer_name=base_name, edge_style=edge_style, label_style=label_style)

    def extract_messages_from_uml(self, sequence_diagram, actors, participants, layer_name, edge_style, label_style):
        lines = sequence_diagram.split('\n')
        action_id = 0
        for line in lines:
            strip = line.strip()
            entity = starts_with_any(strip, actors, participants)
            if (entity == 'actor') | (entity == 'participant'):
                data = extract_info(line)
                print(entity)
                print(data)
                try:
                    # connect vertex of actor1 actor2 using arrow and message
                    action_id = action_id + 1
                    self.add_link_uml(
                        self.actors_to_nodes[data[0]],
                        self.actors_to_nodes[data[1]],
                        action=[f'{action_id}: {data[2]}'],
                        layer_name=layer_name,
                        edge_style=edge_style, label_style=label_style)
                except KeyError:
                    print('No such node')
                    if entity == 'actor':
                        node_id = generate_hash(data[0])
                        self.add_vertex(node_id=node_id, node_name=data[0], node_type='actor', layer_name=layer_name)

                        self.add_link_uml(
                            f'actor:{node_id}',
                            self.actors_to_nodes[data[1]],
                            action=[f'{action_id}: {data[2]}'],
                            layer_name=layer_name,
                            edge_style=edge_style, label_style=label_style)

    def read_uml_mappings(self, yaml_name: str):
        self.actors_to_nodes = {}
        with open(yaml_name, 'r') as file:
            data = yaml.safe_load(file)
            for vertex in data['nodes']:
                node_id = vertex['node_id']
                actor = vertex['actor']
                self.actors_to_nodes[actor] = node_id
