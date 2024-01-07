---
layout: default
title: ECS Service
parent: AWS Components
nav_order: 3
date: 2024-01-07
---

# ECS Service
{: .d-inline-block .no_toc }

New (v0.3.19)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


## Node Type: ``ecs_service``

## Rendering:

![lambda](output/jpg/ecs_service.jpg)

## Code Snippet:

```python
{% root_include_snippet ../tests/aws/test_ecs_service.py %}
```

## drawio ecs_service vertex:

```xml
<mxCell id="vertex:ecs_service:arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc" parent="1" vertex="1">
    <mxGeometry width="39" height="48" as="geometry"/>
</mxCell>
```
---

## Advanced for Geeks:

### Style:
```html
style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D45B07;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ecs_service;"
```

| attribute | value |
|:----------|:------|
|align| left |
|aspect| fixed |
|dashed| 0 |
|fillColor| #D45B07 |
|fontColor| #232F3E |
|fontSize| 12 |
|fontStyle| 0 |
|gradientColor| none |
|html| 1 |
|outlineConnect| 0 |
|pointerEvents| 1 |
|shape| mxgraph.aws4.ecs_service |
|sketch| 0 |
|strokeColor| none |
|verticalAlign| top |
|verticalLabelPosition| bottom |

### Vertex size:

| attribute | value |
|:---------|:-----------|
| width    | 39  |
| height   |48|

### Full XML dump:
```xml
<mxfile host="multicloud-diagrams" agent="PIP package multicloud-diagrams. Generate resources in draw.io compatible format for Cloud infrastructure. Copyrights @ Roman Tsypuk 2023. MIT license." type="MultiCloud">
    <diagram id="diagram_1" name="AWS components">
        <mxGraphModel dx="1015" dy="661" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="1">
            <root>
                <mxCell id="0"/>
                <mxCell id="1" parent="0"/>
                <mxCell id="vertex:ecs_service:arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc" value="&lt;b&gt;Name&lt;/b&gt;: Nginx_Service&lt;BR&gt;&lt;b&gt;ARN&lt;/b&gt;: arn:aws:ecs:us-west-1:123456789012:service/fargate-cluster/service-fg-svc&lt;BR&gt;-----------&lt;BR&gt;&lt;b&gt;serviceName&lt;/b&gt;: service-fg-svc&lt;BR&gt;&lt;b&gt;clusterArn&lt;/b&gt;: arn:aws:ecs:eu-west-1:123456789012:cluster/rules-dev-fargate-cluster&lt;BR&gt;&lt;b&gt;serviceRegistries&lt;/b&gt;: arn:aws:servicediscovery:eu-west-1:123456789012:service/srv-t&lt;BR&gt;&lt;b&gt;status&lt;/b&gt;: ACTIVE&lt;BR&gt;&lt;b&gt;desiredCount&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;runningCount&lt;/b&gt;: 1&lt;BR&gt;&lt;b&gt;pendingCount&lt;/b&gt;: 0&lt;BR&gt;&lt;b&gt;launchType&lt;/b&gt;: FARGATE&lt;BR&gt;&lt;b&gt;platformVersion&lt;/b&gt;: LATEST&lt;BR&gt;&lt;b&gt;platformFamily&lt;/b&gt;: Linux&lt;BR&gt;&lt;b&gt;taskDefinition&lt;/b&gt;: arn:aws:ecs:eu-west-1:123456789012:task-definition/service-fg-task:15" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D45B07;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=left;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.ecs_service;" parent="1" vertex="1">
                    <mxGeometry width="39" height="48" as="geometry"/>
                </mxCell>
            </root>
        </mxGraphModel>
    </diagram>
</mxfile>
```

### drawio file:

Download generated ``ecs_service.drawio``:

[Download](output/drawio/ecs_service.drawio){: .btn .btn-purple }