from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_dynamo(self):
        # docs
        self.node_type = 'security_hub'

        # given
        mcd = MultiCloudDiagrams()

        # when
        hub_arn = 'arn:aws:security_hub:eu-west-1:123456789012:security_hub/1'
        security_hub = 'security_hub'
        metadata = {
            'WAF enabled': True,
            'DisablePorts': True,
            'Connected to ALB': 'IDs',
        }
        mcd.add_vertex(node_id=hub_arn, node_name=security_hub, node_type='security_hub', metadata=metadata)

        # then
        expected = {'id': 'vertex:security_hub:arn:aws:security_hub:eu-west-1:123456789012:security_hub/1',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.security_hub;',
                    'value': '<b>Name</b>: security_hub<BR><b>ARN</b>: '
                             'arn:aws:security_hub:eu-west-1:123456789012:security_hub/1<BR>-----------<BR><b>WAF '
                             'enabled</b>: True<BR><b>DisablePorts</b>: True<BR><b>Connected to '
                             'ALB</b>: IDs',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'security_hub', self.node_type)

        # docs
        self.mcd = mcd
