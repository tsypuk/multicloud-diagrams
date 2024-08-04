from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_vpc_lattice(self):
        # docs
        self.node_type = 'vpc_lattice'

        # given
        mcd = MultiCloudDiagrams()

        # when
        vpc_lattice_service_arn = 'arn:aws:vpc_lattice:us-west-1:123456789012:service/vpc_lattice/123'
        vpc_lattice_name = 'Virtual Private Network'
        metadata = {
            'vpc_name': 'private VPC',
            'cidr': '172.23.20.20/0',
            'subnets': "A,B,C"
        }
        mcd.add_vertex(node_id=vpc_lattice_service_arn, node_name=vpc_lattice_name, node_type='vpc_lattice', metadata=metadata)

        # then
        expected = {'id': 'vertex:vpc_lattice:arn:aws:vpc_lattice:us-west-1:123456789012:service/vpc_lattice/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.vpc_lattice;',
                    'value': '<b>Name</b>: Virtual Private Network<BR><b>ARN</b>: '
                             'arn:aws:vpc_lattice:us-west-1:123456789012:service/vpc_lattice/123<BR>-----------<BR><b>vpc_name</b>: '
                             'private VPC<BR><b>cidr</b>: 172.23.20.20/0<BR><b>subnets</b>: A,B,C',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'vpc_lattice', self.node_type)

        # docs
        self.mcd = mcd
