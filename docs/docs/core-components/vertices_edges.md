---
layout: default
title: Vertices & Edges
parent: Core Components
nav_order: 1
---

# Vertices & Edges

Tables are responsive by default, allowing wide tables to have a horizontal scroll to access columns outside of the normal viewport.

<div class="code-example" markdown="1">

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

</div>
```markdown
| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |
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
