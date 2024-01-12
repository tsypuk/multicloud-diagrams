---
layout: default
title: Customizing Vertex
parent: CORE Components
nav_order: 3
date: 2023-08-16
---

# Customizing Vertex
{: .d-inline-block  .no_toc}

New (v0.3.13)
{: .label .label-green }


## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Use Style Object to override any parameter

When passing ``style`` parameter, we can customize the representation of particular Vertex. Here is the list of most widely used
parameters of style.

```python
style = {
    'fillColor': '#FF0000',
    'fillOpacity': '50',
    'shadow': '1',
    'gradientColor': '#FFFF33',
    'gradientDirection': 'north'
}
```

{: .highlight }
Each Node in this documentation has full list of its style parameters. You can check all styles at ``Advanced for Geeks`` section.

## Changing FillColor to RED (node with Error or Alarm):

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py color_red%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/color_red.jpg)


## Adding Opacity and Background Shadow:

### Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py color_shadow_opacity%}
```

## Rendering:
{: .no_toc }

![layers](output/jpg/color_shadow_opacity.jpg)

## Gradient Fill

When specifying ``gradient fill`` it is mandatory to set 3 style params:
- fillColor
- gradientColor
- gradientDirection

``gradientDirection`` can have the following values:
- north
- south
- west
- east
- radial

## Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py color_gradient%}
```

## Rendering:
{: .no_toc }
![layers](output/jpg/color_gradient.jpg)


## Change the Direction of Vertex:

## Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py color_direction%}
```

## Rendering:
{: .no_toc }
![layers](output/jpg/color_direction.jpg)


## Vertex without any labels:

## Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py color_nolabel%}
```

## Rendering:
{: .no_toc }
![layers](output/jpg/color_nolabel.jpg)


## Applying Colors to Table

## Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py color_table%}
```

## Rendering
{: .no_toc }

![layers](output/jpg/color_table.jpg)

## Hiding NODE ID information when rendering

{: .highlight }
Extra parameter, **hide_id = true** allows to render only node name avoiding any additional information.

## Code Snippet:
{: .no_toc }

```python
{% root_include_snippet ../tests/core/test_colors.py no_id%}
```

## Rendering
{: .no_toc }

![layers](output/jpg/color_no_id.jpg)
