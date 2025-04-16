# Weekend Python Projects

This repository contains a collection of Python projects designed for weekend-focused learning and skill-building in various data-related domains. Each project is intended to be achievable within a weekend timeframe, providing practical experience with essential Python libraries and technologies.

## Projects

### 1. COVID-19 Data Analysis

* **Description:** Explores COVID-19 pandemic trends, correlations, and potential relationships with other datasets.
* **Technologies:** pandas, matplotlib, seaborn
* **Key Skills:** Data cleaning, data aggregation, data visualization, exploratory data analysis
* **Data Source:** "Covid19\_Confirmed\_dataset.csv" and "covid19\_deaths\_dataset.csv" 
* **Files:**
    * `covid19_analysis.py` 
    * `./Dataset/Covid19_Confirmed_dataset.csv`
    * `./Dataset/covid19_deaths_dataset.csv`
* **How to Run:**
    1.  Ensure you have Python 3.x installed.
    2.  Install the required libraries: `pip install pandas matplotlib seaborn`
    3.  Run the script: `python covid19_analysis.py`

### 2. Tweet Emotion Recognition with TensorFlow

* **Description:** Implements machine learning models for sentiment analysis of Twitter data.
* **Technologies:** TensorFlow, Keras, Numpy, Matplotlib, scikit-learn, Jupyter Notebook
* **Key Skills:** Natural language processing (NLP), model building, training, and evaluation, sentiment analysis
* **Data Source:** Can be founded at [Kaggle Emotions dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)

* **Files:**

   * `confusion_matrix.png` - Image of the confusion matrix from the model.
   
   * `dataset/` - Folder containing the data used for training and testing.
   
   * `LICENSE` - License file for the project (MIT).
   
   * `README.md` - This file containing project information.
   
   * `requirements.txt` - List of dependencies required for the project.

**Tweet_Emotion_Recognition.ipynb** - Jupyter notebook containing the code for building, training, and evaluating the model.

* **How to Run:**
  
    1.  Ensure you have Python 3.x and TensorFlow installed.
    2.  Install the required libraries: `pip install tensorflow \[other libraries]`
    3.  Follow the instructions in the project's folder.

### 3. Create Your First Python Program From UST

* **Description:** Introductory Python programming project (focused on UST data or a specific application).
* **Technologies:** Python basics
* **Key Skills:** Basic Python syntax, data manipulation, \[*Add specific skills*]
* **Data Source:** \[*Specify data source if applicable*]
* **Files:**


* **How to Run:**
    1.  Ensure you have Python 3.x installed.
    2.  Run the script: `python your_script.py`

### 4. ETL Pipelines with Python: Gather Spotify Data

* **Description:** This project builds and orchestrates ETL (Extract, Transform, Load) pipelines that interact with the Spotify API. The goal is to gather and structure music-related data for analytical and processing purposes.
* **Technologies:** Python, Docker, Apache Airflow, Spotipy, Pandas, JSON, PostgreSQL
* **Key Skills:** Data pipeline development, API integration, automated workflows with Airflow, data transformation and persistence using SQL
* **Data Source:** [Spotify Developer API](https://developer.spotify.com/documentation/web-api)

* **Files and Structure:**
  - `.env.example`: Template for environment variables including Spotify credentials.
  - `.gitignore`: Specifies untracked files to ignore in version control.
  - `airflow/`: Contains DAGs and Airflow-specific configuration for orchestrating ETL jobs.
  - `assets/`: Stores visual and reference assets (e.g., diagrams, documentation).
  - `config/`: Configuration settings for pipelines and environment.
  - `data/`: Directory for storing processed or intermediate data.
  - `docker-compose.yaml`: Used to spin up Docker containers for Airflow and supporting services.
  - `Dockerfile.airflow`: Custom Dockerfile to build the Airflow environment.
  - `example-raw-data.json`: Example of raw data retrieved from the Spotify API.
  - `generate_env.sh`: Script to generate `.env` file from `.env.example`.
  - `requirements.txt`: Lists Python dependencies.
  - `scripts/`: Utility scripts for ETL steps or testing.
  - `sql/`: SQL queries or schema definitions.

* **How to Run:**
  1. Ensure you have Python 3.x and Docker installed.
  2. Clone this repository and navigate to the project folder.
  3. Run `generate_env.sh` to generate your `.env` file with the correct environment variables.
  4. Add your Spotify API credentials in the `.env` file.
  5. Install the required libraries locally (optional for testing):  
     ```bash
     pip install spotipy pandas requests python-dotenv
     ```
  6. Start the Docker containers (Airflow, PostgreSQL, etc.):  
     ```bash
     docker-compose up --build
     ```
  7. Access the Airflow web interface at `http://localhost:8080` and trigger the ETL DAG.

---

## Commentary on Project Structure and Pipeline Design

This ETL project is designed to ensure modularity, scalability, and reproducibility. Leveraging **Apache Airflow**, the workflow orchestration is handled through clearly defined DAGs, enabling easy scheduling, monitoring, and dependency management.

One of the standout aspects is the use of Docker and environment variables to provide a fully containerized and configurable development setup. This enhances portability across machines and team members.

The inclusion of an example JSON file (`example-raw-data.json`) offers a quick glance at the kind of data retrieved, aiding both debugging and development of downstream processes.

Additionally, the separation of configuration, scripts, and SQL files follows best practices for managing complex data pipelines. This structure supports both experimentation and production deployment.

To enhance robustness and accuracy, future iterations of this pipeline could include:

- Validation checks on retrieved data
- Logging and error-handling mechanisms within DAGs
- Integration with a data warehouse for scalable analytics

This project provides an excellent foundation for anyone aiming to explore real-world data engineering concepts using Spotify's rich API ecosystem.


### 5. API Configuration in Python: Create a REST API

* **Description:** Develops RESTful APIs using Python frameworks.
* **Technologies:** Python, Flask or FastAPI
* **Key Skills:** API design, RESTful principles, web frameworks, request handling
* **Files:**
    * \[*List your Python files*]
* **How to Run:**
    1.  Ensure you have Python 3.x installed.
    2.  Install the required libraries: `pip install Flask` or `pip install FastAPI`
    3.  Run the API application.

### 6. Best Practices for Data Processing in Big Data

* **Description:** Implements efficient data processing techniques for large-scale datasets.
* **Technologies:** Python, \[*Add libraries like PySpark if applicable*]
* **Key Skills:** Data processing, big data concepts, performance optimization
* **Files:**
    * \[*List your Python files*]
* **How to Run:**
    1.  Ensure you have Python 3.x installed.
    2.  Install the required libraries: `pip install pyspark` (if applicable)
    3.  Follow the instructions in the project's folder.

## How to Contribute

## License

**MIT License**

Copyright (c) 2023 Jefferson Mendes

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

