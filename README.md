# **AutoML with Kubeflow, MLflow, and Streamlit**  

## **📌 Project Overview**  
This project demonstrates an **end-to-end machine learning pipeline** using **Kubeflow Pipelines** and **MLflow** for **automated model training, hyperparameter tuning, and experiment tracking**. The best-performing model is deployed via **FastAPI** and visualized using a **Streamlit dashboard**.  

👉 **Automated ML pipeline** using **Kubeflow Pipelines**  
👉 **Hyperparameter tuning** using **RandomizedSearchCV**  
👉 **Experiment tracking & model logging** using **MLflow**  
👉 **Model deployment** using **FastAPI**  
👉 **Interactive dashboard** using **Streamlit**  
👉 **GitHub Actions** for automation  

---

## **📁 Project Structure**  

```
📂 MLopsShowcase
 ├── 📂 components/           # Kubeflow pipeline components
 │   ├── download_data/       # Data download component
 │   ├── train/             # Model training component
 │   ├── evaluate/          # Model evaluation component
 │   └── deploy.py          # Model serving API
 ├── 📂 pipeline/            # Kubeflow pipeline definition
 ├── 📂 frontend/            # Streamlit dashboard
 ├── 📂 docker/             # Docker base configuration file
 ├── 📂 .github/            # GitHub Actions workflows
 ├── requirements.base.txt   # Base Python dependencies
 ├── .env                   # Environment variables
 ├── example.env           # Example environment variables
 └── README.md             # Project documentation
```  

---

The goal of this project is not to make a very interesting data science pipeline, but to approximate a real-life dev&prod pipeline with proper CI/CD, with kubeflow running locally. The project is still in progress. So there is still gaps etc.

Currently on the to-do list:
- setup proper dev environment.
- add automated deployment.
- integrate mlflow back into the automated pipeline.
- auto deploy new model if it outperforms. 
- automate backend and frontend deployment to HF spaces and render.
