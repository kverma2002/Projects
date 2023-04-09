from NN_Utils import (
    load_data, accuracy_score
)
from NN import neural_Network, preprocess_data

import numpy as np
import time
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print(f"Loading data from file...")
    start_time = time.time()
    raw_data = load_data()
    load_time = time.time() - start_time
    print(f"Data loaded - time elapsed from start: {load_time:0.9f}")
    print(f"Beginning data preprocessing and cleaning...")
    
    
    train_inputs, train_labels, test_inputs, test_labels =\
        preprocess_data(*raw_data)
    load_time = time.time() - start_time
    
    print(f"Data preprocessed - time elapsed from start: {load_time:0.9f}")
    
    
    print(f"Example training input: {train_inputs[0]} - label: {train_labels[0]}")
    accuracy_rate, average_misclassify_rate = 0,0
    
    epochs = [10,25, 50,75, 100, 125, 150, 175 ,200, 225,250, 275, 300, 350, 400, 450, 500]
    accuracies = []
    for x in epochs:
        accuracy_rate = neural_Network(train_inputs, train_labels, test_inputs, test_labels, x)
        accuracies.append(accuracy_rate)
        
    print(f"Max accuracy - {np.max(accuracies)} - Epochs: {epochs[np.argmax(accuracies)]}")
    plt.plot(epochs, accuracies)
    plt.xlabel('epochs')
    plt.ylabel('accuracy')
    plt.title('Accuracy based on number of epochs')
    plt.show()
        
    
    
    
    

    

    