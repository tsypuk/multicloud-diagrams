from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_iam_role(self):
        # docs
        self.node_type = 'iam_role'

        # given
        mcd = MultiCloudDiagrams()

        # when
        iam_role_arn = 'arn:aws:iam::123456789012:role/ec2-cloudwatch-role'
        mcd.add_vertex(node_id=iam_role_arn, node_name='ec2-cloudwatch', node_type='iam_role')

        # then
        expected = {
            'id': 'vertex:iam_role:arn:aws:iam::123456789012:role/ec2-cloudwatch-role',
            'parent': '1',
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.role;fillColor=#759C3E;gradientColor=none;',
            'value': '<b>Name</b>: ec2-cloudwatch<BR><b>ARN</b>: '
                     'arn:aws:iam::123456789012:role/ec2-cloudwatch-role',
            'vertex': '1'
        }
        self.verify_resource(expected, mcd.mx_file, 'ec2-cloudwatch', 'iam_role')

        # docs
        self.mcd = mcd
