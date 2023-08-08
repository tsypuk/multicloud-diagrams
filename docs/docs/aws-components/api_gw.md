---
layout: default
title: API Gateway
parent: AWS Components
nav_order: 1
date: 2023-08-06
---

# API Gateway
{: .d-inline-block }

New (v0.2.0)
{: .label .label-green }

## Node Type: ``api_gw``

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_api_gw.py %}
```

## Rendering:

![lambda](output/jpg/api_gw.jpg)

## drawio api_gw vertex:

```xml
<?xml version="1.0" ?>
<mxCell id="vertex:api_gw:esf19s3pag" parent="1" vertex="1">
    <mxGeometry width="76.5" height="93" as="geometry"/>
</mxCell>
```

## Advanced for Geeks:

### Style:
```html
style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.api_gateway;fillColor=#D9A741;gradientColor=none;"
```

| attribute | value |
|:----------|:------|
                |align| left |
                |dashed| 0 |
                |fillColor| #D9A741 |
                |gradientColor| none |
                |html| 1 |
                |outlineConnect| 0 |
                |shape| mxgraph.aws3.api_gateway |
                |verticalAlign| top |
                |verticalLabelPosition| bottom |
    
### Vertex size:

| width    | 76.5  |
|:---------|:-----------|
| height   | 93 |

### Full XML dump:
```xml
        <?xml version="1.0" ?>
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:api_gw:esf19s3pag" value="&lt;b&gt;Name&lt;/b&gt;: APIGW integration with DynamoDB&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: esf19s3pag&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;api_key_source&lt;/b&gt;: HEADER&lt;BR&gt;&lt;b&gt;endpoint_configuration&lt;/b&gt;: {'types': ['EDGE']}" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;shape=mxgraph.aws3.api_gateway;fillColor=#D9A741;gradientColor=none;" parent="1" vertex="1">
                    <mxGeometry width="76.5" height="93" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``api_gw.drawio``:

[Download](output/drawio/api_gw.drawio){: .btn .btn-purple }