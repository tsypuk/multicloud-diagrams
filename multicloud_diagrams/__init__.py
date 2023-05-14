import xml.etree.ElementTree as et
import logging
import os.path


class MultiCloudDiagrams:
    def __init__(self):
        self.mxfile = et.Element('mxfile', host="multicloud-diagrams",
                                 agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.",
                                 type="MultiCloud")
        self.diagram = et.SubElement(self.mxfile, 'diagram', id="diagram_1", name="AWS components")
        self.mx_graph_model = et.SubElement(self.diagram, 'mxGraphModel', dx="1015", dy="661", grid="1", gridSize="10",
                                            guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1",
                                            pageScale="1", pageWidth="850", pageHeight="1100", math="0", shadow="0")
        self.root = et.SubElement(self.mx_graph_model, 'root')
        self.mx_cell_id_0 = et.SubElement(self.root, 'mxCell', id="0")
        self.mx_cell_id_1 = et.SubElement(self.root, 'mxCell', id="1", parent="0")

    prev_coords = {}

    supported_vertex = {
        'lambda_function': {
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;shape=mxgraph.aws3.lambda_function;prIcon=server;fillColor=#F58534;gradientColor=none;html=1;',
            'width': '69',
            'height': '72',
            'nodeLevel': '4'
        },
        'sqs': {
            'style': 'shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;fillColor=#F58534;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom',
            'width': '78',
            'height': '78',
            'nodeLevel': '4'},
        'sns': {
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;',
            'width': '78',
            'height': '78',
            'nodeLevel': '4'
        },
        'iam_role': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.role;fillColor=#759C3E;gradientColor=none;',
            'width': '94.5',
            'height': '79.5',
            'nodeLevel': '3'},
        'dynamo': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.dynamo_db;fillColor=#2E73B8;gradientColor=none;',
            'width': '72',
            'height': '81',
            'nodeLevel': '1'},
        'dynamo_stream': {
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#2E27AD;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.dynamodb_stream',
            'width': '78',
            'height': '78',
            'nodeLevel': '1'},
        'api_gw': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.api_gateway;fillColor=#D9A741;gradientColor=none;',
            'width': '76.5',
            'height': '93',
            'nodeLevel': '4'},
        's3': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.bucket_with_objects;fillColor=#E05243;gradientColor=none;',
            'width': '60',
            'height': '61.5',
            'nodeLevel': '4'},
        'kms': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.kms;fillColor=#759C3E;gradientColor=none;',
            'width': '76.5',
            'height': '93',
            'nodeLevel': '4'},
        'ssm': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.parameter_store;fillColor=#759C3E;gradientColor=none;',
            'width': '75',
            'height': '102',
            'nodeLevel': '4'},
        'iam_policy': {
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F8624;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.policy;',
            'width': '78',
            'height': '67',
            'nodeLevel': '1'},
        'iam_permission': {
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.permissions_2;fillColor=#D2D3D3;gradientColor=none;',
            'width': '46.5',
            'height': '63',
            'nodeLevel': '2'},
        'fallback_vertex': {
            'style': 'sketch=0;aspect=fixed;html=1;points=[];align=center;image;fontSize=12;image=img/lib/mscae/Info.svg;',
            'width': '100',
            'height': '100',
            'nodeLevel': '1'}
    }

    def get_vertex_metadata(self, node_type: str) -> object:
        if node_type in self.supported_vertex:
            return self.supported_vertex[node_type]
        else:
            logging.warn(
                f'No such nodeType: {node_type} in the Library (using deafult fallback icon Info). Please contact maintainer to add it, or provide MergeRequest')
            return self.supported_vertex['fallback_vertex']

    @staticmethod
    def stringify_dict(metadata: dict) -> str:
        if metadata != '':
            # return '<BR>-----------<BR>' + '<BR>'.join([f'<b>{k.capitalize()}</b>: {v}' for k, v in metadata.items()])
            return '<BR>-----------<BR>' + '<BR>'.join([f'<b>{k}</b>: {v}' for k, v in metadata.items()])
        else:
            return ''

    def add_list(self, table_name='', rows=[]):
        width = "300"

        mx_cell = et.SubElement(self.root,
                                'mxCell',
                                id=f'vertex:{table_name}:list',
                                value=f'<b>{table_name}</b>',
                                style=("swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;"
                                       "startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;"
                                       "collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;"),
                                parent="1",
                                vertex="1")

        mx_geometry = et.SubElement(mx_cell, 'mxGeometry', width=width,
                                    height=str(30 * (1 + len(rows))))
        mx_geometry.set('as', 'geometry')

        # Position Vertex based on X,Y cords
        if f'vertex:{table_name}:list' in self.prev_coords:
            if 'x' in self.prev_coords[f'vertex:{table_name}:list']:
                mx_geometry.set('x', self.prev_coords[f'vertex:{table_name}:list']['x'])
            if 'y' in self.prev_coords[f'vertex:{table_name}:list']:
                mx_geometry.set('y', self.prev_coords[f'vertex:{table_name}:list']['y'])

        for index, item in enumerate(rows):
            mx_cell = et.SubElement(self.root,
                                    'mxCell',
                                    id=f'vertex:{table_name}:row:{index}',
                                    value=item,
                                    style=("text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;"
                                           "spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];"
                                           "portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;"),
                                    parent=f'vertex:{table_name}:list',
                                    vertex="1")

            mx_geometry = et.SubElement(mx_cell, 'mxGeometry', width=width, height="30")
            mx_geometry.set('as', 'geometry')
            # Position Vertex based on X,Y cords
            if f'vertex:{table_name}:row:{index}' in self.prev_coords:
                if 'x' in self.prev_coords[f'vertex:{table_name}:row:{index}']:
                    mx_geometry.set('x', self.prev_coords[f'vertex:{table_name}:row:{index}']['x'])
                if 'y' in self.prev_coords[f'vertex:{table_name}:row:{index}']:
                    mx_geometry.set('y', self.prev_coords[f'vertex:{table_name}:row:{index}']['y'])

    def add_vertex(self, id: str, node_name: str, arn: str, metadata='', node_type=''):

        # check that there is no such vertex already
        exist = False
        for mx_cell in self.root:
            # print(mxCell.attrib['id'])
            if mx_cell.attrib['id'] == f'vertex:{node_type}:{id}':
                logging.warning(f'Already exists: vertex:{node_type}:{id} name:{node_name}')
                exist = True
                break

        if not exist:
            shape_parameters = self.get_vertex_metadata(node_type)

            stringified_metadata = self.stringify_dict(metadata)

            mx_cell = et.SubElement(self.root,
                                    'mxCell',
                                    id=f'vertex:{node_type}:{id}',
                                    # id = f'vertex:{ARN}',
                                    value=f'<b>Name</b>: {node_name}<BR><b>ARN</b>: {arn} {stringified_metadata}',
                                    style=("verticalLabelPosition=bottom;"
                                           "html=1;"
                                           "verticalAlign=top;"
                                           "aspect=fixed;align=left;"
                                           "pointerEvents=1;"
                                           f"{shape_parameters['style']}"
                                           ""),
                                    parent="1",
                                    vertex="1")

            mx_cell.insert(0, et.Comment(f'vertex:{node_name}'))
            mx_geometry = et.SubElement(mx_cell, 'mxGeometry', width=shape_parameters['width'],
                                        height=shape_parameters['height'])
            mx_geometry.set('as', 'geometry')

            # Position Vertex based on X,Y cords
            if f'vertex:{node_type}:{id}' in self.prev_coords:
                if 'x' in self.prev_coords[f'vertex:{node_type}:{id}']:
                    mx_geometry.set('x', self.prev_coords[f'vertex:{node_type}:{id}']['x'])
                if 'y' in self.prev_coords[f'vertex:{node_type}:{id}']:
                    mx_geometry.set('y', self.prev_coords[f'vertex:{node_type}:{id}']['y'])

    def add_vertex_list(self, vertexes):
        for vertex in vertexes:
            self.add_vertex(id=vertex['id'], node_name=vertex['nodeName'], metadata=vertex['nodeDescription'],
                            node_type=vertex['nodeType'])
        return

    @staticmethod
    def _stringify_labels(labels: []) -> str:
        if len(labels) > 0:
            return '<BR>'.join([f'{k}' for k in labels])
        else:
            return ''

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
                                        mxLabel.attrib['value'] = old_label + '<BR><BR>' + self._stringify_labels([label])

                                break
                    break
            if not edge_exist:
                mx_cell = et.SubElement(self.root,
                                        'mxCell',
                                        id=f'edge:{src_node_id}:to:{dest_node_id}',
                                        style=f'endFill=0;endArrow={start};endArrow={end};',
                                        parent="1",
                                        source=f'vertex:{src_node_id}',
                                        target=f'vertex:{dest_node_id}',
                                        edge="2")

                mx_cell.insert(0, et.Comment(f'edge:{src_node_id}:to:{dest_node_id}'))
                mx_geometry = et.SubElement(mx_cell, 'mxGeometry')
                mx_geometry.set('as', 'geometry')

                # Add label to edge
                if len(labels) > 0:
                    # style="edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];"
                    # style="edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;
                    mx_cell = et.SubElement(self.root,
                                            'mxCell',
                                            id=f'label:{src_node_id}:to:{dest_node_id}',
                                            value=self._stringify_labels(labels),
                                            style="edgeLabel;html=1;align=left;verticalAlign=middle;resizable=0;points=[];labelBackgroundColor=none;",
                                            parent=f'edge:{src_node_id}:to:{dest_node_id}',
                                            vertex="1",
                                            connectable="0")
                    # <mxGeometry relative="1" as="geometry">
                    mx_geometry = et.SubElement(mx_cell,
                                                'mxGeometry',
                                                relative="1"
                                                )
                    mx_geometry.set('as', 'geometry')
                    # <mxPoint as="offset"/>
                    mx_geometry = et.SubElement(mx_geometry, 'mxPoint')
                    mx_geometry.set('as', 'offset')
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

    def add_bidirectional_link(self, src_node_id, dst_node_id):
        self.add_connection(src_node_id, dst_node_id, "classic", "classic")

    def add_unidirectional_link(self, src_node_id, dst_node_id):
        self.add_connection(src_node_id, dst_node_id, "none", "classic")

    def add_unidirectional_reverse_link(self, src_node_id, dst_node_id):
        self.add_connection(src_node_id, dst_node_id, "classic", "none")

    def add_link_list(self, links):
        for link in links:
            self.add_link(src_node_id=link['sourceNodeID'], dst_node_id=link['destinationNodeID'])
        return

    def read_coords_from_file(self, file_name: str):
        if os.path.isfile(file_name):
            tree = et.parse(file_name)
            root = tree.getroot()

            for neighbor in root.iter('mxCell'):
                if neighbor.get('id').startswith("vertex:"):
                    data = neighbor.find('mxGeometry')
                    cords = {}
                    if data.get('x') is not None:
                        cords['x'] = data.get('x')
                    if data.get('y') is not None:
                        cords['y'] = data.get('y')
                    self.prev_coords[neighbor.get('id')] = cords

    def export_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            tree = et.ElementTree(self.mxfile)
            et.indent(tree, space="\t", level=0)
            tree.write(file, encoding='utf-8')
        return
