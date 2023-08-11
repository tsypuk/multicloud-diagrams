from multicloud_diagrams import MultiCloudDiagrams
from utils.templating import TestRendering


class TestCoreVertexInIsolation(TestRendering):

    def test_yaml(self):
        # docs
        self.node_type = 'yaml'

        # given
        mcd = MultiCloudDiagrams()
        output_file = 'docs/docs/core-components/output/drawio/yaml.drawio'
        mcd.read_coords_from_file(output_file)

        # when
        # Read cloud resources declared in yaml format
        mcd.augment_from_yaml('samples/samples/augmented_resources.yaml')

        # then
        # expected = {
        #     'id': 'vertex:Integration Response:list',
        #     'parent': '1',
        #     'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;'
        #              'resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
        #     'value': '<b>Integration Response</b>',
        #     'vertex': '1'
        # }

        # self.verify_list(expected=expected, mx_file=mcd.mx_file, resource_name='LSI:users_to_model-users-idx', expected_list=expected_list)

        # docs
        self.mcd = mcd

    def test_yaml_to_existing_file(self):
        # docs
        self.node_type = 'yaml2'

        # given
        mcd = MultiCloudDiagrams()
        output_file = 'docs/docs/core-components/output/drawio/yaml2.drawio'
        mcd.read_coords_from_file(output_file)

        # Diagrams as a Code: add Lambda and DynamoDB
        mcd.add_vertex(node_id="arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name", node_name='prod-lambda-name',
                       node_type='lambda_function')
        mcd.add_vertex(node_id='arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table', node_name='prod-dynamo-table',
                       node_type='dynamo')
        mcd.add_link('lambda_function:arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name',
                     'dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table',
                     action=['GET permissions'])

        # when
        # Add resources from YAML-file
        mcd.augment_from_yaml('samples/samples/augmented_resources2.yaml')

        # then
        # expected = {
        #     'id': 'vertex:Integration Response:list',
        #     'parent': '1',
        #     'style': 'swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;'
        #              'resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;',
        #     'value': '<b>Integration Response</b>',
        #     'vertex': '1'
        # }

        # self.verify_list(expected=expected, mx_file=mcd.mx_file, resource_name='LSI:users_to_model-users-idx', expected_list=expected_list)

        # docs
        self.mcd = mcd
