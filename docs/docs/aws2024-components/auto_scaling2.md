---
layout: default
title: Auto Scaling 2
parent: AWS2024 Components
nav_order: 3
date: 2024-07-10
---

# Auto Scaling 2
{: .d-inline-block .no_toc }

New (v0.3.79)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``auto_scaling2``

## Rendering:

![lambda](output/jpg/auto_scaling2.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_auto_scaling2.py %}
```

## drawio auto_scaling2 vertex:

```xml
<mxCell id="vertex:auto_scaling2:arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.auto_scaling2;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #ED7100 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.auto_scaling2 |
|shape| mxgraph.aws4.resourceIcon |
|sketch| 0 |
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
                <mxCell id="vertex:auto_scaling2:arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1" value="&lt;b&gt;Name&lt;/b&gt;: auto_scaling2&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:auto_scaling2:eu-west-1:123456789012:auto_scaling2/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;AutoScalingGroupName&lt;/b&gt;: web-instances&lt;BR&gt;&lt;b&gt;PolicyName&lt;/b&gt;: scale-up&lt;BR&gt;&lt;b&gt;PolicyARN&lt;/b&gt;: ARN&lt;BR&gt;&lt;b&gt;PolicyType&lt;/b&gt;: inline&lt;BR&gt;&lt;b&gt;AdjustmentType&lt;/b&gt;: negative&lt;BR&gt;&lt;b&gt;MinAdjustmentStep&lt;/b&gt;: 2&lt;BR&gt;&lt;b&gt;MinAdjustmentMagnitude&lt;/b&gt;: 2&lt;BR&gt;&lt;b&gt;ScalingAdjustment&lt;/b&gt;: 5&lt;BR&gt;&lt;b&gt;Cooldown&lt;/b&gt;: 4" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.auto_scaling2;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``auto_scaling2.drawio``:

[Download](output/drawio/auto_scaling2.drawio){: .btn .btn-purple }