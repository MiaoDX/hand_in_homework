# Artistic Tessellations by Growing Curves

The author propose to tessellate a region by **growing curves**:

Employs a **particle system** where particle trails from curves, control the final effects by variations of the initial placement, the placement order, curve direction, and curve properties.

With **smoothed vector field**, we can create image-based mosaic automatically, with other techniques we can reveal some irregular pattern shown in natural scenario, like cracks, scales and rivers and create the illusion of 3D shapes.

## Related work & drawback

* regular tessellations:

region-based methods, not suitable for natural patterns with elongated, irregular, or curved tiles; control over site placement is insufficient.

* non-photorealistic rendering (NPR):

deal with images either with region-based methods like mosaics or with stroke-
based methods **separately**

## Proposed method

* instead of tessellating with individual tiles (or regions), we build the boundary of each tile by the growth of curves
* employs a particle system where **particle trails** form curves
* propose an automatic mosaic method with good texture suggestion
* expand the idea to present both abstract and natural patterns, introducing two variations, a splitting technique and a stacking technique.

## Particle system

Physical simulation implemented with forward Euler integration. Each time step $(\Delta t = 0.01)$, the particle system updates a new position x from previous velocity $v_0$ and previous position $x_0$ based on the dynamics. The sequence of positions constructs a curve. 

The key calculations are as follows:

$a=\frac{F}{m}$ for a force F, $v=v_0+a\times \Delta t, x=x_0+v\times \Delta t$, and we use unit mass $m=1$. We use **different force configurations for different purposes**.


## Different force configurations for different purposes

### mosaic styles

we read $\overrightarrow{F}$ from a vector field (smooth first).

### other abstracts and natural patterns

we use the Lorentz force, previously used to generate magnetic curves:

We use a constant $\overrightarrow{B}={0,0,-1}$, which generates a 2D curve forcing the particle to move in the $xy$ plane:

$$\overrightarrow{F}=q\overrightarrow{v}\times \overrightarrow{B}$$

The value of the charge $q$ controls the curvature of the curve, and we assign it as $q=s\ast f(t)$, so change $f(t)$ we get what we want, there are four types demonstrated in this paper.

* Type I, $f(t)=(500-t)^{0.8}$
* Type II, random irregular curve
    - Used in Splitting Technique to generate cracks or leaves like curve
* Type III,  a slightly flatter curve $f(t) = 0.001\ast (t-((int)(t/500))\ast 500$
    - Used in Stacking Technique to create the illusion of 3D shapes
* Type IV, $f(t) = sgn(AngleChange(f(t_0)) > θ(t)))\ast (f(t_0)+Random(0.0001,0.01))$
    - Jigsaw-like example

## In conclusion

* we can change different $\overrightarrow{F}$ to get different forms
* the study of a group of particles and the management for the collision intersections might bring very convincing illusions of 3D shapes (as pointed out by the author).

