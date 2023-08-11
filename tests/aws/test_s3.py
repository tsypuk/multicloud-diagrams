from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_s3(self):
        # docs
        self.node_type = 's3'

        # given
        mcd = MultiCloudDiagrams()

        # when
        s3_arn = 'arn:aws:s3:::content_bucket'

        metadata = {
            'x-amz-bucket-region': 'eu-west-1',
            'CreationDate': '2023-11-11',
            'Transitions': "[{'Days': 60, 'StorageClass': 'GLACIER'}]",
            'AbortIncompleteMultipartUpload': "{'DaysAfterInitiation': 5}",
            'PublicAccessBlockConfiguration': "{'BlockPublicAcls': True, 'IgnorePublicAcls': True, 'BlockPublicPolicy': True, 'RestrictPublicBuckets': True}",
            'Expiration': "{'Days': 90}",
            'LifecycleConfiguration': 'NO',
            'CORSConfiguration': 'NO',
            'LoggingConfiguration': 'NO',
            'Versioning': 'Enabled',
            'MFADelete': 'Disabled'
        }

        mcd.add_vertex(node_id=s3_arn, node_name='content_bucket', node_type='s3', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:s3:arn:aws:s3:::content_bucket',
            'parent': '1',
            'style': 'outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.bucket_with_objects;fillColor=#E05243;gradientColor=none;',
            'value': '<b>Name</b>: content_bucket<BR><b>ARN</b>: '
                     'arn:aws:s3:::content_bucket<BR>-----------<BR><b>x-amz-bucket-region</b>: '
                     'eu-west-1<BR><b>CreationDate</b>: 2023-11-11<BR><b>Transitions</b>: '
                     "[{'Days': 60, 'StorageClass': "
                     "'GLACIER'}]<BR><b>AbortIncompleteMultipartUpload</b>: "
                     "{'DaysAfterInitiation': "
                     "5}<BR><b>PublicAccessBlockConfiguration</b>: {'BlockPublicAcls': "
                     "True, 'IgnorePublicAcls': True, 'BlockPublicPolicy': True, "
                     "'RestrictPublicBuckets': True}<BR><b>Expiration</b>: {'Days': "
                     '90}<BR><b>LifecycleConfiguration</b>: '
                     'NO<BR><b>CORSConfiguration</b>: NO<BR><b>LoggingConfiguration</b>: '
                     'NO<BR><b>Versioning</b>: Enabled<BR><b>MFADelete</b>: Disabled',
            'vertex': '1'
        }

        self.verify_resource(expected, mcd.mx_file, 'content_bucket', 's3')

        # docs
        self.mcd = mcd
