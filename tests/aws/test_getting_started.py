from multicloud_diagrams import MultiCloudDiagrams

from utils.utils import TestUtilities


class TestAWSVertexInIsolation(TestUtilities):

    def test_getting_started_1(self):
        # given
        # Create a new cloud diagram
        mcd = MultiCloudDiagrams()

        # when
        func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name'
        mcd.add_vertex(node_id=func_arn, node_name='prod-lambda-name', node_type='lambda_function')

        role_arn = 'arn:aws:iam::123456789012:role/prod-lambda-name'
        mcd.add_vertex(node_id=role_arn, node_name='role-lambda-name', node_type='iam_role')
        mcd.add_link(src_node_id=f'lambda_function:{func_arn}', dst_node_id=f'iam_role:{role_arn}')

        mcd.export_to_file('/tmp/diagram.drawio')

        # then
        print('test')

    def test_getting_started_2(self):
        # given
        # Create a new cloud diagram
        mcd = MultiCloudDiagrams()

        # when
        output_file = '/tmp/diagram.drawio'
        mcd.read_coords_from_file(output_file)

        func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name'
        mcd.add_vertex(node_id=func_arn, node_name='prod-lambda-name', node_type='lambda_function')

        role_arn = 'arn:aws:iam::123456789012:role/prod-lambda-name'
        mcd.add_vertex(node_id=role_arn, node_name='role-lambda-name', node_type='iam_role')

        cw_policy_arn = "arn:aws:iam::123456789012:policy/prod-cloudwatch-policy"
        mcd.add_vertex(node_id=cw_policy_arn, node_name='prod-cloudwatch-policy', node_type='iam_policy')

        s3_policy_arn = "arn:aws:iam::123456789012:policy/prod-s3-policy"
        mcd.add_vertex(node_id=s3_policy_arn, node_name='prod-s3-policy', node_type='iam_policy')

        mcd.add_link(src_node_id=f'lambda_function:{func_arn}', dst_node_id=f'iam_role:{role_arn}')
        mcd.add_link(f'iam_role:{role_arn}', f'iam_policy:{cw_policy_arn}')
        mcd.add_link(f'iam_role:{role_arn}', f'iam_policy:{s3_policy_arn}')

        # We can write to same Diagram
        mcd.export_to_file(output_file)

        # Or write to a new Diagram version
        mcd.export_to_file('/tmp/diagram_v2.drawio')

        # then
        print('test')
