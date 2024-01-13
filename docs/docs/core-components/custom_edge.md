---
layout: default
title: Customizing Edge
parent: CORE Components
nav_order: 3
date: 2023-08-16
---

# Customizing Edge
{: .d-inline-block  .no_toc}

New (v0.3.13)
{: .label .label-green }


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Style Object, Predefined Connections, Generic Customizer

When passing ``style`` parameter, we can customize the representation of particular Edge. Here is the list of most widely used
parameters of style (there are much mode of them, you can customize any).

```python
style = {
    'dashed': '1',
    'strokeColor': '#FF3333',
    'strokeWidth': '3',
    'orthogonalLoop': '1',
    'edgeStyle': 'orthogonalEdgeStyle',
    'curved': '1',
    'startArrow': 'oval',
    'endArrow': 'classicThin',
}
```

{: .highlight }
``multicloud-diagrams`` provides top level functions to apply defined styles based on name. Also, there is generic function ``add_connection``
that has ``style`` parameter to customize any style.

# Predefined Connections:

## Adding standard edge connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py connection%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection.jpg)


## Bidirectional Connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py add_bidirectional_link%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection_bidirectional.jpg)

## Unidirectional Connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py add_unidirectional_link%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection_unidirectional.jpg)

# Generic Customizer:

## Dashed Connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py add_dashed%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection_dashed.jpg)

## Stroked Colored Connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py add_connection_stroked%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection_stroked.jpg)

## Rounded Connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py add_connection_rounded%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection_custom.jpg)


## EdgeStyle Connection

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_connections.py add_connection_edge%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/connection_edgeStyle.jpg)


# Add additional note to existing Label of existing Edge

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/test_adding_note.py note%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/note.jpg)