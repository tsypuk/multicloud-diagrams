---
layout: default
title: {{desc}}
parent: {{provider | upper }} Components
nav_order: 3
date: {{date}}
---

# {{desc}}
{: .d-inline-block .no_toc }

New (v{{version}})
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

{% if details is defined %}
{: .note }
{{details}}

---
{% endif %}

## Node Type: ``{{node_type}}``

## Rendering:

![lambda](output/jpg/{{node_type}}.jpg)

## Code Snippet:

```python
{{"{% root_include_snippet ../tests/" + provider + "/test_" + node_type + ".py %" + "}"}}
```

## drawio {{node_type}} vertex:

```xml
{{xml_node}}
```
---

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

{% if width is defined or height is defined%}
### Vertex size:

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
