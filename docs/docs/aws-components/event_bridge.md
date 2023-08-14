---
layout: default
title: Event Bridge
parent: AWS Components
nav_order: 3
date: 2023-08-06
---

# Event Bridge
{: .d-inline-block }

New (v0.3.11)
{: .label .label-green }


---

## Node Type: ``event_bridge``

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_event_bridge.py %}
```

## Rendering:

![lambda](output/jpg/event_bridge.jpg)

## drawio event_bridge vertex:

```xml
<mxCell id="vertex:event_bridge:arn:aws:scheduler:eu-west-1:123456789012:schedule/group-1/schedule-rate" parent="1" vertex="1">
    <mxGeometry width="78" height="78" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #BC1356 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| #FF4F8B |
|gradientDirection| north |
|html| 1 |
|outlineConnect| 0 |
|resIcon| mxgraph.aws4.eventbridge |
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
                <mxCell id="vertex:event_bridge:arn:aws:scheduler:eu-west-1:123456789012:schedule/group-1/schedule-rate" value="&lt;b&gt;Name&lt;/b&gt;: schedule-rate&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:scheduler:eu-west-1:123456789012:schedule/group-1/schedule-rate&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;Creation Date&lt;/b&gt;: 2023-06-19 13:16:38&lt;BR&gt;&lt;b&gt;End Date&lt;/b&gt;: 2023-09-30 12:30:00&lt;BR&gt;&lt;b&gt;SubscriptionsPending&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;Flexible Time Window&lt;/b&gt;: {'Mode': 'OFF'}&lt;BR&gt;&lt;b&gt;Group Name&lt;/b&gt;: group-1&lt;BR&gt;&lt;b&gt;input&lt;/b&gt;: {&quot;key1&quot;:&quot;val1&quot;,&quot;key2&quot;:&quot;val2&quot;}&lt;BR&gt;&lt;b&gt;Modification Date&lt;/b&gt;: 2023-06-19 13:30:33&lt;BR&gt;&lt;b&gt;Retry Policy&lt;/b&gt;: {'MaximumEventAgeInSeconds': 86400, 'MaximumRetryAttempts': 185}&lt;BR&gt;&lt;b&gt;Role ARN&lt;/b&gt;: arn:aws:iam::123456789012:role/serverless/event_bridge_role&lt;BR&gt;&lt;b&gt;Schedule Expression&lt;/b&gt;: rate(60 days)&lt;BR&gt;&lt;b&gt;Schedule Expression_timezone&lt;/b&gt;: UTC&lt;BR&gt;&lt;b&gt;State&lt;/b&gt;: ENABLED&lt;BR&gt;&lt;b&gt;Target&lt;/b&gt;: arn:aws:lambda:eu-west-1:123456789012:function:target-lambda" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=#FF4F8B;gradientDirection=north;fillColor=#BC1356;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eventbridge;" parent="1" vertex="1">
                    <mxGeometry width="78" height="78" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``event_bridge.drawio``:

[Download](output/drawio/event_bridge.drawio){: .btn .btn-purple }