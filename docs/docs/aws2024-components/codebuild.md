---
layout: default
title: CodeBuild
parent: AWS2024 Components
nav_order: 3
date: 2024-07-16
---

# CodeBuild
{: .d-inline-block .no_toc }

New (v0.3.84)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``codebuild``

## Rendering:

![lambda](output/jpg/codebuild.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_codebuild.py %}
```

## drawio codebuild vertex:

```xml
<mxCell id="vertex:codebuild:arn:aws:codebuild:us-west-1:123456789012:service/codebuild/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codebuild;"
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
|resIcon| mxgraph.aws4.codebuild |
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
                <mxCell id="vertex:codebuild:arn:aws:codebuild:us-west-1:123456789012:service/codebuild/123" value="&lt;b&gt;Name&lt;/b&gt;: Code Build&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:codebuild:us-west-1:123456789012:service/codebuild/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;name&lt;/b&gt;: Build Java src&lt;BR&gt;&lt;b&gt;arn&lt;/b&gt;: ARN&lt;BR&gt;&lt;b&gt;description&lt;/b&gt;: SpringBoot app&lt;BR&gt;&lt;b&gt;source&lt;/b&gt;: CODECOMMIT&lt;BR&gt;&lt;b&gt;gitCloneDepth&lt;/b&gt;: 10&lt;BR&gt;&lt;b&gt;fetchSubmodules&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;auth&lt;/b&gt;: OAUTH&lt;BR&gt;&lt;b&gt;reportBuildStatus&lt;/b&gt;: True" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.codebuild;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``codebuild.drawio``:

[Download](output/drawio/codebuild.drawio){: .btn .btn-purple }