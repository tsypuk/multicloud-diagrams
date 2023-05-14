from multicloud_diagrams import MultiCloudDiagrams


def main():
    mcd = MultiCloudDiagrams()

    prefix = 'prod'
    roles_file = f'../output/iam_output.{prefix}.iam-roles.drawio'

    mcd.read_coords_from_file(roles_file)

    func_arn = 'arn:aws:lambda:eu-west-1:123456789:function:prod-lambda-name'
    mcd.add_vertex(id=func_arn, node_name='prod-lambda-name', arn=func_arn, node_type='lambda_function')
    role_arn = 'arn:aws:iam::123456789:role/prod-lambda-name'
    mcd.add_vertex(id=role_arn, node_name='role-lambda-name', arn=role_arn, node_type='iam_role')
    mcd.add_link(src_node_id="lambda_function:" + func_arn, dst_node_id="iam_role:" + role_arn)

    cw_policy_arn = "arn:aws:iam::123456789:policy/prod-cloudwatch-policy"
    mcd.add_vertex(id=cw_policy_arn, node_name='prod-cloudwatch-policy', arn=cw_policy_arn, node_type='iam_policy')
    mcd.add_link("iam_role:" + role_arn, "iam_policy:" + cw_policy_arn)

    s3_policy_arn = "arn:aws:iam::123456789:policy/prod-s3-policy"
    mcd.add_vertex(id=s3_policy_arn, node_name='prod-s3-policy', arn=s3_policy_arn, node_type='iam_policy')
    mcd.add_link("iam_role:" + role_arn, "iam_policy:" + s3_policy_arn)

    mcd.export_to_file(roles_file)


if __name__ == "__main__":
    main()
