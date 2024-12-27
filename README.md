**Point Cloud Clustering with DBSCAN**
This project applies DBSCAN (Density-Based Spatial Clustering of Applications with Noise) to segment point cloud data into meaningful clusters. The approach is designed to handle both ideal and real-world point cloud data, with an emphasis on clustering precision and noise reduction. The script performs preprocessing, clustering, visualization, and exports clustered point cloud data into separate files for further analysis.

**Approach**:
1. Point Cloud Preprocessing
Voxel Grid Down-Sampling: A voxel grid filter is applied to down-sample the point cloud. This reduces the point cloud density by averaging the points within each voxel (3D grid cell). This step is crucial for reducing computation time and ensuring efficient clustering.
Noise Removal (Real-World Data): For real-world data, a statistical outlier removal filter is applied. This filter identifies points that are far from the local neighborhood and removes them, which helps reduce noise caused by imperfections in the point cloud data. This step is skipped for ideal data, as it is usually clean.
2. Clustering with DBSCAN
DBSCAN: DBSCAN is a density-based clustering algorithm. It groups points that are closely packed together (i.e., they have many neighbors within a certain radius). Points that are far from other points are labeled as noise and not assigned to any cluster. We chose DBSCAN because:
It does not require the number of clusters to be predefined.
It is robust to noise, making it suitable for real-world data that may contain outliers.
Parameters: The eps (epsilon) parameter defines the maximum distance between two points to be considered as part of the same cluster, and the min_samples parameter defines the minimum number of points required to form a dense region (i.e., a cluster). These parameters were fine-tuned separately for ideal and real-world data:
Ideal Data (PLY): eps=0.05 and min_samples=10 work well because the ideal data is clean and uniformly distributed.
Real-World Data (PCD): For noisy data, eps=0.1 and min_samples=20 provide better clustering results by accommodating the noise and imperfections.
<br>3. Visualization<br>
The clusters are visualized with each cluster assigned a unique color. Points that are classified as noise (label -1 by DBSCAN) are colored black to distinguish them from the rest of the points.
We used Open3D for visualization, which provides an interactive 3D viewer to inspect the clustered point clouds.
4. Exporting Clusters
After clustering, each cluster is exported as a separate PCD file. This allows for easy inspection and further processing of each individual cluster.
Justifications for the Approach
DBSCAN was chosen because it is well-suited for point cloud data, which often contains varying densities and noise. Unlike k-means, DBSCAN does not require specifying the number of clusters, which is advantageous for point clouds where the number of clusters is unknown.
Voxel Grid Down-Sampling helps reduce the number of points in large point clouds, improving the speed of clustering and making the process more efficient.
Noise Removal for Real-World Data helps to improve the quality of the clustering by filtering out random outliers, which are typical in data captured from sensors in real-world environments.

**Instructions**:
<br>
1. Clone the Repository
Clone this repository to your local machine:


git clone https://github.com/acrobyte007/Praan-Climate-Tech

2. Install Dependencies
Install the necessary Python libraries:

pip install open3d numpy scikit-learn matplotlib
3. Prepare Point Cloud Files
Ensure you have the following point cloud files:
Ideal data: A PLY file representing the simulated or perfect point cloud data.
Real-world data: A PCD file representing the captured point cloud data, which may contain noise.
Place these files in the same directory as the script.
4. Update File Paths
In the Python script (point_cloud_clustering.py), update the paths for the ideal and real-world point cloud files:

ideal_file = "ideal_data.ply"   
real_file = "real_world_data.pcd"
<br>
5. Run the Code
Run the Python script
<br>
6. Output<br>
The script will process the point cloud files, perform clustering, and visualize the results in an interactive 3D viewer.
The clustered point clouds will be saved as separate PCD files, named as ideal_data_cluster_X.pcd and real_world_data_cluster_X.pcd, where X is the cluster label.
<br>7. Visualize Results<br>
After running the script, Open3D's interactive viewer will open, allowing you to inspect the clusters. You can also open the saved PCD files in any point cloud viewer.
<br>
**Relevant Details about the Implementation**:<br>
Point Cloud File Format: The script supports both PLY (ideal) and PCD (real-world) point cloud formats.
DBSCAN Parameters:
eps=0.05, min_samples=10 for ideal data (PLY).
eps=0.1, min_samples=20 for real-world data (PCD).
Point Cloud Processing:
Down-Sampling: Reduces the number of points by applying voxel grid filtering.
Noise Removal: For real-world data, outlier points are removed using statistical outlier removal to improve the clustering quality.
Fine-Tuning
The eps and min_samples parameters are crucial for the success of DBSCAN clustering:

For ideal data, fine-tuning the parameters to smaller values (like eps=0.05) is effective, as the data is clean and well-behaved.
For real-world data, we need larger eps (0.1) and more min_samples (20) to account for noise and varying point densities. There may need to experiment with different values to find the best clustering results for specific dataset.
