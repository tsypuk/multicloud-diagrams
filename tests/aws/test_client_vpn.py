from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_dynamo(self):
        # docs
        self.node_type = 'client_vpn'

        # given
        mcd = MultiCloudDiagrams()

        # when
        vpn_arn = 'aws:clientvpn:us-west-1:prod/cvpn-endpoint-0e3b'
        vpn_name = 'vpc-client-vpn'
        metadata = {
            'SplitTunnel': False,
            'DNSServer': '8.8.8.8',
            'VPNProtocol': 'openVPN',
            'Transport': 'UDP',
            'VPNPort': 443,
            'ClientCertificateARN': 'arn:aws:acm:us-west-1:123456789012:certificate/cd2e',
            'ServerCertificateARN': 'arn:aws:acm:us-west-1:123456789012:certificate/7d100',
            'Authentication type': 'certificate-authentication',
            'DNS Name': '*.cvpn-endpoint-0e3b.prod.clientvpn.us-west-1.amazonaws.com'
        }
        mcd.add_vertex(node_id=vpn_arn, node_name=vpn_name, node_type='client_vpn', metadata=metadata)

        # then
        expected = {'id': 'vertex:client_vpn:aws:clientvpn:us-west-1:prod/cvpn-endpoint-0e3b',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.client_vpn;',
                    'value': '<b>Name</b>: vpc-client-vpn<BR><b>ARN</b>: '
                             'aws:clientvpn:us-west-1:prod/cvpn-endpoint-0e3b<BR>-----------<BR><b>SplitTunnel</b>: '
                             'False<BR><b>DNSServer</b>: 8.8.8.8<BR><b>VPNProtocol</b>: '
                             'openVPN<BR><b>Transport</b>: UDP<BR><b>VPNPort</b>: '
                             '443<BR><b>ClientCertificateARN</b>: '
                             'arn:aws:acm:us-west-1:123456789012:certificate/cd2e<BR><b>ServerCertificateARN</b>: '
                             'arn:aws:acm:us-west-1:123456789012:certificate/7d100<BR><b>Authentication '
                             'type</b>: certificate-authentication<BR><b>DNS Name</b>: '
                             '*.cvpn-endpoint-0e3b.prod.clientvpn.us-west-1.amazonaws.com',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'vpc-client-vpn', self.node_type)

        # docs
        self.mcd = mcd
