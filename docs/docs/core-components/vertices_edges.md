---
layout: default
title: Vertices & Edges
parent: Core Components
nav_order: 1
---

# Vertices & Edges

## Vertex

```python
def add_vertex(self, 
               node_id: str, node_name: str, arn: str = None, metadata: dict = None,
               node_type: str = '', layer_name: str = None, layer_id: str = None,
               fill_color: str = None, x: int = None, y: int = None)
```

| Mandatory |           |
|:----------|:------------------|
| node_id   | good swedish fish |
| node_name | good and plenty   |
| arn       | good `oreos`      |
| node_type | good `zoute` drop |


| Optional   |        |
|:-----------|:------------------|
| metadata   | good swedish fish |
| layer_name | good swedish fish |
| layer_id   | good swedish fish |
| fill_color | good swedish fish |
| x          | good swedish fish |
| y          | good swedish fish |

## Edge

Each ``vertex`` has a mandatory and optional attributes.

| Optional Attributes  | head two          |
|:---------------------|:------------------|
| metadata             | good swedish fish |

To see the list of all supported nodes (currently AWS and on-prem), syntax of each node with examples, please follow to ``AWS Components`` section

Vertices are connected using edges, by specifying source and target Vertex IDs. Also allowing to add labels to connection.

ID syntax is: ``RESOURCE_TYPE:ARN``
Examples: f'lambda_function:{func_arn}' f'iam_role:{role_arn}'
