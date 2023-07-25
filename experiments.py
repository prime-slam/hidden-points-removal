import sys
from points_removal_scripts.open3d_based_script import HPR_open3d
from points_removal_scripts.mesh_based_script import HPR_mesh_based, test_scan2
import numpy as np

def get_visible_points_from_file(path):
    index = 0
    marked_visibility = []
    with open(path, 'r') as data:
        while True:
            point = data.readline()
            if not point:
                cloud_size = index
                break

            marked_visibility.append(float(point.split()[5]))
            index += 1
    return cloud_size, marked_visibility

def count_accuracy(cloud_size, estimated_visibility, marked_visibility):
    coincide = 0
    for i in range(cloud_size):
        if marked_visibility[i] == estimated_visibility[i]:
            coincide += 1

    if cloud_size != 0:
        return coincide / cloud_size
    else:
        return "empty cloud"

# Calculate open3d method
cloud_path = sys.argv[1]

pcd, pt_map = HPR_open3d.hidden_points_removal(cloud_path)
cloud_size, marked_visibility = get_visible_points_from_file(cloud_path)

estimated_visibility = [0] * cloud_size
visible_indexes = np.asarray(pt_map)
for i in range(cloud_size):
    if i in visible_indexes:
        estimated_visibility[i] = 1

print("an accuracy score is: ", count_accuracy(cloud_size, estimated_visibility, marked_visibility))

# Calculate our method

# pcd, estimated_visibility =
HPR_mesh_based.hidden_points_removal(cloud_path)
# cloud_size, marked_visibility = get_visible_points_from_file(cloud_path)
# print("an accuracy score is: ", count_accuracy(cloud_size, estimated_visibility, marked_visibility))