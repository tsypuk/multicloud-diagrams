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

    def test_diagram_mx_graph_model(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)
        diagram = tree.find("./")

        # then
        self.assertEqual('diagram', diagram.tag)
        self.assertEqual('diagram_1', diagram.attrib['id'])
        self.assertEqual('AWS components', diagram.attrib['name'])