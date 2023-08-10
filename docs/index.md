---
layout: default
title: Home
nav_order: 1
description: "Just the Docs is a responsive Jekyll theme with built-in search that is easily customizable and hosted on GitHub Pages."
permalink: /
---
# UNDER DEVELOPMENT ! 

# Generate you Cloud Infrastructure into popular draw.io format
{: .fs-9 }

As an architect, developer, or DevOps professional with experience in using Public Cloud Providers, we all recognize the crucial importance of well-documented 
infrastructure and architecture with diagrams for driving successful projects. 

Throughout my journey, I have explored multiple tools available in the market but found them lacking in meeting our specific requirements.

{: .fs-6 .fw-300 }

# Why multicloud-diagrams is written on Python

The choice of Python as the programming language for our initial project was driven by several key factors that align seamlessly with our goals and requirements. Here's why Python was selected as the foundation for our project's development:

- **Seamless Integration and Data Ingestion using AWS Boto3** (official SDK for Amazon Web Services, developed in Python).
- **Simplicity**: Python's clean and readable syntax simplifies the development process. 
Its ease of use and elegant structure enable to focus on the core components without being bogged down by unnecessary complexities.
- **Broad Appeal among DevOps and Developers**: Python's popularity within the DevOps and Development communities is undeniable. 
Its extensive adoption is a testament to its effectiveness for building robust applications. 
By choosing Python, we cater to a broader audience, fostering collaboration and easing the learning curve for newcomers.
- **Cross-Platform Availability**: Python's cross-platform compatibility ensures that our project can be run on a wide array of environments without compatibility issues.
Whether you're working on Windows, macOS, or Linux, Python's ubiquity guarantees consistent functionality across platforms.

[Get started now](docs/configuration.html){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View it on GitHub][multicloud-diagrams repo]{: .btn .fs-5 .mb-4 .mb-md-0 }

---

{: .warning }
> This website documents the features of the current `main` branch of the ``multicloud-diagrams``. See [the CHANGELOG]({% link CHANGELOG.md %}) for a list of releases, new features, and bug fixes.

### Features:
- allows to generate drawio diagram with predefined styles for popular aws services, support graph-based connection with named edges
- supports single and batch elements append to diagram
- duplicates detection to prevent ball of mud in file format and diagram
- verification that both vertices present on diagram when adding edge connection between them
- if the node is not present, fallback to default icon when rendering
- read previous version of drawio file and reuses existing vertices coordinates when generating a new version
- generate diagram from ``YAML`` definition
- mix and augment Diagram-as-code, real infra crawler, static yaml-based content to diagram


### Supported Nodes Landscape:

![landscape.png](https://github.com/tsypuk/multicloud-diagrams/raw/main/landscape.png)

### Cloud Provides:

#### Supported:

![aws provider](https://img.shields.io/badge/AWS-orange?logo=amazon-aws&color=ff9900)
![on premise provider](https://img.shields.io/badge/OnPremise-orange?color=5f87bf)

#### Planned to be added:
![azure provider](https://img.shields.io/badge/Azure-orange?logo=microsoft-azure&color=0089d6)
![gcp provider](https://img.shields.io/badge/GCP-orange?logo=google-cloud&color=4285f4)


## Getting started


## About the project

``Multicloud Diagrams`` is &copy; 2023-{{ "now" | date: "%Y" }} by [Roman Tsypuk](https://tsypuk.github.io/roman_tsypuk.html).

### License

``multicloud-diagrams`` is distributed by an [MIT license](https://github.com/tsypuk/multicloud-diagrams/tree/main/LICENSE.txt).

### Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. Read more about becoming a contributor in [our GitHub repo](https://github.com/tsypuk/multicloud-diagrams#contributing).

#### Thank you to the contributors of ``multicloud-diagrams``

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="32" height="32" alt="{{ contributor.login }}"></a>
  </li>
{% endfor %}
</ul>

### Code of Conduct

Just the Docs is committed to fostering a welcoming community.

[View our Code of Conduct](https://github.com/tsypuk/multicloud-diagrams/tree/main/CODE_OF_CONDUCT.md) on GitHub repository.

----

[Jekyll]: https://jekyllrb.com
[Markdown]: https://daringfireball.net/projects/markdown/
[Liquid]: https://github.com/Shopify/liquid/wiki
[Front matter]: https://jekyllrb.com/docs/front-matter/
[Jekyll configuration]: https://jekyllrb.com/docs/configuration/
[multicloud-diagrams repo]: https://github.com/tsypuk/multicloud-diagrams
[GitHub Pages]: https://pages.github.com/
[GitHub Pages / Actions workflow]: https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/
