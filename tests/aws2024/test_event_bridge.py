from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_event_bridge(self):
        # docs
        self.node_type = 'event_bridge'

        # given
        mcd = MultiCloudDiagrams()

        # when
        event_bridge_arn = 'arn:aws:scheduler:eu-west-1:123456789012:schedule/group-1/schedule-rate'
        metadata = {
            "Creation Date": "2023-06-19 13:16:38",
            "End Date": "2023-09-30 12:30:00",
            "SubscriptionsPending": 0,
            "Flexible Time Window": "{'Mode': 'OFF'}",
            "Group Name": "group-1",
            "input": '{"key1":"val1","key2":"val2"}',
            "Modification Date": "2023-06-19 13:30:33",
            "Retry Policy": "{'MaximumEventAgeInSeconds': 86400, 'MaximumRetryAttempts': 185}",
            "Role ARN": "arn:aws:iam::123456789012:role/serverless/event_bridge_role",
            "Schedule Expression": "rate(60 days)",
            "Schedule Expression_timezone": "UTC",
            "State": "ENABLED",
            "Target": "arn:aws:lambda:eu-west-1:123456789012:function:target-lambda"
        }

        mcd.add_vertex(node_id=event_bridge_arn, node_name='schedule-rate', node_type='event_bridge', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:event_bridge:arn:aws:scheduler:eu-west-1:123456789012:schedule/group-1/schedule-rate',
            'parent': '1',
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;'
                     'dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;'
                     'resIcon=mxgraph.aws4.eventbridge;',
            'value': '<b>Name</b>: schedule-rate<BR><b>ARN</b>: '
                     'arn:aws:scheduler:eu-west-1:123456789012:schedule/group-1/schedule-rate<BR>-----------<BR><b>Creation '
                     'Date</b>: 2023-06-19 13:16:38<BR><b>End Date</b>: 2023-09-30 '
                     '12:30:00<BR><b>SubscriptionsPending</b>: 0<BR><b>Flexible Time '
                     "Window</b>: {'Mode': 'OFF'}<BR><b>Group Name</b>: "
                     'group-1<BR><b>input</b>: '
                     '{"key1":"val1","key2":"val2"}<BR><b>Modification Date</b>: '
                     '2023-06-19 13:30:33<BR><b>Retry Policy</b>: '
                     "{'MaximumEventAgeInSeconds': 86400, 'MaximumRetryAttempts': "
                     '185}<BR><b>Role ARN</b>: '
                     'arn:aws:iam::123456789012:role/serverless/event_bridge_role<BR><b>Schedule '
                     'Expression</b>: rate(60 days)<BR><b>Schedule '
                     'Expression_timezone</b>: UTC<BR><b>State</b>: '
                     'ENABLED<BR><b>Target</b>: '
                     'arn:aws:lambda:eu-west-1:123456789012:function:target-lambda',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'internal.fifo', 'event_bridge')

        # docs
        self.mcd = mcd
