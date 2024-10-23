import pandas as pd

def generate_features(df):
    features = pd.DataFrame()
    features['id'] = df['id']
    
    # Генерация признаков
    features['mean'] = df['values'].apply(np.mean)
    features['std'] = df['values'].apply(np.std)
    features['min'] = df['values'].apply(np.min)
    features['max'] = df['values'].apply(np.max)
    
    # Другие признаки можно добавить здесь

    return features

if __name__ == "__main__":
    train = pd.read_parquet('data/train.parquet')
    test = pd.read_parquet('data/test.parquet')
    
    X_train = generate_features(train)
    X_test = generate_features(test)
    
    X_train.to_csv('data/X_train.csv', index=False)
    X_test.to_csv('data/X_test.csv', index=False)
