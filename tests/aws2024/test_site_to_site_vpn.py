from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_site_to_site_vpn(self):
        # docs
        self.node_type = 'site_to_site_vpn'

        # given
        mcd = MultiCloudDiagrams()

        # when
        site_to_site_vpn_service_arn = 'arn:aws:site_to_site_vpn:us-west-1:123456789012:service/site_to_site_vpn/123'
        site_to_site_vpn_name = 'Site to Site VPN'
        metadata = {
            'vpn_name': 'Office Seatle',
            'cidr': '172.23.20.20/0',
            'connection_endpoint': "202.1.1.14"
        }
        mcd.add_vertex(node_id=site_to_site_vpn_service_arn, node_name=site_to_site_vpn_name, node_type='site_to_site_vpn', metadata=metadata)

        # then
        expected = {'id': 'vertex:site_to_site_vpn:arn:aws:site_to_site_vpn:us-west-1:123456789012:service/site_to_site_vpn/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.site_to_site_vpn;',
                    'value': '<b>Name</b>: Site to Site VPN<BR><b>ARN</b>: '
                             'arn:aws:site_to_site_vpn:us-west-1:123456789012:service/site_to_site_vpn/123<BR>-----------<BR><b>vpn_name</b>: '
                             'Office Seatle<BR><b>cidr</b>: '
                             '172.23.20.20/0<BR><b>connection_endpoint</b>: 202.1.1.14',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'site_to_site_vpn', self.node_type)

        # docs
        self.mcd = mcd
