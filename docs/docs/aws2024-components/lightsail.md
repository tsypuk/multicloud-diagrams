---
layout: default
title: Lightsail
parent: AWS2024 Components
nav_order: 3
date: 2024-07-08
---

# Lightsail
{: .d-inline-block .no_toc }

New (v0.3.77)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``lightsail``

## Rendering:

![lambda](output/jpg/lightsail.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_lightsail.py %}
```

## drawio lightsail vertex:

```xml
<mxCell id="vertex:lightsail:arn:aws:lightsail:eu-west-1:123456789012:lightsail/1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lightsail;"
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
|resIcon| mxgraph.aws4.lightsail |
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
                <mxCell id="vertex:lightsail:arn:aws:lightsail:eu-west-1:123456789012:lightsail/1" value="&lt;b&gt;Name&lt;/b&gt;: Lightsail&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:lightsail:eu-west-1:123456789012:lightsail/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;name&lt;/b&gt;: Instance1&lt;BR&gt;&lt;b&gt;arn&lt;/b&gt;: ARN&lt;BR&gt;&lt;b&gt;supportCode&lt;/b&gt;: java&lt;BR&gt;&lt;b&gt;createdAt&lt;/b&gt;: 2024-07-08&lt;BR&gt;&lt;b&gt;location&lt;/b&gt;: {'availabilityZone': 'az-1', 'regionName': 'us-east-1'}&lt;BR&gt;&lt;b&gt;resourceType&lt;/b&gt;: Instance" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lightsail;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``lightsail.drawio``:

[Download](output/drawio/lightsail.drawio){: .btn .btn-purple }