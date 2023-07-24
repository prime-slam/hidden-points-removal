import sys
import HPR_open3d
import HPR_ours
import numpy as np
import open3d as o3d

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

command_line_args = sys.argv[1:]
if command_line_args[0] == "1":
    cloud_paths = open(command_line_args[1], 'r')
    try:
        cloud = cloud_paths.readline().split('\n')[0]
        while cloud:
            pcd, pt_map = HPR_open3d.hidden_points_removal(cloud)
            cloud_size, marked_visibility = get_visible_points_from_file(cloud)

            estimated_visibility = [0] * cloud_size
            visible_indexes = np.asarray(pt_map)
            for i in range(cloud_size):
                if i in visible_indexes:
                    estimated_visibility[i] = 1

            print("an accuracy score is: ", count_accuracy(cloud_size, estimated_visibility, marked_visibility))
            cloud = cloud_paths.readline().split('\n')[0]
    finally:
        cloud_paths.close()
if command_line_args[0] == "2":
    cloud_paths = open(command_line_args[1], 'r')
    mesh_paths = open(command_line_args[2], 'r')
    try:
        cloud = cloud_paths.readline().split('\n')[0]
        mesh = mesh_paths.readline().split('\n')[0]
        while cloud and mesh:
            pcd, estimated_visibility = HPR_ours.hidden_points_removal(mesh, cloud)
            cloud_size, marked_visibility = get_visible_points_from_file(cloud)
            print("an accuracy score is: ", count_accuracy(cloud_size, estimated_visibility, marked_visibility))
            cloud = cloud_paths.readline().split('\n')[0]
            mesh = mesh_paths.readline().split('\n')[0]
    finally:
        cloud_paths.close()
        mesh_paths.close()
