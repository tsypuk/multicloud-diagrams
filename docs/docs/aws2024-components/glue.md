---
layout: default
title: Glue
parent: AWS2024 Components
nav_order: 3
date: 2024-06-15
---

# Glue
{: .d-inline-block .no_toc }

New (v0.3.52)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``glue``

## Rendering:

![lambda](output/jpg/glue.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_glue.py %}
```

## drawio glue vertex:

```xml
<mxCell id="vertex:glue:arn:aws:glue:us-west-1:123456789012:service/glue/1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.glue;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #8C4FFF |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.glue |
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
                <mxCell id="vertex:glue:arn:aws:glue:us-west-1:123456789012:service/glue/1" value="&lt;b&gt;Name&lt;/b&gt;: Glue&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:glue:us-west-1:123456789012:service/glue/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;stateMachineArn&lt;/b&gt;: arn:aws:glue:us-west-1:123456789012:service/step_function/machine1&lt;BR&gt;&lt;b&gt;JobMode&lt;/b&gt;: NOTEBOOK&lt;BR&gt;&lt;b&gt;ExecutionProperty&lt;/b&gt;: {'MaxConcurrentRuns': 123}&lt;BR&gt;&lt;b&gt;MaxRetries&lt;/b&gt;: 5&lt;BR&gt;&lt;b&gt;AllocatedCapacity&lt;/b&gt;: 1024&lt;BR&gt;&lt;b&gt;Timeout&lt;/b&gt;: 250&lt;BR&gt;&lt;b&gt;MaxCapacity&lt;/b&gt;: 10.0&lt;BR&gt;&lt;b&gt;WorkerType&lt;/b&gt;: G.1X" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.glue;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``glue.drawio``:

[Download](output/drawio/glue.drawio){: .btn .btn-purple }