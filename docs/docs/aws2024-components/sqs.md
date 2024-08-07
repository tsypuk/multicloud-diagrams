---
layout: default
title: SQS
parent: AWS2024 Components
nav_order: 3
date: 2024-07-01
---

# SQS
{: .d-inline-block .no_toc }

New (v0.2.0)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``sqs``

## Rendering:

![lambda](output/jpg/sqs.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_sqs.py %}
```

## drawio sqs vertex:

```xml
<mxCell id="vertex:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #BC1356 |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #FF4F8B |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.sqs |
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
                <mxCell id="vertex:sqs:arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo" value="&lt;b&gt;Name&lt;/b&gt;: int-eu-live-events.fifo&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:sqs:eu-west-1:123456789012:int-eu-live-events.fifo&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;DelaySeconds&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;FifoQueue&lt;/b&gt;: TRUE&lt;BR&gt;&lt;b&gt;ReceiveMessageWaitTimeSeconds&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;SqsManagedSseEnabled&lt;/b&gt;: false&lt;BR&gt;&lt;b&gt;VisibilityTimeout&lt;/b&gt;: 30" style="sketch=0;outlineConnect=0;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sqs;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``sqs.drawio``:

[Download](output/drawio/sqs.drawio){: .btn .btn-purple }