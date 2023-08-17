from multicloud_diagrams import MultiCloudDiagrams, update_style_by_key

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
        mcd.add_vertex(node_id=sns_arn, node_name='internal.fifo', node_type='sns', metadata=metadata)

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

    def test_add_custom_node_color(self):
        # given
        mcd = MultiCloudDiagrams()
        node_style = {'fillColor': '#FF0000'}

        sns_arn = 'arn:aws:sns:eu-west-1:123456789012:internal.fifo'
        metadata = {
            "Owner": 123456789012,
            "SubscriptionsConfirmed": 3,
            "SubscriptionsPending": 0
        }

        # when
        mcd.add_vertex(node_id=sns_arn, node_name='internal.fifo', node_type='sns', metadata=metadata,
                       style=node_style)

        # then
        expected = {
            'id': 'vertex:sns:arn:aws:sns:eu-west-1:123456789012:internal.fifo',
            'value': '<b>Name</b>: internal.fifo<BR><b>ARN</b>: arn:aws:sns:eu-west-1:123456789012:internal.fifo'
                     '<BR>-----------<BR>'
                     '<b>Owner</b>: 123456789012<BR><b>SubscriptionsConfirmed</b>: 3<BR><b>SubscriptionsPending</b>: 0',
            'parent': '1',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'internal.fifo', 'sns', style=node_style)

    def test_update_fill_color(self):
        # given
        style = "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;"
        color = '#FF0000'

        # when
        result = update_style_by_key(style_str=style, key='fillColor', value=color)

        # then
        expected = "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#FF0000;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;"
        self.assertEqual(expected, result)

    def test_no_fill_color(self):
        # given
        style = "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;"
        color = '#FF0000'

        # when
        result = update_style_by_key(style_str=style, key='fillColor', value=color)

        # then
        expected = "sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;fillColor=#FF0000;"
        self.assertEqual(expected, result)
