---
layout: default
title: Transit Gateway
parent: AWS2024 Components
nav_order: 3
date: 2024-08-06
---

# Transit Gateway
{: .d-inline-block .no_toc }

New (v0.3.105)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``transit_gateway``

## Rendering:

![lambda](output/jpg/transit_gateway.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_transit_gateway.py %}
```

## drawio transit_gateway vertex:

```xml
<mxCell id="vertex:transit_gateway:arn:aws:transit_gateway:us-west-1:123456789012:service/transit_gateway/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;"
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
|resIcon| mxgraph.aws4.transit_gateway |
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
                <mxCell id="vertex:transit_gateway:arn:aws:transit_gateway:us-west-1:123456789012:service/transit_gateway/123" value="&lt;b&gt;Name&lt;/b&gt;: Transit Gateway&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:transit_gateway:us-west-1:123456789012:service/transit_gateway/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;TransitGatewayId&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;TransitGatewayArn&lt;/b&gt;: ARN&lt;BR&gt;&lt;b&gt;State&lt;/b&gt;: available&lt;BR&gt;&lt;b&gt;OwnerId&lt;/b&gt;: acc-id&lt;BR&gt;&lt;b&gt;CreationTime&lt;/b&gt;: 2024-08-06&lt;BR&gt;&lt;b&gt;AutoAcceptSharedAttachments&lt;/b&gt;: enable&lt;BR&gt;&lt;b&gt;DefaultRouteTableAssociation&lt;/b&gt;: enable&lt;BR&gt;&lt;b&gt;DefaultRouteTablePropagation&lt;/b&gt;: enable&lt;BR&gt;&lt;b&gt;VpnEcmpSupport&lt;/b&gt;: disable&lt;BR&gt;&lt;b&gt;DnsSupport&lt;/b&gt;: enable&lt;BR&gt;&lt;b&gt;SecurityGroupReferencingSupport&lt;/b&gt;: enable&lt;BR&gt;&lt;b&gt;MulticastSupport&lt;/b&gt;: enable" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``transit_gateway.drawio``:

[Download](output/drawio/transit_gateway.drawio){: .btn .btn-purple }