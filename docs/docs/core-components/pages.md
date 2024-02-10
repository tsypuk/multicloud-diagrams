---
layout: default
title: Pages
parent: CORE Components
nav_order: 3
date: 2024-10-02
---

# Pages
{: .d-inline-block }

New (v0.3.27)
{: .label .label-green }

Drawio support adding pages (aka Tabs). Using following API we can create page, switch between pages and add vertices and edges to dedicated page.

## Code Snippet:

Let's explore how to interact with pages starting from simple example - by adding 2 pages with layers and nodes: 

```python
{% root_include_snippet ../tests/core/test_page.py page%}
```

## Rendering:

![layers](output/jpg/page_2.jpg)

### Full XML dump:

```xml
{% root_include docs/core-components/output/drawio/page_2.drawio%}
```

### drawio file:

Download generated ``pages_2.drawio``:

[Download](output/drawio/pages_2.drawio){: .btn .btn-purple }

