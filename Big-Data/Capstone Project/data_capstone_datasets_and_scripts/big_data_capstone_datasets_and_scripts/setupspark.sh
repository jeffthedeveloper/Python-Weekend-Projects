#!/bin/bash
# Updated environment setup for modern systems

# Install conda (replaces Anaconda)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda

# Initialize conda
source $HOME/miniconda/bin/activate
conda init bash

# Create environment with modern packages
conda create -n game_analytics python=3.10 pyspark=3.4 neo4j=5.12 -y

# Install additional tools
conda install -c conda-forge jupyterlab pandas numpy matplotlib -y

# Configure Spark
echo "export SPARK_HOME=$HOME/miniconda/envs/game_analytics/lib/python3.10/site-packages/pyspark" >> ~/.bashrc
echo "export PATH=$PATH:$SPARK_HOME/bin" >> ~/.bashrc