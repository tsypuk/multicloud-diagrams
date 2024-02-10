import os
import unittest
import json
import xml.etree.ElementTree as Et

from multicloud_diagrams import customize


class TestUtilities(unittest.TestCase):
    supported_vertex = {}
    provider_services = {}
    no_rendering = ['yaml', 'vertex', 'layer', 'page', 'edge', 'color', 'connection']

    def setUp(self) -> None:
        project_folder = os.path.dirname(os.path.abspath(__file__))
        for provider in ['aws', 'fallback', 'onprem', 'azure', 'gcp', 'core']:
            path = os.path.join(project_folder, f'../multicloud_diagrams/providers/{provider}.json')
            with open(path, 'r') as file:
                json_data = json.load(file)
            self.supported_vertex.update(json_data)
            self.provider_services[provider] = list(json_data.keys())
        self.supported_vertex['yaml'] = {}

    def get_provider_by_service_name(self, service_name) -> str:
        for substring in self.no_rendering:
            if substring in service_name:
                return 'core'
        for provider, value in self.provider_services.items():
            if service_name in value:
                return provider
        return 'fallback'

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
        self.assertNotIn('shadow', root.attrib)

    def verify_diagrams(self, diagrams):
        diagram = diagrams[0]

        # then
        self.assertEqual(1, len(diagrams))
        self.assertEqual('diagram', diagram.tag)
        self.assertEqual('diagram_1', diagram.attrib['id'])
        self.assertEqual('AWS components', diagram.attrib['name'])

    def verify_mx_graph_models(self, mx_graph_models, shadow_mode=True):
        mx_graph_model = mx_graph_models[0]
        shadow_value = '0'
        if shadow_mode:
            shadow_value = '1'

        # then
        self.assertEqual(1, len(mx_graph_models))
        self.assertEqual('mxGraphModel', mx_graph_model.tag)
        expected = {'dx': '1015', 'dy': '661', 'grid': '1', 'gridSize': '10', 'guides': '1', 'tooltips': '1', 'connect': '1', 'arrows': '1', 'fold': '1', 'page': '1', 'pageScale': '1',
                    'pageWidth': '850', 'pageHeight': '1100', 'math': '0', 'shadow': shadow_value}
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

    def verify_resource(self, expected: dict, mx_file: Et.Element, resource_name, resource_type, debug_mode=False, style=None):
        if style is None:
            style = {}
        tree = Et.ElementTree(mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_vertex_in_isolation(mx_cells)

        if resource_type not in self.supported_vertex:
            resource_type = 'fallback_vertex'

        # 'style' is verified based on providers file content
        if 'style' in expected:
            del expected['style']
        expected['style'] = self.supported_vertex[resource_type]['style']

        customize(expected, style=style)

        children = mx_cells[2].findall("./*")

        self.verify_mx_cell(mx_cells[2], expected)
        children_count = 1
        if debug_mode:
            comment = children[0]
            self.assertEqual(f'vertex:{resource_name}', comment.text)
            self.assertEqual(0, len(comment.attrib))
            children_count = 2
            mx_geometry = children[1]
        else:
            mx_geometry = children[0]

        self.assertEqual(children_count, len(children))
        self.assertEqual('mxGeometry', mx_geometry.tag)
        self.assertEqual('geometry', mx_geometry.attrib['as'])
        # 'height', 'width' are verified based on providers file content
        self.assertEqual(self.supported_vertex[resource_type]['height'], mx_geometry.attrib['height'])
        self.assertEqual(self.supported_vertex[resource_type]['width'], mx_geometry.attrib['width'])

    def verify_layers(self, mx_cells, layers_count, mcd):
        self.assertEqual(layers_count + 1, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        expected_layer = {1: ''}
        self.verify_mx_cell(mx_cells[1], expected={'id': f'{1}', 'parent': '0'})
        for id in range(1, layers_count, 1):
            self.verify_mx_cell(mx_cells[id + 1], expected={'id': f'{id + 1}', 'parent': '0', 'value': f'L{id + 1}'})
            if id > 0:
                expected_layer[id + 1] = f'L{id + 1}'
        self.assertEqual(expected_layer, mcd.layers)

    def verify_mx_geometry(self, children):
        self.assertEqual(1, len(children))
        mx_geometry = children[0]
        self.assertEqual('mxGeometry', mx_geometry.tag)
        self.assertEqual('geometry', mx_geometry.attrib['as'])

    def verify_list(self, expected: dict, expected_list: [dict], mx_file: Et.Element, resource_name, debug_mode=False):
        tree = Et.ElementTree(mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(len(expected_list), len(mx_cells))
        for index, expected_item in enumerate(expected_list):
            self.verify_mx_cell(mx_cells[index], expected=expected_item)

        children = mx_cells[2].findall("./*")
        self.verify_mx_cell(mx_cells[2], expected)

        children_count = 1
        if debug_mode:
            comment = children[0]
            self.assertEqual(f'vertex:{resource_name}', comment.text)
            self.assertEqual(0, len(comment.attrib))
            children_count = 2
            mx_geometry = children[1]
        else:
            mx_geometry = children[0]

        self.assertEqual(children_count, len(children))
        self.assertEqual('mxGeometry', mx_geometry.tag)
        self.assertEqual('geometry', mx_geometry.attrib['as'])
        # 'height', 'width' are verified based on providers file content
        # self.assertEqual(self.supported_vertex[resource_type]['height'], mx_geometry.attrib['height'])
        # self.assertEqual(self.supported_vertex[resource_type]['width'], mx_geometry.attrib['width'])
