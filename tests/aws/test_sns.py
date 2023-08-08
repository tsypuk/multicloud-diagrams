from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_sns(self):
        # docs
        self.node_type = 'sns'

        # given
        mcd = MultiCloudDiagrams()

        # when
        sns_arn = 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
        metadata = {
            "Owner": 123456789012,
            "SubscriptionsConfirmed": 3,
            "SubscriptionsPending": 0
        }
        mcd.add_vertex(node_id=sns_arn, node_name='internal.fifo', arn=sns_arn, node_type='sns', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:sns:arn:aws:sns:eu-west-1:123456789012:internal.fifo',
            'value': '<b>Name</b>: internal.fifo<BR><b>ARN</b>: arn:aws:sns:eu-west-1:123456789012:internal.fifo'
                     '<BR>-----------<BR>'
                     '<b>Owner</b>: 123456789012<BR><b>SubscriptionsConfirmed</b>: 3<BR><b>SubscriptionsPending</b>: 0',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'internal.fifo', 'sns')

        # docs
        self.mcd = mcd
