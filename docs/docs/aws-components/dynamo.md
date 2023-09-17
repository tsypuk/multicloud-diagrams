---
layout: default
title: DynamoDB
parent: AWS Components
nav_order: 3
date: 2023-08-11
---

# DynamoDB
{: .d-inline-block .no_toc }

New (v0.2.0)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``dynamo``

## Rendering:

![lambda](output/jpg/dynamo.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_dynamo.py %}
```

## drawio dynamo vertex:

```xml
<mxCell id="vertex:dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table" parent="1" vertex="1">
    <mxGeometry width="72" height="81" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.dynamo_db;fillColor=#2E73B8;gradientColor=none;"
```

| attribute | value |
|:----------|:------|
|align| left |
|dashed| 0 |
|fillColor| #2E73B8 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|shape| mxgraph.aws3.dynamo_db |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 72  |
| height   |81|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:dynamo:arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table" value="&lt;b&gt;Name&lt;/b&gt;: prod-dynamo-table&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:dynamodb:eu-west-1:123456789012:table/prod-dynamo-table&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;DeletionProtectionEnabled&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;ItemCount&lt;/b&gt;: 900&lt;BR&gt;&lt;b&gt;TableSizeBytes&lt;/b&gt;: 123&lt;BR&gt;&lt;b&gt;Replicas&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;RCU&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;WCU&lt;/b&gt;: 1" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.dynamo_db;fillColor=#2E73B8;gradientColor=none;" parent="1" vertex="1">
                    <mxGeometry width="72" height="81" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``dynamo.drawio``:

[Download](output/drawio/dynamo.drawio){: .btn .btn-purple }