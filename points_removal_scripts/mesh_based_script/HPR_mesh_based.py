import numpy as np
import open3d as o3d

from points_removal_scripts.mesh_based_script.mesh_generation import generate_mesh


def hidden_points_removal(point_cloud_path):
    pcd = o3d.io.read_point_cloud(point_cloud_path)
    mesh = generate_mesh(point_cloud_path)
    mesh = o3d.t.geometry.TriangleMesh.from_legacy(mesh)
    # Creating raycasting scene
    scene = o3d.t.geometry.RaycastingScene()
    scene.add_triangles(mesh)

    # Creating rays from (0, 0, 0) to points with normalization
    pcd_points = np.asarray(pcd.points)
    distances_to_points = np.linalg.norm(pcd_points, axis=1)
    rays = np.zeros((len(pcd_points), 6))
    rays[:, 3:] = pcd_points
    rays = rays / distances_to_points[:, None]
    rays = rays.astype(np.float32)
    cast_results = scene.cast_rays(rays)

    # Selecting points that are no more than 10 cm away from the intersection with the mesh
    hit_distances = cast_results["t_hit"].numpy()
    visibility_mask = (hit_distances + 0.1) >= distances_to_points
    estimated_visibility = visibility_mask

    pcd_points_new = pcd_points[visibility_mask]
    new_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(pcd_points_new))
    return new_pcd, estimated_visibility
