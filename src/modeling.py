"""
Funções de modelagem
"""
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score, recall_score, precision_score

def evaluate_model(model, X_test, y_test):
    """Avalia modelo e retorna métricas"""
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    metrics = {
        'recall': recall_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'auc_roc': roc_auc_score(y_test, y_proba),
        'confusion_matrix': confusion_matrix(y_test, y_pred)
    }
    
    return metrics, y_pred, y_proba
