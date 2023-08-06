from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities


# NOTE!!! Content of this file is mapped to documentation with lines position

class TestAWSVertexInIsolation(TestUtilities):

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
        mcd.add_vertex(node_id=table_arn, node_name=table_name, arn=table_arn, node_type='dynamo', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
            'value': ('<b>Name</b>: prod-dynamo-table<BR><b>ARN</b>: arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table'
                      '<BR>-----------<BR>'
                      '<b>DeletionProtectionEnabled</b>: True<BR><b>ItemCount</b>: 900<BR><b>TableSizeBytes</b>: 123'),
            'parent': '1',
            'vertex': '1'
        }
        self.verify_aws_resource(expected, mcd.mx_file, 'prod-dynamo-table', 'dynamo')
