# Hidden Points Removal #
## Description ##
This work presents two HPR methods: 1st - from open3d, 2nd - based by mesh generation. There is marked dataset 
([link](https://visibility.labri.fr/)) consisting of 3 point clouds, where is every point labeled with a 
visibility characteristic. Every cloud was processed by HPR methods and the results were compared. In folder 
points_removal_scripts you can find both of the methods, experiments.py is used to perform these methods and count an
accuracy according to marked dataset. Dockerfile is provided to build docker-image as well.
## Installation ##
1. Run this in your terminal:
```
    git clone git@github.com:prime-slam/hidden-points-removal.git
```
2. Enter the folder:
```
    cd hidden-points-removal
```
3. Install [Docker](https://www.docker.com) if you don't have it yet 
4. Build docker-image by running the following command:
```
    docker build -t makeitdense .
```
6. Download [dataset](https://visibility.labri.fr/)
7. Run image by:
```
    docker run --rm -it -v {path_to_visibility_dataset_folder}/:/workspace/dataset makeitdense
```
8. To test methods on point cloud run:
```
    python3 experiments.py {path_to_point_cloud}
```
## Compare results ##
|   Method   | accuracy on 1st cloud | accuracy on 2nd cloud | accuracy on 3rd cloud |
|:----------:|:---------------------:|:---------------------:|:---------------------:|
|   open3d   |         0.541         |         0.54          |         0.427         |
| mesh-based |         0.798         |         0.763         |         0.711         |
![Point cloud before processed by open3d method](https://www.dropbox.com/s/o0vf06vyzqjqyr2/HPR_open3d_before.png?dl=0)
![Point cloud after processed by open3d method](https://www.dropbox.com/s/o0vf06vyzqjqyr2/HPR_open3d_after.png?dl=0)