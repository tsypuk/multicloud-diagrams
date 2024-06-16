from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_glue(self):
        # docs
        self.node_type = 'kinesis_video_stream'

        # given
        mcd = MultiCloudDiagrams()

        # when
        kinesis_video_stream_service_arn = 'arn:aws:kinesis_video_stream:us-west-1:123456789012:kinesis_video_stream/glue/1'
        kinesis_video_stream_service_name = 'Glue'
        metadata = {
            'stateMachineArn': 'arn:aws:kinesis_video_stream:us-west-1:123456789012:service/kinesis_video_stream/machine1',
            'StreamName': 'web-video-stream',
            'MediaType': 'mpg4',
            'KmsKeyId': 'arn:aws:kms:us-west-1:123456789012:service/kms/k1',
            'Version': 'string',
            'Status': 'ACTIVE',
            'DataRetentionInHours': 36
        }
        mcd.add_vertex(node_id=kinesis_video_stream_service_arn, node_name=kinesis_video_stream_service_name, node_type='kinesis_video_stream', metadata=metadata)

        # then
        expected = {'id': 'vertex:kinesis_video_stream:arn:aws:kinesis_video_stream:us-west-1:123456789012:kinesis_video_stream/glue/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kinesis_video_streams;',
                    'value': '<b>Name</b>: Glue<BR><b>ARN</b>: '
                             'arn:aws:kinesis_video_stream:us-west-1:123456789012:kinesis_video_stream/glue/1<BR>-----------<BR><b>stateMachineArn</b>: '
                             'arn:aws:kinesis_video_stream:us-west-1:123456789012:service/kinesis_video_stream/machine1<BR><b>StreamName</b>: '
                             'web-video-stream<BR><b>MediaType</b>: mpg4<BR><b>KmsKeyId</b>: '
                             'arn:aws:kms:us-west-1:123456789012:service/kms/k1<BR><b>Version</b>: '
                             'string<BR><b>Status</b>: ACTIVE<BR><b>DataRetentionInHours</b>: 36',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'kinesis_video_stream', self.node_type)

        # docs
        self.mcd = mcd
