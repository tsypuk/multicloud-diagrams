---
layout: default
title: Amazon S3 Glacier
parent: AWS Components
nav_order: 3
date: 2024-02-06
---

# Amazon S3 Glacier
{: .d-inline-block .no_toc }

New (v0.3.27)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``glacier``

## Rendering:

![lambda](output/jpg/glacier.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_glacier.py %}
```

## drawio glacier vertex:

```xml
<mxCell id="vertex:glacier:arn:aws:glacier:::content_bucket" parent="1" vertex="1">
    <mxGeometry width="76.5" height="93" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.glacier;fillColor=#E05243;gradientColor=none;"
```

| attribute | value |
|:----------|:------|
|align| left |
|dashed| 0 |
|fillColor| #E05243 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|shape| mxgraph.aws3.glacier |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 76.5  |
| height   |93|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:glacier:arn:aws:glacier:::content_bucket" value="&lt;b&gt;Name&lt;/b&gt;: content_bucket&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:glacier:::content_bucket&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;x-amz-bucket-region&lt;/b&gt;: eu-west-1&lt;BR&gt;&lt;b&gt;CreationDate&lt;/b&gt;: 2023-11-11&lt;BR&gt;&lt;b&gt;AbortIncompleteMultipartUpload&lt;/b&gt;: {'DaysAfterInitiation': 5}&lt;BR&gt;&lt;b&gt;Expiration&lt;/b&gt;: {'Days': 90}&lt;BR&gt;&lt;b&gt;MFADelete&lt;/b&gt;: Disabled" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.glacier;fillColor=#E05243;gradientColor=none;" parent="1" vertex="1">
                    <mxGeometry width="76.5" height="93" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``glacier.drawio``:

[Download](output/drawio/glacier.drawio){: .btn .btn-purple }