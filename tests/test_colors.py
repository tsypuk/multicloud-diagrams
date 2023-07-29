from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities


class TestMultiCloudDiagramsColors(TestUtilities):

    def test_add_default_node_color(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        sns_arn = 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
        metadata = {
            "Owner": 123456789012,
            "SubscriptionsConfirmed": 3,
            "SubscriptionsPending": 0
        }
        mcd.add_vertex(id=sns_arn, node_name='internal.fifo', arn=sns_arn, node_type='sns', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:sns:arn:aws:sns:eu-west-1:123456789012:internal.fifo',
            'value': '<b>Name</b>: internal.fifo<BR><b>ARN</b>: arn:aws:sns:eu-west-1:123456789012:internal.fifo<BR>-----------<BR><b>Owner</b>: 123456789012<BR><b>SubscriptionsConfirmed</b>: 3<BR><b>SubscriptionsPending</b>: 0',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_aws_resource(expected, mcd.mx_file, 'internal.fifo', 'sns')

    def test_add_custom_node_color(self):
        # given
        mcd = MultiCloudDiagrams()
        node_color = '#FF0000'

        sns_arn = 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
        metadata = {
            "Owner": 123456789012,
            "SubscriptionsConfirmed": 3,
            "SubscriptionsPending": 0
        }

        # when
        mcd.add_vertex(id=sns_arn, node_name='internal.fifo', arn=sns_arn, node_type='sns', metadata=metadata, fill_color=node_color)

        # then
        expected = {
            'id': 'vertex:sns:arn:aws:sns:eu-west-1:123456789012:internal.fifo',
            'value': '<b>Name</b>: internal.fifo<BR><b>ARN</b>: arn:aws:sns:eu-west-1:123456789012:internal.fifo<BR>-----------<BR><b>Owner</b>: 123456789012<BR><b>SubscriptionsConfirmed</b>: 3<BR><b>SubscriptionsPending</b>: 0',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_aws_resource(expected, mcd.mx_file, 'internal.fifo', 'sns', fill_color=node_color)
