import pandas as pd
import joblib

# Загрузка модели и тестовых данных
model = joblib.load('model/rf_model.joblib')
X_test = pd.read_csv('data/X_test.csv')

# Предсказания
predictions = model.predict_proba(X_test)[:, 1]
submission = pd.DataFrame({'id': X_test['id'], 'score': predictions})

# Сохранение в файл
submission.to_csv('submission.csv', index=False)
