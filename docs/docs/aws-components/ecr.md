---
layout: default
title: Elastic Container Registry
parent: AWS Components
nav_order: 3
date: 2024-01-15
---

# Elastic Container Registry
{: .d-inline-block .no_toc }

New (v0.3.22)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``ecr``

## Rendering:

![lambda](output/jpg/ecr.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_ecr.py %}
```

## drawio ecr vertex:

```xml
<mxCell id="vertex:ecr:arn:i-1234567890abcdef0" parent="1" vertex="1">
    <mxGeometry width="69" height="72" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.ecr;fillColor=#F58534;gradientColor=none;"
```

| attribute | value |
|:----------|:------|
|align| left |
|dashed| 0 |
|fillColor| #F58534 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|shape| mxgraph.aws3.ecr |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 69  |
| height   |72|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:ecr:arn:i-1234567890abcdef0" value="&lt;b&gt;Name&lt;/b&gt;: Registry for images&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:i-1234567890abcdef0&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;images&lt;/b&gt;: 23&lt;BR&gt;&lt;b&gt;ImageId&lt;/b&gt;: ami-0abcdef1234567890&lt;BR&gt;&lt;b&gt;multiarch&lt;/b&gt;: 13" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.ecr;fillColor=#F58534;gradientColor=none;" parent="1" vertex="1">
                    <mxGeometry width="69" height="72" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``ecr.drawio``:

[Download](output/drawio/ecr.drawio){: .btn .btn-purple }