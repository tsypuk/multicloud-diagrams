---
layout: default
title: Actor
parent: CORE Components
nav_order: 3
date: 2024-01-12
---

# Actor
{: .d-inline-block .no_toc }

New (v0.3.15)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``actor``

## Rendering:

![lambda](output/jpg/actor.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/core/test_actor.py %}
```

## drawio actor vertex:

```xml
<mxCell id="vertex:actor:777abc" parent="1" vertex="1">
    <mxGeometry width="30" height="60" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;"
```

| attribute | value |
|:----------|:------|
|html| 1 |
|outlineConnect| 0 |
|shape| umlActor |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 30  |
| height   |60|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:actor:777abc" value="&lt;b&gt;Name&lt;/b&gt;: User" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;" parent="1" vertex="1">
                    <mxGeometry width="30" height="60" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``actor.drawio``:

[Download](output/drawio/actor.drawio){: .btn .btn-purple }