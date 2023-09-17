---
layout: default
title: Client VPN
parent: AWS Components
nav_order: 3
date: 2023-09-17
---

# Client VPN
{: .d-inline-block .no_toc }

New (v0.3.14)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``client_vpn``

## Rendering:

![lambda](output/jpg/client_vpn.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_client_vpn.py %}
```

## drawio client_vpn vertex:

```xml
<mxCell id="vertex:client_vpn:aws:clientvpn:us-west-1:prod/cvpn-endpoint-0e3b" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.client_vpn;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #5A30B5 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #945DF2 |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.client_vpn |
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
                <mxCell id="vertex:client_vpn:aws:clientvpn:us-west-1:prod/cvpn-endpoint-0e3b" value="&lt;b&gt;Name&lt;/b&gt;: vpc-client-vpn&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: aws:clientvpn:us-west-1:prod/cvpn-endpoint-0e3b&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;SplitTunnel&lt;/b&gt;: False&lt;BR&gt;&lt;b&gt;DNSServer&lt;/b&gt;: 8.8.8.8&lt;BR&gt;&lt;b&gt;VPNProtocol&lt;/b&gt;: openVPN&lt;BR&gt;&lt;b&gt;Transport&lt;/b&gt;: UDP&lt;BR&gt;&lt;b&gt;VPNPort&lt;/b&gt;: 443&lt;BR&gt;&lt;b&gt;ClientCertificateARN&lt;/b&gt;: arn:aws:acm:us-west-1:123456789012:certificate/cd2e&lt;BR&gt;&lt;b&gt;ServerCertificateARN&lt;/b&gt;: arn:aws:acm:us-west-1:123456789012:certificate/7d100&lt;BR&gt;&lt;b&gt;Authentication type&lt;/b&gt;: certificate-authentication&lt;BR&gt;&lt;b&gt;DNS Name&lt;/b&gt;: *.cvpn-endpoint-0e3b.prod.clientvpn.us-west-1.amazonaws.com" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.client_vpn;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``client_vpn.drawio``:

[Download](output/drawio/client_vpn.drawio){: .btn .btn-purple }