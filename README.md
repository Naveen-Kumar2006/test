# House Price Prediction API

An end-to-end Machine Learning regression project that predicts house prices using a trained Decision Tree Regressor and exposes the model through a FastAPI REST API.

## 🚀 Features

- Data preprocessing with Scikit-learn
- Missing-value handling
- Feature scaling
- Decision Tree Regression
- Hyperparameter tuning with GridSearchCV
- 5-fold cross-validation
- Model evaluation using MAE, MSE, RMSE and R²
- Saved ML pipeline using Joblib
- FastAPI REST API
- Swagger API documentation
- Dockerized application

## 🤖 Machine Learning

**Model:** Decision Tree Regressor

**Hyperparameter tuning:** GridSearchCV with 5-fold cross-validation

### Best Parameters

- `max_depth`: 7
- `min_samples_split`: 10
- `min_samples_leaf`: 4
- `max_features`: None

### Model Performance

| Metric | Score |
|---|---:|
| CV R² | 0.9780 |
| Test R² | 0.9755 |
| Test MAE | 1,213,295.65 |
| Test RMSE | 1,779,533.37 |

## 📊 Input Features

The API accepts:

- `area_sqft`
- `bedrooms`
- `bathrooms`
- `stories`
- `parking`

## ⚡ FastAPI

Run the API locally:

```bash
uvicorn main:app --reload
