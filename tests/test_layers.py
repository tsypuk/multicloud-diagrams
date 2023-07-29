from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as ET

from utils.utils import TestUtilities


class TestMultiCloudDiagramsLayers(TestUtilities):

    def test_default_layer(self):
        # given-when
        mcd = MultiCloudDiagrams(debug_mode=True)

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 1, mcd)

    def test_add_2_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        mcd.add_layer('L2')

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 2, mcd)

    def test_add_3_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        mcd.add_layer('L2')
        mcd.add_layer('L3')

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 3, mcd)

    def test_get_layer_id_single_layer(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        layer_id = mcd.get_layer_id(layer_name='')

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)
        self.assertEqual(1, layer_id)

    def test_get_layer_name_2_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)
        mcd.add_layer('L2')

        # when
        layer_id = mcd.get_layer_id(layer_name='')
        layer_id_l2 = mcd.get_layer_id(layer_name='L2')

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 2, mcd)
        self.assertEqual(1, layer_id)
        self.assertEqual(2, layer_id_l2)

    def test_get_layer_id_2_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)
        mcd.add_layer('L2')

        # when
        layer_id = mcd.get_layer_id(layer_id=1)
        layer_id_l2 = mcd.get_layer_id(layer_id=2)

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 2, mcd)
        self.assertEqual(1, layer_id)
        self.assertEqual(2, layer_id_l2)

    def test_get_layer_by_name_not_exist_id(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        with self.assertRaises(AttributeError):
            mcd.get_layer_id(layer_name='L2')

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)

    def test_get_layer_by_id_not_exist_id(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        with self.assertRaises(AttributeError):
            mcd.get_layer_id(layer_id=2)

        # then
        tree = ET.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)
