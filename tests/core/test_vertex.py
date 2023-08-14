from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_vertex(self):
        # docs
        self.node_type = 'vertex'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function')

        # then
        # docs
        self.mcd = mcd

    def test_vertex_metadata(self):
        # docs
        self.node_type = 'vertex_meta'

        # given
        mcd = MultiCloudDiagrams()
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

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       metadata=metadata)

        # then
        # docs
        self.mcd = mcd

    def test_edge(self):
        # docs
        self.node_type = 'edge'

        # given
        mcd = MultiCloudDiagrams()
        mcd.read_coords_from_file('docs/docs/core-components/output/drawio/edge.drawio')
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function')
        mcd.add_vertex(node_id='arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
                       node_name='prod-dynamo-table',
                       node_type='dynamo')

        # when
        mcd.add_link('lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name',
                     'dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
                     action=['GET permissions', 'GET userinfo'])

        # then
        # docs
        self.mcd = mcd
