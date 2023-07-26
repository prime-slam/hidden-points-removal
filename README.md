# Hidden Points Removal #
## Description ##
This work presents two HPR methods: 1st - from open3d, 2nd - based by mesh generation. There is marked dataset 
consisting of 3 point clouds, where is every point labeled with a visibility characteristic. Both of the clouds were
processed by HPR methods and the results were compared. 
## Usage ##
To test methods on point cloud run from the root of repository:
```
    python3 experiments.py {path_to_point_cloud}
```
## Compare results ##
|   Method   | accuracy on 1st cloud  | accuracy on 2st cloud  | accuracy on 3st cloud |
|:----------:|:----------------------:|:----------------------:|:---------------------:|
|   open3d   |   0.5409711189623693   |   0.5392236819793121   |  0.4268948570861496   |
| mesh-based |   0.7980016835416025   |   0.762885474116003    |   0.711016091696132   |

![My Image](images/before_HPR_open3d.png.jpg)

![My Image](images/after_HPR_open3d.png.jpg)