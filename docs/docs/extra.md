---
layout: default
title: DRAWIO How-To
nav_order: 4
---

# DRAWIO How To
{: .no_toc }

Draw.io has gained widespread popularity as an extensively used editor and file format. Apart from the standard web browser version, it offers various other scenarios for usage, which include:

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---

```python
{% root_include ../samples/samples/aws_iam_from_yaml.py %}
```

## Offline draw.io installation

```shell
brew cask install drawio
```

https://github.com/jgraph/drawio-desktop/releases/

## draw.io in CLI

Here's a command-line example demonstrating how to convert the vector representation of a landscape.drawio file into an output PNG file, while scaling its size to be twice as large
(you can use create and use short ``alias`` in ``CLI`` instead of specifying the full path):

```shell
/Applications/draw.io.app/Contents/MacOS/draw.io -x --border 2 -f png --scale 2 -o landscape.png landscape.drawio
```

Other arguments:

| argument                | description                                                                                                                                                                                        |
|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -f, --format <format>   | if output file name extension is specified, this option is ignored (file type is determined from output extension, possible export formats are pdf, png, jpg, svg, vsdx, and xml) (default: "pdf") |
| -q, --quality <quality> | output image quality for JPEG (default: 90)                                                                                                                                                        |
| t, --transparent        | set transparent background for PNG                                                                                                                                                                 |
| -b, --border <border>   | sets the border width around the diagram (default: 0)                                                                                                                                              |
| -s, --scale <scale>     | scales the diagram size                                                                                                                                                                            |
| --width <width>         | fits the generated image/pdf into the specified width, preserves aspect ratio.                                                                                                                     |
| --height <height>       | fits the generated image/pdf into the specified height, preserves aspect ratio.                                                                                                                    |

## drawio in the browser

Lorem Ipsum

## IntelijIdea drawio plugin

Lorem Ipsum
