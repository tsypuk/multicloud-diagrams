from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et

from test_utils import TestUtilities


class TestMultiCloudDiagramsDefaultDrawIO(TestUtilities):

    def test_drawio_preambula(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)

        # then
        self.verify_mxfile(tree.findall("."))

    def test_diagram(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)

        # then
        # ./diagram/
        self.verify_diagrams(tree.findall("./"))

    def test_mx_graph_model(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)

        # then
        # ./diagram/mxGraphModel/
        self.verify_mx_graph_models(tree.findall("/*/"))

    def test_root(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)

        # then
        # ./diagram/mxGraphModel/root
        self.verify_roots(tree.findall("./*/*/"))

    def test_mx_cell(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        tree = et.ElementTree(mcd.mxfile)

        # then
        # ./diagram/mxGraphModel/root/mxCell
        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(2, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        self.verify_mx_cell(mx_cells[1], expected={'id': '1', 'parent': '0'})
