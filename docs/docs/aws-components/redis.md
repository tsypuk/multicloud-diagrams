---
layout: default
title: Redis
parent: AWS Components
nav_order: 3
date: 2024-01-08
---

# Redis
{: .d-inline-block .no_toc }

New (v0.3.20)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``redis``

## Rendering:

![lambda](output/jpg/redis.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_redis.py %}
```

## drawio redis vertex:

```xml
<mxCell id="vertex:redis:arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94" parent="1" vertex="1">
    <mxGeometry width="50" height="42" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;aspect=fixed;html=1;align=left;image;fontSize=12;image=img/lib/mscae/Cache_Redis_Product.svg;labelBackgroundColor=none;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|fontSize| 12 |
|html| 1 |
|image|  |
|image| img/lib/mscae/Cache_Redis_Product.svg |
|labelBackgroundColor| none |
|sketch| 0 |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 50  |
| height   |42|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:redis:arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94" value="&lt;b&gt;Name&lt;/b&gt;: arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:redis:eu-west-1:123456789012/redis/562320f29dbdc94&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;connectivity&lt;/b&gt;: CONNECTED&lt;BR&gt;&lt;b&gt;cluster_nodes&lt;/b&gt;: 3&lt;BR&gt;&lt;b&gt;volume&lt;/b&gt;: 15GB" style="sketch=0;aspect=fixed;html=1;align=left;image;fontSize=12;image=img/lib/mscae/Cache_Redis_Product.svg;labelBackgroundColor=none;" parent="1" vertex="1">
                    <mxGeometry width="50" height="42" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``redis.drawio``:

[Download](output/drawio/redis.drawio){: .btn .btn-purple }