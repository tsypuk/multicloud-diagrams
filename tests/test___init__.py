from unittest import TestCase

from multicloud_diagrams import MultiCloudDiagrams, update_fill_color, stringify_dict


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

    def test_stringify_dict(self):
        # given
        metadata = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
        # when
        result = stringify_dict(metadata)
        # then
        self.assertEqual('<BR>-----------<BR><b>key1</b>: value1<BR><b>key2</b>: value2<BR><b>key3</b>: value3', result)

    def test_stringify_dict_empty(self):
        # given
        metadata = {}
        # when
        result = stringify_dict(metadata)
        # then
        self.assertEqual('', result)

    def test_update_fill_color(self):
        # given-when
        result = update_fill_color(
            style_str='sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;',
            node_color='#FF0000')
        # then
        self.assertEqual(
            'sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#FF0000;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sns;',
            result)
