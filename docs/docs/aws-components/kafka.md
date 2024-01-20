---
layout: default
title: Managed Kafka Service
parent: AWS Components
nav_order: 3
date: 2024-01-08
---

# Managed Kafka Service
{: .d-inline-block .no_toc }

New (v0.3.20)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``kafka``

## Rendering:

![lambda](output/jpg/kafka.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_kafka.py %}
```

## drawio kafka vertex:

```xml
<mxCell id="vertex:kafka:arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_streaming_for_kafka;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #5A30B5 |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #945DF2 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.managed_streaming_for_kafka |
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
                <mxCell id="vertex:kafka:arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94" value="&lt;b&gt;Name&lt;/b&gt;: arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:mks:eu-west-1:123456789012/kafka/562320f29dbdc94&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;connectivity&lt;/b&gt;: CONNECTED&lt;BR&gt;&lt;b&gt;topics&lt;/b&gt;: 13&lt;BR&gt;&lt;b&gt;messages&lt;/b&gt;: 2048" style="sketch=0;outlineConnect=0;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_streaming_for_kafka;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``kafka.drawio``:

[Download](output/drawio/kafka.drawio){: .btn .btn-purple }