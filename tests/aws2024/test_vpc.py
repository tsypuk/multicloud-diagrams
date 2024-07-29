from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_vpc(self):
        # docs
        self.node_type = 'vpc'

        # given
        mcd = MultiCloudDiagrams()

        # when
        vpc_privatelink_service_arn = 'arn:aws:vpc:us-west-1:123456789012:service/vpc/123'
        vpc_privatelink_name = 'Virtual Private Network'
        metadata = {
            'vpc_name': 'private VPC',
            'cidr': '172.23.20.20/0',
            'subnets': "A,B,C"
        }
        mcd.add_vertex(node_id=vpc_privatelink_service_arn, node_name=vpc_privatelink_name, node_type='vpc', metadata=metadata)

        # then
        expected = {'id': 'vertex:vpc:arn:aws:vpc:us-west-1:123456789012:service/vpc/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.vpc;',
                    'value': '<b>Name</b>: Virtual Private Network<BR><b>ARN</b>: '
                             'arn:aws:vpc:us-west-1:123456789012:service/vpc/123<BR>-----------<BR><b>vpc_name</b>: '
                             'private VPC<BR><b>cidr</b>: 172.23.20.20/0<BR><b>subnets</b>: A,B,C',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'vpc', self.node_type)

        # docs
        self.mcd = mcd
