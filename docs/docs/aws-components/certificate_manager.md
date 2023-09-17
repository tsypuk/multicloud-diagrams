---
layout: default
title: Certificate Manager
parent: AWS Components
nav_order: 3
date: 2023-09-17
---

# Certificate Manager
{: .d-inline-block .no_toc }

New (v0.3.14)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``certificate_manager``

## Rendering:

![lambda](output/jpg/certificate_manager.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_certificate_manager.py %}
```

## drawio certificate_manager vertex:

```xml
<mxCell id="vertex:certificate_manager:arn:aws:acm:us-west-1:123456789012:certificate/cd2e" parent="1" vertex="1">
    <mxGeometry width="59" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F8624;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.certificate_manager;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #3F8624 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|pointerEvents| 1 |
|shape| mxgraph.aws4.certificate_manager |
|sketch| 0 |
|strokeColor| none |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 59  |
| height   |78|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:certificate_manager:arn:aws:acm:us-west-1:123456789012:certificate/cd2e" value="&lt;b&gt;Name&lt;/b&gt;: Client Certificate&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:acm:us-west-1:123456789012:certificate/cd2e&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:acm:us-west-1:123456789012:certificate/cd2e&lt;BR&gt;&lt;b&gt;Domain&lt;/b&gt;: client1.domain.tld&lt;BR&gt;&lt;b&gt;Type&lt;/b&gt;: Imported&lt;BR&gt;&lt;b&gt;Public Key info&lt;/b&gt;: RSA 2048&lt;BR&gt;&lt;b&gt;Signature algorithm&lt;/b&gt;: SHA-256 with RSA" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#3F8624;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.certificate_manager;" parent="1" vertex="1">
                    <mxGeometry width="59" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``certificate_manager.drawio``:

[Download](output/drawio/certificate_manager.drawio){: .btn .btn-purple }