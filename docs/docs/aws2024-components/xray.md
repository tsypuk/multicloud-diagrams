---
layout: default
title: X-ray
parent: AWS2024 Components
nav_order: 3
date: 2024-07-21
---

# X-ray
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
{% root_include_snippet ../tests/aws2024/test_xray.py %}
```

## drawio xray vertex:

```xml
<mxCell id="vertex:xray:arn:aws:xray:us-west-1:123456789012:service/xray/tracing" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.xray;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #C925D1 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.xray |
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
                <mxCell id="vertex:xray:arn:aws:xray:us-west-1:123456789012:service/xray/tracing" value="&lt;b&gt;Name&lt;/b&gt;: End-to-End-Tracing&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:xray:us-west-1:123456789012:service/xray/tracing&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: service-xray&lt;BR&gt;&lt;b&gt;clusterArn&lt;/b&gt;: arn:aws:xray:eu-west-1:123456789012:service/tracing&lt;BR&gt;&lt;b&gt;serviceRegistries&lt;/b&gt;: arn:aws:xray:eu-west-1:123456789012:service/srv-t&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;includeFragments&lt;/b&gt;: true&lt;BR&gt;&lt;b&gt;sampling&lt;/b&gt;: 25&lt;BR&gt;&lt;b&gt;platformVersion&lt;/b&gt;: LATEST&lt;BR&gt;&lt;b&gt;platformFamily&lt;/b&gt;: Linux" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.xray;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``xray.drawio``:

[Download](output/drawio/xray.drawio){: .btn .btn-purple }