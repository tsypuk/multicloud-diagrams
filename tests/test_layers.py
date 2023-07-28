from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et

from utils.utils import TestUtilities


class TestMultiCloudDiagramsLayers(TestUtilities):

    def test_default_layer(self):
        # given-when
        mcd = MultiCloudDiagrams(debug_mode=True)

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 1, mcd)

    def test_add_2_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        mcd.add_layer('L2')

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 2, mcd)

    def test_add_3_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        mcd.add_layer('L2')
        mcd.add_layer('L3')

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")

        self.verify_layers(mx_cells, 3, mcd)

    def verify_layers(self, mx_cells, layers_count, mcd):
        self.assertEqual(layers_count + 1, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        expected_layer = {1: ''}
        for id in range(layers_count):
            self.verify_mx_cell(mx_cells[id + 1], expected={'id': f'{id + 1}', 'parent': '0'})
            if id > 0:
                expected_layer[id + 1] = f'L{id + 1}'
        self.assertEqual(expected_layer, mcd.layers)

    def test_get_layer_id_single_layer(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        layer_id = mcd.get_layer_id(layer_name='')

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)
        self.assertEqual(1, layer_id)

    def test_get_layer_id_2_layers(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)
        mcd.add_layer('L2')

        # when
        layer_id = mcd.get_layer_id(layer_name='')
        layer_id_l2 = mcd.get_layer_id(layer_name='L2')

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

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
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 2, mcd)
        self.assertEqual(1, layer_id)
        self.assertEqual(2, layer_id_l2)

    def test_get_layer_not_exist_id(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        with self.assertRaises(AttributeError):
            mcd.get_layer_id(layer_name='L2')

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)

    def test_get_layer_not_exist_id(self):
        # given
        mcd = MultiCloudDiagrams(debug_mode=True)

        # when
        with self.assertRaises(AttributeError):
            mcd.get_layer_id(layer_id=2)

        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.verify_layers(mx_cells, 1, mcd)
