"""
Funções de processamento de dados
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

def create_temporal_features(df):
    """Cria features temporais"""
    df['Time_Hours'] = df['Time'] / 3600
    df['Hour'] = (df['Time'] / 3600) % 24
    df['Hour_Sin'] = np.sin(2 * np.pi * df['Hour'] / 24)
    df['Hour_Cos'] = np.cos(2 * np.pi * df['Hour'] / 24)
    return df

def scale_features(X_train, X_test, features):
    """Normaliza features usando RobustScaler"""
    scaler = RobustScaler()
    X_train[features] = scaler.fit_transform(X_train[features])
    X_test[features] = scaler.transform(X_test[features])
    return X_train, X_test, scaler