---
layout: default
title: Integration
parent: CORE Components
nav_order: 4
date: 2023-08-07
---

## Integration


```mermaid
flowchart LR
subgraph .
A[multicloud-diagrams\n Framework] <-->| r/w | B[DRAWIO \n diagram];
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

- ``Diagrams as a Code`` approach is initially implemented from early versions. You can track syntax of resources declaration
for [Core](/docs/core-components/), [AWS](/docs/aws-components/) and [On-Prem](/docs/onprem-components/) resources.
- ingestion resources declared in [external ``YAML`` file](/docs/core-components/yaml.html)
  