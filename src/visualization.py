"""
Funções de visualização
"""
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, title='Confusion Matrix'):
    """Plota matriz de confusão"""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='RdYlGn_r', ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylabel('Real', fontsize=12)
    ax.set_xlabel('Predito', fontsize=12)
    plt.tight_layout()
    return fig

def plot_roc_curve(fpr, tpr, auc_score):
    """Plota curva ROC"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(fpr, tpr, label=f'AUC = {auc_score:.4f}', linewidth=2)
    ax.plot([0, 1], [0, 1], 'k--', linewidth=1)
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('ROC Curve')
    ax.legend()
    ax.grid(alpha=0.3)
    return fig