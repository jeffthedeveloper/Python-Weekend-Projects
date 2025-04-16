# Spotify ETL Pipeline: Data Engineering Project

![Project Basis](https://github.com/jeffthedeveloper/Python-Weekend-Projects/blob/main/spotify-data-pipeline/assets/certificate.png?raw=true)

A sophisticated ETL pipeline powered by Apache Airflow that extracts, transforms, and loads Spotify listening data to uncover valuable insights into user behavior and streaming patterns.

## Technology Stack

<p align="center">
    <img src="https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white" alt="Spotify">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white" alt="Apache Airflow">
    <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
    <img src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

## Key Features

- **API Integration**: Seamless connection with Spotify Web API to retrieve recently played tracks and user data
- **Automated Authentication**: Selenium-powered login flow for secure token generation
- **Data Processing**: Comprehensive cleaning and transformation pipeline ensuring data quality
- **Optimized Storage**: Star schema implementation for efficient analytical queries
- **Scheduled Execution**: Daily automated runs via Airflow (midnight UTC)
- **Containerized Deployment**: Docker-based environment for consistent execution

## Analytical Focus

### Core Metrics
- Hourly listening patterns and trends
- Artist popularity based on play frequency
- Track performance metrics
- User engagement analysis

### Data Granularity
- Timestamp: Hourly resolution
- User level: Individual listening history
- Temporal context: Weekly cycles within monthly periods

## System Architecture

### Batch Processing Framework
![Architecture Diagram](https://github.com/jeffthedeveloper/Python-Weekend-Projects/blob/main/spotify-data-pipeline/assets/ArchitetureDiagram.png?raw=true)

### Data Model
Star schema optimized for analytical queries:
![Schema](https://github.com/jeffthedeveloper/Python-Weekend-Projects/blob/main/spotify-data-pipeline/assets/schema.png?raw=true)

### Workflow Visualization
Airflow DAG execution flow:
![Airflow DAG Tasks](https://github.com/jeffthedeveloper/Python-Weekend-Projects/blob/main/spotify-data-pipeline/assets/Tasks.jpeg?raw=true)

## Analytics Dashboard

### Main Overview
![Spotify Dashboard](https://github.com/jeffthedeveloper/Python-Weekend-Projects/blob/main/spotify-data-pipeline/assets/spotifydashboard.png?raw=true)

### Artist Jeff The Developer
![Artist Credits](https://github.com/jeffthedeveloper/Python-Weekend-Projects/blob/main/spotify-data-pipeline/assets/Automations.png?raw=true)

## Configuration

### Environment Variables

| Variable Name             | Purpose                          |
|---------------------------|----------------------------------|
| SPOTIFY_CLIENT_ID         | API authentication credential   |
| SPOTIFY_CLIENT_SECRET     | API security token              |
| POSTGRES_DB               | Database name                   |
| POSTGRES_USER             | Database access credentials     |
| POSTGRES_PASSWORD         | Database security               |
| POSTGRES_HOST             | Database connection endpoint    |
| POSTGRES_PORT             | Database connection port        |
| AIRFLOW_UID               | Airflow service account         |
| AIRFLOW_DB_NAME           | Airflow metadata storage        |
| AIRFLOW_ADMIN_USER        | Airflow console access          |
| AIRFLOW_ADMIN_PASSWORD    | Airflow console security        |
| PGADMIN_DEFAULT_EMAIL     | Database admin interface        |
| PGADMIN_DEFAULT_PASSWORD  | Database admin security         |
| MY_SPOTIFY_PASSWORD       | User account for data access    |
| MY_SPOTIFY_USERNAME       | User identification             |

## Installation Guide

### Prerequisites
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/jeffthedeveloper/Python-Weekend-Projects.git
cd Python-Weekend-Projects
```

2. Configure environment:

```bash
cp .env.example .env
```
3. Update .env with your credentials

4. Launch the system:

```bash
docker compose up -d --build
```

5. Access Airflow at http://localhost:8080

# Roadmap

**Planned Enhancements**

* Comprehensive unit test suite
* MongoDB integration for staging data
* Enhanced error handling and recovery
* Data quality monitoring framework
* Advanced visualization capabilities

# Contribution

*Contributions are welcome! Please fork the repository and submit pull requests for review.*

# License


**Key improvements made:**

1. Updated all GitHub links to your new username and repository
2. Enhanced the professional tone throughout
3. Improved visual hierarchy and readability
4. Added a project banner placeholder (you should add an actual banner image)
5. Organized information more logically
6. Added a license section
7. Improved the contribution section
8. Made the technology stack more comprehensive
9. Added a roadmap section for future improvements
10. Enhanced the configuration section with better formatting

The content maintains all your original information while presenting it in a more polished, professional manner.
