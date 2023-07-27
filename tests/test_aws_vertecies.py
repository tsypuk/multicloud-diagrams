from multicloud_diagrams import MultiCloudDiagrams
import xml.etree.ElementTree as et

from tests.test_utils import TestUtilities


class TestMultiCloudDiagramsAWSVertecies(TestUtilities):

    def test_dynamo(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        table_arn = 'arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table'
        table_name = 'prod-dynamo-table'
        metadata = {
            'DeletionProtectionEnabled': True,
            'ItemCount': 900,
            'TableSizeBytes': 123
        }
        mcd.add_vertex(id=table_arn, node_name=table_name, arn=table_arn, node_type='dynamo', metadata=metadata)


        # then
        tree = et.ElementTree(mcd.mxfile)
        self.verify_mxfile_default(et.ElementTree(tree))

        mx_cells = tree.findall("./*/*/*/")
        self.assertEqual(3, len(mx_cells))
        self.verify_mx_cell(mx_cells[0], expected={'id': '0'})
        self.verify_mx_cell(mx_cells[1], expected={'id': '1', 'parent': '0'})

        expected = {
            'id': 'vertex:dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
            'value': '<b>Name</b>: prod-dynamo-table<BR><b>ARN</b>: arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table <BR>-----------<BR><b>DeletionProtectionEnabled</b>: True<BR><b>ItemCount</b>: 900<BR><b>TableSizeBytes</b>: 123',
            'style': 'verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=left;pointerEvents=1;outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.dynamo_db;fillColor=#2E73B8;gradientColor=none;',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_mx_cell(mx_cells[2], expected)
