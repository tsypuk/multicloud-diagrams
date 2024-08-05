from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_global_accelerator(self):
        # docs
        self.node_type = 'global_accelerator'

        # given
        mcd = MultiCloudDiagrams()

        # when
        global_accelerator_service_arn = 'arn:aws:global_accelerator:us-west-1:123456789012:service/global_accelerator/123'
        global_accelerator_name = 'Global Accelerator'
        metadata = {
            'AcceleratorArn': 'ARN',
            'Name': 'cross-vertical-http',
            'IpAddressType': 'DUAL_STACK',
            'Enabled': True,
            'DnsName': 'local.dns.com',
            'Status': 'DEPLOYED',
            'CreatedTime': '2024-08-05',
            'DualStackDnsName': 'ipv4&v6',
        }
        mcd.add_vertex(node_id=global_accelerator_service_arn, node_name=global_accelerator_name, node_type='global_accelerator', metadata=metadata)

        # then
        expected = {'id': 'vertex:global_accelerator:arn:aws:global_accelerator:us-west-1:123456789012:service/global_accelerator/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.global_accelerator;',
                    'value': '<b>Name</b>: Global Accelerator<BR><b>ARN</b>: '
                             'arn:aws:global_accelerator:us-west-1:123456789012:service/global_accelerator/123<BR>-----------<BR><b>AcceleratorArn</b>: '
                             'ARN<BR><b>Name</b>: cross-vertical-http<BR><b>IpAddressType</b>: '
                             'DUAL_STACK<BR><b>Enabled</b>: True<BR><b>DnsName</b>: '
                             'local.dns.com<BR><b>Status</b>: DEPLOYED<BR><b>CreatedTime</b>: '
                             '2024-08-05<BR><b>DualStackDnsName</b>: ipv4&v6',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'global_accelerator', self.node_type)

        # docs
        self.mcd = mcd
