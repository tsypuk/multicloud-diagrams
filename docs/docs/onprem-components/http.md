---
layout: default
title: HTTP server
parent: ONPREM Components
nav_order: 3
date: 2023-08-06
---

# HTTP server
{: .d-inline-block }

New (v0.3.3)
{: .label .label-green }


---

## Node Type: ``http``

## Code Snippet:

```python
{% root_include_snippet ../tests/onprem/test_http.py %}
```

## Rendering:

![lambda](output/jpg/http.jpg)

## drawio http vertex:

```xml
<?xml version="1.0" ?>
<mxCell id="vertex:http:https://somedomain.com" parent="1" vertex="1">
    <mxGeometry width="63" height="66" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.http_protocol;fillColor=#5294CF;gradientColor=none;"
```

| attribute | value |
|:----------|:------|
|align| left |
|dashed| 0 |
|fillColor| #5294CF |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|shape| mxgraph.aws3.http_protocol |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 63  |
| height   |66|

### Full XML dump:
```xml
        <?xml version="1.0" ?>
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:http:https://somedomain.com" value="&lt;b&gt;Name&lt;/b&gt;: mock_data&lt;BR&gt;&lt;b&gt;ID&lt;/b&gt;: https://somedomain.com&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;Owner&lt;/b&gt;: organization1&lt;BR&gt;&lt;b&gt;authorizer&lt;/b&gt;: auth0&lt;BR&gt;&lt;b&gt;Throttling&lt;/b&gt;: 500" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.http_protocol;fillColor=#5294CF;gradientColor=none;" parent="1" vertex="1">
                    <mxGeometry width="63" height="66" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``http.drawio``:

[Download](output/drawio/http.drawio){: .btn .btn-purple }