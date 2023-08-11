---
layout: default
title: Load from YAML
parent: CORE Components
nav_order: 2
date: 2023-08-11
---

# Load resources from YAML file
{: .d-inline-block }

New (v0.3.8)
{: .label .label-green }

{: .highlight }
Ingest extra resources from yaml configuration into DRAWIO diagram. Allows to add vertices and edges to empty diagram
or to existing one. To cover the case if there are relationships that you can not programmatically query but want to visualtize.
## Node Type: ``snapshot``

## yaml file with declaration of resource:

Currently, it is supports 3 different syntax's of declaration: 
- src/dst are linked to yaml vertices by name
- src/dst are linked by ARN (ARN can be present in same yaml, or loaded programmatically)
- mixed of 1st and 2nd

```yaml
{% root_include ../samples/samples/augmented_resources.yaml %}
```

## Code Snippet:

```python
{% root_include_snippet ../tests/core/test_yaml.py yaml%}
```

## Rendering:

![lambda](output/jpg/yaml.jpg)


### drawio file:

Download generated ``yaml.drawio``:

[Download](output/drawio/yaml.drawio){: .btn .btn-purple }

## Augment resources both from code and YAML:

{: .highlight }
Other option is to combine Diagrams as Code (DaC) by declaring all resources in code and also ingest additional vertices from YAML file.
This is very useful when you have custom resources that are not supported by libraries to query (not available in ``boto3`` or on-prem resources).

## yaml file with resources declaration:

```yaml
{% root_include ../samples/samples/augmented_resources2.yaml %}
```

## Code Snippet:

```python
{% root_include_snippet ../tests/core/test_yaml.py yaml_to_existing_file %}
```

## Rendering:

![lambda](output/jpg/yaml2.jpg)


### drawio file:

Download generated ``yaml2.drawio``:

[Download](output/drawio/yaml2.drawio){: .btn .btn-purple }
