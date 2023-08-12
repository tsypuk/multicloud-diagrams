from multicloud_diagrams import MultiCloudDiagrams
from utils.utils import TestUtilities


class TestAWSVertexInIsolation(TestUtilities):

    def test_read_from_file(self):
        # docs
        self.node_type = 'lambda_function'

        # given
        mcd = MultiCloudDiagrams()

        # when
        file_name = f'docs/docs/aws-components/output/drawio/{self.node_type}.drawio'
        mcd.read_nodes_from_file(file_name)

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
        self.verify_resource(expected, mcd.mx_file, 'producer-lambda', 'lambda_function')

        # docs
        self.mcd = mcd
