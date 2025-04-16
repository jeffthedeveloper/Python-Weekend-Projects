# File: game_analytics_pipeline.py
"""
Modern Game Analytics Pipeline with:
- Automated dataset download
- Advanced clustering (HDBSCAN, GMM)
- Dimensionality reduction (UMAP)
- Validation metrics
- Visualizations (heatmaps, KDE, boxplots)
- Temporal analysis
"""

import os
import opendatasets as od
import sys
import pandas as pd
import numpy as np
from datetime import datetime

def check_dependencies():
    """Verify all required packages are installed"""
    required = [
        'opendatasets', 'pandas', 'numpy', 
        'sklearn', 'umap', 'seaborn', 'matplotlib'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("Error: Missing required packages. Please install with:")
        print(f"pip install {' '.join(missing)}")
        sys.exit(1)

def main():
    check_dependencies()
    
    # Now safely import everything
    import opendatasets as od
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    
    print("All dependencies verified. Starting pipeline...")
    
    # Rest of your original script here...
    # [Keep all the existing functions and logic]

if __name__ == "__main__":
    main()

# ========================
# 1. DATA DOWNLOAD MODULE
# ========================
def download_datasets():
    """Download and extract required datasets from Kaggle"""
    datasets = {
        'mobile_games': 'https://www.kaggle.com/datasets/yufengsui/mobile-games-ab-testing',
        'lol_chats': 'https://www.kaggle.com/datasets/simshengqiang/leagueoflegendschats'
    }
    
    for name, url in datasets.items():
        od.download(url, data_dir=f'./data/{name}')
        print(f"Downloaded {name} dataset")

# ======================
# 2. DATA PROCESSING
# ======================
def process_data():
    """Process raw data into analysis-ready formats"""
    # Process mobile games data
    mobile_df = pd.read_csv('./data/mobile_games/cookie_cats.csv')
    
    # Feature engineering
    mobile_df['ad_clicks'] = mobile_df['ad_clicked'].astype(int)
    mobile_df['date'] = pd.to_datetime(mobile_df['timestamp']).dt.date
    
    # Process chat data
    chat_df = pd.read_csv('./data/lol_chats/chat.csv')
    chat_df['timestamp'] = pd.to_datetime(chat_df['timestamp'])
    
    # Save processed files
    mobile_df.to_csv('./processed/mobile_processed.csv', index=False)
    chat_df.to_csv('./processed/chat_processed.csv', index=False)
    
    return mobile_df, chat_df

# =========================
# 3. ADVANCED CLUSTERING
# =========================
def perform_clustering(df):
    """Run modern clustering algorithms with validation"""
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import HDBSCAN
    from sklearn.mixture import GaussianMixture
    from sklearn.metrics import silhouette_score
    
    # Prepare features
    features = df[['ad_clicks', 'spend', 'sessions']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # HDBSCAN clustering
    hdb = HDBSCAN(min_cluster_size=50)
    df['hdbscan_cluster'] = hdb.fit_predict(scaled_features)
    
    # GMM clustering
    gmm = GaussianMixture(n_components=3)
    df['gmm_cluster'] = gmm.fit_predict(scaled_features)
    
    # Validation
    print(f"Silhouette Score: {silhouette_score(scaled_features, df['gmm_cluster']):.2f}")
    
    return df

# ===========================
# 4. DIMENSIONALITY REDUCTION
# ===========================
def reduce_dimensions(df):
    """Apply UMAP/t-SNE for visualization"""
    import umap
    import matplotlib.pyplot as plt
    
    reducer = umap.UMAP(n_components=2)
    embedding = reducer.fit_transform(df[['ad_clicks', 'spend', 'sessions']])
    
    plt.scatter(embedding[:, 0], embedding[:, 1], c=df['gmm_cluster'])
    plt.savefig('./visualizations/cluster_umap.png')
    plt.close()

# ========================
# 5. VISUALIZATION MODULE
# ========================
def create_visualizations(df):
    """Generate all required visualizations"""
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True)
    plt.savefig('./visualizations/correlation_heatmap.png')
    plt.close()
    
    # KDE Plot
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x='spend', hue='gmm_cluster')
    plt.savefig('./visualizations/spend_distribution.png')
    plt.close()
    
    # Temporal Analysis
    plt.figure(figsize=(12, 6))
    df.groupby('date')['spend'].mean().plot()
    plt.savefig('./visualizations/temporal_trends.png')
    plt.close()

# ========================
# 6. MAIN EXECUTION FLOW
# ========================
if __name__ == "__main__":
    # Create directory structure
    os.makedirs('./data', exist_ok=True)
    os.makedirs('./processed', exist_ok=True)
    os.makedirs('./visualizations', exist_ok=True)
    
    # Run pipeline
    download_datasets()
    mobile_df, chat_df = process_data()
    
    # Cluster analysis
    clustered_df = perform_clustering(mobile_df)
    clustered_df.to_csv('./processed/clustered_data.csv', index=False)
    
    # Visualization
    reduce_dimensions(clustered_df)
    create_visualizations(clustered_df)
    
    print("Pipeline executed successfully!")