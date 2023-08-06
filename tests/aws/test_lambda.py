from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities
# NOTE!!! Content of this file is mapped to documentation with lines position

class TestAWSVertexInIsolation(TestUtilities):

    def test_lambda(self):
        # given
        mcd = MultiCloudDiagrams()

        # when
        func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:producer-lambda'
        metadata = {
            "CodeSize": 1234,
            "Handler": "main",
            "Layers": 0,
            "Memory": 128,
            "PackageType": "Zip",
            "Runtime": "go1.x",
            "Timeout": 30,
            "TracingConfig": "{'Mode': 'Active'}",
            "Version": "$LATEST"
        }
        mcd.add_vertex(node_id=func_arn, node_name='producer-lambda', arn=func_arn, node_type='lambda_function', metadata=metadata)

        # then
        expected = {
            'id': 'vertex:lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:producer-lambda',
            'value': "<b>Name</b>: producer-lambda<BR><b>ARN</b>: arn:aws:lambda:eu-west-1:123456789012:function:producer-lambda"
                     "<BR>-----------<BR>"
                     "<b>CodeSize</b>: 1234<BR><b>Handler</b>: main<BR><b>Layers</b>: 0<BR><b>Memory</b>: 128<BR><b>PackageType</b>: Zip<BR>"
                     "<b>Runtime</b>: go1.x<BR><b>Timeout</b>: 30<BR><b>TracingConfig</b>: {'Mode': 'Active'}<BR><b>Version</b>: $LATEST",
            'parent': '1',
            'vertex': '1'
        }
        self.verify_aws_resource(expected, mcd.mx_file, 'producer-lambda', 'lambda_function')
