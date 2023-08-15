from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities
import xml.etree.ElementTree as Et


class TestMCDList(TestUtilities):

    def test_map(self):
        # given
        table_name = 'prod-dynamo-table'
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_map(table_name=f'Schema:{table_name}', map={
            'First': 'Value1',
            'Second': 'Value2'
        })
        # mcd.dump()

        # then
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(5, len(mx_cells))

        expected = {
            'id': 'vertex:Schema:prod-dynamo-table:list',
            'parent': '1',
            'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;'
                     'resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
            'value': '<b>Schema:prod-dynamo-table</b>',
            'vertex': '1'
        }

        expected_list = [
            {'id': '0'},
            {'id': '1', 'parent': '0'},
            {'id': 'vertex:Schema:prod-dynamo-table:list', 'value': '<b>Schema:prod-dynamo-table</b>',
             'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;'
                      'resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
             'parent': '1', 'vertex': '1'},
            {'id': 'vertex:Schema:prod-dynamo-table:row:0', 'value': '<b>First</b>: Value1',
             'style': 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;',
             'parent': 'vertex:Schema:prod-dynamo-table:list', 'vertex': '1'},
            {'id': 'vertex:Schema:prod-dynamo-table:row:1', 'value': '<b>Second</b>: Value2',
             'style': 'text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;',
             'parent': 'vertex:Schema:prod-dynamo-table:list', 'vertex': '1'}
        ]

        self.verify_list(expected=expected, mx_file=mcd.mx_file, resource_name='LSI:users_to_model-users-idx', expected_list=expected_list)

    def test_empty_map(self):
        # given
        table_name = 'prod-dynamo-table'
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_map(table_name=f'Schema:{table_name}')
        # mcd.dump()

        # then
        tree = Et.ElementTree(mcd.mx_file)
        self.verify_mxfile_default(tree)

        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(3, len(mx_cells))

        expected = {
            'id': 'vertex:Schema:prod-dynamo-table:list',
            'parent': '1',
            'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;'
                     'resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
            'value': '<b>Schema:prod-dynamo-table</b>',
            'vertex': '1'
        }

        expected_list = [
            {'id': '0'},
            {'id': '1', 'parent': '0'},
            {'id': 'vertex:Schema:prod-dynamo-table:list', 'value': '<b>Schema:prod-dynamo-table</b>',
             'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;'
                      'resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
             'parent': '1', 'vertex': '1'},
        ]

        self.verify_list(expected=expected, mx_file=mcd.mx_file, resource_name='LSI:users_to_model-users-idx', expected_list=expected_list)
