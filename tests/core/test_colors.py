from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_color_red(self):
        # docs
        self.node_type = 'color_red'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       style={'fillColor': '#FF0000'})

        # then
        # docs
        self.mcd = mcd

    def test_color_blue(self):
        # docs
        self.node_type = 'color_blue'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       style={'fillColor': '#0000FF'})

        # then
        # docs
        self.mcd = mcd

    def test_color_table(self):
        # docs
        self.node_type = 'color_table'

        # given
        mcd = MultiCloudDiagrams()

        # when
        rows = [
            'IndexName',
            'IndexSizeBytes',
            'IndexStatus',
        ]

        mcd.add_list(table_name='LSI:users_to_model-users-idx', rows=rows, fill_color='#FF9933;')

        # then
        # docs
        self.mcd = mcd
