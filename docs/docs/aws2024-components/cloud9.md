---
layout: default
title: Cloud9
parent: AWS2024 Components
nav_order: 3
date: 2024-07-21
---

# Cloud9
{: .d-inline-block .no_toc }

New (v0.3.91)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``cloud9``

## Rendering:

![lambda](output/jpg/cloud9.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_cloud9.py %}
```

## drawio cloud9 vertex:

```xml
<mxCell id="vertex:cloud9:arn:aws:cloud9:us-west-1:123456789012:service/cloud9/123" parent="1" vertex="1">
    <mxGeometry width="78" height="50" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#C925D1;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.cloud9;"
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
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|shape| mxgraph.aws4.cloud9 |
|sketch| 0 |
|strokeColor| none |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 78  |
| height   |50|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:cloud9:arn:aws:cloud9:us-west-1:123456789012:service/cloud9/123" value="&lt;b&gt;Name&lt;/b&gt;: Code Star&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:cloud9:us-west-1:123456789012:service/cloud9/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;id&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;name&lt;/b&gt;: Dev env&lt;BR&gt;&lt;b&gt;description&lt;/b&gt;: Development env&lt;BR&gt;&lt;b&gt;type&lt;/b&gt;: ssh&lt;BR&gt;&lt;b&gt;connectionType&lt;/b&gt;: CONNECT_SSH&lt;BR&gt;&lt;b&gt;arn&lt;/b&gt;: ARN&lt;BR&gt;&lt;b&gt;lifecycle&lt;/b&gt;: CREATING" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#C925D1;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.cloud9;" parent="1" vertex="1">
                    <mxGeometry width="78" height="50" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``cloud9.drawio``:

[Download](output/drawio/cloud9.drawio){: .btn .btn-purple }