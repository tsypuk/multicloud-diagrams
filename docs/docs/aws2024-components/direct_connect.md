---
layout: default
title: Direct Connect
parent: AWS2024 Components
nav_order: 3
date: 2024-06-16
---

# Direct Connect
{: .d-inline-block .no_toc }

New (v0.3.56)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``direct_connect``

## Rendering:

![lambda](output/jpg/direct_connect.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_direct_connect.py %}
```

## drawio direct_connect vertex:

```xml
<mxCell id="vertex:direct_connect:arn:aws:direct_connect:us-west-1:123456789012:direct_connect/glue/1" parent="1" vertex="1">
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
                <mxCell id="vertex:direct_connect:arn:aws:direct_connect:us-west-1:123456789012:direct_connect/glue/1" value="&lt;b&gt;Name&lt;/b&gt;: Glue&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:direct_connect:us-west-1:123456789012:direct_connect/glue/1&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;ownerAccount&lt;/b&gt;: 123456789012&lt;BR&gt;&lt;b&gt;connectionId&lt;/b&gt;: 777&lt;BR&gt;&lt;b&gt;connectionName&lt;/b&gt;: Vodafone-telco&lt;BR&gt;&lt;b&gt;connectionState&lt;/b&gt;: available&lt;BR&gt;&lt;b&gt;region&lt;/b&gt;: us-west-1&lt;BR&gt;&lt;b&gt;location&lt;/b&gt;: San Diego&lt;BR&gt;&lt;b&gt;bandwidth&lt;/b&gt;: 5G&lt;BR&gt;&lt;b&gt;vlan&lt;/b&gt;: 9099&lt;BR&gt;&lt;b&gt;partnerName&lt;/b&gt;: ISP locator&lt;BR&gt;&lt;b&gt;lagId&lt;/b&gt;: 2WAN+&lt;BR&gt;&lt;b&gt;awsDevice&lt;/b&gt;: pfsense:ID:775&lt;BR&gt;&lt;b&gt;jumboFrameCapable&lt;/b&gt;: True&lt;BR&gt;&lt;b&gt;awsDeviceV2&lt;/b&gt;: enabled" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.transit_gateway;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``direct_connect.drawio``:

[Download](output/drawio/direct_connect.drawio){: .btn .btn-purple }