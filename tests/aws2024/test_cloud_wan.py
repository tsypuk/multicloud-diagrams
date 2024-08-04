from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_cloud_wan(self):
        # docs
        self.node_type = 'cloud_wan'

        # given
        mcd = MultiCloudDiagrams()

        # when
        cloud_wan_service_arn = 'arn:aws:cloud_wan:us-west-1:123456789012:service/cloud_wan/123'
        cloud_wan_name = 'Private 5g'
        metadata = {
            'ASN-interconnect': 4405,
            'ANS': 3301,
            'edge-location': 'us-east-1',
            'attachment': 'Site-to-Site-ID'
        }
        mcd.add_vertex(node_id=cloud_wan_service_arn, node_name=cloud_wan_name, node_type='cloud_wan', metadata=metadata)

        # then
        expected = {'id': 'vertex:cloud_wan:arn:aws:cloud_wan:us-west-1:123456789012:service/cloud_wan/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloud_wan;',
                    'value': '<b>Name</b>: Private 5g<BR><b>ARN</b>: '
                             'arn:aws:cloud_wan:us-west-1:123456789012:service/cloud_wan/123<BR>-----------<BR><b>ASN-interconnect</b>: '
                             '4405<BR><b>ANS</b>: 3301<BR><b>edge-location</b>: '
                             'us-east-1<BR><b>attachment</b>: Site-to-Site-ID',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'cloud_wan', self.node_type)

        # docs
        self.mcd = mcd
