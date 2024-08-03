from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_vpc(self):
        # docs
        self.node_type = 'private_5g'

        # given
        mcd = MultiCloudDiagrams()

        # when
        private_5g_service_arn = 'arn:aws:private_5g:us-west-1:123456789012:service/private_5g/123'
        private_5g_name = 'Private 5g'
        metadata = {
            'geolocation-lat': 44,
            'geolocation-lon': 33,
            'license-application-date': '02-08-2024',
            'inter-connection-provider': 'Verizon'
        }
        mcd.add_vertex(node_id=private_5g_service_arn, node_name=private_5g_name, node_type='private_5g', metadata=metadata)

        # then
        expected = {'id': 'vertex:private_5g:arn:aws:private_5g:us-west-1:123456789012:service/private_5g/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.private_5g;',
                    'value': '<b>Name</b>: Private 5g<BR><b>ARN</b>: '
                             'arn:aws:private_5g:us-west-1:123456789012:service/private_5g/123<BR>-----------<BR><b>geolocation-lat</b>: '
                             '44<BR><b>geolocation-lon</b>: '
                             '33<BR><b>license-application-date</b>: '
                             '02-08-2024<BR><b>inter-connection-provider</b>: Verizon',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'private_5g', self.node_type)

        # docs
        self.mcd = mcd
