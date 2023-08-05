---
layout: default
title: Getting started
nav_order: 2
---

# Getting started
{: .no_toc }

Welcome to ``multicloud-diagrams`` 👋 This section will walk you through the basic installation process and provide a quick example to get you started. 
If you're looking for more advanced features and customization options, be sure to explore the subsequent sections in our comprehensive documentation.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}
   
---


## Dependency details

The ``multicloud-diagrams`` package is a Python library that provides support for major ``Python`` versions, including ``3.7``, ``3.8``, ``3.9``, ``3.10``, and ``3.11``.
The package ensures compatibility with these Python versions by running tests using a Git workflow.
These tests are designed to verify that the library functions as expected across each mentioned Python version.

The package is readily accessible on [PyPI: https://pypi.org/project/multicloud-diagrams/](https://pypi.org/project/multicloud-diagrams/) 
for easy installation and usage. As an open-source project, it encourages community participation and welcomes contributions from developers
[https://github.com/tsypuk/multicloud-diagrams](https://github.com/tsypuk/multicloud-diagrams)
Whether you want to use the package's functionalities or contribute to its improvement, it offers a user-friendly experience, backed by an active and engaged community.




## Installation

You can install ``multicloud-diagrams`` using ``pip``, the package manager for Python:

```shell
pip install multicloud-diagrams
```

If you are using ``poetry`` follow this instructions:

```shell
poetry add multicloud-diagrams
```

Edit your ``project.toml`` and add ``multicloud-diagrams`` as dependecy:

```yaml
[ tool.poetry.dependencies ]
  python = "^3.7"
  pyyaml = "^6.0"
  multicloud-diagrams = "^0.3.10"
```

## Usage

{: .d-inline-block }

The minimum configuration requires importing MultiCloudDiagrams, adding vertices, connecting them with links and exporting to output file. 

```python
from multicloud_diagrams import MultiCloudDiagrams

# Create a new cloud diagram
mcd = MultiCloudDiagrams()

output_file = '../output/diagram.drawio'
func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name'
mcd.add_vertex(node_id=func_arn, node_name='prod-lambda-name', arn=func_arn, node_type='lambda_function')

role_arn = 'arn:aws:iam::123456789012:role/prod-lambda-name'
mcd.add_vertex(node_id=role_arn, node_name='role-lambda-name', arn=role_arn, node_type='iam_role')
mcd.add_link(src_node_id=f'lambda_function:{func_arn}', dst_node_id=f'iam_role:{role_arn}')

mcd.export_to_file(output_file)
```

## Open drawio editor and position nodes manually or using automated Alignment

{: .d-inline-block }

## Reuse coordinates from previous diagram version

{: .d-inline-block }

New (v0.2.1)
{: .label .label-green }

```python
from multicloud_diagrams import MultiCloudDiagrams

# Create a new cloud diagram
mcd = MultiCloudDiagrams()

output_file = '../output/diagram.drawio'
mcd.read_coords_from_file(output_file)

func_arn = 'arn:aws:lambda:eu-west-1:123456789012:function:prod-lambda-name'
mcd.add_vertex(node_id=func_arn, node_name='prod-lambda-name', arn=func_arn, node_type='lambda_function')

role_arn = 'arn:aws:iam::123456789012:role/prod-lambda-name'
mcd.add_vertex(node_id=role_arn, node_name='role-lambda-name', arn=role_arn, node_type='iam_role')
mcd.add_link(src_node_id=f'lambda_function:{func_arn}', dst_node_id=f'iam_role:{role_arn}')

# We can write to same Diagram
mcd.export_to_file(output_file)

# Or write to a new Diagram version
mcd.export_to_file('../output/diagram.drawio')
```

## Vertices and Edges

Each ``vertex`` has a mandatory and optional attributes.

Mandatory Attributes:
- node_id
- node_name
- arn
- node_type

Optional Attributes:
- metadata

To see the list of all supported nodes (currently AWS and on-prem), syntax of each node with examples, please follow to ``AWS Components`` section


Vertices are connected using edges, by specifying source and target Vertex IDs. Also allowing to add labels to connection.

ID syntax is: ``RESOURCE_TYPE:ARN``
Examples: f'lambda_function:{func_arn}' f'iam_role:{role_arn}'

For more advanced use cases, detailed customization options, and in-depth functionalities, please continue exploring the next sections in our documentation. There, you will find a wealth of information to help you leverage the full potential of multicloud-diagrams in your projects. Happy diagramming!