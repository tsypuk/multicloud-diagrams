---
layout: default
title: App Sync
parent: AWS Components
nav_order: 3
date: 2024-06-08
---

# App Sync
{: .d-inline-block .no_toc }

New (v0.3.46)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``app_sync``

## Rendering:

![lambda](output/jpg/app_sync.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_app_sync.py %}
```

## drawio app_sync vertex:

```xml
<mxCell id="vertex:app_sync:arn:aws:app_sync:us-west-1:123456789012:service/app_sync/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.appsync;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #BC1356 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #FF4F8B |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.appsync |
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
                <mxCell id="vertex:app_sync:arn:aws:app_sync:us-west-1:123456789012:service/app_sync/123" value="&lt;b&gt;Name&lt;/b&gt;: App Sync&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:app_sync:us-west-1:123456789012:service/app_sync/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: app_sync&lt;BR&gt;&lt;b&gt;userPoolId&lt;/b&gt;: 123&lt;BR&gt;&lt;b&gt;awsRegion&lt;/b&gt;: eu-west-1&lt;BR&gt;&lt;b&gt;defaultAction&lt;/b&gt;: ALLOW&lt;BR&gt;&lt;b&gt;appIdClientRegex&lt;/b&gt;: 123*&lt;BR&gt;&lt;b&gt;authenticationType&lt;/b&gt;: API_KEY |AMAZON_COGNITO_USER_POOLS&lt;BR&gt;&lt;b&gt;xrayEnabled&lt;/b&gt;: True" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.appsync;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``app_sync.drawio``:

[Download](output/drawio/app_sync.drawio){: .btn .btn-purple }