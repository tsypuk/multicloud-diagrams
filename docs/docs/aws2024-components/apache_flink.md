---
layout: default
title: Managed Apache Flink
parent: AWS2024 Components
nav_order: 3
date: 2024-06-23
---

# Managed Apache Flink
{: .d-inline-block .no_toc }

New (v0.3.62)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``apache_flink``

## Rendering:

![lambda](output/jpg/apache_flink.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_apache_flink.py %}
```

## drawio apache_flink vertex:

```xml
<mxCell id="vertex:apache_flink:arn:aws:apache_flink:us-west-1:123456789012:apache_flink/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_service_for_apache_flink;"
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
|resIcon| mxgraph.aws4.managed_service_for_apache_flink |
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
                <mxCell id="vertex:apache_flink:arn:aws:apache_flink:us-west-1:123456789012:apache_flink/123" value="&lt;b&gt;Name&lt;/b&gt;: Registry for images&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:apache_flink:us-west-1:123456789012:apache_flink/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;ApplicationName&lt;/b&gt;: DemoAppProcesor&lt;BR&gt;&lt;b&gt;RuntimeEnvironment&lt;/b&gt;: FLINK-1_8&lt;BR&gt;&lt;b&gt;InputSchema&lt;/b&gt;: {'RecordFormat': {'RecordFormatType': 'JSON'}}&lt;BR&gt;&lt;b&gt;FlinkApplicationConfiguration&lt;/b&gt;: {'CheckpointConfiguration': {'ConfigurationType': 'DEFAULT', 'CheckpointingEnabled': True, 'CheckpointInterval': 60, 'MinPauseBetweenCheckpoints': 10}, 'ParallelismConfiguration': {'ConfigurationType': 'DEFAULT', 'Parallelism': 3, 'ParallelismPerKPU': 10, 'AutoScalingEnabled': True}}" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.managed_service_for_apache_flink;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``apache_flink.drawio``:

[Download](output/drawio/apache_flink.drawio){: .btn .btn-purple }