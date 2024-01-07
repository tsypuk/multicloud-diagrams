---
layout: default
title: Elastic Container Service
parent: AWS Components
nav_order: 3
date: 2024-01-07
---

# Elastic Container Service
{: .d-inline-block .no_toc }

New (v0.3.17)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``ecs``

## Rendering:

![lambda](output/jpg/ecs.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_ecs.py %}
```

## drawio ecs vertex:

```xml
<mxCell id="vertex:ecs:arn:aws:ecs:eu-west-1:12345689012:cluster/fargate-cluster" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ecs;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #D05C17 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #F78E04 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.ecs |
|shape| mxgraph.aws4.resourceIcon |
|strokeColor| #ffffff |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 78  |
| height   |78|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:ecs:arn:aws:ecs:eu-west-1:12345689012:cluster/fargate-cluster" value="&lt;b&gt;Name&lt;/b&gt;: Prod-cluster&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:ecs:eu-west-1:12345689012:cluster/fargate-cluster&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;runningTasksCount&lt;/b&gt;: 50&lt;BR&gt;&lt;b&gt;pendingTasksCount&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;activeServicesCount&lt;/b&gt;: 50&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F78E04;gradientDirection=north;fillColor=#D05C17;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ecs;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``ecs.drawio``:

[Download](output/drawio/ecs.drawio){: .btn .btn-purple }