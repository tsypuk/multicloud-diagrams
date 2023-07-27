from unittest import TestCase

from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et


class TestMultiCloudDiagramsDrawIO(TestCase):

    def test_drawio_preambula(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        root = tree.find(".")

        # then
        self.assertEqual('mxfile', root.tag)
        self.assertEqual('multicloud-diagrams', root.attrib['host'])
        self.assertEqual('PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license.', root.attrib['agent'])
        self.assertEqual('MultiCloud', root.attrib['type'])

    def test_diagram(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        diagram = tree.find("./")

        # then
        self.assertEqual('diagram', diagram.tag)
        self.assertEqual('diagram_1', diagram.attrib['id'])
        self.assertEqual('AWS components', diagram.attrib['name'])

    def test_mx_graph_model(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        mx_graph_model = tree.find("./diagram/")

        # then
        self.assertEqual('mxGraphModel', mx_graph_model.tag)
        expected = {'dx': '1015', 'dy': '661', 'grid': '1', 'gridSize': '10', 'guides': '1', 'tooltips': '1', 'connect': '1', 'arrows': '1', 'fold': '1', 'page': '1', 'pageScale': '1', 'pageWidth': '850', 'pageHeight': '1100', 'math': '0', 'shadow': '0'}
        self.assertEqual(expected, mx_graph_model.attrib)