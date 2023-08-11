---
layout: default
title: {{desc}}
parent: {{provider | upper }} Components
nav_order: 3
date: 2023-08-06
---

# {{desc}}
{: .d-inline-block }

New (v{{version}})
{: .label .label-green }

{% if details is defined %}
{: .note }
{{details}}
{% endif %}
## Node Type: ``{{node_type}}``

## Code Snippet:

```python
{{"{% root_include_snippet ../tests/" + provider + "/test_" + node_type + ".py %" + "}"}}
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

| attribute | value |
|:----------|:------|
{% for pair in styles| sort(attribute=0) %}
{% if pair[0] != '' %}
|{{ pair[0] }}| {{ pair[1] }} |
{% endif %}
{% endfor %}

### Vertex size:

{% if width is defined or height is defined%}
| attribute | value |
|:---------|:-----------|
{% if width is defined %}
| width    | {{width}}  |
{% endif %}
{% if height is defined %}
| height   |{{height}}|
{% endif %}
{% endif %}

### Full XML dump:
```xml
        {{xml_full}}
```

### drawio file:

Download generated ``{{node_type}}.drawio``:

[Download](output/drawio/{{node_type}}.drawio){: .btn .btn-purple }
