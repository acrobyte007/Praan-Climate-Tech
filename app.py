import open3d as o3d
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Function to load and preprocess point cloud data (down-sampling and noise removal)
def load_and_preprocess_pcd(file_path, voxel_size=0.05, noise_removal=True):
    # Load the point cloud
    pcd = o3d.io.read_point_cloud(file_path)
    
    # Apply voxel grid down-sampling
    pcd = pcd.voxel_down_sample(voxel_size)
    
    # Noise removal using statistical outlier removal (only for real-world data)
    if noise_removal:
        pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
    
    return pcd

# Function to perform DBSCAN clustering on point cloud data
def perform_dbscan_clustering(pcd, eps=0.05, min_samples=10):
    # Convert point cloud to numpy array
    points = np.asarray(pcd.points)
    
    # Perform DBSCAN clustering
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(points)
    
    return labels

# Function to visualize point cloud clusters with different colors
def visualize_clusters(pcd, labels):
    unique_labels = np.unique(labels)
    colors = plt.cm.jet(np.linspace(0, 1, len(unique_labels)))[:, :3]  # Color map
    
    # Assign colors based on cluster labels
    colored_points = np.array([colors[label] if label != -1 else [0, 0, 0] for label in labels])
    pcd.colors = o3d.utility.Vector3dVector(colored_points)
    
    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd])

# Function to save each cluster as a separate PCD file
def save_clusters_as_pcd(pcd, labels, file_prefix):
    unique_labels = np.unique(labels)
    for label in unique_labels:
        # Select points belonging to the current cluster
        cluster_points = np.asarray(pcd.points)[labels == label]
        
        # Create new point cloud for the cluster
        cluster_pcd = o3d.geometry.PointCloud()
        cluster_pcd.points = o3d.utility.Vector3dVector(cluster_points)
        
        # Save the cluster to a new PCD file
        o3d.io.write_point_cloud(f"{file_prefix}_cluster_{label}.pcd", cluster_pcd)
        print(f"Cluster {label} saved as {file_prefix}_cluster_{label}.pcd")

# Main function to process and cluster both ideal (PLY) and real-world (PCD) data
def process_point_clouds(ideal_file, real_file, voxel_size=0.05, eps_ideal=0.05, min_samples_ideal=10, eps_real=0.1, min_samples_real=20):
    # Load and preprocess ideal data (PLY)
    ideal_pcd = load_and_preprocess_pcd(ideal_file, voxel_size)
    
    # Load and preprocess real-world data (PCD)
    real_pcd = load_and_preprocess_pcd(real_file, voxel_size, noise_removal=True)
    
    # Perform DBSCAN clustering for ideal data
    print("Clustering ideal data...")
    labels_ideal = perform_dbscan_clustering(ideal_pcd, eps=eps_ideal, min_samples=min_samples_ideal)
    visualize_clusters(ideal_pcd, labels_ideal)
    
    # Perform DBSCAN clustering for real-world data
    print("Clustering real-world data...")
    labels_real = perform_dbscan_clustering(real_pcd, eps=eps_real, min_samples=min_samples_real)
    visualize_clusters(real_pcd, labels_real)
    
    # Save the clusters as separate PCD files
    save_clusters_as_pcd(ideal_pcd, labels_ideal, "ideal_data")
    save_clusters_as_pcd(real_pcd, labels_real, "real_world_data")


ideal_file = "Ideal.ply"   
real_file = "Real World PCD.pcd"  

# Process the point clouds
process_point_clouds(ideal_file, real_file)
