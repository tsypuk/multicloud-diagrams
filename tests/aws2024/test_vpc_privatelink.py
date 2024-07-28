from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_vpc_privatelink(self):
        # docs
        self.node_type = 'vpc_privatelink'

        # given
        mcd = MultiCloudDiagrams()

        # when
        vpc_privatelink_service_arn = 'arn:aws:vpc_privatelink:us-west-1:123456789012:service/vpc_privatelink/123'
        vpc_privatelink_name = 'Private Link Connection'
        metadata = {
            'service_name': 's3',
            'endpoint_url': 'https://bucket.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com'
        }
        mcd.add_vertex(node_id=vpc_privatelink_service_arn, node_name=vpc_privatelink_name, node_type='vpc_privatelink', metadata=metadata)

        # then
        expected = {'id': 'vertex:vpc_privatelink:arn:aws:vpc_privatelink:us-west-1:123456789012:service/vpc_privatelink/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.vpc_privatelink;',
                    'value': '<b>Name</b>: Private Link Connection<BR><b>ARN</b>: '
                             'arn:aws:vpc_privatelink:us-west-1:123456789012:service/vpc_privatelink/123<BR>-----------<BR><b>service_name</b>: '
                             's3<BR><b>endpoint_url</b>: '
                             'https://bucket.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'vpc_privatelink', self.node_type)

        # docs
        self.mcd = mcd
