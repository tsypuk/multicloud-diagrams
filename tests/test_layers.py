from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as Et

from utils.utils import TestUtilities


class TestMultiCloudDiagramsLayers(TestUtilities):

    def test_default_layer(self):
        # given-when
        mcd = MultiCloudDiagrams(debug_mode=True)

        # then
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 1, mcd)

    def test_add_2_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        mcd.add_layer('L2')

        # then
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 2, mcd)

    def test_add_same_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        mcd.add_layer('L2')
        mcd.add_layer('L2')

        # then
        tree = Et.ElementTree(mcd.mx_file)
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
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 3, mcd)

        # This file will be used to verify that layers are loaded
        file_name = 'tests/3_layers.drawio'
        mcd.export_to_file(file_name)

    def test_get_layer_id_single_layer(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        layer_id = mcd.get_layer_id(layer_name='')

        # then
        tree = Et.ElementTree(mcd.mx_file)
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
        tree = Et.ElementTree(mcd.mx_file)
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
        tree = Et.ElementTree(mcd.mx_file)
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
        tree = Et.ElementTree(mcd.mx_file)
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
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)

    def test_read_layers_from_file(self):
        # given
        mcd = MultiCloudDiagrams()
        # file contains 3 layers default, L2, L3
        # file_name = '3_layers.drawio'
        file_name = 'tests/3_layers.drawio'

        # when
        mcd.read_nodes_from_file(file_name)

        # then
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 3, mcd)
