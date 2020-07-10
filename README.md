# pyBlades (Geometric Algebra)

__pyBlades__ (`pyblades`) is a Python package for Geometric Algebra computations and modelling.

## How to use this Package

_Stay tuned..._

## What is Geometric Algebra?

__Geometric Algebra__ is based on the Abstract Algebra work of Hestenes, Clifford, Graßmann, and others. In classical Euclidean Algebra the Vector Space is denoted as an extension of the Vector Field over the Set of Real Values or Complex Values.

These are the standard vector-based coordinate-systems that are used throughout contemporary 20th/21st-Century science and engineering. Yet, one of the many mathematical limitations of a Vector Space is that while an Inner-Product is generic for any data dimensionality, there is no similarly generic Outer-Product.

There _is_ a [Cross Product](https://en.wikipedia.org/wiki/Cross_product) defined exclusively for 3-dimensional data, but its computation-algorithm is not extensible to other dimensionalities.

__Geometric Algebra__ introduces the generalized/abstracted concept of vectors known as "blades", which support Interior, Exterior, Inner, Outer, Scalar, and Geometric Product operations.

In __Geometric Algebra__ a __blade__ is a local volume of local-dimensionality _within_ the dimensionality of an Algebraic Space.

This is a different approach to computations and modelling than Classical Linear Algebra, so it may be easier to understand through an introductory example, as provided in the next section.

### Example (Euclidean)

For example, let's look at the Euclidean Space of 3-dimensions. We will symbolically defer to this Space-Dimensionality by the letter `n`. So in this case we have: `n = 3`.

By __Geometric Algebra__ definitions, this Space supports __blades__ (spatial-volumes) of local-dimensionalities from 0 up through 3. The local-Dimensionality of a __blade__ is colloquially referred to as its __grade__ or __gradality__. Thus, the __gradality__ of all __blades__ in this example Space are within the set of `{0, 1, 2, 3}`, which actually correspond to the following volumes:

| Gradality (`k`) | Volume Type    |
| --------------- |:--------------:|
| 0               | Point          |
| 1               | Line-Segment   |
| 2               | Parallelogram  |
| 3               | Parallelepiped |

We also note that under Euclidean Algebra, we have the Euclidean Distance metric that explicitly defines _uniqueness_ of data-points in the Space, such that each data-point is defined by an algebraic tuple of length 3, in this example. The length of the elemental Algebraic tuples is colloquially known as the __plicality__ of a Set Element. In this definition, we are using __blades__ as those Elements, and under a Euclidean Space the Space-Dimensionality and the Algebraic Plicality are equivalent by construction. So, even though we would refer to the __plicality__ symbolically with a lowercase-L (`l`), in this case we have `n = l = 3`.

> [_plica_](https://en.wiktionary.org/wiki/plica) refers to a "fold" or a "crease", thus the chosen name for the operational "folds" (numeric values) that are involved in the computation of the Algebraic Field and Space operations.

By construction Euclidean Algebra is `n`-dimensional and `n`-plical, but this is not true for all Algebraic Spaces. For example, under a Projective Space that is `n`-dimensional the Algebra is `(n + 1)`-plical, which is why an `(n-1)`-dimensional Projective Geometry is used to model Geometric Optics in an `n`-dimensional Euclidean Geometry.

So, again, what is a __blade__?

In this example, a `1`-__blade__ (where `k = 1`) is equivalent to the common notion of a "vector".

> __Blades__ are actually quite similar to __tensors__, except that where the Tensor-Product is [commutative](https://en.wikipedia.org/wiki/Commutative_property), the Geometric-Product is anti-commutative. This makes it an order-preserving dyadic operator which allows for extra information to be embedded in the result of the operation. The benefit is essentially that it adds a binary "sign" to __blades__, such that `-b` and `+b` have the same "magnitude" but opposite "directionality". __Blades__ represent the concept of "Directed Volumes" -- also known as "Directional Volumes".

A single "point" of volume is infinitesimally small, in its contents, but it still "exists". Essentially it is a number. So like how `1`-__blades__ are Vectors, `0`-__blades__ are Scalars (signed numerical values).

`k`, the grade or gradality, thus conveniently represents the number of elemental tuples required to define the __blade__. So for `k = 0` over the Set of Real Values, there's `0` tuples, but we still need a real-value for the __blade__, thus the `0`-blade is simply a Real Valued number, and its directionality is its binary sign (`+`/`-`).

For `k = 1`, we have a Vector, which is a tuple of Real Valued numbers, each number has a binary sign, and the overall vector itself has a directionality to it based on the values in the tuple. The length of that tuple is `l`, the plicality. The dimensionality of the Algebraic Space, `n`, is the maximum possible value for `k`, such that there are no __blades__ in an Algebra that have a grade higher than `n`.

In our `n = l = 3` Euclidean example, a `k = 1` __blade__ named `a` might be represented like: `(a_x, a_y, a_z)`, where the magnitude of `a`, also known as the "Absolute Value" is: `|a| = sqrt((a_x ** 2) + (a_y ** 2) + (a_z ** 2))`, the square-root of the sum of the squares (the Euclidean "norm" or "distance-metric").

A `k = 0` blade might be something like `+7`, positive-seven.

A `k = 2` blade would be represented by two tuples, both of length `l = 3`, essentially creating a `3x2` or `2x3` "matrix", similar to how Tensors are often represented as a matrices.

A `k = 3` blade is represented as three tuples, all of length `l = 3`, and the tuples essentially make-up the "vector" definitions of the axes of the `k`-dimensional local-volume that is the __blade__.

A `0` __blade__ has no volume, it is a scalar. For `k = 1`, they have one axis, making them `1`-dimensional, which means that the volume _is_ the length, thus they are lines (line-segments).

When `k = 2` there are two axes that are, by definition, orthogonal to one another, meaning that on the plane where they both lie the angle between them is `90`-degrees (`pi/2` or tau). If you took the inner product of the `1`-__blades__ that define any `2`-__blade__, the result is always `0` -- there's zero amount of projection or "shared volume" between them. These orthogonal "axes" form the outline of half the planar volume defined by a `2`-__blade__. The local-volume is itself a parallelogram.

If `C` is our `2`-__blade__ created from `1`-__blades__ `a` and `b`, then `C = a ^ b` (where `^` is the Wedge-Product, _a.k.a._ the Exterior-Product), such that the sides of `C` are `a` and `b`:

```
      b
    -----
   /    /
a /  C / a
 /    /
 -----
   b
```

As mentioned before `-C = b ^ a`:

```
      b
    -----
   /    /
a / -C / a
 /    /
 -----
   b
```

Identical, but with different "directionality".

> If you're familiar with OpenGL or graphics programs, this comes-up a lot with "faces" of polytopes that are either facing "in" or "out", essentially the direction of the "normal" (vector) on the face determines if it will be drawn or lit with respect to the 3D Engine's camera for a scene, depending on how the light-source vectors are oriented with respect to the normal vector for each face.

A `k = 3` blade will then be a parallelepiped (a 3D parallelogram), a polytope defined by the volume between three `1`-__blades__, or (equivalently) by the volume of a `2`-__blade__ that is "swept"-along a `1`-__blade__.

In fact, the "sweeping" concept may arguably be one of the best metaphorical explanations for how the Wedge-Product (Exterior Product) works.

### Why is this useful?

The benefit of modelling mathematical constructs with __blades__ is simultaneously conceptual and relational.

Conceptually, the __blades__ can easily represent volumes of polytopes and spheroids of any dimensionality.

Relationally, __blades__ unify scalars, lines, planes, and other higher-dimensional volumes into a common algebra with consistent formulas and relationships.

Since the __blades__ are abstract mathematical constructs, they're not explicitly tied to any kind of data domain or representation. This means that they can be used for time-varying data, probability distribution functions, calculus, and mixed-domain data.

And given the Abstract Algebra construction, the plicality unifies Euclidean and Projective Geometry to use the same mathematical elements, without needing to create a lot of one-off exceptions and exemptions. Instead of defining mathematics by exceptions from Classical Linear Algebra, they can be unified in a well-defined Abstract Algebra.

Falling-out of all of this are lots of things like rotations, transformations, and intersections that are much easier to define and symbolically represent.

The difficulty is that the Inner Products (Contractions) and Exterior Product definitions are relatively more complicated to introduce. But again, the benefit is that the complexity of these operations simplify many of the other "downstream" operators.

## References

- https://en.wikipedia.org/wiki/B%C3%A9zier_curve
- https://en.wikipedia.org/wiki/Exterior_algebra
- https://en.wikipedia.org/wiki/Geometric_algebra
- https://en.wikipedia.org/wiki/Clifford_algebra
- https://en.wikipedia.org/wiki/Dual_quaternion
- https://en.wikipedia.org/wiki/Dual_space
- https://en.wikipedia.org/wiki/Conformal_geometric_algebra

## Copyright

Copyright (c) 2020, Tommy P. Keane
