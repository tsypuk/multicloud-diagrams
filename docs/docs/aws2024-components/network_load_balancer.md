---
layout: default
title: Network Load Balancer
parent: AWS2024 Components
nav_order: 3
date: 2024-08-07
---

# Network Load Balancer
{: .d-inline-block .no_toc }

New (v0.3.105)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``network_load_balancer``

## Rendering:

![lambda](output/jpg/network_load_balancer.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws2024/test_network_load_balancer.py %}
```

## drawio network_load_balancer vertex:

```xml
<mxCell id="vertex:network_load_balancer:arn:aws:network_load_balancer:us-west-1:123456789012:service/network_load_balancer/123" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.network_load_balancer;"
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
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|pointerEvents| 1 |
|shape| mxgraph.aws4.network_load_balancer |
|sketch| 0 |
|strokeColor| none |
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
                <mxCell id="vertex:network_load_balancer:arn:aws:network_load_balancer:us-west-1:123456789012:service/network_load_balancer/123" value="&lt;b&gt;Name&lt;/b&gt;: Network Load Balancer&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:network_load_balancer:us-west-1:123456789012:service/network_load_balancer/123&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;LoadBalancerArn&lt;/b&gt;: ARN&lt;BR&gt;&lt;b&gt;DNSName&lt;/b&gt;: test&lt;BR&gt;&lt;b&gt;CanonicalHostedZoneId&lt;/b&gt;: 4&lt;BR&gt;&lt;b&gt;CreatedTime&lt;/b&gt;: 2024-08-07&lt;BR&gt;&lt;b&gt;LoadBalancerName&lt;/b&gt;: ingestion&lt;BR&gt;&lt;b&gt;Scheme&lt;/b&gt;: internet-facing&lt;BR&gt;&lt;b&gt;VpcId&lt;/b&gt;: test-vpc" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.network_load_balancer;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``network_load_balancer.drawio``:

[Download](output/drawio/network_load_balancer.drawio){: .btn .btn-purple }