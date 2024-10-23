# VK_test
# Временные ряды классификация

## Структура проекта
- `data/` - данные для обучения и тестирования.
- `notebooks/` - Jupyter ноутбук с EDA и обучением модели.
- `scripts/` - скрипты для генерации признаков и предсказания.
- `submission.csv` - файл с предсказаниями.

## Установка зависимостей
Установите необходимые библиотеки:
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
pyarrow


## Запуск
1. Выполните EDA и обучение модели в Jupyter Notebook.
2. Запустите `scripts/feature_generation.py` для генерации признаков.
3. Запустите `scripts/predict.py` для получения предсказаний.

Файл `submission.csv` будет создан в корне проекта.
