---
layout: default
title: Neptune Managed Service
parent: AWS Components
nav_order: 3
date: 2024-02-29
---

# Neptune Managed Service
{: .d-inline-block .no_toc }

New (v0.3.33)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``neptune``

## Rendering:

![lambda](output/jpg/neptune.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_neptune.py %}
```

## drawio neptune vertex:

```xml
<mxCell id="vertex:neptune:arn:aws:rds:us-east-2:123456789012:db:my-neptune-instance-1" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #3334B9 |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #4D72F3 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.neptune |
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
                <mxCell id="vertex:neptune:arn:aws:rds:us-east-2:123456789012:db:my-neptune-instance-1" value="&lt;b&gt;Name&lt;/b&gt;: UsersGraph&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:rds:us-east-2:123456789012:db:my-neptune-instance-1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;data&lt;/b&gt;: 96000&lt;BR&gt;&lt;b&gt;BackupRetentionPeriod&lt;/b&gt;: 123&lt;BR&gt;&lt;b&gt;CharacterSetName&lt;/b&gt;: UTF-8&lt;BR&gt;&lt;b&gt;DatabaseName&lt;/b&gt;: UsersGraph&lt;BR&gt;&lt;b&gt;Endpoint&lt;/b&gt;: my-neptune-instance-1.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182&lt;BR&gt;&lt;b&gt;ReaderEndpoint&lt;/b&gt;: my-neptune-instance-1.cluster-ro-123456789012.us-east-1.neptune.amazonaws.com:8182&lt;BR&gt;&lt;b&gt;MultiAZ&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;Engine&lt;/b&gt;: Neptune&lt;BR&gt;&lt;b&gt;EngineVersion&lt;/b&gt;: v8&lt;BR&gt;&lt;b&gt;StorageEncrypted&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;IAMDatabaseAuthenticationEnabled&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;CopyTagsToSnapshot&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;DeletionProtection&lt;/b&gt;: False&lt;BR&gt;&lt;b&gt;CrossAccountClone&lt;/b&gt;: False" style="sketch=0;outlineConnect=0;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``neptune.drawio``:

[Download](output/drawio/neptune.drawio){: .btn .btn-purple }