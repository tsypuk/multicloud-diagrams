from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_elastic_network_adapter(self):
        # docs
        self.node_type = 'elastic_network_adapter'

        # given
        mcd = MultiCloudDiagrams()

        # when
        elastic_network_adapter_service_arn = 'arn:aws:elastic_network_adapter:us-west-1:123456789012:service/elastic_network_adapter/123'
        elastic_network_adapter_name = 'Elastic Network Adapter'
        metadata = {
            'AllocationId': 'test',
            'AssociationId': '4',
            'IpOwnerId': 'main-account',
            'PublicDnsName': 'test.com',
            'PublicIp': '127.0.0.1',
            'CustomerOwnedIp': 'org',
            'CarrierIp': '127.0.0.1'
        }
        mcd.add_vertex(node_id=elastic_network_adapter_service_arn, node_name=elastic_network_adapter_name, node_type='elastic_network_adapter', metadata=metadata)

        # then
        expected = {'id': 'vertex:elastic_network_adapter:arn:aws:elastic_network_adapter:us-west-1:123456789012:service/elastic_network_adapter/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.elastic_network_adapter;',
                    'value': '<b>Name</b>: Elastic Network Adapter<BR><b>ARN</b>: '
                             'arn:aws:elastic_network_adapter:us-west-1:123456789012:service/elastic_network_adapter/123<BR>-----------<BR><b>AllocationId</b>: '
                             'test<BR><b>AssociationId</b>: 4<BR><b>IpOwnerId</b>: '
                             'main-account<BR><b>PublicDnsName</b>: test.com<BR><b>PublicIp</b>: '
                             '127.0.0.1<BR><b>CustomerOwnedIp</b>: org<BR><b>CarrierIp</b>: '
                             '127.0.0.1',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'elastic_network_adapter', self.node_type)

        # docs
        self.mcd = mcd
