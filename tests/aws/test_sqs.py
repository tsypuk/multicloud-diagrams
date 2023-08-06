from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities
# NOTE!!! Content of this file is mapped to documentation with lines position

class TestAWSVertexInIsolation(TestUtilities):

    def test_sqs(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        sqs_arn = 'arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo'
        metadata = {
            "DelaySeconds": 0,
            "FifoQueue": "TRUE",
            "ReceiveMessageWaitTimeSeconds": 0,
            "SqsManagedSseEnabled": "false",
            "VisibilityTimeout": 30
        }
        mcd.add_vertex(node_id=sqs_arn, node_name='int-eu-live-events.fifo', arn=sqs_arn, node_type='sqs', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo',
            'value': '<b>Name</b>: int-eu-live-events.fifo<BR><b>ARN</b>: arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo'
                     '<BR>-----------<BR>'
                     '<b>DelaySeconds</b>: 0<BR><b>FifoQueue</b>: TRUE<BR><b>ReceiveMessageWaitTimeSeconds</b>: 0<BR><b>SqsManagedSseEnabled</b>: false<BR><b>VisibilityTimeout</b>: 30',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_aws_resource(expected, mcd.mx_file, 'int-eu-live-events.fifo', 'sqs')
