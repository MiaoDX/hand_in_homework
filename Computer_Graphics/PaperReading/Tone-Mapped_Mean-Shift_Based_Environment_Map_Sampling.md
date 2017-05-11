# Tone-Mapped Mean-Shift Based Environment Map Sampling

This paper presents a novel approach for environment map sampling, which use adaptive mean-shift image clustering with aid of tone-mapping.

## Problem to solve

Huge computational burden will show up when applying environment map (like HDR environment map) for 3D rendering, since these maps can have thousands of directional light sources corresponding to image pixels. 

So, we would like effective methods to make environment map suitable for 3D rendering. And **environment map sampling** is appealing since it reduces the computational scale greatly by means of approximating environment maps with a finite number of directional lights, so we need a nice way to sample the map. The final result is decompose an environment map into **small strata**, with **one** directional light casted in one stratum.

## Proposed method

There are many prior work in this filed, the proposed method distinguish itself in these ways:

* Irregular decomposition: 

Over-segments an environment map by adaptive mean-shift clustering, with larger kernel sizes for higher intensities, so can do well on **non-uniform** intensity distribution of environment maps

* Adaptive Mean-Shift Clustering by Tone-Mapping: 

Classical Mean-Shift Clustering get low-quality segmentation results for HDR environment maps. So, intuitively, we want to define a larger bandwidth in the high-intensity range, and a smaller bandwidth in the low-intensity range. However, not so easy to do (the k-nearest neighbor way).

So, the author ***change the point of view***, 

>**We think that using adaptive bandwidth is equivalent to adjusting intensity values of the environment map**. Following this idea, we compress the intensity range adaptively, with more compression on the high intensity range. After non-linear compression, we still adopt a fixed bandwidth, which eventually corresponds to a varying bandwidth in the original intensity range.

Wow, pretty neat.

And then, much better segments can be generated for HRD map.

* Strata Construction via Adaptive Split-and-Merge

The segments cannot be treated as strata directly, since 

1. number of segments is not **user-controlled**
2. some visible light (highlight) regions may occupy large (or relatively large) area, leading to high **importance** metric values, and thus they will need
more light samples. 

So, the author proposed a Split-and-Merge method to do this, for the **importance** part they adopt method from "Structured importance sampling of environment maps".

An intuitive explanation is as below:

* Split regions whose energy is much larger than the average importance

These regions are less importance region with more energy than they should have

* Merge: hierarchically combines the neighboring regions while maintaining importance balance.

A little like ***Huffman coding***, merge the region with the
***minimum*** importance metric value and choose the region combination is the ***minimum among all possible choices***.

* And the ***Adaptive merging using adjacency matrix*** is also pretty sweet.

## Personal Opinion 

Make hard things easy and easy things done is one of my motto, this work meet this really well.

* **We think that using adaptive bandwidth is equivalent to adjusting intensity values of the environment map** makes adaptive segment much easier
* ***Huffman coding*** method (in my opinion) makes merge choice pretty clear
* ***Adaptive merging using adjacency matrix*** looks nice.
