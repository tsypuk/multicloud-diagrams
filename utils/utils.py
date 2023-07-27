import unittest


class TestUtilities(unittest.TestCase):

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
        self.verify_mx_graph_models(tree.findall("/*/"))
        self.verify_roots(tree.findall("./*/*/"))
