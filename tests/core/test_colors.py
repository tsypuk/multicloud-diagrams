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
        input_file_previous_version = 'docs/docs/core-components/output/drawio/color_gradient.drawio'
        mcd.read_coords_from_file(input_file_previous_version)
        style = {
            'fillColor': '#FFFF33',
            'gradientColor': '#3399FF',
            'noLabel': '1'
        }

        # when
        for gradientDirection in ['north', 'south', 'east', 'west', 'radial']:
            style['gradientDirection'] = gradientDirection
            mcd.add_vertex(node_id=f"arn:aws:lambda:eu-west-1:123456789012:function:{gradientDirection}",
                           node_name=f'gradientDirection:{gradientDirection}',
                           node_type='lambda_function',
                           style=style)

        # then
        # docs
        self.mcd = mcd

    def test_color_nolabel(self):
        # docs
        self.node_type = 'color_nolabel'

        # given
        mcd = MultiCloudDiagrams()
        input_file_previous_version = 'docs/docs/core-components/output/drawio/color_nolabel.drawio'
        mcd.read_coords_from_file(input_file_previous_version)

        # when
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:nolabel",
                       node_name='no-label',
                       node_type='lambda_function',
                       style={'noLabel': '1'})

        # then
        # docs
        self.mcd = mcd

    def test_color_direction(self):
        # docs
        self.node_type = 'color_direction'

        # given
        mcd = MultiCloudDiagrams()
        input_file_previous_version = 'docs/docs/core-components/output/drawio/color_direction.drawio'
        mcd.read_coords_from_file(input_file_previous_version)

        style = {
            'noLabel': '1'
        }

        # when
        for direction in ['north', 'south', 'east', 'west']:
            style['direction'] = direction
            mcd.add_vertex(node_id=f"arn:aws:lambda:eu-west-1:123456789012:function:{direction}",
                           node_name=f'gradientDirection:{direction}',
                           node_type='lambda_function',
                           style=style)

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
