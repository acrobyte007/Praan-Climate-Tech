**Point Cloud Clustering with DBSCAN**<br>
This project applies DBSCAN (Density-Based Spatial Clustering of Applications with Noise) to segment point cloud data into meaningful clusters. The approach is designed to handle both ideal and real-world point cloud data, with an emphasis on clustering precision and noise reduction. The script performs preprocessing, clustering, visualization, and exports clustered point cloud data into separate files for further analysis.<br>
<br>
**Approach**:<br>
1. Point Cloud Preprocessing<br>
Voxel Grid Down-Sampling: A voxel grid filter is applied to down-sample the point cloud. This reduces the point cloud density by averaging the points within each voxel (3D grid cell). This step is crucial for reducing computation time and ensuring efficient clustering.<br>
Noise Removal (Real-World Data): For real-world data, a statistical outlier removal filter is applied. This filter identifies points that are far from the local neighborhood and removes them, which helps reduce noise caused by imperfections in the point cloud data. This step is skipped for ideal data, as it is usually clean.<br>
<br>
2. Clustering with DBSCAN<br>
DBSCAN: DBSCAN is a density-based clustering algorithm. It groups points that are closely packed together (i.e., they have many neighbors within a certain radius). Points that are far from other points are labeled as noise and not assigned to any cluster. We chose DBSCAN because:<br>
- It does not require the number of clusters to be predefined.<br>
- It is robust to noise, making it suitable for real-world data that may contain outliers.<br>
<br>
Parameters: The eps (epsilon) parameter defines the maximum distance between two points to be considered as part of the same cluster, and the min_samples parameter defines the minimum number of points required to form a dense region (i.e., a cluster). These parameters were fine-tuned separately for ideal and real-world data:<br>
- Ideal Data (PLY): eps=0.05 and min_samples=10 work well because the ideal data is clean and uniformly distributed.<br>
- Real-World Data (PCD): For noisy data, eps=0.1 and min_samples=20 provide better clustering results by accommodating the noise and imperfections.<br>
<br>
3. Visualization<br>
The clusters are visualized with each cluster assigned a unique color. Points that are classified as noise (label -1 by DBSCAN) are colored black to distinguish them from the rest of the points.<br>
We used Open3D for visualization, which provides an interactive 3D viewer to inspect the clustered point clouds.<br>
<br>
4. Exporting Clusters<br>
After clustering, each cluster is exported as a separate PCD file. This allows for easy inspection and further processing of each individual cluster.<br>
<br>
**Justifications for the Approach**<br>
- DBSCAN was chosen because it is well-suited for point cloud data, which often contains varying densities and noise. Unlike k-means, DBSCAN does not require specifying the number of clusters, which is advantageous for point clouds where the number of clusters is unknown.<br>
- Voxel Grid Down-Sampling helps reduce the number of points in large point clouds, improving the speed of clustering and making the process more efficient.<br>
- Noise Removal for Real-World Data helps to improve the quality of the clustering by filtering out random outliers, which are typical in data captured from sensors in real-world environments.<br>
<br>
**Instructions**:<br>
1. Clone the Repository<br>
Clone this repository to your local machine:<br>
<br>
git clone https://github.com/acrobyte007/Praan-Climate-Tech<br>
<br>
2. Install Dependencies<br>
Install the necessary Python libraries:<br>
<br>
pip install open3d numpy scikit-learn matplotlib<br>
<br>
3. Prepare Point Cloud Files<br>
Ensure you have the following point cloud files:<br>
- Ideal data: A PLY file representing the simulated or perfect point cloud data.<br>
- Real-world data: A PCD file representing the captured point cloud data, which may contain noise.<br>
Place these files in the same directory as the script.<br>
<br>
4. Update File Paths<br>
In the Python script (point_cloud_clustering.py), update the paths for the ideal and real-world point cloud files:<br>
<br>
ideal_file = "ideal_data.ply"<br>
real_file = "real_world_data.pcd"<br>
<br>
5. Run the Code<br>
Run the Python script<br>
<br>
6. Output<br>
The script will process the point cloud files, perform clustering, and visualize the results in an interactive 3D viewer.<br>
The clustered point clouds will be saved as separate PCD files, named as ideal_data_cluster_X.pcd and real_world_data_cluster_X.pcd, where X is the cluster label.<br>
<br>
7. Visualize Results<br>
After running the script, Open3D's interactive viewer will open, allowing you to inspect the clusters. You can also open the saved PCD files in any point cloud viewer.<br>
<br>
**Relevant Details about the Implementation**:<br>
- Point Cloud File Format: The script supports both PLY (ideal) and PCD (real-world) point cloud formats.<br>
- DBSCAN Parameters:<br>
  - eps=0.05, min_samples=10 for ideal data (PLY).<br>
  - eps=0.1, min_samples=20 for real-world data (PCD).<br>
- Point Cloud Processing:<br>
  - Down-Sampling: Reduces the number of points by applying voxel grid filtering.<br>
  - Noise Removal: For real-world data, outlier points are removed using statistical outlier removal to improve the clustering quality.<br>
- Fine-Tuning:<br>
  - The eps and min_samples parameters are crucial for the success of DBSCAN clustering:<br>
    - For ideal data, fine-tuning the parameters to smaller values (like eps=0.05) is effective, as the data is clean and well-behaved.<br>
    - For real-world data, we need larger eps (0.1) and more min_samples (20) to account for noise and varying point densities. There may need to experiment with different values to find the best clustering results for specific dataset.<br>
