---
layout: default
title: Resource Access Manager
parent: AWS Components
nav_order: 3
date: 2024-06-04
---

# Resource Access Manager
{: .d-inline-block .no_toc }

New (v0.3.43)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``resource_access_manager``

## Rendering:

![lambda](output/jpg/resource_access_manager.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_resource_access_manager.py %}
```

## drawio resource_access_manager vertex:

```xml
<mxCell id="vertex:resource_access_manager:arn:aws:resource_access_manager:us-west-1:123456789012:service/resource_access_manager/" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.resource_access_manager;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #C7131F |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #F54749 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.resource_access_manager |
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
                <mxCell id="vertex:resource_access_manager:arn:aws:resource_access_manager:us-west-1:123456789012:service/resource_access_manager/" value="&lt;b&gt;Name&lt;/b&gt;: resource_access_manager&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:resource_access_manager:us-west-1:123456789012:service/resource_access_manager/&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: resource_access_manager&lt;BR&gt;&lt;b&gt;clusterArn&lt;/b&gt;: arn:aws:resource_access_manager:eu-west-1:123456789012:cluster/resource_access_manager&lt;BR&gt;&lt;b&gt;serviceRegistries&lt;/b&gt;: arn:aws:resource_access_manager:eu-west-1:123456789012:service/resource_access_manager&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;platformVersion&lt;/b&gt;: LATEST&lt;BR&gt;&lt;b&gt;deployment&lt;/b&gt;: arn:aws:resource_access_manager:eu-west-1:123456789012/resource_access_manager:15" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.resource_access_manager;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``resource_access_manager.drawio``:

[Download](output/drawio/resource_access_manager.drawio){: .btn .btn-purple }