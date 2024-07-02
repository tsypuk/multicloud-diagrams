from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_timestream(self):
        # docs
        self.node_type = 'timestream'

        # given
        mcd = MultiCloudDiagrams()

        # when
        timestream_service_arn = 'arn:aws:timestream:us-west-1:123456789012:timestream/glue/1'
        timestream_service_name = 'Timestream'
        metadata = {
            'Arn': 'ARN',
            'TableName': 'DataLocator',
            'DatabaseName': 'Primary',
            'TableStatus': 'ACTIVE',
            'MemoryStoreRetentionPeriodInHours': 2,
            'MagneticStoreRetentionPeriodInDays': 1,
            'EnableMagneticStoreWrites': True,
            'MagneticStoreRejectedDataLocation': {
                'S3Configuration': {
                    'BucketName': 'backup',
                    'EncryptionOption': 'SSE_S3',
                }
            },
            'CompositePartitionKey': [
                {
                    'Type': 'DIMENSION',
                    'Name': 'D1',
                    'EnforcementInRecord': 'REQUIRED',
                },
            ]
        }

        mcd.add_vertex(node_id=timestream_service_arn, node_name=timestream_service_name, node_type='timestream', metadata=metadata)

        # then
        expected = {'id': 'vertex:timestream:arn:aws:timestream:us-west-1:123456789012:timestream/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.timestream;',
                    'value': '<b>Name</b>: Timestream<BR><b>ARN</b>: '
                             'arn:aws:timestream:us-west-1:123456789012:timestream/glue/1<BR>-----------<BR><b>Arn</b>: '
                             'ARN<BR><b>TableName</b>: DataLocator<BR><b>DatabaseName</b>: '
                             'Primary<BR><b>TableStatus</b>: '
                             'ACTIVE<BR><b>MemoryStoreRetentionPeriodInHours</b>: '
                             '2<BR><b>MagneticStoreRetentionPeriodInDays</b>: '
                             '1<BR><b>EnableMagneticStoreWrites</b>: '
                             'True<BR><b>MagneticStoreRejectedDataLocation</b>: '
                             "{'S3Configuration': {'BucketName': 'backup', 'EncryptionOption': "
                             "'SSE_S3'}}<BR><b>CompositePartitionKey</b>: [{'Type': 'DIMENSION', "
                             "'Name': 'D1', 'EnforcementInRecord': 'REQUIRED'}]",
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'timestream', self.node_type)

        # docs
        self.mcd = mcd
