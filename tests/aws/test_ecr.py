from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_ecr(self):
        # docs
        self.node_type = 'ecr'

        # given
        mcd = MultiCloudDiagrams()

        # when
        ecr_arn = 'arn:i-1234567890abcdef0'
        ecr_name = 'Registry for images'
        metadata = {
            "images": 23,
            "ImageId": "ami-0abcdef1234567890",
            "multiarch": 13,
        }
        mcd.add_vertex(node_id=ecr_arn, node_name=ecr_name, node_type='ecr', metadata=metadata)

        # then
        expected = {'id': 'vertex:ecr:arn:i-1234567890abcdef0',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.ecr;fillColor=#F58534;gradientColor=none;',
                    'value': '<b>Name</b>: Registry for images<BR><b>ARN</b>: '
                             'arn:i-1234567890abcdef0<BR>-----------<BR><b>images</b>: '
                             '23<BR><b>ImageId</b>: ami-0abcdef1234567890<BR><b>multiarch</b>: 13',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'ECR', self.node_type)

        # docs
        self.mcd = mcd
