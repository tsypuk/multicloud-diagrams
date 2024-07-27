from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestAWSVertexInIsolation(TestRendering):

    def test_cloudfront(self):
        # docs
        self.node_type = 'cloudfront'

        # given
        mcd = MultiCloudDiagrams()

        # when
        cloudfront_service_arn = 'arn:aws:cloudfront:us-west-1:123456789012:service/cloudfront/123'
        cloudfront_name = 'Code Catalyst'
        metadata = {
            'Name': 'Token validation',
            'Status': 'active',
            'Runtime': 'cloudfront-js-1.0',
            'FunctionMetadata': 'env data',
            'FunctionARN': 'ARN',
        }
        mcd.add_vertex(node_id=cloudfront_service_arn, node_name=cloudfront_name, node_type='cloudfront', metadata=metadata)

        # then
        expected = {'id': 'vertex:cloudfront:arn:aws:cloudfront:us-west-1:123456789012:service/cloudfront/123',
                    'parent': '1',
                    'style': 'sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;',
                    'value': '<b>Name</b>: Code Catalyst<BR><b>ARN</b>: '
                             'arn:aws:cloudfront:us-west-1:123456789012:service/cloudfront/123<BR>-----------<BR><b>Name</b>: '
                             'Token validation<BR><b>Status</b>: active<BR><b>Runtime</b>: '
                             'cloudfront-js-1.0<BR><b>FunctionMetadata</b>: env '
                             'data<BR><b>FunctionARN</b>: ARN',
                    'vertex': '1'}
        self.verify_resource(expected, mcd.mx_file, 'cloudfront', self.node_type)

        # docs
        self.mcd = mcd
