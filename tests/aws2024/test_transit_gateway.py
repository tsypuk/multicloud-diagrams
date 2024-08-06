from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_transit_gateway(self):
        # docs
        self.node_type = 'transit_gateway'

        # given
        mcd = MultiCloudDiagrams()

        # when
        transit_gateway_service_arn = 'arn:aws:transit_gateway:us-west-1:123456789012:service/transit_gateway/123'
        transit_gateway_name = 'Transit Gateway'
        metadata = {
            'TransitGatewayId': 1,
            'TransitGatewayArn': 'ARN',
            'State': 'available',
            'OwnerId': 'acc-id',
            'CreationTime': '2024-08-06',
            'AutoAcceptSharedAttachments': 'enable',
            'DefaultRouteTableAssociation': 'enable',
            'DefaultRouteTablePropagation': 'enable',
            'VpnEcmpSupport': 'disable',
            'DnsSupport': 'enable',
            'SecurityGroupReferencingSupport': 'enable',
            'MulticastSupport': 'enable'
        }
        mcd.add_vertex(node_id=transit_gateway_service_arn, node_name=transit_gateway_name, node_type='transit_gateway', metadata=metadata)

        # then
        expected = {'id': 'vertex:transit_gateway:arn:aws:transit_gateway:us-west-1:123456789012:service/transit_gateway/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;',
                    'value': '<b>Name</b>: Transit Gateway<BR><b>ARN</b>: '
                             'arn:aws:transit_gateway:us-west-1:123456789012:service/transit_gateway/123<BR>-----------<BR><b>TransitGatewayId</b>: '
                             '1<BR><b>TransitGatewayArn</b>: ARN<BR><b>State</b>: '
                             'available<BR><b>OwnerId</b>: acc-id<BR><b>CreationTime</b>: '
                             '2024-08-06<BR><b>AutoAcceptSharedAttachments</b>: '
                             'enable<BR><b>DefaultRouteTableAssociation</b>: '
                             'enable<BR><b>DefaultRouteTablePropagation</b>: '
                             'enable<BR><b>VpnEcmpSupport</b>: disable<BR><b>DnsSupport</b>: '
                             'enable<BR><b>SecurityGroupReferencingSupport</b>: '
                             'enable<BR><b>MulticastSupport</b>: enable',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'transit_gateway', self.node_type)

        # docs
        self.mcd = mcd
