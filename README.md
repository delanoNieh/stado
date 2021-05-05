# Spatio-Temporal Action Detection with Occlusion

> Pytorch implementation of [Spatio-Temporal Action Detection with Occlusion]().
> 
> Take [Actions as Moving Points](https://arxiv.org/abs/2001.04608) (MOC) as the baseline model.

<br/>

## Overview  

![architecture](/readme/architecture.png?raw=true)

STADO is decomposed into one module and three crucial head branches:
- (1) **Mask-Guided Attention Module** [mga.png](readme/mga.png)

 Produced a spatial attention mask to modulate features generated by the backbone to focus on non-occlusion patterns.

- (2) **Multi-Task Branches** [branches.png](readme/branches.png)

 Realized action detection and recognition.

 (a) ***Center Branch*** for center localization and action recognition.

 (b) ***Movement Branch*** for movement estimation at adjacent frames to form moving point trajectories.

 (c) ***Box Branch*** for spatial extent detection by directly regressing bounding box size at the estimated center point of each frame.

<br/>

## Usage

### 1. Installation
Please refer to [Installation.md](readme/Installation.md) for installation instructions.

### 2. Dataset
Please refer to [Dataset.md](readme/Dataset.md) for dataset setup instructions.

### 3. Evaluation
You can follow the instructions in [Evaluation.md](readme/Evaluation.md) to evaluate our model and reproduce the results in original paper.

### 4. Train
You can follow the instructions in [Train.md](readme/Train.md) to train our models.

<br/>

## References

- Baseline model codes from [MOC](https://github.com/MCG-NJU/MOC-Detector).
- Data augmentation codes from [ACT](https://github.com/vkalogeiton/caffe/tree/act-detector).
- Evaluation codes from [ACT](https://github.com/vkalogeiton/caffe/tree/act-detector).
- DLA-34 backbone codes from [CenterNet](https://github.com/xingyizhou/CenterNet).

  [MOC LICENSE](https://github.com/MCG-NJU/MOC-Detector/blob/master/LICENSE)

  [ACT LICENSE](https://github.com/vkalogeiton/caffe/blob/act-detector/LICENSE)
  
  [CenterNet LICENSE](https://github.com/xingyizhou/CenterNet/blob/master/LICENSE)
  
  See more in [NOTICE](readme/NOTICE)

