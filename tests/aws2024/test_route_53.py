from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_route_53(self):
        # docs
        self.node_type = 'route_53'

        # given
        mcd = MultiCloudDiagrams()

        # when
        route_53_service_arn = 'arn:aws:route_53:us-west-1:123456789012:service/route_53/123'
        route_53_service_name = 'Route53'
        metadata = {
            "serviceName": "route_53",
            'HostedZones': '4',
            'dnsSec': True,
            'Limit': 'MAX_HEALTH_CHECKS_BY_OWNER',
            'HealthCheckConfig': {
                'IPAddress': '127.0.0.1',
                'Port': 433,
                'Type': 'HTTP | HTTPS'
            }
        }
        mcd.add_vertex(node_id=route_53_service_arn, node_name=route_53_service_name, node_type='route_53', metadata=metadata)

        # then
        expected = {'id': 'vertex:route_53:arn:aws:route_53:us-west-1:123456789012:service/route_53/123',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.route_53;fillColor=#F58536;gradientColor=none;',
                    'value': '<b>Name</b>: Route53<BR><b>ARN</b>: '
                             'arn:aws:route_53:us-west-1:123456789012:service/route_53/123<BR>-----------<BR><b>serviceName</b>: '
                             'route_53<BR><b>HostedZones</b>: 4<BR><b>dnsSec</b>: '
                             'True<BR><b>Limit</b>: '
                             'MAX_HEALTH_CHECKS_BY_OWNER<BR><b>HealthCheckConfig</b>: '
                             "{'IPAddress': '127.0.0.1', 'Port': 433, 'Type': 'HTTP | HTTPS'}",
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'route_53', self.node_type)

        # docs
        self.mcd = mcd
