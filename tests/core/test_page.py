from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_page(self):
        # docs
        self.node_type = 'page_2'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_page("second_page")
        mcd.add_layer('Processing')
        # Add lambda to 1st layer
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       layer_name="Processing")

        mcd.add_page("third_page")
        mcd.add_layer('Storage')
        # Add dynamo to 2nd layer
        mcd.add_vertex(node_id='arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
                       node_name='prod-dynamo-table',
                       node_type='dynamo',
                       layer_name="Storage")

        # return back to 1st page
        mcd.switch_page("second_page")
        mcd.add_vertex(node_id='arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table2',
                       node_name='prod-dynamo-table-2',
                       node_type='dynamo',
                       layer_name="Storage")
        # then
        # docs
        self.mcd = mcd
