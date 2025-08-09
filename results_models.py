import matplotlib.pyplot as plt
import numpy as np

# Data
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']
models = [
    'reproduce W-CNN \n (ALL dataset)', 
    'CatBoost + W-CNN \n (ALL dataset)', 
    'reproduce CatBoost \n (AML dataset, 27 features)', 
    'CatBoost + W-CNN \n (AML dataset, 27 features)', 
    'CatBoost + W-CNN \n (AML dataset, 44,754 features)', 
    'CatBoost + W-CNN \n (our dataset, 22,777 features)'
]
scores = np.array([
    [86.05, 80, 73, 76], 
    [87.88, 82.5, 81.58, 81.12],  
    [99.64, 100, 99.55, 99.77], 
    [99.84, 100, 99.80, 99.90],  
    [99.41, 98.83, 99.70, 99.62],   
    [99.56, 99.56, 99.49, 99.52], 
])

execute_times = [286.33, 1182.23, 1199.05, 1459.76, 2737.41, 1980.5] 

# Bar Chart
plt.figure(figsize=(14, 6))
x = np.arange(len(metrics))
bar_width = 0.15
colors = ['skyblue', 'deepskyblue', 'lightcoral', 'brown', 'turquoise', 'teal']

for i, model in enumerate(models):
    bars = plt.bar(x + i*bar_width, scores[i], width=bar_width, label=model, color=colors[i])
    for bar, score in zip(bars, scores[i]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 f'{score:.1f}', ha='center', va='bottom', fontsize=10)
plt.xticks(x + bar_width * (len(models) // 2), metrics, fontsize=14)
plt.ylabel('Score (%)', fontsize=14)
plt.ylim(60, 105)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=12)
plt.title('Model Performance Metrics', fontsize=16)
plt.tight_layout()
plt.show()

# Execution Time Line Chart
plt.figure(figsize=(14, 5))
plt.plot(np.arange(len(models)), execute_times, marker='o', linewidth=2, color=colors[i])
plt.xticks(np.arange(len(models)), models, rotation=45, ha='right', fontsize=14)
plt.ylabel('Execute Time (s)', fontsize=18)
plt.title('Model Execution Time', fontsize=18)
for i, time in enumerate(execute_times):
    plt.text(i, time + 0.5, f'{time:.1f}', ha='center', va='bottom', color='black', fontsize=16)
plt.tight_layout()
plt.show()

# Extended models
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']
models = [
    'CatBoost + W-CNN \n (our dataset, 22,777 features)',
    'CatBoost + W-CNN \n (multi-omics dataset)', 
    'CatBoost + 1D_CNN - BiLTSM - 1D_CNN \n (our dataset, 22,777 features)', 
]
scores = np.array([ 
    [99.56, 99.56, 99.49, 99.52], 
    [97,96.94,96.95,96.93],
    [96.58,94.37,95.33,94.73]
])

plt.figure(figsize=(14, 6))
x = np.arange(len(metrics))
bar_width = 0.15
colors = ['skyblue','lightcoral', 'turquoise']

for i, model in enumerate(models):
    bars = plt.bar(x + i*bar_width, scores[i], width=bar_width, label=model, color=colors[i])
    for bar, score in zip(bars, scores[i]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                 f'{score:.1f}', ha='center', va='bottom', fontsize=10)
plt.xticks(x + bar_width * (len(models) // 2), metrics, fontsize=14)
plt.ylabel('Score (%)', fontsize=14)
plt.ylim(60, 105)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=12)
plt.title('Model Performance Metrics', fontsize=16)
plt.tight_layout()
plt.show()

models = [
    'CatBoost + W-CNN \n (our dataset, 22,777 features)',
    'CatBoost + W-CNN \n (multi-omics dataset)', 
    'CatBoost + 1D_CNN - BiLTSM - 1D_CNN \n (our dataset, 22,777 features)'
]
execute_times = [1980.5, 344.9, 2038.74]
line_color = 'skyblue'

plt.figure(figsize=(10, 5))
plt.plot(np.arange(len(models)), execute_times, marker='o', color=line_color, markersize=10, linewidth=2, label='Execute Time (s)')
for i, time in enumerate(execute_times):
    plt.text(i, time + 30, f'{time:.2f}', ha='center', va='bottom', fontsize=12)
plt.xticks(np.arange(len(models)), models, ha='center', fontsize=12)
plt.ylabel('Execute Time (s)', fontsize=14)
plt.title('Model Execution Time', fontsize=14)
plt.ylim(0, max(execute_times) * 1.2)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18), fontsize=12, ncol=1)
plt.tight_layout()
plt.show()

# Extended Data
metrics_2 = ['Accuracy', 'Precision', 'Recall', 'F1-score']
models_2 = [99.74, 89.17, 95.83, 96.32]  # One model's scores


x = np.arange(len(metrics_2))
bar_width = 0.5
colors = ['skyblue', 'deepskyblue', 'lightcoral', 'brown']

plt.figure(figsize=(8, 6))
bars = plt.bar(x, models_2, width=bar_width, color=colors)


for bar, score in zip(bars, models_2):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             f'{score:.2f}', ha='center', va='bottom', fontsize=12)

plt.xticks(x, metrics_2, fontsize=16)
plt.ylabel('Score (%)', fontsize=16)
plt.ylim(60, 105)
plt.title('Model Performance Metrics', fontsize=16)
plt.tight_layout()
plt.show()
