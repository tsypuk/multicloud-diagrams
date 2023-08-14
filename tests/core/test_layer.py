from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_layer(self):
        # docs
        self.node_type = 'layer_3'

        # given
        mcd = MultiCloudDiagrams()
        output_file = 'docs/docs/core-components/output/drawio/layer_3.drawio'
        mcd.read_coords_from_file(output_file)

        # when
        # Create 2 layers
        mcd.add_layer('Processing')
        mcd.add_layer('Storage')

        # Add lambda to 1st layer
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       layer_name="Processing")

        # Add dynamo to 2nd layer
        mcd.add_vertex(node_id='arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
                       node_name='prod-dynamo-table',
                       node_type='dynamo',
                       layer_name="Storage")
        mcd.add_link('lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name',
                     'dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
                     action=['GET permissions'])

        # then
        # docs
        self.mcd = mcd
