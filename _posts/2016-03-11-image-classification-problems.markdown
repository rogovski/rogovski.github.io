---
layout: post
title:  "Image Classification Problems"
date:   2016-03-02 13:14:00 -0500
categories: mathematics statistics
description: "A list problems that arise in computer image classification"
---

source [cs231n.github.io](http://cs231n.github.io).

1. Viewpoint variation. A single instance of an object can be oriented in many ways with respect to the camera.
2. Scale variation. Visual classes often exhibit variation in their size (size in the real world, not only in terms of their extent in the image).
3. Deformation. Many objects of interest are not rigid bodies and can be deformed in extreme ways.
4. Occlusion. The objects of interest can be occluded. Sometimes only a small portion of an object (as little as few pixels) could be visible.
5. Illumination conditions. The effects of illumination are drastic on the pixel level.
6. Background clutter. The objects of interest may blend into their environment, making them hard to identify.
7. Intra-class variation. The classes of interest can often be relatively broad, such as chair. There are many different types of these objects, each with their own appearance.