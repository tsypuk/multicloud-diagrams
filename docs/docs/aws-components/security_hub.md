---
layout: default
title: Security Hub
parent: AWS Components
nav_order: 3
date: 2024-06-06
---

# Security Hub
{: .d-inline-block .no_toc }

New (v0.3.43)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``security_hub``

## Rendering:

![lambda](output/jpg/security_hub.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_security_hub.py %}
```

## drawio security_hub vertex:

```xml
<mxCell id="vertex:security_hub:arn:aws:security_hub:eu-west-1:123456789012:security_hub/1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.security_hub;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #C7131F |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #F54749 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.security_hub |
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
                <mxCell id="vertex:security_hub:arn:aws:security_hub:eu-west-1:123456789012:security_hub/1" value="&lt;b&gt;Name&lt;/b&gt;: security_hub&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:security_hub:eu-west-1:123456789012:security_hub/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;WAF enabled&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;DisablePorts&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;Connected to ALB&lt;/b&gt;: IDs" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.security_hub;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``security_hub.drawio``:

[Download](output/drawio/security_hub.drawio){: .btn .btn-purple }