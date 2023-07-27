from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et

from utils.utils import TestUtilities


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
        self.verify_mx_graph_models(tree.findall("./*/"))

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

    def test_comment(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)
        resource_type = "test"
        resource_name = "test_name"

        # when
        mcd.add_vertex(id="123", node_name=resource_name, arn="test_arn", metadata={}, node_type=resource_type)

        # then
        expected = {
            'id': 'vertex:test:123',
            'value': '<b>Name</b>: test_name<BR><b>ARN</b>: test_arn ',
            'style': 'sketch=0;aspect=fixed;html=1;points=[];align=center;image;fontSize=12;image=img/lib/mscae/Info.svg;',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_aws_resource(expected, mcd.mxfile, resource_name, 'fallback_vertex', debug_mode=True)
