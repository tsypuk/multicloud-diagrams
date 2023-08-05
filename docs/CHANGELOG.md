---
title: CHANGELOG
layout: default
---

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [0.3.10](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.3.10) - 2023-08-01

<small>[Compare with 0.3.9](https://github.com/tsypuk/multicloud-diagrams/compare/0.3.9...0.3.10)</small>

### Docs

- udpated readme ([791d298](https://github.com/tsypuk/multicloud-diagrams/commit/791d29859860514c26e6b9fd85ca794e45014f9a) by Roman Tsypuk).
- updated changelog ([c61e12c](https://github.com/tsypuk/multicloud-diagrams/commit/c61e12cd8666e61cec62c29eee5968c723859297) by Roman Tsypuk).

### Features

- added snapshot to diagram ([b855cc5](https://github.com/tsypuk/multicloud-diagrams/commit/b855cc58a665f07a519748112635d5d7b867d3c9) by Roman Tsypuk).
- added fillColor change for any AWS node; added tests ([8e40b52](https://github.com/tsypuk/multicloud-diagrams/commit/8e40b52f17e88b75cc5a48220e79c0f84db610c0) by Roman Tsypuk).
- added shadow mode for rendering ([21cc025](https://github.com/tsypuk/multicloud-diagrams/commit/21cc025717b3be461a3b076a034a64741eb08e29) by Roman Tsypuk).
- aws nodes can be added to different drawio layers ([b58584f](https://github.com/tsypuk/multicloud-diagrams/commit/b58584fcf9d9cee06ea2eff2eb9a47a484ec99e1) by Roman Tsypuk).
- support layers in the draw.io ([e210ec9](https://github.com/tsypuk/multicloud-diagrams/commit/e210ec94af94d22bfb2a2652a8845056a519b43b) by Roman Tsypuk).

### Tests

- added label in edge verification; added fill dump function ([97e08e1](https://github.com/tsypuk/multicloud-diagrams/commit/97e08e10070e89cc340470ecc8dd9c2f9fda1fcb) by Roman Tsypuk).
- added edge connection link between edges (sqs and lambda) ([17083d8](https://github.com/tsypuk/multicloud-diagrams/commit/17083d8ff98afcfc7513abd6b1bb75e58876df96) by Roman Tsypuk).
- refactoring ([86b9a82](https://github.com/tsypuk/multicloud-diagrams/commit/86b9a824be6e706b7a784299377cf8dfa4887c83) by Roman Tsypuk).
- debug_mode verification added ([5cdbd93](https://github.com/tsypuk/multicloud-diagrams/commit/5cdbd93aaa2d8c3e2eb82eb14705d290a35e8637) by Roman Tsypuk).
- full generic verification of aws node based on provider.json; fixed style duplicated values ([99259b5](https://github.com/tsypuk/multicloud-diagrams/commit/99259b5c5fea387d0b149dfa62cbee35733953f3) by Roman Tsypuk).
- added lambda vertex verification ([f936b9a](https://github.com/tsypuk/multicloud-diagrams/commit/f936b9a653374771f6afa9effd3189c24a28b9da) by Roman Tsypuk).
- added sns vertex verification ([8be56a5](https://github.com/tsypuk/multicloud-diagrams/commit/8be56a5bb87c16537b21fb9bd17bd3510087d42a) by Roman Tsypuk).
- added sqs vertex verification ([03ecea8](https://github.com/tsypuk/multicloud-diagrams/commit/03ecea8433c5b3a8995198bd219d72eb0fcff253) by Roman Tsypuk).
- move utils ([167db1a](https://github.com/tsypuk/multicloud-diagrams/commit/167db1a6b34190f0f000c61f8ba212581860c8b2) by Roman Tsypuk).
- added aws dynamodb vertex verification ([536e357](https://github.com/tsypuk/multicloud-diagrams/commit/536e357737c6c2da7ff48bbfc73a65cadea94608) by Roman Tsypuk).
- cover default drawio; small refactoring ([ac357f4](https://github.com/tsypuk/multicloud-diagrams/commit/ac357f4cdc4fba523b659dc9140c1dd29085d659) by Roman Tsypuk).
- added github tests run ([8dcda03](https://github.com/tsypuk/multicloud-diagrams/commit/8dcda03e51c141f34853581512112701e0c1491d) by Roman Tsypuk).

## [0.3.9](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.3.9) - 2023-07-24

<small>[Compare with 0.3.2](https://github.com/tsypuk/multicloud-diagrams/compare/0.3.2...0.3.9)</small>

### Docs

- updated docs ([0ef5b6d](https://github.com/tsypuk/multicloud-diagrams/commit/0ef5b6de770589f3d8c906bd98e2db1591964650) by Roman Tsypuk).

### Features

- coordinates of label on edges are persisted; reload label position from previous version of diagram ([a630f2c](https://github.com/tsypuk/multicloud-diagrams/commit/a630f2cefdc3707b53645275390cce713f95c7b6) by Roman Tsypuk).
- list element marked with bold key and stroke text for value; added ':' delimiter ([7ac91e4](https://github.com/tsypuk/multicloud-diagrams/commit/7ac91e47227c1e57b7b8f3777dc54e40a72c61da) by Roman Tsypuk).
- height and width are persisted; loaded from previous diagram version for all nodes and lists ([b9f8437](https://github.com/tsypuk/multicloud-diagrams/commit/b9f84373fa172d459c611d84b19ed9385a768d69) by Roman Tsypuk).
- added support for mq, http, amazon mq, added call  with enum service ([a92bc42](https://github.com/tsypuk/multicloud-diagrams/commit/a92bc4225323230ce99d8da609c8c25ad1e89b05) by Roman Tsypuk).
- added table fill for drawio; tableID is optional for backward compatibility ([3bd6351](https://github.com/tsypuk/multicloud-diagrams/commit/3bd635187282d7779d0e4e200960429acd03af54) by Roman Tsypuk).

## [0.3.2](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.3.2) - 2023-06-15

<small>[Compare with 0.3.1](https://github.com/tsypuk/multicloud-diagrams/compare/0.3.1...0.3.2)</small>

### Features

- add ID,width to list element drawio ([d7b8764](https://github.com/tsypuk/multicloud-diagrams/commit/d7b87646e54bed3a94c9821063cd809240335c71) by Roman Tsypuk).
- Moved fallback icons to dedicated file. Added loading all cloud providers. updated augmented_resources.yaml ([182b2fc](https://github.com/tsypuk/multicloud-diagrams/commit/182b2fc94d0555f0a5f134de36dfb84de5998ba3) by Roman Tsypuk).

## [0.3.1](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.3.1) - 2023-05-18

<small>[Compare with 0.3.0](https://github.com/tsypuk/multicloud-diagrams/compare/0.3.0...0.3.1)</small>

## [0.3.0](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.3.0) - 2023-05-17

<small>[Compare with 0.2.5](https://github.com/tsypuk/multicloud-diagrams/compare/0.2.5...0.3.0)</small>

### Docs

- defined usage options (response parser, as-a-code, yaml-based) ([d875d80](https://github.com/tsypuk/multicloud-diagrams/commit/d875d800cff91dd874cf1e2d87f58c5431ad5d5d) by Roman Tsypuk).

### Features

- added parsing resources from YAML file; support 3options for src/dst edge declaration; YAML definitions can be augmented with other resources ([e1e847d](https://github.com/tsypuk/multicloud-diagrams/commit/e1e847d88e8ab5ecd74e7af6d6379c7c63236a64) by Roman Tsypuk).

### Tests

- added to test to verify yaml parsing for 3 options of edge declaration ([4dbd24e](https://github.com/tsypuk/multicloud-diagrams/commit/4dbd24ed9ab148abebd0621a89488fd2e9e8891f) by Roman Tsypuk).

## [0.2.5](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.2.5) - 2023-05-16

<small>[Compare with 0.2.4](https://github.com/tsypuk/multicloud-diagrams/compare/0.2.4...0.2.5)</small>

### Docs

- cosmetics; configuration; f setup ([1a22aab](https://github.com/tsypuk/multicloud-diagrams/commit/1a22aabf8f38f4192ff1b1cbd9378f03d1c7cebe) by Roman Tsypuk).

### Features

- added parsing of DynamoDB from boto3 spec with rendering table, stream, schema, lsi, gsi, attributes ([1c87828](https://github.com/tsypuk/multicloud-diagrams/commit/1c8782881454a34e4e7c5b5020a5fc7e0761de63) by Roman Tsypuk).

## [0.2.4](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.2.4) - 2023-05-14

<small>[Compare with 0.2.3](https://github.com/tsypuk/multicloud-diagrams/compare/0.2.3...0.2.4)</small>

## [0.2.3](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.2.3) - 2023-05-14

<small>[Compare with 0.2.2](https://github.com/tsypuk/multicloud-diagrams/compare/0.2.2...0.2.3)</small>

## [0.2.2](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.2.2) - 2023-05-14

<small>[Compare with 0.2.1](https://github.com/tsypuk/multicloud-diagrams/compare/0.2.1...0.2.2)</small>

### Docs

- updated project details ([3cc1796](https://github.com/tsypuk/multicloud-diagrams/commit/3cc17965a991268c818539e8c140cdf862cbe59d) by Roman Tsypuk).

## [0.2.1](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.2.1) - 2023-05-14

<small>[Compare with 0.2.0](https://github.com/tsypuk/multicloud-diagrams/compare/0.2.0...0.2.1)</small>

### Features

- added reload coordinates from previous file version; added samples for aws iam ([8cc38fa](https://github.com/tsypuk/multicloud-diagrams/commit/8cc38faf0a7960dfc640412ced16610a12d843ed) by Roman Tsypuk).

## [0.2.0](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.2.0) - 2023-05-14

<small>[Compare with 0.1.0](https://github.com/tsypuk/multicloud-diagrams/compare/0.1.0...0.2.0)</small>

### Features

- added rendering of aws components ([82367c6](https://github.com/tsypuk/multicloud-diagrams/commit/82367c686a1a2dfbdeac7ed37462f1b3b8064804) by Roman Tsypuk).
- added multicloud draw.io core structure ([a4bf4d3](https://github.com/tsypuk/multicloud-diagrams/commit/a4bf4d3dd68258dea785e7929c6971d35f4e63a8) by Roman Tsypuk).

## [0.1.0](https://github.com/tsypuk/multicloud-diagrams/releases/tag/0.1.0) - 2023-05-14

<small>[Compare with first commit](https://github.com/tsypuk/multicloud-diagrams/compare/311af69012640937355931d70b2a0d8013b45585...0.1.0)</small>

### Docs

- updated project descriptions; gitignore updated ([54187c6](https://github.com/tsypuk/multicloud-diagrams/commit/54187c60a9826bce3a6db2fd87da4ee7b07bc817) by Roman Tsypuk).

