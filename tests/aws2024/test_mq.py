from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_mq(self):
        # docs
        self.node_type = 'mq'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mq_arn = 'arn:aws:mq:eu-west-1:123456789012:mq/group-1/schedule-rate'
        metadata = {
            "DelaySeconds": 0,
            "FifoQueue": "TRUE",
            "ReceiveMessageWaitTimeSeconds": 0,
            "SqsManagedSseEnabled": "false",
            "VisibilityTimeout": 30
        }

        mcd.add_vertex(node_id=mq_arn, node_name='schedule-rate', node_type='mq', metadata=metadata)

        # then
        expected = {'id': 'vertex:mq:arn:aws:mq:eu-west-1:123456789012:mq/group-1/schedule-rate',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.mq;',
                    'value': '<b>Name</b>: schedule-rate<BR><b>ARN</b>: '
                             'arn:aws:mq:eu-west-1:123456789012:mq/group-1/schedule-rate<BR>-----------<BR><b>DelaySeconds</b>: '
                             '0<BR><b>FifoQueue</b>: '
                             'TRUE<BR><b>ReceiveMessageWaitTimeSeconds</b>: '
                             '0<BR><b>SqsManagedSseEnabled</b>: '
                             'false<BR><b>VisibilityTimeout</b>: 30',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'internal.fifo', 'mq')

        # docs
        self.mcd = mcd
