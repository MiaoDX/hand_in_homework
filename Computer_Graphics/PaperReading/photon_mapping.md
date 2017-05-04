# Global Illumination using Photon Maps 

This paper is one chapter of the book *Rendering Techniques ’96 (Pro-ceedings of the Seventh Eurographics Workshop on Rendering)*, pages 21–30, 1996, with some extension.

This paper presents a two pass global illumination method based on the concept of photon maps. The two passes are Constructing the Photon Maps and Rendering respectively. 

## To be more detailed, it use two photon maps:

### *a caustics photon map*:  
* store photons corresponding to caustics
* created by emitting photons towards the specular objects in the scene and storing these as they hit diffuse surfaces
* normal and shadow photon
* high density of photons

### *a global photon map*: 
* a rough approximation of the light/flux within the scene 
* created by emitting photons towards all objects (environment lighting?)

These two separate photon maps has improved both the speed, reduced the memory requirements and improved the accuracy of the method.

In rendered step, it use four separate parts:

$$Rendering Light = Direct Illumination + Specular Reflection + Caustics + Soft Indirect Illumination$$

And each part can be calculated using the two photon map, detailed info can be found in section 5.


## Personal Opinion 

Since I have not pay much attention to light reasoning before, the methods shown in the article is inspiring especially in the part of divide lighting into four parts.

The methods was proposed before 1996 and there must be more theory and implement show up latter.

