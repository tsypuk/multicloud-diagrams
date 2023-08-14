---
layout: default
title: DRAWIO How-to
nav_order: 6
date: 2023-08-07
---

# DRAWIO How-to
{: .no_toc }

Draw.io has gained widespread popularity as an extensively used editor and file format. Apart from the standard web browser version, it offers various other scenarios for usage, which include:

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}
---


## Offline draw.io installation

DrawIO is available for installation as standalone app: [https://github.com/jgraph/drawio-desktop/releases/](https://github.com/jgraph/drawio-desktop/releases/).

MacOS command to install:

```shell
brew cask install drawio
```

![img.png](images/drawio-desktop.png)

## draw.io as CLI

Also, not many users are aware, but you can use installed DrawIO app as a command-line tool.
Here we are converting the vector representation of a ``landscape.drawio`` file into an output ``PNG`` file, while scaling its size to be twice as large
(you define and use ``short`` or ``alias`` in ``CLI`` instead of specifying the full path):

```shell
/Applications/draw.io.app/Contents/MacOS/draw.io -x --border 2 -f png --scale 2 -o landscape.png landscape.drawio
```

{: .highlight }
Very useful to use in automated Pipelines, to convert diagrams into desired output format (png, pdf, jpg, msvg, vsdx, xml) of you ``catalogue`` representation. 

Other available CLI arguments:

| argument                          | description                                                                                                                                                                                        |
|:----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -f, --format <format>             | if output file name extension is specified, this option is ignored (file type is determined from output extension, possible export formats are pdf, png, jpg, svg, vsdx, and xml) (default: "pdf") |
| -q, --quality <quality>           | output image quality for JPEG (default: 90)                                                                                                                                                        |
| -t, --transparent                 | set transparent background for PNG                                                                                                                                                                 |
| -b, --border <border>             | sets the border width around the diagram (default: 0)                                                                                                                                              |
| -s, --scale <scale>               | scales the diagram size                                                                                                                                                                            |
| --width <width>                   | fits the generated image/pdf into the specified width, preserves aspect ratio.                                                                                                                     |
| --height <height>                 | fits the generated image/pdf into the specified height, preserves aspect ratio.                                                                                                                    |
| -x, --export                      | export the input file/folder based on the given options                                                                                                                                            |
| -r, --recursive                   | for a folder input, recursively convert all files in sub-folders also                                                                                                                              |
| -o, --output <output file/folder> | specify the output file/folder. If omitted, the input file name is used for output with the specified format as extension                                                                          |

Example of ``CLI`` command that will recursively convert all ``drawio`` files in ``docs/docs/aws-components/output/drawio`` folder, convert them into ``JPG`` with ``100%`` quality
and output as multiple ``jpeg`` files into folder ``docs/docs/aws-components/output/jpg``

```shell
/Applications/draw.io.app/Contents/MacOS/draw.io -q 100 -x -f jpg -r -o docs/docs/aws-components/output/jpg docs/docs/aws-components/output/drawio 
```

## draw.io in any  browser

The browser version is likely the most widely used one, as I've observed numerous engineers start their journey from it.
Also, useful when you are on another setup (any machine has ``browser``).

Simply go to: [https://app.diagrams.net/](https://app.diagrams.net/)

![img.png](images/drawio-browser.png)

## IntelliJ IDEA drawio plugin

The best IDEA for development, perfectly integrated ``drawio`` plugin. Nothing to add, just enjoy it 😎

![img.png](images/drawio-idea.png)
