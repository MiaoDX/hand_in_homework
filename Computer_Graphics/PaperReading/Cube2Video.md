# Cube2Video: Navigate Between Cubic Panoramas in Real-Time

Navigate a sparse point-to-point of collection panoramas can be a less pleasant viewing experience, since they will bring users apparent visual discontinuity. The proposed methods overcome this by make the cubic panoramas into much more smoothy movie via triangle-to-triangle homography-based warping and interpolate novel viewpoints from the given reference panoramas.


## Outlines

* extend the matching-triangulation-interpolation procedure with special considerations of the spherical domain
    - employ angular error metric to get reliable sparse correspondences between two cubic panoramas
    - applied convex hull triangulation to triangulate the panorama normalized on the unit sphere
    - interpolate a new warping scheme between pairs of spherical triangles
* proposing a (spherical) triangle-to-triangle warping, which combines homography and affine transformation
    - achieve physically plausible and visually pleasant interpolation results
* describe a compensation transformation to improve the temporal smoothness of the synthesized video

## Some noticeable parts

### Finding Reliable Correspondences

**angular error metric**

assume the angels between different correspondence pairs are close

Avoid wrong candidate matches lie on or close is antipodal to the epipolar plane by translate the point into the second panorama sphere, and calculate the
angle between the resulting and its possible match, if the angle is too much, great chance this is a false positve.

### Triangulating Panoramas

triangulating a panorama by applying convex hull triangulation algorithm on the feature points.

**checking-and-rematching process** to solve such overlaps in the triangulating process.

**ping-pong technique** to deal with the remain unchanged unmatched regions.

### Generating A Novel View

Interpolating the panoramas by simply projecting the scene points
causes temporal shaking in the generated video.

This is mainly caused by estimation errors in the reconstruction of 3D scene
points.

Solution: transform the gray curve (simply projecting) to make its starting and end point coincide with the desired ones.


### Implements

It seems that the program is really no trival.


## Conclusion

At that time, the panoramas is not so widely used and since the commerial usage is mainly Google Street View (nowdays, many player have entered this area), and they are not so into the smoothy nagivation since the sample distance can be a little too large. While nowdays, more and more applications show up and more players come into this field, this work shows more value.