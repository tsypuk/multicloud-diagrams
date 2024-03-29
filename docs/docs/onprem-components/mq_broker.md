---
layout: default
title: MQ Broker
parent: ONPREM Components
nav_order: 3
date: 2023-08-11
---

# MQ Broker
{: .d-inline-block .no_toc }

New (v0.3.3)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``mq_broker``

## Rendering:

![lambda](output/jpg/mq_broker.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/onprem/test_mq_broker.py %}
```

## drawio mq_broker vertex:

```xml
<mxCell id="vertex:mq_broker:mq.eventbroker.somedomain.com" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;gradientColor=none;fillColor=#B0084D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.mq_broker;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #B0084D |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|pointerEvents| 1 |
|shape| mxgraph.aws4.mq_broker |
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
                <mxCell id="vertex:mq_broker:mq.eventbroker.somedomain.com" value="&lt;b&gt;Name&lt;/b&gt;: broker&lt;BR&gt;&lt;b&gt;ID&lt;/b&gt;: mq.eventbroker.somedomain.com&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;Nodes&lt;/b&gt;: 4&lt;BR&gt;&lt;b&gt;Active Master&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;Errors&lt;/b&gt;: 3&lt;BR&gt;&lt;b&gt;Storage&lt;/b&gt;: 4G&lt;BR&gt;&lt;b&gt;Client&lt;/b&gt;: 15" style="sketch=0;outlineConnect=0;gradientColor=none;fillColor=#B0084D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.mq_broker;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``mq_broker.drawio``:

[Download](output/drawio/mq_broker.drawio){: .btn .btn-purple }