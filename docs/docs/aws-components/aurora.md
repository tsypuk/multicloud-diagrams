---
layout: default
title: Aurora
parent: AWS Components
nav_order: 3
date: 2024-01-31
---

# Aurora
{: .d-inline-block .no_toc }

New (v0.3.25)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``aurora``

## Rendering:

![lambda](output/jpg/aurora.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_aurora.py %}
```

## drawio aurora vertex:

```xml
<mxCell id="vertex:aurora:arn:aws:aurora:eu-west-1:123456789012" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.aurora;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #3334B9 |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #4D72F3 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.aurora |
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
                <mxCell id="vertex:aurora:arn:aws:aurora:eu-west-1:123456789012" value="&lt;b&gt;Name&lt;/b&gt;: arn:aws:aurora:eu-west-1:123456789012/MainDB&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:aurora:eu-west-1:123456789012&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;records&lt;/b&gt;: 224000&lt;BR&gt;&lt;b&gt;engine&lt;/b&gt;: InnoDB&lt;BR&gt;&lt;b&gt;volume&lt;/b&gt;: 2048Mb&lt;BR&gt;&lt;b&gt;cpu&lt;/b&gt;: 512&lt;BR&gt;&lt;b&gt;memory&lt;/b&gt;: 2048&lt;BR&gt;&lt;b&gt;version&lt;/b&gt;: 5.72" style="sketch=0;outlineConnect=0;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.aurora;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``aurora.drawio``:

[Download](output/drawio/aurora.drawio){: .btn .btn-purple }