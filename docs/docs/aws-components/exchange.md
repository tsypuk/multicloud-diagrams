---
layout: default
title: Exchange
parent: AWS Components
nav_order: 3
date: 2024-05-12
---

# Exchange
{: .d-inline-block .no_toc }

New (v0.3.40)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``exchange``

## Rendering:

![lambda](output/jpg/exchange.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_exchange.py %}
```

## drawio exchange vertex:

```xml
<mxCell id="vertex:exchange:arn:aws:exchange:us-west-1:123456789012:service/exchange/data" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.data_exchange;"
```

| attribute | value |
|:----------|:------|
|align| center |
|aspect| fixed |
|dashed| 0 |
|fillColor| #5A30B5 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #945DF2 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.data_exchange |
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
                <mxCell id="vertex:exchange:arn:aws:exchange:us-west-1:123456789012:service/exchange/data" value="&lt;b&gt;Name&lt;/b&gt;: Exchange&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:exchange:us-west-1:123456789012:service/exchange/data&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: datasync&lt;BR&gt;&lt;b&gt;clusterArn&lt;/b&gt;: arn:aws:exchange:eu-west-1:123456789012:/exchange&lt;BR&gt;&lt;b&gt;serviceRegistries&lt;/b&gt;: arn:aws:exchange:eu-west-1:123456789012:service/exchange&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;launchType&lt;/b&gt;: SFTP connection" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.data_exchange;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``exchange.drawio``:

[Download](output/drawio/exchange.drawio){: .btn .btn-purple }