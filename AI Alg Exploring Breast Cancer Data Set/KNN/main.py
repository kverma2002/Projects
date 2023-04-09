from KNN_utils import (
    accuracy_score,
    load_data
)
from KNN import k_nearest_neighbors, preprocess_data
import numpy as np
import time
import matplotlib.pyplot as plt
from tabulate import tabulate
if __name__ == "__main__":
    print(f"Loading data from file...")
    start_time = time.time()
    raw_data = load_data()
    load_time = time.time() - start_time
    print(f"Data loaded - time elapsed from start: {load_time:0.9f}")
    print(f"Beginning data preprocessing and cleaning...")
    processed_training_inputs, processed_testing_inputs, processed_training_labels, processed_testing_labels =\
        preprocess_data(*raw_data)
    load_time = time.time() - start_time
    print(f"Data preprocessed - time elapsed from start: {load_time:0.9f}")
    print(f"Example training input: {processed_training_inputs[0]} - label: {processed_training_labels[0]}")
    l_norms = [-1, 1, 2, 3, 4, 5, 6, np.inf]
    k_max = 30
    accuracies = np.zeros((k_max, len(l_norms)))
    table = np.empty((0,9))
    table = np.vstack((table, ["K", "L=-1", "L=1", "L=2", "L=3", "L=4", "L=5", "L=6", "L=inf"]))
    sizes = []
    x = []
    for k in range(1, k_max+1):
        arr = []
        arr.append(k)
        for l_i, l_norm in enumerate(l_norms):
            print(f"Running kNN with k= {k}, l= {l_norm}")
            predicted_labels = k_nearest_neighbors(
                predict_on=processed_testing_inputs,
                reference_points=processed_training_inputs,
                reference_labels=processed_training_labels,
                k=k,
                l=l_norm,
            )
            load_time = time.time() - start_time
            print(f"kNN completer - time elapsed from start: {load_time:0.9f}")
            accuracies[k-1, l_i] = accuracy_score(processed_testing_labels, predicted_labels)
            arr.append(round(accuracies[k-1, l_i], 4))
            sizes.append(l_norm)
            x.append(k)
        table = np.vstack((table, arr))
    best_accuracy = np.max(accuracies)
    best_k, best_metric = np.where(accuracies == best_accuracy)
    print(f"Highest accuracy achieved: {best_accuracy:0.4f}")
    for k, l in zip(best_k, best_metric):
        print(f"\t k= {k+1} - l= {l_norms[l]}]")
    
    print(tabulate(table))

    sizes = np.where(sizes == 'inf', 7, sizes)
    sizes = np.power(sizes, 1.5)
    sizes = sizes * 2
    plt.scatter(x, accuracies, s = sizes)
    plt.ylim(0,1)
    plt.xlabel('K')
    plt.ylabel('Accuracies')
    plt.title('K to accuracies (Dot size base on L')
    plt.show()
    
