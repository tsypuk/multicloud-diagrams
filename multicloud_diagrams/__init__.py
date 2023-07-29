import json
import xml.etree.ElementTree as Et
import logging
import os.path
import pkgutil
from enum import Enum
from typing import Union
import re

import yaml


class AWS(Enum):
    lambda_function = "lambda_function"
    sqs = "sqs"
    sns = "sns"
    iam_role = "iam_role"
    iam_policy = "iam_policy"
    iam_permission = "iam_permission"
    dynamo = "dynamo"
    dynamo_stream = "dynamo_stream"
    api_gw = "api_gw"
    s3 = "s3"
    kms = "kms"
    ssm = "ssm"
    mq = "mq"


class OnPrem(Enum):
    http = "http"
    mq_broker = "mq_broker"


Services = Union[AWS, OnPrem]


def update_fill_color(style_str, node_color):
    pattern = r'fillColor=([^;]+)'
    # Replace the 'fillColor' value with the node_color
    return re.sub(pattern, f'fillColor={node_color}', style_str)


def stringify_dict(metadata: dict) -> str:
    if metadata:
        # return '<BR>-----------<BR>' + '<BR>'.join([f'<b>{k.capitalize()}</b>: {v}' for k, v in metadata.items()])
        return '<BR>'.join([f'<b>{k}</b>: {v}' for k, v in metadata.items()])
    else:
        return ''


def build_vertex_id(vertex_details, edge, src_dst_marker: str):
    resource = {}
    if f'{src_dst_marker}_arn' in edge:
        resource["type"] = edge[f"{src_dst_marker}_type"]
        resource["arn"] = edge[f'{src_dst_marker}_arn']
    elif src_dst_marker in edge:
        resource = [vertex for vertex in vertex_details if vertex['name'] == edge[src_dst_marker]][0]
    return f'{resource["type"]}:{resource["arn"]}'


def stringify_labels(labels: []) -> str:
    if len(labels) > 0:
        return '<BR>'.join([f'{k}' for k in labels])
    else:
        return ''


def assemble_node_name(node_name, arn, metadata):
    return f'<b>Name</b>: {node_name}<BR><b>ARN</b>: {arn}{"<BR>-----------<BR>" + stringify_dict(metadata) if metadata else ""}'


class MultiCloudDiagrams:
    def __init__(self, debug_mode=False, shadow=True, layer_name=''):
        self.mx_file = Et.Element('mxfile',
                                  host="multicloud-diagrams",
                                  agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.",
                                  type="MultiCloud")

        self.diagram = Et.SubElement(self.mx_file, 'diagram', id="diagram_1", name="AWS components")
        self.mx_graph_model = Et.SubElement(self.diagram, 'mxGraphModel', dx="1015", dy="661", grid="1", gridSize="10",
                                            guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                            pageScale="1", pageWidth="850", pageHeight="1100", math="0")
        if shadow:
            self.mx_graph_model.attrib['shadow'] = '1'
        else:
            self.mx_graph_model.attrib['shadow'] = '0'

        self.root = Et.SubElement(self.mx_graph_model, 'root')
        self.layers = {}
        self.mx_cell_id_0 = Et.SubElement(self.root, 'mxCell', id="0")
        self.add_layer(layer_name)
        self.debug_mode = debug_mode

    def add_layer(self, layer_name: str = ''):
        self.layers[self.get_current_layer_count() + 1] = layer_name
        self.mx_cell_id_0 = Et.SubElement(self.root, 'mxCell', id=f"{self.get_current_layer_count()}", parent="0")
        if layer_name != '':
            self.mx_cell_id_0.attrib['value'] = layer_name

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

    # Load supported vertexes for registered Cloud Providers
    providers = ['aws_services', 'azure_services', 'gcp_services', 'on_prem_services', 'fallback']
    for provider in providers:
        path = pkgutil.get_data(__package__, f'providers/{provider}.json')
        supported_vertex.update(json.loads(path.decode("utf-8")))

    def get_node_template(self, node_type: str) -> dict:
        if node_type in self.supported_vertex:
            return self.supported_vertex[node_type].copy()
        else:
            logging.warning(
                f'No such nodeType: {node_type} in the Library (using default fallback icon Info). Please contact maintainer to add it, or provide MergeRequest')
            return self.supported_vertex['fallback_vertex'].copy()

    # green fill_color=#d5e8d4
    # red fill_color=#f8cecc;"
    # TODO cover with tests list
    def add_list(self, table_id='', table_name='', fill_color='', rows=[], width="300"):
        if not table_id:
            table_id = table_name
        # TODO mode all styling to external resource file
        style = (
            "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;"
            "resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;"
        )

        if fill_color:
            style += f"fillColor={fill_color}"

        mx_cell = Et.SubElement(self.root,
                                'mxCell',
                                id=f'vertex:{table_id}:list',
                                value=f'<b>{table_name}</b>',
                                style=style,
                                parent="1",
                                vertex="1")

        mx_geometry = Et.SubElement(mx_cell, 'mxGeometry', width=width,
                                    height=str(30 * (1 + len(rows))))
        mx_geometry.set('as', 'geometry')

        # Position Vertex based on X,Y cords
        self.update_vertex_coords_width_height_from_prev_version(mx_geometry, f'vertex:{table_id}:list')

        for index, item in enumerate(rows):
            name, value = item.split(":", 1)
            mx_cell = Et.SubElement(self.root,
                                    'mxCell',
                                    id=f'vertex:{table_id}:row:{index}',
                                    value=f'<b>{name}</b>: {value}',
                                    style=("text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;"
                                           "spacingLeft=4;spacingRight=4;overflow=hidden;"
                                           "portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;"),
                                    parent=f'vertex:{table_id}:list',
                                    vertex="1")

            mx_geometry = Et.SubElement(mx_cell, 'mxGeometry', width=width, height="30")
            mx_geometry.set('as', 'geometry')
            # Position Vertex based on X,Y cords
            self.update_vertex_coords_width_height_from_prev_version(mx_geometry, f'vertex:{table_id}:row:{index}')

    def add_service(self, id: str, node_name: str, arn: str, metadata: dict = None, node_enum=Services):
        if metadata is None:
            metadata = {}
        # Type checking
        if not isinstance(node_enum, Services):
            raise TypeError('node_enum must be an instance of AWS,OnPrem Enum')
        self.add_vertex(id, node_name, arn, metadata, node_enum.value)

    def add_vertex(self, id: str, node_name: str, arn: str, metadata: dict = None, node_type: str = '', layer_name: str = None, layer_id: str = None, fill_color: str = None):
        if metadata is None:
            metadata = {}
        # check that there is no such vertex already
        exist = False
        for mx_cell in self.root:
            # print(mxCell.attrib['id'])
            if mx_cell.attrib['id'] == f'vertex:{node_type}:{id}':
                logging.warning(f'Already exists: vertex:{node_type}:{id} name:{node_name}')
                exist = True
                break

        if not exist:
            node_template = self.get_node_template(node_type)
            if fill_color is not None:
                node_template['style'] = update_fill_color(node_template['style'], fill_color)

            parent_id = str(self.get_layer_id(layer_name, layer_id))
            mx_cell = Et.SubElement(self.root,
                                    'mxCell',
                                    id=f'vertex:{node_type}:{id}',
                                    value=assemble_node_name(node_name, arn, metadata),
                                    style=f"{node_template['style']}",
                                    parent=parent_id,
                                    vertex="1")
            if self.debug_mode:
                mx_cell.insert(0, Et.Comment(f'vertex:{node_name}'))
            mx_geometry = Et.SubElement(mx_cell, 'mxGeometry', width=node_template['width'],
                                        height=node_template['height'])
            mx_geometry.set('as', 'geometry')

            # Position Vertex based on X,Y cords
            self.update_vertex_coords_width_height_from_prev_version(mx_geometry, f'vertex:{node_type}:{id}')

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

    def add_vertex_list(self, vertexes):
        for vertex in vertexes:
            self.add_vertex(id=vertex['id'], arn=vertex[id], node_name=vertex['nodeName'], metadata=vertex['nodeDescription'],
                            node_type=vertex['nodeType'])
        return

    # TODO add tests for connection
    def add_connection(self, src_node_id, dest_node_id, start, end, labels=[]):
        # Check that both source and destination exist, before creating edge
        found = 0
        for mx_cell in self.root:
            # print(mxCell.attrib['id'])
            if mx_cell.attrib['id'] == f'vertex:{src_node_id}':
                found += 1
            if mx_cell.attrib['id'] == f'vertex:{dest_node_id}':
                found += 1
            if found == 2:
                break

        if found == 2:
            # check that Edge does not exist
            edge_exist = False
            for mx_cell in self.root:
                if mx_cell.attrib['id'] == f'edge:{src_node_id}:to:{dest_node_id}':
                    edge_exist = True
                    # update the labels
                    for mxLabel in self.root:
                        if mxLabel.attrib['id'] == f'label:{src_node_id}:to:{dest_node_id}':
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
                mx_cell = Et.SubElement(self.root,
                                        'mxCell',
                                        id=f'edge:{src_node_id}:to:{dest_node_id}',
                                        style=f'endFill=0;endArrow={start};endArrow={end};',
                                        parent="1",
                                        source=f'vertex:{src_node_id}',
                                        target=f'vertex:{dest_node_id}',
                                        edge="2")

                if self.debug_mode:
                    mx_cell.insert(0, Et.Comment(f'edge:{src_node_id}:to:{dest_node_id}'))
                mx_geometry = Et.SubElement(mx_cell, 'mxGeometry')
                mx_geometry.set('as', 'geometry')

                # Add label to edge
                if len(labels) > 0:
                    # style="edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];"
                    # style="edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;
                    mx_cell = Et.SubElement(self.root,
                                            'mxCell',
                                            id=f'label:{src_node_id}:to:{dest_node_id}',
                                            value=stringify_labels(labels),
                                            style="edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;",
                                            parent=f'edge:{src_node_id}:to:{dest_node_id}',
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

                    self.update_vertex_coords_from_prev_version(mx_geometry, f'label:{src_node_id}:to:{dest_node_id}')

                    # </mxGeometry>
                    # </mxCell>
            else:
                logging.warning(
                    f'Already exist edge:{src_node_id}:to:{dest_node_id}')
        else:
            logging.error(
                f'Not both vertexes present to build Edge between them (expected vertex:{src_node_id} & vertex:{dest_node_id})')

    def add_link(self, src_node_id, dst_node_id, action=[]):
        self.add_connection(src_node_id, dst_node_id, "none", "none", action)

    def add_bidirectional_link(self, src_node_id, dst_node_id, action=[]):
        self.add_connection(src_node_id, dst_node_id, "classic", "classic", action)

    def add_unidirectional_link(self, src_node_id, dst_node_id, action=[]):
        self.add_connection(src_node_id, dst_node_id, "none", "classic", action)

    def add_unidirectional_reverse_link(self, src_node_id, dst_node_id, action=[]):
        self.add_connection(src_node_id, dst_node_id, "classic", "none", action)

    def add_link_list(self, links):
        for link in links:
            self.add_link(src_node_id=link['sourceNodeID'], dst_node_id=link['destinationNodeID'])
        return

    def augment_from_yaml(self, yaml_name: str):
        with open(yaml_name, 'r') as file:
            data = yaml.safe_load(file)
            for vertex in data['vertices']:
                self.add_vertex(
                    id=vertex['arn'],
                    node_name=vertex['name'],
                    arn=vertex['arn'],
                    node_type=vertex['type'],
                    # optional attributes
                    metadata={},
                    # icon
                )
            for edge in data['edges']:
                self.add_link(
                    src_node_id=build_vertex_id(data['vertices'], edge, 'src'),
                    dst_node_id=build_vertex_id(data['vertices'], edge, 'dst'),
                    action=[edge['label']]
                )

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

    def export_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            tree = Et.ElementTree(self.mx_file)
            Et.indent(tree, space="\t", level=0)
            tree.write(file, encoding='utf-8')
        return
