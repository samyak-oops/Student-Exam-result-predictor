import os
import sys
import pickle
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        best_models = {}

        for model_name, model in models.items():
            para = params.get(model_name, {})

            gs = GridSearchCV(model, para, cv=5)
            gs.fit(X_train, y_train)

            best_model = gs.best_estimator_  # already trained

            # Predictions
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_score
            best_models[model_name] = best_model

        return report, best_models

    except Exception as e:
        raise CustomException(e, sys)