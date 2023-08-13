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

{: .d-inline-block }
``Diagrams as a Code`` approach is initially implemented from early versions. You can track syntax of resources declaration
for [Core](/docs/core-components/), [AWS](/docs/aws-components/) and [On-Prem](/docs/onprem-components/) resources.

New (v0.2.1)
{: .label .label-green }

{: .d-inline-block }
ingestion resources declared in external ``YAML`` file

New (v0.3.8)
{: .label .label-green }

<BR>
