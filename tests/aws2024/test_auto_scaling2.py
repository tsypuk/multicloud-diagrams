from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_auto_scaling2(self):
        # docs
        self.node_type = 'auto_scaling2'

        # given
        mcd = MultiCloudDiagrams()

        # when
        auto_scaling2_service_arn = 'arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1'
        auto_scaling2_service_name = 'auto_scaling2'
        metadata = {
            'AutoScalingGroupName': 'web-instances',
            'PolicyName': 'scale-up',
            'PolicyARN': 'ARN',
            'PolicyType': 'inline',
            'AdjustmentType': 'negative',
            'MinAdjustmentStep': 2,
            'MinAdjustmentMagnitude': 2,
            'ScalingAdjustment': 5,
            'Cooldown': 4,
        }

        mcd.add_vertex(node_id=auto_scaling2_service_arn, node_name=auto_scaling2_service_name, node_type='auto_scaling2', metadata=metadata)

        # then
        expected = {'id': 'vertex:auto_scaling2:arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.auto_scaling2;',
                    'value': '<b>Name</b>: auto_scaling2<BR><b>ARN</b>: '
                             'arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1<BR>-----------<BR><b>AutoScalingGroupName</b>: '
                             'web-instances<BR><b>PolicyName</b>: scale-up<BR><b>PolicyARN</b>: '
                             'ARN<BR><b>PolicyType</b>: inline<BR><b>AdjustmentType</b>: '
                             'negative<BR><b>MinAdjustmentStep</b>: '
                             '2<BR><b>MinAdjustmentMagnitude</b>: 2<BR><b>ScalingAdjustment</b>: '
                             '5<BR><b>Cooldown</b>: 4',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'auto_scaling2', self.node_type)

        # docs
        self.mcd = mcd
