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
📂 automl-kubeflow-mlflow  
 ├── 📂 data/              # Dataset storage  
 ├── 📂 components/        # Kubeflow pipeline components  
 │   ├── preprocess.py     # Data preprocessing  
 │   ├── train.py          # Model training & tuning  
 │   ├── evaluate.py       # Model evaluation  
 │   ├── deploy.py         # Model serving API  
 ├── 📂 pipeline/          # Kubeflow pipeline definition  
 │   ├── pipeline.py       # Main Kubeflow pipeline script  
 ├── 📂 frontend/          # Streamlit dashboard (Hugging Face Spaces)  
 ├── 📂 mlflow/            # MLflow experiment tracking  
 ├── Dockerfile            # Containerization of pipeline components  
 ├── requirements.txt      # Python dependencies  
 ├── .github/workflows/    # GitHub Actions for automation  
 │   ├── deploy.yml        # Auto-deploy pipeline & model  
 ├── README.md             # Project documentation  
```  

---

## **🚀 How It Works**  

### **1️⃣ Setup & Infrastructure**  
- **GitHub Actions** triggers **training & deployment** automatically.  
- **MLflow** logs experiments (hosted on Google Colab or remote storage).  
- **Model & Dashboard** are deployed on **Hugging Face Spaces**.  

### **2️⃣ Build the ML Pipeline**  
1. **Preprocessing Step**  
   - Load **Iris dataset**.  
   - Split into **train/test** sets.  
   - Save processed data as an artifact.  

2. **Hyperparameter Tuning & Model Training**  
   - Train **Random Forest, XGBoost, and SVM** models.  
   - Optimize **hyperparameters** using **RandomizedSearchCV**.  
   - Log all experiments with **MLflow**.  
   - Save the **best model** for deployment.  

3. **Model Evaluation**  
   - Compute **accuracy, precision, recall, F1-score**.  
   - Log metrics in **MLflow**.  

4. **Model Deployment**  
   - Deploy the best model with **FastAPI** (running on Hugging Face Spaces).  
   - Expose an API endpoint for predictions.  

### **3️⃣ Interactive Streamlit Dashboard**  
- Hosted on **Hugging Face Spaces**.  
- Displays **experiment results, best model, and API testing**.  

### **4️⃣ Automation with GitHub Actions**  
- Automatically **triggers training** on code push.  
- Deploys **updated model & dashboard** after training.  

---

## **📌 How to Run Locally**  

### **🔹 Install Dependencies**  
```bash  
pip install -r requirements.txt  
```

### **🔹 Run Pipeline Scripts**  
```bash  
python components/preprocess.py  
python components/train.py  
python components/evaluate.py  
```

### **🔹 Serve Model Locally**  
```bash  
uvicorn components.deploy:app --reload  
```

### **🔹 Run Streamlit Dashboard**  
```bash  
cd frontend  
streamlit run app.py  
```

---

## **🛠️ Deployment Status**  
✅ **GitHub Actions enabled**  
✅ **Model deployed on Hugging Face Spaces**  
✅ **Dashboard live on Hugging Face Spaces**  

---



# commands backup:
```
cd mnt/c/Users/rvhoo/My\ Documents/projects/MLopsShowcase/components/

docker build -f Dockerfile -t robinvhoorn/mlops-showcase-download_data:latest .
docker push robinvhoorn/mlops-showcase-download_data:latest

docker build -f Dockerfile -t robinvhoorn/mlops-showcase-train:latest .
docker push robinvhoorn/mlops-showcase-train:latest

docker build -f Dockerfile -t robinvhoorn/mlops-showcase-evaluate:latest .
docker push robinvhoorn/mlops-showcase-evaluate:latest
```