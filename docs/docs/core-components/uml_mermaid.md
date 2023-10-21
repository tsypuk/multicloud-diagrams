---
layout: default
title: UML from mermaid
parent: CORE Components
nav_order: 5
date: 2023-10-21
---

## UML ingestion from mermaid format

{: .d-inline-block .no_toc }

New (v0.3.15)
{: .label .label-green }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---


{: .note }
Record are rows of text.

---

Latest ``Multicloud-diagrams`` feature allows automatically parse sequence UML diagrams, detect actors, actions and represent them on source Diagram as additional connected nodes with aliases.
This makes documenting infrastructure even more robust.

## Source infrastructure Diagram:

We have existing infrastructure diagram that describes ``AWS`` components of architecture:
- [diagram drawio](output/drawio/output.prod.end2end.drawio)

![Starting](output/jpg/output.prod.end2end.jpg)

## Mermaid UML Diagrams

Following UML diagram in ``mermaid`` format describes ``File upload`` stage:
- [file_upload.mermaid](../samples/samples/file_upload.mermaid)

### Mermaid UML rendered diagram:

```mermaid
{% root_include ../samples/samples/file_upload.mermaid%}
```

### Advanced for Geeks(Mermaid UML sources):

```
{% root_include ../samples/samples/file_upload.mermaid%}
```

Next UML diagram in ``mermaid`` format describes ``Processing`` stage:
- [file_upload.mermaid](../samples/samples/process.mermaid)

### Mermaid UML rendered diagram:

```mermaid
{% root_include ../samples/samples/process.mermaid%}
```

### Advanced for Geeks(Mermaid UML sources):

```
{% root_include ../samples/samples/process.mermaid%}
```

## Ingesting UML metadata into multicloud-diagrams:

### Load initial ``drawio`` infra diagram

As usual, we create a new diagram using ``Diagrams-As-a-Code`` or open exising one:

```python
{% root_include ../samples/samples/aws_mermaid_uml.py 1:11%}
```

### Define mappings 

Now it is time to define mappings between diagram elements ``ID``s and aliases used in ``UML`` sequence diagram.

```python
{% root_include ../samples/samples/aws_mermaid_uml.py 14:14%}
```

### Mapping format structure 

Mappings are defined in ``yaml`` format, they specify relations between ``actor`` from UML and ``node_id`` from diagrams.

```yaml
{% root_include ../samples/samples/uml_mapping.yml%}
```

### Generate MetaInformation Layer

For each UML diagram, ``multicloud-diagrams`` will created ``Layer`` in ``draw-io`` and augment relations and actions to existing elements.

Customization of colors, fonts, arrows are fully supported. In this example we are creating distinct styles for each UML diagram (they will be rendered with different colors).

```python
{% root_include ../samples/samples/aws_mermaid_uml.py 15:32%}
```

Augment second ``UML`` diagram into ``multicloud-diagrams`` with different styles instrumented.

```python
{% root_include ../samples/samples/aws_mermaid_uml.py 34:52%}
```

There is option to overwrite the same file or produce a new one. We will use the second option.

```python
{% root_include ../samples/samples/aws_mermaid_uml.py 54:55%}
```

### Result File

![result](output/jpg/output.prod_uml.end2end.jpg)

### Fully Editable Diagram with Layers from UML

Each layer has a name of UML file that we ingested, all actions from each UML are marked with numbers, customized with colors and added on top of existing infra elements (draggable, editable):

![drawio-uml.gif](https://github.com/tsypuk/multicloud-diagrams/raw/main/docs/docs/images/uml_animated.gif?raw=True)

---
