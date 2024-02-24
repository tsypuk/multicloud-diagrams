---
layout: default
title: Integration
parent: CORE Components
nav_order: 4
date: 2023-08-07
---

## Integration:

```mermaid
flowchart LR
subgraph Engine
A[multicloud-diagrams\n Framework] <-->| r/w | B[DRAWIO \n diagram:latest];
A[multicloud-diagrams\n Framework] -->| w | C[Historical \n repo];
end

subgraph Data Sources
Y[YAML] --> A
D[DaC \n Diagrams as Code] --> A
BOTO3[AWS boto3 library] --> A
IAC[IaC \n infrastructure as code] --> A
UML[UML \n sequence diagrams] --> A
M[Mingrammer migration] --> A
end
```

## Implemented Integartions:

- ``Diagrams as a Code`` approach is initially implemented from early versions. You can track syntax of resources declaration
for [Core](../core-components), [AWS](../aws-components) and [On-Prem](../onprem-components) resources.
- ingestion resources declared in [external ``YAML`` file](../core-components/yaml.html)
- augment from UML sequence diagrams [mermaid UML format](../core-components/uml.md)
- augment from UML sequence diagrams [plantuml UML format](../core-components/uml.md)
  