---
layout: default
title: DynamoDB Stream
parent: AWS Components
nav_order: 1
date: 2023-08-06
---

# DynamoDB Stream
{: .d-inline-block }

New (v0.2.0)
{: .label .label-green }

## Node Type: ``dynamo_stream``

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_dynamo_stream.py %}
```

## Rendering:

![lambda](output/jpg/dynamo_stream.jpg)

## drawio dynamo_stream vertex:

```xml
<?xml version="1.0" ?>
<mxCell id="vertex:dynamo_stream:arn:aws:dynamodb:eu-west-1:123456789012:table/test-table/stream" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#2E27AD;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.dynamodb_stream"
```

| attribute | value |
|:----------|:------|
            |align| left |
                |aspect| fixed |
                |dashed| 0 |
                |fillColor| #2E27AD |
                |fontColor| #232F3E |
                |fontSize| 12 |
                |fontStyle| 0 |
                |gradientColor| none |
                |html| 1 |
                |outlineConnect| 0 |
                |pointerEvents| 1 |
                |shape| mxgraph.aws4.dynamodb_stream |
                |sketch| 0 |
                |strokeColor| none |
                |verticalAlign| top |
                |verticalLabelPosition| bottom |
    
### Vertex size:

| width    | 78  |
|:---------|:-----------|
| height   | 78 |

### Full XML dump:
```xml
        <?xml version="1.0" ?>
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:dynamo_stream:arn:aws:dynamodb:eu-west-1:123456789012:table/test-table/stream" value="&lt;b&gt;Name&lt;/b&gt;: 2022-12-05T06:41:33.817&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:dynamodb:eu-west-1:123456789012:table/test-table/stream&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;LatestStreamLabel&lt;/b&gt;: 2022-12-05T06:41:33.817&lt;BR&gt;&lt;b&gt;StreamViewType&lt;/b&gt;: NEW_AND_OLD_IMAGES" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#2E27AD;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.dynamodb_stream" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``dynamo_stream.drawio``:

[Download](output/drawio/dynamo_stream.drawio){: .btn .btn-purple }