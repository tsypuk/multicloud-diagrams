---
layout: default
title: AWS Backup
parent: AWS Components
nav_order: 3
date: 2024-05-08
---

# AWS Backup
{: .d-inline-block .no_toc }

New (v0.3.36)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``backup``

## Rendering:

![lambda](output/jpg/backup.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_backup.py %}
```

## drawio backup vertex:

```xml
<mxCell id="vertex:backup:arn:aws:backup:us-west-1:123456789012:service/backup" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.backup;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #277116 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #60A337 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.backup |
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
                <mxCell id="vertex:backup:arn:aws:backup:us-west-1:123456789012:service/backup" value="&lt;b&gt;Name&lt;/b&gt;: Full Dynamo&amp;RDS backup&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:backup:us-west-1:123456789012:service/backup&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: backup&lt;BR&gt;&lt;b&gt;Entities&lt;/b&gt;: Dynamo,RDS&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;desiredCount&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;schedule&lt;/b&gt;: none&lt;BR&gt;&lt;b&gt;pendingCount&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;platformVersion&lt;/b&gt;: LATEST&lt;BR&gt;&lt;b&gt;platformFamily&lt;/b&gt;: Linux&lt;BR&gt;&lt;b&gt;deployment&lt;/b&gt;: arn:aws:backup:eu-west-1:123456789012:deployment/backup:15" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.backup;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``backup.drawio``:

[Download](output/drawio/backup.drawio){: .btn .btn-purple }