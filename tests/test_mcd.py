from unittest import TestCase

from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et


class TestMultiCloudDiagramsDefaultDrawIO(TestCase):

    def test_drawio_preambula(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        roots = tree.findall(".")
        root = roots[0]

        # then
        self.assertEqual(1, len(roots))
        self.assertEqual('mxfile', root.tag)
        self.assertEqual('multicloud-diagrams', root.attrib['host'])
        self.assertEqual('PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.',
                         root.attrib['agent'])
        self.assertEqual('MultiCloud', root.attrib['type'])

    def test_diagram(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        diagrams = tree.findall("./")
        diagram = diagrams[0]

        # then
        self.assertEqual(1, len(diagrams))
        self.assertEqual('diagram', diagram.tag)
        self.assertEqual('diagram_1', diagram.attrib['id'])
        self.assertEqual('AWS components', diagram.attrib['name'])

    def test_mx_graph_model(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        # ./diagram/
        mx_graph_models = tree.findall("/*/")
        mx_graph_model = mx_graph_models[0]

        # then
        self.assertEqual(1, len(mx_graph_models))
        self.assertEqual('mxGraphModel', mx_graph_model.tag)
        expected = {'dx': '1015', 'dy': '661', 'grid': '1', 'gridSize': '10', 'guides': '1', 'tooltips': '1', 'connect': '1', 'arrows': '1', 'fold': '1', 'page': '1', 'pageScale': '1',
                    'pageWidth': '850', 'pageHeight': '1100', 'math': '0', 'shadow': '0'}
        self.assertEqual(expected, mx_graph_model.attrib)

    def test_root(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        # ./diagram/mxGraphModel/root
        roots = tree.findall("./*/*/*")
        root = roots[0]

        # then
        self.assertEqual(1, len(roots))
        self.assertEqual('root', root.tag)
        expected = {}
        self.assertEqual(expected, root.attrib)

    def test_mx_cell(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        # ./diagram/mxGraphModel/root/mxCell
        mxcells = tree.findall("./*/*/*/*")

        # then
        self.assertEqual(2, len(mxcells))
        self.verify_mx_cell(mxcells[0], expected={'id': '0'})
        self.verify_mx_cell(mxcells[1], expected={'id': '1', 'parent': '0'})

    def verify_mx_cell(self, mx_cell, expected):
        self.assertEqual('mxCell', mx_cell.tag)
        self.assertEqual(expected, mx_cell.attrib)
