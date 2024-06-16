---
layout: default
title: Kinesis Video Stream
parent: AWS2024 Components
nav_order: 3
date: 2024-06-15
---

# Kinesis Video Stream
{: .d-inline-block .no_toc }

New (v)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``kinesis_video_stream``

## Rendering:

![lambda](output/jpg/kinesis_video_stream.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_kinesis_video_stream.py %}
```

## drawio kinesis_video_stream vertex:

```xml
<mxCell id="vertex:kinesis_video_stream:arn:aws:kinesis_video_stream:us-west-1:123456789012:kinesis_video_stream/glue/1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kinesis_video_streams;"
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
|resIcon| mxgraph.aws4.kinesis_video_streams |
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
                <mxCell id="vertex:kinesis_video_stream:arn:aws:kinesis_video_stream:us-west-1:123456789012:kinesis_video_stream/glue/1" value="&lt;b&gt;Name&lt;/b&gt;: Glue&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:kinesis_video_stream:us-west-1:123456789012:kinesis_video_stream/glue/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;stateMachineArn&lt;/b&gt;: arn:aws:kinesis_video_stream:us-west-1:123456789012:service/kinesis_video_stream/machine1&lt;BR&gt;&lt;b&gt;StreamName&lt;/b&gt;: web-video-stream&lt;BR&gt;&lt;b&gt;MediaType&lt;/b&gt;: mpg4&lt;BR&gt;&lt;b&gt;KmsKeyId&lt;/b&gt;: arn:aws:kms:us-west-1:123456789012:service/kms/k1&lt;BR&gt;&lt;b&gt;Version&lt;/b&gt;: string&lt;BR&gt;&lt;b&gt;Status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;DataRetentionInHours&lt;/b&gt;: 36" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kinesis_video_streams;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``kinesis_video_stream.drawio``:

[Download](output/drawio/kinesis_video_stream.drawio){: .btn .btn-purple }