from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities
import xml.etree.ElementTree as Et


class TestMCDList(TestUtilities):

    def test_list(self):
        # given
        table_name = 'prod-dynamo-table'
        # table_arn = 'arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table'
        mcd = MultiCloudDiagrams()
        rows_keys = [
            'First: row',
            'Second: row'
        ]

        # when
        mcd.add_list(table_name=f'Schema:{table_name}', rows=rows_keys)
        # mcd.dump()
        # then

        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(5, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        self.verify_mx_cell(mx_cells[1], expected={'id': '1', 'parent': '0'})

        # TODO finish test
