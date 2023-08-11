from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_dynamo_stream(self):
        # docs
        self.node_type = 'dynamo_stream'

        # given
        mcd = MultiCloudDiagrams()

        # when
        stream_arn = 'arn:aws:dynamodb:eu-west-1:123456789012:table/test-table/stream'
        stream_name = '2022-12-05T06:41:33.817'
        metadata = {
            'LatestStreamLabel': '2022-12-05T06:41:33.817',
            'StreamViewType': 'NEW_AND_OLD_IMAGES'
        }

        mcd.add_vertex(node_id=stream_arn, node_name=stream_name, node_type='dynamo_stream', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:dynamo_stream:arn:aws:dynamodb:eu-west-1:123456789012:table/test-table/stream',
            'parent': '1',
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#2E27AD;strokeColor=none;dashed=0;'
                     'verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;'
                     'pointerEvents=1;shape=mxgraph.aws4.dynamodb_stream',
            'value': '<b>Name</b>: 2022-12-05T06:41:33.817<BR><b>ARN</b>: '
                     'arn:aws:dynamodb:eu-west-1:123456789012:table/test-table/stream<BR>-----------<BR><b>LatestStreamLabel</b>: '
                     '2022-12-05T06:41:33.817<BR><b>StreamViewType</b>: '
                     'NEW_AND_OLD_IMAGES',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, '2022-12-05T06:41:33.817', self.node_type)

        # docs
        self.mcd = mcd
