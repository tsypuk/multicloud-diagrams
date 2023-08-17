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

    def test_color_shadow_opacity(self):
        # docs
        self.node_type = 'color_shadow_opacity'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       style={
                           'fillColor': '#00FF00',
                           'fillOpacity': '50',
                           'shadow': '1'
                       })

        # then
        # docs
        self.mcd = mcd

    def test_color_gradient(self):
        # docs
        self.node_type = 'color_gradient'

        # given
        mcd = MultiCloudDiagrams()

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name",
                       node_name='prod-lambda-name',
                       node_type='lambda_function',
                       style={
                           'fillColor': '#FFFF33',
                           'gradientColor': '#3333FF',
                           'gradientDirection': 'north'
                       })

        # then
        # docs
        self.mcd = mcd


def test_color_table(self):
    # docs
    self.node_type = 'color_table'

    # given
    mcd = MultiCloudDiagrams()
    rows = [
        'IndexName',
        'IndexSizeBytes',
        'IndexStatus',
    ]
    style = {
        'fillColor': '#FF9933',
    }

    # when
    mcd.add_list(table_name='LSI:users_to_model-users-idx', rows=rows, style=style)

    # then
    # docs
    self.mcd = mcd
