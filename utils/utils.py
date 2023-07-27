import os
import unittest
import json
import xml.etree.ElementTree as et


class TestUtilities(unittest.TestCase):
    supported_vertex = {}

    def setUp(self) -> None:
        project_folder = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(project_folder, f'../multicloud_diagrams/providers/aws_services.json')
        with open(path, 'r') as file:
            json_data = json.load(file)

        self.supported_vertex.update(json_data)

    def verify_mx_cell(self, mx_cell, expected):
        # then
        self.assertEqual('mxCell', mx_cell.tag)
        self.assertEqual(expected, mx_cell.attrib)

    def verify_mxfile(self, roots):
        root = roots[0]

        # then
        self.assertEqual(1, len(roots))
        self.assertEqual('mxfile', root.tag)
        self.assertEqual('multicloud-diagrams', root.attrib['host'])
        self.assertEqual('PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.',
                         root.attrib['agent'])
        self.assertEqual('MultiCloud', root.attrib['type'])

    def verify_diagrams(self, diagrams):
        diagram = diagrams[0]

        # then
        self.assertEqual(1, len(diagrams))
        self.assertEqual('diagram', diagram.tag)
        self.assertEqual('diagram_1', diagram.attrib['id'])
        self.assertEqual('AWS components', diagram.attrib['name'])

    def verify_mx_graph_models(self, mx_graph_models):
        mx_graph_model = mx_graph_models[0]

        # then
        self.assertEqual(1, len(mx_graph_models))
        self.assertEqual('mxGraphModel', mx_graph_model.tag)
        expected = {'dx': '1015', 'dy': '661', 'grid': '1', 'gridSize': '10', 'guides': '1', 'tooltips': '1', 'connect': '1', 'arrows': '1', 'fold': '1', 'page': '1', 'pageScale': '1',
                    'pageWidth': '850', 'pageHeight': '1100', 'math': '0', 'shadow': '0'}
        self.assertEqual(expected, mx_graph_model.attrib)

    def verify_roots(self, roots):
        root = roots[0]

        # then
        self.assertEqual(1, len(roots))
        self.assertEqual('root', root.tag)
        expected = {}
        self.assertEqual(expected, root.attrib)

    def verify_mxfile_default(self, tree):
        self.verify_mxfile(tree.findall("."))
        self.verify_diagrams(tree.findall("./"))
        self.verify_mx_graph_models(tree.findall("./*/"))
        self.verify_roots(tree.findall("./*/*/"))

    def verify_vertex_in_isolation(self, mx_cells):
        self.assertEqual(3, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        self.verify_mx_cell(mx_cells[1], expected={'id': '1', 'parent': '0'})

    def verify_aws_resource(self, expected: dict, mx_file: et.Element, resource_name, resource_type):
        tree = et.ElementTree(mx_file)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_vertex_in_isolation(mx_cells)

        # 'style' is verified based on providers file content
        if 'style' in expected: del expected['style']
        expected['style'] = self.supported_vertex[resource_type]['style']

        self.verify_mx_cell(mx_cells[2], expected)
        # <!--vertex:node-name-->
        # <mxGeometry width="69" height="72" as="geometry"/>
        children = mx_cells[2].findall("./*")
        self.assertEqual(2, len(children))

        comment = children[0]
        self.assertEqual(f'vertex:{resource_name}', comment.text)
        self.assertEqual(0, len(comment.attrib))

        mx_geometry = children[1]
        self.assertEqual('mxGeometry', mx_geometry.tag)
        self.assertEqual('geometry', mx_geometry.attrib['as'])
        # 'height', 'width' are verified based on providers file content
        self.assertEqual(self.supported_vertex[resource_type]['height'], mx_geometry.attrib['height'])
        self.assertEqual(self.supported_vertex[resource_type]['width'], mx_geometry.attrib['width'])
