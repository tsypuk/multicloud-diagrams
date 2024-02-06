from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_glacier(self):
        # docs
        self.node_type = 'glacier'

        # given
        mcd = MultiCloudDiagrams()

        # when
        glacier_arn = 'arn:aws:glacier:::content_bucket'

        metadata = {
            'x-amz-bucket-region': 'eu-west-1',
            'CreationDate': '2023-11-11',
            'AbortIncompleteMultipartUpload': "{'DaysAfterInitiation': 5}",
            'Expiration': "{'Days': 90}",
            'MFADelete': 'Disabled'
        }

        mcd.add_vertex(node_id=glacier_arn, node_name='content_bucket', node_type='glacier', metadata=metadata)

        # then
        expected = {'id': 'vertex:glacier:arn:aws:glacier:::content_bucket',
                    'parent': '1',
                    'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.glacier;fillColor=#E05243;gradientColor=none;',
                    'value': '<b>Name</b>: content_bucket<BR><b>ARN</b>: '
                             'arn:aws:glacier:::content_bucket<BR>-----------<BR><b>x-amz-bucket-region</b>: '
                             'eu-west-1<BR><b>CreationDate</b>: '
                             '2023-11-11<BR><b>AbortIncompleteMultipartUpload</b>: '
                             "{'DaysAfterInitiation': 5}<BR><b>Expiration</b>: {'Days': "
                             '90}<BR><b>MFADelete</b>: Disabled',
                    'vertex': '1'}

        self.verify_resource(expected, mcd.mx_file, 'content_bucket', 'glacier')

        # docs
        self.mcd = mcd
