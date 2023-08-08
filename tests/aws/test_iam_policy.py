from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_iam_policy(self):
        # docs
        self.node_type = 'iam_policy'

        # given
        mcd = MultiCloudDiagrams()

        # when
        iam_policy_arn = 'arn:aws:iam::123456789012:policy/ecs-cloudwatch-userPolicy'
        mcd.add_vertex(node_id=iam_policy_arn, node_name='ecs-cloudwatch-userPolicy', arn=iam_policy_arn, node_type='iam_policy')

        # then
        expected = {
            'id': 'vertex:iam_policy:arn:aws:iam::123456789012:policy/ecs-cloudwatch-userPolicy',
            'parent': '1',
            'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F8624;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.policy;',
            'value': '<b>Name</b>: ecs-cloudwatch-userPolicy<BR><b>ARN</b>: '
                     'arn:aws:iam::123456789012:policy/ecs-cloudwatch-userPolicy',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'ecs-cloudwatch-userPolicy', 'iam_policy')

        # docs
        self.mcd = mcd
