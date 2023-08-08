from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_dynamo(self):
        # docs
        self.node_type = 'dynamo'

        # given
        mcd = MultiCloudDiagrams()

        # when
        table_arn = 'arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table'
        table_name = 'prod-dynamo-table'
        metadata = {
            'DeletionProtectionEnabled': True,
            'ItemCount': 900,
            'TableSizeBytes': 123,
            'Replicas': 0,
            'RCU': 1,
            'WCU': 1
        }
        mcd.add_vertex(node_id=table_arn, node_name=table_name, arn=table_arn, node_type='dynamo', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
            'parent': '1',
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.dynamo_db;fillColor=#2E73B8;gradientColor=none;',
            'value': '<b>Name</b>: prod-dynamo-table<BR><b>ARN</b>: '
                     'arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table<BR>-----------<BR><b>DeletionProtectionEnabled</b>: '
                     'True<BR><b>ItemCount</b>: 900<BR><b>TableSizeBytes</b>: '
                     '123<BR><b>Replicas</b>: 0<BR><b>RCU</b>: 1<BR><b>WCU</b>: 1',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'prod-dynamo-table', self.node_type)

        # docs
        self.mcd = mcd
