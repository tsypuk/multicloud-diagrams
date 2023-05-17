MultiCloud Diagrams is a package for generating and rendering Diagrams-As-a-Code (DAG) in popular drawio format for different Cloud providers.

- you can use it by defining ``Diagrams as a Code``, compile to drawio vector format, edit vector drawio representation (align components location).
- other option is to query infrastructure elements with popular libraries, like aws boto, preprocess desired elements and compile them into drawio using ``multicloud-diagrams``.

- **Source code:** https://github.com/tsypuk/multicloud-diagrams
- **PyPI multicloud-diagrams:** https://pypi.org/project/multicloud-diagrams/
- **Sponsor project:** https://patreon.com/tsypuk
- **View changelog:** https://github.com/tsypuk/multicloud-diagrams/blob/main/CHANGELOG.MD
- **Bug reports:** https://github.com/tsypuk/multicloud-diagrams/issues
- **Samples and examples:** https://github.com/tsypuk/multicloud-diagrams/tree/main/samples/samples

### Features:
- allows to generate drawio diagram with predefined styles for popular aws services, support graph-based connection with named edges
- supports single and batch elements append to diagram
- duplicates detection to prevent ball of mud in file format and diagram
- verification that both vertices present on diagram when adding edge connection between them 
- if the node is not present, fallback to default icon when rendering
- read previous version of drawio file and reuses existing vertices coordinates when generating a new version
- generate diagram from ``YAML`` definition
- mix and augment Diagram-as-code, real infra crawler, static yaml-based content to diagram

### Supported AWS services:

- lambda_function
- sqs
- sns
- iam_role/iam_policy/iam_permission
- dynamo/dynamo_stream
- api_gw
- s3
- kms
- ssm

### Library can be used with different approaches and even mix all of them. Samples and usage:

#### 1. Generating AWS DynamoDB Details drawio diagram based on library, http, awscli, etc. Example based on boto3 DynamoDB response

```json
{
        'AttributeDefinitions': [
            {
                'AttributeName': 'first',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'second',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'third',
                'AttributeType': 'B'
            },
        ],
        'TableName': 'prod-dynamo-table',
        'KeySchema': [
            {
                'AttributeName': 'string',
                'KeyType': 'HASH'
            },
        ],
        'TableSizeBytes': 123,
        'ItemCount': 123,
        'TableArn': 'arn:aws:dynamodb:eu-west-1:123456789:table/prod-dynamo-table',
        'LocalSecondaryIndexes': [{
...       
...
...
          
          'SSEDescription': {
            'Status': 'ENABLED',
            'SSEType': 'KMS',
            'KMSMasterKeyArn': 'string',
          },
          'DeletionProtectionEnabled': True
        }
```

- Source [aws_dynamo.py](https://github.com/tsypuk/multicloud-diagrams/samples/samples/aws_dynamo_boto3_response.py)
- Output compiled [drawio diagram](https://github.com/tsypuk/multicloud-diagrams/samples/output/output.prod.dynamo.drawio):

![output.prod.dynamo.png](https://github.com/tsypuk/multicloud-diagrams/raw/main/samples/output/png/output.prod.dynamo.png?raw=True)

#### 2. Diagrams as a Code. DAG. Generating AWS IAM Graph from the code based on DAG declaration:

```python
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
```

- Source [aws_dynamo.py](https://github.com/tsypuk/multicloud-diagrams/samples/samples/aws_iam_roles_from_code.py)
- Output compiled [drawio diagram](https://github.com/tsypuk/multicloud-diagrams/samples/output/output.prod.iam-roles.drawio)

![output.prod.iam-roles.png](https://github.com/tsypuk/multicloud-diagrams/blob/main/samples/output/png/output.prod.iam-roles.png?raw=True)


#### 3. Generating Diagram from YAML source

```yaml
vertices:
  - name: prod-lambda-name
    type: lambda_function
    arn: arn:aws:lambda:eu-west-1:123456789:function:prod-lambda-name
  - name: role-lambda-name
    type: iam_role
    arn: arn:aws:iam::123456789:role/prod-lambda-name
  - name: prod-cloudwatch-policy
    icon: broker
    type: iam_policy
    arn: arn:aws:iam::123456789:policy/prod-cloudwatch-policy
  - name: prod-s3-policy
    type: iam_policy
    arn: arn:aws:iam::123456789:policy/prod-s3-policy
  - name: prod-dynamodb-policy
    type: iam_policy
    arn: arn:aws:iam::123456789:policy/prod-dynamo-policy
edges:
#  1st approach src/dst are linked to yaml vertices by name
  - { src: prod-lambda-name, dst: role-lambda-name, label: HasRole, link_type: none }
  - { src: role-lambda-name, dst: prod-cloudwatch-policy, label: Allow CloudWatch logs, link_type: none }
#  2nd approach src/dst are linked by ARN (ARN can be present in same yaml, or loaded programmatically)
  - {
    src_arn: arn:aws:iam::123456789:role/prod-lambda-name,
    src_type: iam_role,
    dst_arn: arn:aws:iam::123456789:policy/prod-s3-policy,
    dst_type: iam_policy,
    label: Allow S3 access,
    link_type: none }
# 3rd approach is mixed of 1st and 2nd
  - {
    src_arn: arn:aws:iam::123456789:role/prod-lambda-name,
    src_type: iam_role,
    dst: prod-dynamodb-policy,
    label: Allow DynamoDB read access,
    link_type: none }
```

- Source [[aws_iam_from_yaml.py](https://github.com/tsypuk/multicloud-diagrams/samples/samples/[aws_iam_from_yaml.py)
- Output compiled [drawio diagram](https://github.com/tsypuk/multicloud-diagrams/samples/output/output.prod.iam-roles-from-yaml.drawio)

![output.prod.iam-roles.png](https://github.com/tsypuk/multicloud-diagrams/blob/main/samples/output/png/output.prod.iam-roles-from-yaml.png?raw=True)


### FYI:

OpenSource Guide, [How to contribute to opensource](https://opensource.guide/)