import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def preprocess_data(training_inputs, testing_inputs, training_labels, testing_labels):
    
    x_data = np.concatenate((training_inputs, testing_inputs))
    y_data = np.concatenate((training_labels, testing_labels))
    
    for x in range(9):
       values, counts = np.unique(x_data[:,x].astype(str), return_counts = True)
       y = counts.argmax()
       x_data[(x_data[:,x]).astype(str) == '?', x] = values[y]
      
    x_data[(x_data[:,0]).astype(str) == "10-19", 0] = 1
    x_data[(x_data[:,0]).astype(str) == "20-29", 0] = 2
    x_data[(x_data[:,0]).astype(str) == "30-39",0] = 3
    x_data[(x_data[:,0]).astype(str) == "40-49",0] = 4
    x_data[(x_data[:,0]).astype(str) == "50-59",0] = 5
    x_data[(x_data[:,0]).astype(str) == '60-69',0] = 6
    x_data[(x_data[:,0]).astype(str) == '70-79',0] = 7
    x_data[(x_data[:,0]).astype(str) == '80-89',0] = 8
    x_data[(x_data[:,0]).astype(str) == '90-99',0] = 9
     
    x_data[(x_data[:,2]).astype(str) == "0-4", 2] = 1
    x_data[(x_data[:,2]).astype(str) == "5-9", 2] = 2
    x_data[(x_data[:,2]).astype(str) == "10-14",2] = 3
    x_data[(x_data[:,2]).astype(str) == "15-19",2] = 4
    x_data[(x_data[:,2]).astype(str) == "20-24",2] = 5
    x_data[(x_data[:,2]).astype(str) == '25-29',2] = 6
    x_data[(x_data[:,2]).astype(str) == '30-34',2] = 7
    x_data[(x_data[:,2]).astype(str) == '35-39',2] = 8
    x_data[(x_data[:,2]).astype(str) == '40-44',2] = 9
    x_data[(x_data[:,2]).astype(str) == '45-49',2] = 10
    x_data[(x_data[:,2]).astype(str) == '50-54',2] = 11
    x_data[(x_data[:,2]).astype(str) == '55-59',2] = 12
    
    x_data[(x_data[:,3]).astype(str) == "0-2", 3] = 1
    x_data[(x_data[:,3]).astype(str) == "3-5", 3] = 2
    x_data[(x_data[:,3]).astype(str) == "6-8",3] = 3
    x_data[(x_data[:,3]).astype(str) == "9-11",3] = 4
    x_data[(x_data[:,3]).astype(str) == "12-14",3] = 5
    x_data[(x_data[:,3]).astype(str) == '15-17',3] = 6
    x_data[(x_data[:,3]).astype(str) == '18-20',3] = 7
    x_data[(x_data[:,3]).astype(str) == '21-23',3] = 8
    x_data[(x_data[:,3]).astype(str) == '24-26',3] = 9
    x_data[(x_data[:,3]).astype(str) == '27-29',3] = 10
    x_data[(x_data[:,3]).astype(str) == '30-32',3] = 11
    x_data[(x_data[:,3]).astype(str) == '33-35',3] = 12
    x_data[(x_data[:,3]).astype(str) == '36-39',3] = 13
    
    x_data[(x_data[:,5]).astype(str) == "1", 5] = 0
    x_data[(x_data[:,5]).astype(str) == "2", 5] = 1
    x_data[(x_data[:,5]).astype(str) == "3",5] = 2
    
    x_data[(x_data[:,4]).astype(str) == "yes", 4] = 1
    x_data[(x_data[:,4]).astype(str) == "no", 4] = 0
    
    x_data[(x_data[:,6]).astype(str) == "left", 6] = 1
    x_data[(x_data[:,6]).astype(str) == "right",6] = 0
    
    x_data[(x_data[:,8]).astype(str) == "yes", 8] = 1
    x_data[(x_data[:,8]).astype(str) == "no", 8] = 0
    
    x_data[(x_data[:,1]).astype(str) == "ge40", 1] = 0
    x_data[(x_data[:,1]).astype(str) == "premeno", 1] = 1
    x_data[(x_data[:,1]).astype(str) == "lt40", 1] = 2
    
    x_data[(x_data[:,7]).astype(str) == "right_up", 7] = 0
    x_data[(x_data[:,7]).astype(str) == "left_up", 7] = 1
    x_data[(x_data[:,7]).astype(str) == "central", 7] = 2
    x_data[(x_data[:,7]).astype(str) == "left_low", 7] = 3
    x_data[(x_data[:,7]).astype(str) == "right_low", 7] = 4
    
    preProc = preprocessing.LabelEncoder()
    for x in range(len(x_data[0])):
        if(x != 6):
            print(x)
            x_data[x] = preProc.fit_transform(x_data[x])
    
    print(y_data)
    y_data = preProc.fit_transform(y_data)
            
    train_inputs,test_inputs,train_labels, test_labels = train_test_split(x_data, y_data, test_size=.3, random_state = 42)
    print(f"TI:{len(train_inputs)} - TL: {len(train_labels)} - TeI: {len(test_inputs)}")
    return train_inputs, train_labels, test_inputs, test_labels
            
    
    

def neural_Network(train_inputs, train_labels, test_inputs, test_labels, itterations):
    
    clf = MLPClassifier(hidden_layer_sizes=(20, 10, 2), random_state = 5, verbose = True, learning_rate_init=.01, max_iter=itterations)
    print(len(train_inputs))
    print(len(train_labels))
    clf.fit(train_inputs, train_labels)
    print(len(train_inputs))
    print(len(train_labels))
    pred = clf.predict(test_inputs)
    
    
    return accuracy_score(test_labels, pred)


