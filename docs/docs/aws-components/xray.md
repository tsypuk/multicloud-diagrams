---
layout: default
title: AWS Xray
parent: AWS Components
nav_order: 3
date: 2024-05-14
---

# AWS Xray
{: .d-inline-block .no_toc }

New (v0.3.41)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``xray``

## Rendering:

![lambda](output/jpg/xray.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_xray.py %}
```

## drawio xray vertex:

```xml
<mxCell id="vertex:xray:arn:aws:xray:us-west-1:123456789012:service/xray/tracing" parent="1" vertex="1">
    <mxGeometry width="76.5" height="85.5" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.x_ray;fillColor=#759C3E;gradientColor=none;"
```

| attribute | value |
|:----------|:------|
|align| left |
|dashed| 0 |
|fillColor| #759C3E |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|shape| mxgraph.aws3.x_ray |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 76.5  |
| height   |85.5|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:xray:arn:aws:xray:us-west-1:123456789012:service/xray/tracing" value="&lt;b&gt;Name&lt;/b&gt;: End-to-End-Tracing&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:xray:us-west-1:123456789012:service/xray/tracing&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: service-xray&lt;BR&gt;&lt;b&gt;clusterArn&lt;/b&gt;: arn:aws:xray:eu-west-1:123456789012:service/tracing&lt;BR&gt;&lt;b&gt;serviceRegistries&lt;/b&gt;: arn:aws:xray:eu-west-1:123456789012:service/srv-t&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;includeFragments&lt;/b&gt;: true&lt;BR&gt;&lt;b&gt;sampling&lt;/b&gt;: 25&lt;BR&gt;&lt;b&gt;platformVersion&lt;/b&gt;: LATEST&lt;BR&gt;&lt;b&gt;platformFamily&lt;/b&gt;: Linux" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.x_ray;fillColor=#759C3E;gradientColor=none;" parent="1" vertex="1">
                    <mxGeometry width="76.5" height="85.5" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``xray.drawio``:

[Download](output/drawio/xray.drawio){: .btn .btn-purple }