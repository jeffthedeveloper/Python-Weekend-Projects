# Weekend Python Projects

This repository contains a collection of Python projects designed for weekend-focused learning and skill-building in various data-related domains. Each project is intended to be achievable within a weekend timeframe, providing practical experience with essential Python libraries and technologies.

## Projects

### 1. COVID-19 Data Analysis

* **Description:** Explores COVID-19 pandemic trends, correlations, and potential relationships with other datasets.
* **Technologies:** pandas, matplotlib, seaborn
* **Key Skills:** Data cleaning, data aggregation, data visualization, exploratory data analysis
* **Data Source:** "Covid19_Confirmed_dataset.csv" and "covid19_deaths_dataset.csv" 
* **Files:**
    * `covid19_analysis.py` 
    * `./Dataset/Covid19_Confirmed_dataset.csv`
    * `./Dataset/covid19_deaths_dataset.csv`
* **How to Run:**
    1. Ensure you have Python 3.x installed.
    2. Install the required libraries: `pip install pandas matplotlib seaborn`
    3. Run the script: `python covid19_analysis.py`

### 2. Tweet Emotion Recognition with TensorFlow

* **Description:** Implements machine learning models for sentiment analysis of Twitter data.
* **Technologies:** TensorFlow, Keras, Numpy, Matplotlib, scikit-learn, Jupyter Notebook
* **Key Skills:** Natural language processing (NLP), model building, training, and evaluation, sentiment analysis
* **Data Source:** [Kaggle Emotions dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)
* **Files:**
    * `confusion_matrix.png` - Image of the confusion matrix from the model.
    * `dataset/` - Folder containing the data used for training and testing.
    * `Tweet_Emotion_Recognition.ipynb` - Jupyter notebook with model code
* **How to Run:**
    1. Ensure you have Python 3.x and TensorFlow installed.
    2. Install the required libraries: `pip install tensorflow [other libraries]`
    3. Run the Jupyter notebook: `jupyter notebook Tweet_Emotion_Recognition.ipynb`

### 3. ETL Pipelines with Python: Gather Spotify Data

* **Description:** Builds and orchestrates ETL pipelines that interact with the Spotify API.
* **Technologies:** Python, Docker, Apache Airflow, Spotipy, Pandas, PostgreSQL
* **Key Skills:** Data pipeline development, API integration, automated workflows
* **Data Source:** [Spotify Developer API](https://developer.spotify.com/documentation/web-api)
* **Files:**
    * `docker-compose.yaml` - Docker configuration
    * `airflow/` - Contains DAG definitions
    * `scripts/` - ETL utility scripts
* **How to Run:**
    1. Install Docker and Python 3.x
    2. Run: `docker-compose up --build`
    3. Access Airflow at `http://localhost:8080`

### 4. Basic Python REST API

* **Description:** A lightweight REST API implementation using Python and FastAPI.
* **Technologies:** FastAPI, Uvicorn, Pydantic
* **Key Skills:** API design, request handling, data validation
* **Files:**
    * `main.py` - Core API implementation
    * `models.py` - Data models and schemas
    * `requirements.txt` - Dependency list
* **How to Run:**
    1. Install requirements: `pip install -r requirements.txt`
    2. Start the server: `uvicorn main:app --reload`
    3. Access docs at `http://localhost:8000/docs`

### 5. Big Data Processing - Best Practices

* **Description:** Modern data processing techniques using Databricks and Spark.
* **Technologies:** PySpark, Databricks, Koalas, SparkSQL
* **Key Skills:** Cluster management, distributed computing, streaming data
* **Files:**
    * `databricks_notebooks/` - Collection of .ipynb notebooks
    * `sample_data/` - Example datasets
* **How to Run:**
    1. Create a [Databricks Community Account](https://community.cloud.databricks.com/)
    2. Import notebooks to your workspace
    3. Attach to a cluster and execute cells

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request with clear documentation

## License

**MIT License**

Copyright (c) 2025 Jefferson Mendes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

