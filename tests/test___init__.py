from unittest import TestCase

from multicloud_diagrams import MultiCloudDiagrams


class TestMultiCloudDiagrams(TestCase):
    vertex_details = [{'name': 'prod-lambda-name', 'type': 'lambda_function', 'arn': 'arn:aws:lambda:eu-west-1:123456789:function:prod-lambda-name'},
                      {'name': 'role-lambda-name', 'type': 'iam_role', 'arn': 'arn:aws:iam::123456789:role/prod-lambda-name'},
                      {'name': 'prod-cloudwatch-policy', 'icon': 'broker', 'type': 'iam_policy', 'arn': 'arn:aws:iam::123456789:policy/prod-cloudwatch-policy'},
                      {'name': 'prod-s3-policy', 'type': 'iam_policy', 'arn': 'arn:aws:iam::123456789:policy/prod-s3-policy'},
                      {'name': 'prod-dynamodb-policy', 'type': 'iam_policy', 'arn': 'arn:aws:iam::123456789:policy/prod-dynamo-policy'}]

    def test__build_vertex_id_approach_1_src(self):
        # given
        mcd = MultiCloudDiagrams()
        edge = {'src': 'prod-lambda-name', 'dst': 'role-lambda-name', 'label': 'HasRole', 'link_type': 'none'}
        # when
        result = mcd._build_vertex_id(vertex_details=self.vertex_details, edge=edge, src_dst_marker='src')
        # then
        self.assertEqual('lambda_function:arn:aws:lambda:eu-west-1:123456789:function:prod-lambda-name', result)

    def test__build_vertex_id_approach_1_dst_arn(self):
        # given
        mcd = MultiCloudDiagrams()
        edge = {'src': 'prod-lambda-name', 'dst': 'role-lambda-name', 'label': 'HasRole', 'link_type': 'none'}
        # when
        result = mcd._build_vertex_id(vertex_details=self.vertex_details, edge=edge, src_dst_marker='dst')
        # then
        self.assertEqual('iam_role:arn:aws:iam::123456789:role/prod-lambda-name', result)

    def test__build_vertex_id_approach_2_dst_arn(self):
        # given
        mcd = MultiCloudDiagrams()
        edge = {'src_arn': 'arn:aws:iam::123456789:role/prod-lambda-name', 'src_type': 'iam_role', 'dst_arn': 'arn:aws:iam::123456789:policy/prod-s3-policy', 'dst_type': 'iam_policy',
                'label': 'Allow S3 access', 'link_type': 'none'}
        # when
        result = mcd._build_vertex_id(vertex_details=self.vertex_details, edge=edge, src_dst_marker='dst')
        # then
        self.assertEqual('iam_policy:arn:aws:iam::123456789:policy/prod-s3-policy', result)

    def test__build_vertex_id_approach_2_src_arn(self):
        # given
        mcd = MultiCloudDiagrams()
        edge = {'src_arn': 'arn:aws:iam::123456789:role/prod-lambda-name', 'src_type': 'iam_role', 'dst_arn': 'arn:aws:iam::123456789:policy/prod-s3-policy', 'dst_type': 'iam_policy',
                'label': 'Allow S3 access', 'link_type': 'none'}
        # when
        result = mcd._build_vertex_id(vertex_details=self.vertex_details, edge=edge, src_dst_marker='src')
        # then
        self.assertEqual('iam_role:arn:aws:iam::123456789:role/prod-lambda-name', result)

    def test__build_vertex_id_approach_3_src_arn(self):
        # given
        mcd = MultiCloudDiagrams()
        edge = {'src_arn': 'arn:aws:iam::123456789:role/prod-lambda-name', 'src_type': 'iam_role', 'dst': 'prod-dynamodb-policy',
                'label': 'Allow DynamoDB read access', 'link_type': 'none'}
        # when
        result = mcd._build_vertex_id(vertex_details=self.vertex_details, edge=edge, src_dst_marker='src')
        # then
        self.assertEqual('iam_role:arn:aws:iam::123456789:role/prod-lambda-name', result)

    def test__build_vertex_id_approach_3_dst(self):
        # given
        mcd = MultiCloudDiagrams()
        edge = {'src_arn': 'arn:aws:iam::123456789:role/prod-lambda-name', 'src_type': 'iam_role', 'dst': 'prod-dynamodb-policy',
                'label': 'Allow DynamoDB read access', 'link_type': 'none'}
        # when
        result = mcd._build_vertex_id(vertex_details=self.vertex_details, edge=edge, src_dst_marker='dst')
        # then
        self.assertEqual('iam_policy:arn:aws:iam::123456789:policy/prod-dynamo-policy', result)
