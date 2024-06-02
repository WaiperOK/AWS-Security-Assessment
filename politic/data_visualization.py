
import matplotlib.pyplot as plt
import numpy as np

def plot_event_classification(predictions):
    classes, counts = np.unique(predictions, return_counts=True)
    plt.figure(figsize=(10, 6))
    plt.bar(classes, counts, color='blue')
    plt.xlabel('Event Classes')
    plt.ylabel('Count')
    plt.title('Event Classification Counts')
    plt.show()
