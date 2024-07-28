---
layout: default
title: VPC Private Link
parent: AWS2024 Components
nav_order: 3
date: 2024-07-28
---

# VPC Private Link
{: .d-inline-block .no_toc }

New (v0.3.99)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``vpc_privatelink``

## Rendering:

![lambda](output/jpg/vpc_privatelink.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_vpc_privatelink.py %}
```

## drawio vpc_privatelink vertex:

```xml
<mxCell id="vertex:vpc_privatelink:arn:aws:vpc_privatelink:us-west-1:123456789012:service/vpc_privatelink/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.vpc_privatelink;"
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
|resIcon| mxgraph.aws4.vpc_privatelink |
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
                <mxCell id="vertex:vpc_privatelink:arn:aws:vpc_privatelink:us-west-1:123456789012:service/vpc_privatelink/123" value="&lt;b&gt;Name&lt;/b&gt;: Private Link Connection&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:vpc_privatelink:us-west-1:123456789012:service/vpc_privatelink/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;service_name&lt;/b&gt;: s3&lt;BR&gt;&lt;b&gt;endpoint_url&lt;/b&gt;: https://bucket.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.vpc_privatelink;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``vpc_privatelink.drawio``:

[Download](output/drawio/vpc_privatelink.drawio){: .btn .btn-purple }