# Spatio-Temporal Action Detection with Occlusion
> Pytorch implementation of CMU11785's course project [Spatio-Temporal Action Detection with Occlusion](https://www.youtube.com/watch?v=6nt8--NZlHI).
<br/>

## Overview
![architecture](/readme/architecture.png?raw=true)

STADO can be decomposed into one module and three branches:
1. [**Mask-Guided Attention Module**](readme/mga.png)

    Produces a spatial attention mask to modulate features generated by the backbone to focus on non-occlusion patterns.
2. [**Multi-Task Branches**](readme/branches.png)

    (2.1) **Center Branch** for center localization and action recognition.
    
    (2.2) **Movement Branch** for movement estimation at adjacent frames to form moving point trajectories.
    
    (2.3) **Box Branch** for spatial extent detection by directly regressing bounding box size at the estimated center point of each frame.
<br/>

## Instructions
1. [Installation](readme/Installation.md)
2. [Dataset](readme/Dataset.md)
3. [Train](readme/Train.md)
4. [Evaluation](readme/Evaluation.md)
<br/>

## References
- Baseline model codes from [MOC](https://github.com/MCG-NJU/MOC-Detector) and its [LICENSE](https://github.com/MCG-NJU/MOC-Detector/blob/master/LICENSE).
- Data augmentation codes and evaluation codes from [ACT](https://github.com/vkalogeiton/caffe/tree/act-detector) and its [LICENSE](https://github.com/vkalogeiton/caffe/blob/act-detector/LICENSE).
- DLA-34 backbone codes from [CenterNet](https://github.com/xingyizhou/CenterNet) and its [ LICENSE](https://github.com/xingyizhou/CenterNet/blob/master/LICENSE).
- See more in [NOTICE](readme/NOTICE).

