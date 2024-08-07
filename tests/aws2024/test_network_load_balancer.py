from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_network_load_balancer(self):
        # docs
        self.node_type = 'network_load_balancer'

        # given
        mcd = MultiCloudDiagrams()

        # when
        network_load_balancer_service_arn = 'arn:aws:network_load_balancer:us-west-1:123456789012:service/network_load_balancer/123'
        network_load_balancer_name = 'Network Load Balancer'
        metadata = {
            'LoadBalancerArn': 'ARN',
            'DNSName': 'test',
            'CanonicalHostedZoneId': '4',
            'CreatedTime': '2024-08-07',
            'LoadBalancerName': 'ingestion',
            'Scheme': 'internet-facing',
            'VpcId': 'test-vpc',
        }
        mcd.add_vertex(node_id=network_load_balancer_service_arn, node_name=network_load_balancer_name, node_type='network_load_balancer', metadata=metadata)

        # then
        expected = {'id': 'vertex:network_load_balancer:arn:aws:network_load_balancer:us-west-1:123456789012:service/network_load_balancer/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.network_load_balancer;',
                    'value': '<b>Name</b>: Network Load Balancer<BR><b>ARN</b>: '
                             'arn:aws:network_load_balancer:us-west-1:123456789012:service/network_load_balancer/123<BR>-----------<BR><b>LoadBalancerArn</b>: '
                             'ARN<BR><b>DNSName</b>: test<BR><b>CanonicalHostedZoneId</b>: '
                             '4<BR><b>CreatedTime</b>: 2024-08-07<BR><b>LoadBalancerName</b>: '
                             'ingestion<BR><b>Scheme</b>: internet-facing<BR><b>VpcId</b>: '
                             'test-vpc',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'network_load_balancer', self.node_type)

        # docs
        self.mcd = mcd
