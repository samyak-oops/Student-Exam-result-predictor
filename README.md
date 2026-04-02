# 🎓 Student Exam Performance Predictor

A Machine Learning web application that predicts a student's **math score** based on various factors like gender, parental education, lunch type, and test preparation.

---

## 🚀 Features

* 📊 Predict student math scores using ML models
* 🧠 Multiple models trained (Random Forest, XGBoost, CatBoost, etc.)
* 🔄 Data preprocessing pipeline (scaling + encoding)
* 🌐 Flask-based web application
* 📦 Modular ML pipeline (Data Ingestion → Transformation → Training → Prediction)

---

## 🏗️ Project Structure

```
MLProject/
│
├── app.py                  # Flask app
├── templates/              # HTML files
│     ├── index.html
│     ├── home.html
│
├── artifacts/              # Saved models & preprocessors
│     ├── model.pkl
│     ├── preprocessor.pkl
│
├── src/
│     ├── components/
│     │     ├── data_ingestion.py
│     │     ├── data_transformation.py
│     │     ├── model_trainer.py
│     │
│     ├── pipeline/
│     │     ├── predict_pipeline.py
│     │
│     ├── utils.py
│     ├── exception.py
│     ├── logger.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd MLProject
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🧪 Model Training Pipeline

1. **Data Ingestion**

   * Loads dataset
   * Splits into train/test

2. **Data Transformation**

   * Handles missing values
   * Applies scaling & encoding

3. **Model Training**

   * Trains multiple models
   * Uses GridSearchCV
   * Selects best model based on R² score

---

## 📥 Input Features

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

---

## 📤 Output

* Predicted **Math Score**

---

## 🧠 Algorithms Used

* Linear Regression
* Ridge & Lasso
* Decision Tree
* Random Forest
* KNN
* SVR
* XGBoost
* CatBoost
* AdaBoost

---

## 📸 Screenshots

(Add screenshots here once UI is working)

---

## ⚠️ Common Issues

* ❌ `TemplateNotFound`

  * Ensure HTML files are inside `templates/` folder

* ❌ Form not working

  * Check input `name` matches Flask request keys

---

## 📌 Future Improvements

* Deploy on AWS / Render
* Add user authentication
* Improve UI (Bootstrap / React)
* Add model explainability (SHAP)

---

## 👨‍💻 Author

* Your Name

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
