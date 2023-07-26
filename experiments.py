import argparse
import numpy as np

from points_removal_scripts.mesh_based_script import HPR_mesh_based
from points_removal_scripts.open3d_based_script import HPR_open3d


def get_visible_points_from_file(path):
    index = 0
    marked_visibility = []
    with open(path, "r") as data:
        while True:
            point = data.readline()
            if not point:
                break

            marked_visibility.append(float(point.split()[5]))
            index += 1
    return marked_visibility


def count_accuracy(cloud_size, estimated_visibility, marked_visibility):
    coincide = 0
    for i in range(cloud_size):
        if marked_visibility[i] == estimated_visibility[i]:
            coincide += 1

    if cloud_size != 0:
        return coincide / cloud_size
    else:
        raise ArithmeticError("invalid point cloud data")


# Calculate open3d method
parser = argparse.ArgumentParser(
    description="""
    This script takes path to the cloud data   
    """
)
parser.add_argument("cloud_path", help="path to cloud data")
args = parser.parse_args()
cloud_path = args.cloud_path

pcd, pt_map = HPR_open3d.hidden_points_removal(cloud_path)
marked_visibility = get_visible_points_from_file(cloud_path)
cloud_size = len(marked_visibility)

estimated_visibility = np.zeros(cloud_size)
visible_indexes = np.asarray(pt_map)
estimated_visibility[visible_indexes] = 1

print(
    "an accuracy score is: ",
    count_accuracy(cloud_size, estimated_visibility, marked_visibility),
)

# Calculate our method

pcd, estimated_visibility = HPR_mesh_based.hidden_points_removal(cloud_path)
cloud_size, marked_visibility = get_visible_points_from_file(cloud_path)
print(
    "an accuracy score is: ",
    count_accuracy(cloud_size, estimated_visibility, marked_visibility),
)
