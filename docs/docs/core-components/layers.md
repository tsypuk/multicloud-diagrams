---
layout: default
title: Layers
parent: CORE Components
nav_order: 3
date: 2023-08-07
---

# Layers
{: .d-inline-block }

New (v0.3.10)
{: .label .label-green }

Layers enable the division of infrastructure representation into segmented domains, each with a specific focus on functionality or system attributes.

The following example illustrates the utilization of layers to show the progression of ``api-gateway`` flows, spanning from ``endpoints`` and ``methods`` to the storage system of ``DynamoDB``.
In this context, an additional "IAM" layer is incorporated at the apex, further enhancing the representation.


![draw-apigw.gif](../images/draw-apigw.gif)

Common kinds of callouts include `highlight`, `important`, `new`, `note`, and `warning`.

{: .warning }
These callout names are *not* pre-defined by the theme: you need to define your own names.


[^postfix]:
    You can put the callout markup either before or after its content.

#### An untitled callout
{: .no_toc }

```markdown
{: .highlight }
A paragraph
```

{: .highlight }
A paragraph


#### A single paragraph callout
{: .no_toc }

```markdown
{: .note }
A paragraph
```

`{: .note }`
A paragraph

```markdown
{: .note-title }
> My note title
>
> A paragraph with a custom title callout
```

{: .note-title }
> My note title
>
> A paragraph with a custom title callout

#### A multi-paragraph callout
{: .no_toc }

```markdown
{: .important }
> A paragraph
>
> Another paragraph
>
> The last paragraph
```

{: .important }
> A paragraph
>
> Another paragraph
>
> The last paragraph

```markdown
{: .important-title }
> My important title
>
> A paragraph
>
> Another paragraph
>
> The last paragraph
```

{: .important-title }
> My important title
>
> A paragraph
>
> Another paragraph
>
> The last paragraph

#### An indented callout
{: .no_toc }

```markdown
> {: .highlight }
  A paragraph
```

> {: .highlight }
  A paragraph

#### Indented multi-paragraph callouts
{: .no_toc }

```markdown
> {: .new }
> > A paragraph
> >
> > Another paragraph
> >
> > The last paragraph
```

> {: .new }
> > A paragraph
> >
> > Another paragraph
> >
> > The last paragraph


#### Nested callouts
{: .no_toc }

```markdown
{: .important }
> {: .warning }
> A paragraph
```

{: .important }
> {: .warning }
> A paragraph

#### Opaque background
{: .no_toc }

```markdown
{: .important }
> {: .opaque }
> <div markdown="block">
> {: .warning }
> A paragraph
> </div>
```

{: .important }
> {: .opaque }
> <div markdown="block">
> {: .warning }
> A paragraph
> </div>
