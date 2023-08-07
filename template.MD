---
layout: default
title: {{desc}}
parent: AWS Components
nav_order: 1
date: 2023-08-06
---

# {{desc}}
{: .d-inline-block }

New (v{{version}})
{: .label .label-green }

## Node Type: ``{{node_type}}``

## Code Snippet:

```python
{{ "{% root_include_snippet ../tests/aws/test_" + node_type + ".py %" + "}" }}
```

## Rendering:

![lambda](output/jpg/{{node_type}}.jpg)


## drawio {{node_type}} vertex:

```xml
{{xml_node}}
```

## Advanced for Geeks:

### Style:
```html
style="{{style}}"
```
### Vertex size:

| width     | height   |
|:----------|:---------|
| {{width}} | {{height}}|

### Full XML dump:
```xml
        {{xml_full}}
```

### drawio file:

Download generated ``{{node_type}}.drawio``:

[Download](output/drawio/{{node_type}}.drawio){: .btn .btn-purple }
