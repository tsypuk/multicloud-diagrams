---
layout: default
title: Home
nav_order: 1
description: "Explore and Document Your Cloud Infrastructure with multicloud-diagrams"
permalink: /
---

# Explore and Document Your Cloud Infrastructure with ``multicloud-diagrams``

---
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![PyPI version](https://badge.fury.io/py/multicloud-diagrams.svg)](https://badge.fury.io/py/multicloud-diagrams)
![python version](https://img.shields.io/badge/python-%3E%3D%203.7-blue?logo=python)
![tests](https://github.com/tsypuk/multicloud-diagrams/workflows/Run%20tests/badge.svg?branch=main)

{: .highlight }
As **Professional** **Architects**, **Developers** and **DevOps**  with experience in operating on **Public Cloud Providers**, we all recognize the **crucial importance** of **well-documented**
**Infrastructure** and **Architecture** in a representable form for driving successful projects. 

``multicloud-diagrams`` is a framework that combines multiple approaches: ``Diagrams as a Code`` (Dac), resources ingestion from external ``yaml`` sources, interaction through programmatic ``API`` integration.

It allows to store the Infrastructure snippet in ``drawio`` format, which is editable vector-based representation. 
Since source file is not a Raster form, it is easy to edit, customize, position elements based on our needs and track the history.

---
 
- **Documentation:** [https://tsypuk.github.io/multicloud-diagrams/docs/configuration.html](https://tsypuk.github.io/multicloud-diagrams/docs/configuration.html)
- **Source code:** [https://github.com/tsypuk/multicloud-diagrams](https://github.com/tsypuk/multicloud-diagrams)
- **PyPI multicloud-diagrams:** [https://pypi.org/project/multicloud-diagrams/](https://pypi.org/project/multicloud-diagrams/)
- **Bug reports:** [https://github.com/tsypuk/multicloud-diagrams/issues](https://github.com/tsypuk/multicloud-diagrams/issues)

---

## Support OS Project:

{: .highlight }
Support from sponsors is invaluable for the continued maintenance and development of open-source projects.
You can use any of most popular platforms: ``Patreon`` or ``Buy me a Cofee``, by following these links:

- <a href="https://patreon.com/tsypuk"><img width="32" height="32" class="octicon rounded-2 d-block" alt="patreon" src="https://github.githubassets.com/images/modules/site/icons/funding_platforms/patreon.svg"></a>
- <a href="https://www.buymeacoffee.com/tsypuk" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 32px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

---

## Examples of diagrams generated using ``multicloud-diagrams``:

### End-to-End with AWS resources:

![draw-e2e.gif](https://github.com/tsypuk/multicloud-diagrams/raw/main/docs/docs/images/drawio-end2end.gif?raw=True)

---

### API Gateway with integrations:

![draw-apigw.gif](https://github.com/tsypuk/multicloud-diagrams/raw/main/docs/docs/images/draw-apigw.gif?raw=True)

---

### DynamoDB Insights:

![drawio-dynamodb.gif](https://github.com/tsypuk/multicloud-diagrams/raw/main/docs/docs/images/drawio-dynamodb.gif?raw=True)

---

### Augment Diagram from UML:

![drawio-uml.gif](https://github.com/tsypuk/multicloud-diagrams/raw/main/docs/docs/images/uml_animated.gif?raw=True)

---

## Project Evolution Timeline

```mermaid
gantt
       dateFormat  YYYY-MM-DD
       title MultiCloud Diagrams

       section Core
       aws components, multicloud core    :crit, des1, 2023-05-01,2023-05-14
       coords reload                      :active, des2, after des1, 2023-05-15
       dynamodb from boto                 :done, des3, after des2, 2023-05-17
       read from YAML                     :crit, des4, after des3, 2023-05-17
       added list                         :done, des5, after des4, 2023-06-15
       more aws services, persistent coords :done, des6, after des5, 2023-07-24
       github test runner, more aws services : active, des7, after des6, 2023-08-01
       layers support, snapshot : crit, des8, after des7, 2023-08-01
       docs generated from tests, online documentation, landscape :active, des9, after des8, `2023-08-08`
       added map, customization  :done, des10, after des9, 2023-08-20
       vpn, cert manager  :done, des11, after des10, 2023-09-17
       load from mermaid UML  :crit, des12, after des11, 2023-09-30
       load from plant UML  :crit, des13, after des12, 2023-11-18

       section Releases
       v.0.1.0              :done, 2023-05-14, 3d
       v.0.2.0              :done, 2023-05-15, 3d
       v.0.2.4              :done, 2023-05-15, 3d
       v.0.2.5              :done, 2023-05-16, 3d
       v.0.3.2              :done, 2023-06-15, 3d
       v.0.3.9              :done, 2023-07-24, 3d
       v.3.14               :after 2023-09-17, 3d
       v.3.15               :after 2023-09-30, 3d
       v.3.17               :after 2023-10-24, 3d
       v.3.18               :after 2023-11-18, 3d
```

---

## Supported Cloud Provides:

| provider                                                                                       | supported in ``multicloud-diagrams`` |
|:-----------------------------------------------------------------------------------------------|:-------------------------------------|
| ![aws provider](https://img.shields.io/badge/AWS-orange?logo=amazon-aws&color=ff9900)          | **[x]** since project start          |
| ![on premise provider](https://img.shields.io/badge/OnPremise-orange?color=5f87bf)             | **[x]** since **v0.2.1**             |
| ![azure provider](https://img.shields.io/badge/Azure-orange?logo=microsoft-azure&color=0089d6) | **[  ]**                             |
| ![gcp provider](https://img.shields.io/badge/GCP-orange?logo=google-cloud&color=4285f4)        | **[  ]**                             |

---

## Supported Nodes Landscape (Autogenerated on-release):

![landscape.png](https://github.com/tsypuk/multicloud-diagrams/raw/main/landscape.png?raw=True)

---

## Why ``multicloud-diagrams`` is written on Python?

The choice of Python as the programming language for our initial project was driven by several key factors that align seamlessly with our goals and requirements. Here's why Python was selected as the foundation for our project's development:

- **Seamless Integration and Data Ingestion using AWS Boto3** (official SDK for Amazon Web Services, developed in Python).
- **Simplicity**: Python's clean and readable syntax simplifies the development process.
  Its ease of use and elegant structure enable to focus on the core components without being bogged down by unnecessary complexities.
- **Broad Appeal among DevOps and Developers**: Python's popularity within the DevOps and Development communities is undeniable.
  Its extensive adoption is a testament to its effectiveness for building robust applications.
  By choosing Python, we cater to a broader audience, fostering collaboration and easing the learning curve for newcomers.
- **Cross-Platform Availability**: Python's cross-platform compatibility ensures that our project can be run on a wide array of environments without compatibility issues.
  Whether you're working on Windows, macOS, or Linux, Python's ubiquity guarantees consistent functionality across platforms.

## Why ``multicloud-diagrams`` chooses ``drawio`` as the Output Format?
During my exploration of various tools on this journey, I've encountered several options, each with its own set of advantages and compromises. However, after careful consideration, 
the decision to adopt the drawio format emerged as the optimal choice for several compelling reasons:

- **Editable form** of drawio format provides a great level of customization, enabling users to easily fine-tune diagrams to meet specific needs and scenarios.
- **Widespread Adoption**:  with a broad user base, drawio stands as one of the most widely used diagramming tools, ensuring familiarity and compatibility across diverse teams.
- **Enhanced Plugin and Tool Support**: the format seamlessly integrates with a set of plugins and tools, enriching the ecosystem with expanded capabilities and possibilities.
- **Compact File Sizes**: leveraging the drawio format results in compact file sizes, facilitating swift sharing and distribution without compromising visual quality.
- **Git-trackable Infrastructure Evolution**: allowing for efficient tracking and visualization of infrastructure mutations over time.
- **Smooth Compilation to Raster and other formats**: drawio supports out of the box converting to PNG, JPG, PDF, SVG, VSDX, XML

---

[//]: # (#### Thank you to the contributors of ``multicloud-diagrams``)

[//]: # (<ul class="list-style-none">)
[//]: # ({% for contributor in site.github.contributors %})
[//]: # (  <li class="d-inline-block mr-1">)
[//]: # (     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"></a>)
[//]: # (  </li>)
[//]: # ({% endfor %})
[//]: # (</ul>)


[//]: # ([View our Code of Conduct]&#40;https://github.com/tsypuk/multicloud-diagrams/tree/main/CODE_OF_CONDUCT.md&#41; on GitHub repository.)

[Jekyll]: https://jekyllrb.com
[Markdown]: https://daringfireball.net/projects/markdown/
[Liquid]: https://github.com/Shopify/liquid/wiki
[Front matter]: https://jekyllrb.com/docs/front-matter/
[Jekyll configuration]: https://jekyllrb.com/docs/configuration/
[multicloud-diagrams repo]: https://github.com/tsypuk/multicloud-diagrams
[GitHub Pages]: https://pages.github.com/
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
