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

### Examples
Generating `drawio` diagrams from the code (Diagrams as a Code) for popular Amazon Web Services:

#### AWS DynamoDB Details

- Source [aws_dynamo.py](https://github.com/tsypuk/multicloud-diagrams/samples/samples/aws_dynamo.py)
- Output compiled [drawio diagram](https://github.com/tsypuk/multicloud-diagrams/samples/output/output.prod.dynamo.drawio):

![output.prod.dynamo.png](https://github.com/tsypuk/multicloud-diagrams/raw/main/samples/output/png/output.prod.dynamo.png?raw=True)

#### AWS IAM Graph

- Source [aws_dynamo.py](https://github.com/tsypuk/multicloud-diagrams/samples/samples/aws_iam_roles.py)
- Output compiled [drawio diagram](https://github.com/tsypuk/multicloud-diagrams/samples/output/output.prod.iam-roles.drawio)

![output.prod.iam-roles.png](https://github.com/tsypuk/multicloud-diagrams/blob/main/samples/output/png/output.prod.iam-roles.png?raw=True)

### FYI:

OpenSource Guide, [How to contribute to opensource](https://opensource.guide/)