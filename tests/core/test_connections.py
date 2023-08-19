from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def setUp(self) -> None:
        mcd = MultiCloudDiagrams()
        input_file_previous_version = 'docs/docs/core-components/output/drawio/connection.drawio'
        mcd.read_coords_from_file(input_file_previous_version)
        self.mcd = mcd

        # when
        self.lambda_id = mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:nolabel",
                                        node_name='no-label',
                                        node_type='lambda_function',
                                        style={'noLabel': '1'})

        self.dynamo_id = mcd.add_vertex(node_id="arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table",
                                        node_name='no-label',
                                        node_type='dynamo',
                                        style={'noLabel': '1'})

    def test_connection(self):
        # docs
        self.node_type = 'connection'

        # given
        mcd = MultiCloudDiagrams()
        input_file_previous_version = 'docs/docs/core-components/output/drawio/connection.drawio'
        mcd.read_coords_from_file(input_file_previous_version)

        # when
        lambda_id = mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:nolabel",
                                   node_name='no-label',
                                   node_type='lambda_function',
                                   style={'noLabel': '1'})

        dynamo_id = mcd.add_vertex(node_id="arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table",
                                   node_name='no-label',
                                   node_type='dynamo',
                                   style={'noLabel': '1'})
        mcd.add_link(src_node_id=lambda_id, dst_node_id=dynamo_id, action=['GET data'])

        # then
        # docs
        self.mcd = mcd

    def test_add_bidirectional_link(self):
        # docs
        self.node_type = 'connection_bidirectional'

        # given-when
        self.mcd.add_bidirectional_link(src_node_id=self.lambda_id, dst_node_id=self.dynamo_id, action=['GET data'])

        # then
        # docs

    def test_add_unidirectional_link(self):
        # docs
        self.node_type = 'connection_unidirectional'

        # given-when
        self.mcd.add_unidirectional_link(src_node_id=self.lambda_id, dst_node_id=self.dynamo_id, action=['GET data'])

        # then
        # docs

    def test_add_dashed(self):
        # docs
        self.node_type = 'connection_dashed'

        # given
        style = {
            'dashed': '1',
        }

        # when
        self.mcd.add_connection(src_node_id=self.lambda_id,
                                dst_node_id=self.dynamo_id,
                                edge_style=style,
                                labels=['GET data'])

        # then
        # docs

    def test_add_connection_stroked(self):
        # docs
        self.node_type = 'connection_stroked'

        # given
        style = {
            'strokeColor': '#FF3333',
            'strokeWidth': '3'
        }

        # when
        self.mcd.add_connection(src_node_id=self.lambda_id,
                                dst_node_id=self.dynamo_id,
                                edge_style=style,
                                labels=['GET data'])

        # then
        # docs

    def test_add_connection_rounded(self):
        # docs
        self.node_type = 'connection_custom'

        # given
        style = {
            'orthogonalLoop': '1',
            'edgeStyle': 'orthogonalEdgeStyle',
            'curved': '1',
            'startArrow': 'oval',
            'endArrow': 'classicThin'
        }

        # when
        self.mcd.add_connection(src_node_id=self.lambda_id,
                                dst_node_id=self.dynamo_id,
                                edge_style=style,
                                labels=['GET data'])

        # then
        # docs

    def test_add_connection_edge(self):
        # docs
        self.node_type = 'connection_edgeStyle'

        # given
        style = {
            'edgeStyle': 'elbowEdgeStyle'
        }

        # when
        self.mcd.add_connection(src_node_id=self.lambda_id,
                                dst_node_id=self.dynamo_id,
                                edge_style=style,
                                labels=['GET data'])

        # then
        # docs
