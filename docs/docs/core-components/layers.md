---
layout: default
title: Layers
parent: CORE Components
nav_order: 3
date: 2023-08-07
---

# Layers
{: .d-inline-block }

New (v0.3.10)
{: .label .label-green }

Layers enable the division of infrastructure representation into segmented domains, each with a specific focus on functionality or system attributes.

The following example illustrates the utilization of layers to show the progression of ``api-gateway`` flows, spanning from ``endpoints`` and ``methods`` to the storage system of ``DynamoDB``.
In this context, an additional "IAM" layer is incorporated at the apex, further enhancing the representation.


![draw-apigw.gif](../images/draw-apigw.gif)

## Code Snippet:

Let's explore how to interact with layer starting from simple example - by adding 2 layers ``Storage`` and ``Processing`` with dedicated resources ``lambda function`` and ``dynamoDB`` for each layer: 

```python
{% root_include_snippet ../tests/core/test_layer.py layer%}
```

## Rendering:

![layers](output/jpg/layer_3.jpg)

## Show/Hide Layers with assigned resources:

![layers](../images/drawio-layers.gif)

### Full XML dump:

```xml
{% root_include docs/core-components/output/drawio/layer_3.drawio%}
```

### drawio file:

Download generated ``layer_3.drawio``:

[Download](output/drawio/layer_3.drawio){: .btn .btn-purple }

