---
layout: default
title: Site to site vpn
parent: AWS2024 Components
nav_order: 3
date: 2024-08-04
---

# Site to site vpn
{: .d-inline-block .no_toc }

New (v0.3.103)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``site_to_site_vpn``

## Rendering:

![lambda](output/jpg/site_to_site_vpn.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_site_to_site_vpn.py %}
```

## drawio site_to_site_vpn vertex:

```xml
<mxCell id="vertex:site_to_site_vpn:arn:aws:site_to_site_vpn:us-west-1:123456789012:service/site_to_site_vpn/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.site_to_site_vpn;"
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
|resIcon| mxgraph.aws4.site_to_site_vpn |
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
                <mxCell id="vertex:site_to_site_vpn:arn:aws:site_to_site_vpn:us-west-1:123456789012:service/site_to_site_vpn/123" value="&lt;b&gt;Name&lt;/b&gt;: Site to Site VPN&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:site_to_site_vpn:us-west-1:123456789012:service/site_to_site_vpn/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;vpn_name&lt;/b&gt;: Office Seatle&lt;BR&gt;&lt;b&gt;cidr&lt;/b&gt;: 172.23.20.20/0&lt;BR&gt;&lt;b&gt;connection_endpoint&lt;/b&gt;: 202.1.1.14" style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.site_to_site_vpn;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``site_to_site_vpn.drawio``:

[Download](output/drawio/site_to_site_vpn.drawio){: .btn .btn-purple }