---
layout: default
title: AWS Access Analyzer
parent: AWS Components
nav_order: 3
date: 2024-05-17
---

# AWS Access Analyzer
{: .d-inline-block .no_toc }

New (v0.3.42)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``access_analyzer``

## Rendering:

![lambda](output/jpg/access_analyzer.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_access_analyzer.py %}
```

## drawio access_analyzer vertex:

```xml
<mxCell id="vertex:access_analyzer:arn:aws:access_analyzer:us-west-1:123456789012:service/access_analyzer" parent="1" vertex="1">
    <mxGeometry width="78" height="77" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#BF0816;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.access_analyzer;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #BF0816 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|pointerEvents| 1 |
|shape| mxgraph.aws4.access_analyzer |
|sketch| 0 |
|strokeColor| none |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 78  |
| height   |77|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:access_analyzer:arn:aws:access_analyzer:us-west-1:123456789012:service/access_analyzer" value="&lt;b&gt;Name&lt;/b&gt;: AWS Access Analyzer&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:access_analyzer:us-west-1:123456789012:service/access_analyzer&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: access_analyzer&lt;BR&gt;&lt;b&gt;clusterArn&lt;/b&gt;: arn:aws:access_analyzer:eu-west-1:123456789012:service/access_analyzer&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;findings&lt;/b&gt;: 12&lt;BR&gt;&lt;b&gt;critical&lt;/b&gt;: 2&lt;BR&gt;&lt;b&gt;minor&lt;/b&gt;: 10" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#BF0816;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.access_analyzer;" parent="1" vertex="1">
                    <mxGeometry width="78" height="77" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``access_analyzer.drawio``:

[Download](output/drawio/access_analyzer.drawio){: .btn .btn-purple }