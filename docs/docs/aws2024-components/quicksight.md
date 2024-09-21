---
layout: default
title: Amazon QuickSight
parent: AWS2024 Components
nav_order: 3
date: 2024-09-21
---

# Amazon QuickSight
{: .d-inline-block .no_toc }

New (v0.3.106)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``quicksight``

## Rendering:

![lambda](output/jpg/quicksight.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_quicksight.py %}
```

## drawio quicksight vertex:

```xml
<mxCell id="vertex:quicksight:arn:aws:quicksight:us-west-1:123456789012:service/quicksight/1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.quicksight;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #8C4FFF |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.quicksight |
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
                <mxCell id="vertex:quicksight:arn:aws:quicksight:us-west-1:123456789012:service/quicksight/1" value="&lt;b&gt;Name&lt;/b&gt;: QuickSight&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:quicksight:us-west-1:123456789012:service/quicksight/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;DashboardId&lt;/b&gt;: Custom Dataset&lt;BR&gt;&lt;b&gt;Name&lt;/b&gt;: Aggregation of Req/rate&lt;BR&gt;&lt;b&gt;Status&lt;/b&gt;: CREATION_SUCCESSFUL" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.quicksight;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``quicksight.drawio``:

[Download](output/drawio/quicksight.drawio){: .btn .btn-purple }