import numpy as np
from KNN_utils import edit_distance, feature_names
from queue import PriorityQueue




def preprocess_data(training_inputs, testing_inputs, training_labels, testing_labels):
    processed_training_inputs, processed_testing_inputs = np.empty((0,15)), np.empty((0,15))
    processed_training_labels, processed_testing_labels = ([], [])
    
    # Get modes for each column
    for x in range(9):
        
        values, counts = np.unique(training_inputs[:,x].astype(str), return_counts = True)
        y = counts.argmax()
        training_inputs[(training_inputs[:,x]).astype(str) == '?', x] = values[y]
       
    for x in range(9):
        values, counts = np.unique(testing_inputs[:,x].astype(str), return_counts = True)
        y = counts.argmax()
        testing_inputs[(testing_inputs[:,x]).astype(str) == '?',x] = values[y]
        
    
        
    training_inputs[(training_inputs[:,0]).astype(str) == "10-19", 0] = 1
    training_inputs[(training_inputs[:,0]).astype(str) == "20-29", 0] = 2
    training_inputs[(training_inputs[:,0]).astype(str) == "30-39",0] = 3
    training_inputs[(training_inputs[:,0]).astype(str) == "40-49",0] = 4
    training_inputs[(training_inputs[:,0]).astype(str) == "50-59",0] = 5
    training_inputs[(training_inputs[:,0]).astype(str) == '60-69',0] = 6
    training_inputs[(training_inputs[:,0]).astype(str) == '70-79',0] = 7
    training_inputs[(training_inputs[:,0]).astype(str) == '80-89',0] = 8
    training_inputs[(training_inputs[:,0]).astype(str) == '90-99',0] = 9
    
    testing_inputs[(testing_inputs[:,0]).astype(str) == "10-19", 0] = 1
    testing_inputs[(testing_inputs[:,0]).astype(str) == "20-29", 0] = 2
    testing_inputs[(testing_inputs[:,0]).astype(str) == "30-39",0] = 3
    testing_inputs[(testing_inputs[:,0]).astype(str) == "40-49",0] = 4
    testing_inputs[(testing_inputs[:,0]).astype(str) == "50-59",0] = 5
    testing_inputs[(testing_inputs[:,0]).astype(str) == '60-69',0] = 6
    testing_inputs[(testing_inputs[:,0]).astype(str) == '70-79',0] = 7
    testing_inputs[(testing_inputs[:,0]).astype(str) == '80-89',0] = 8
    testing_inputs[(testing_inputs[:,0]).astype(str) == '90-99',0] = 9
    
    training_inputs[(training_inputs[:,2]).astype(str) == "0-4", 2] = 1
    training_inputs[(training_inputs[:,2]).astype(str) == "5-9", 2] = 2
    training_inputs[(training_inputs[:,2]).astype(str) == "10-14",2] = 3
    training_inputs[(training_inputs[:,2]).astype(str) == "15-19",2] = 4
    training_inputs[(training_inputs[:,2]).astype(str) == "20-24",2] = 5
    training_inputs[(training_inputs[:,2]).astype(str) == '25-29',2] = 6
    training_inputs[(training_inputs[:,2]).astype(str) == '30-34',2] = 7
    training_inputs[(training_inputs[:,2]).astype(str) == '35-39',2] = 8
    training_inputs[(training_inputs[:,2]).astype(str) == '40-44',2] = 9
    training_inputs[(training_inputs[:,2]).astype(str) == '45-49',2] = 10
    training_inputs[(training_inputs[:,2]).astype(str) == '50-54',2] = 11
    training_inputs[(training_inputs[:,2]).astype(str) == '55-59',2] = 12
    
    testing_inputs[(testing_inputs[:,2]).astype(str) == "0-4", 2] = 1
    testing_inputs[(testing_inputs[:,2]).astype(str) == "5-9", 2] = 2
    testing_inputs[(testing_inputs[:,2]).astype(str) == "10-14",2] = 3
    testing_inputs[(testing_inputs[:,2]).astype(str) == "15-19",2] = 4
    testing_inputs[(testing_inputs[:,2]).astype(str) == "20-24",2] = 5
    testing_inputs[(testing_inputs[:,2]).astype(str) == '25-29',2] = 6
    testing_inputs[(testing_inputs[:,2]).astype(str) == '30-34',2] = 7
    testing_inputs[(testing_inputs[:,2]).astype(str) == '35-39',2] = 8
    testing_inputs[(testing_inputs[:,2]).astype(str) == '40-44',2] = 9
    testing_inputs[(testing_inputs[:,2]).astype(str) == '45-49',2] = 10
    testing_inputs[(testing_inputs[:,2]).astype(str) == '50-54',2] = 11
    testing_inputs[(testing_inputs[:,2]).astype(str) == '55-59',2] = 12
    
    training_inputs[(training_inputs[:,3]).astype(str) == "0-2", 3] = 1
    training_inputs[(training_inputs[:,3]).astype(str) == "3-5", 3] = 2
    training_inputs[(training_inputs[:,3]).astype(str) == "6-8",3] = 3
    training_inputs[(training_inputs[:,3]).astype(str) == "9-11",3] = 4
    training_inputs[(training_inputs[:,3]).astype(str) == "12-14",3] = 5
    training_inputs[(training_inputs[:,3]).astype(str) == '15-17',3] = 6
    training_inputs[(training_inputs[:,3]).astype(str) == '18-20',3] = 7
    training_inputs[(training_inputs[:,3]).astype(str) == '21-23',3] = 8
    training_inputs[(training_inputs[:,3]).astype(str) == '24-26',3] = 9
    training_inputs[(training_inputs[:,3]).astype(str) == '27-29',3] = 10
    training_inputs[(training_inputs[:,3]).astype(str) == '30-32',3] = 11
    training_inputs[(training_inputs[:,3]).astype(str) == '33-35',3] = 12
    training_inputs[(training_inputs[:,3]).astype(str) == '36-39',3] = 13
    
    testing_inputs[(testing_inputs[:,3]).astype(str) == "0-2", 3] = 1
    testing_inputs[(testing_inputs[:,3]).astype(str) == "3-5", 3] = 2
    testing_inputs[(testing_inputs[:,3]).astype(str) == "6-8",3] = 3
    testing_inputs[(testing_inputs[:,3]).astype(str) == "9-11",3] = 4
    testing_inputs[(testing_inputs[:,3]).astype(str) == "12-14",3] = 5
    testing_inputs[(testing_inputs[:,3]).astype(str) == '15-17',3] = 6
    testing_inputs[(testing_inputs[:,3]).astype(str) == '18-20',3] = 7
    testing_inputs[(testing_inputs[:,3]).astype(str) == '21-23',3] = 8
    testing_inputs[(testing_inputs[:,3]).astype(str) == '24-26',3] = 9
    testing_inputs[(testing_inputs[:,3]).astype(str) == '27-29',3] = 10
    testing_inputs[(testing_inputs[:,3]).astype(str) == '30-32',3] = 11
    testing_inputs[(testing_inputs[:,3]).astype(str) == '33-35',3] = 12
    testing_inputs[(testing_inputs[:,3]).astype(str) == '36-39',3] = 13
    
    training_inputs[(training_inputs[:,5]).astype(str) == "1", 5] = 0
    training_inputs[(training_inputs[:,5]).astype(str) == "2", 5] = 1
    training_inputs[(training_inputs[:,5]).astype(str) == "3",5] = 2
    
    testing_inputs[(testing_inputs[:,5]).astype(str) == "1", 5] = 0
    testing_inputs[(testing_inputs[:,5]).astype(str) == "2", 5] = 1
    testing_inputs[(testing_inputs[:,5]).astype(str) == "3",5] = 2
    
    training_inputs[(training_inputs[:,4]).astype(str) == "yes", 4] = 1
    training_inputs[(training_inputs[:,4]).astype(str) == "no", 4] = 0
    
    training_inputs[(training_inputs[:,6]).astype(str) == "left", 6] = 1
    training_inputs[(training_inputs[:,6]).astype(str) == "right",6] = 0
    
    training_inputs[(training_inputs[:,8]).astype(str) == "yes", 8] = 1
    training_inputs[(training_inputs[:,8]).astype(str) == "no", 8] = 0
    
    testing_inputs[(testing_inputs[:,4]).astype(str) == "yes", 4] = 1
    testing_inputs[(testing_inputs[:,4]).astype(str) == "no", 4] = 0
    
    testing_inputs[(testing_inputs[:,6]).astype(str) == "left", 6] = 1
    testing_inputs[(testing_inputs[:,6]).astype(str) == "right",6] = 0
    
    testing_inputs[(testing_inputs[:,8]).astype(str) == "yes", 8] = 1
    testing_inputs[(testing_inputs[:,8]).astype(str) == "no", 8] = 0
    
    
    for row in range(len(training_inputs)):
        
        arr = training_inputs[row]
        if(arr[1] == 'ge40'):
            arr = np.append(arr, 1)
            arr = np.append(arr, 0)
            arr = np.append(arr, 0)
        elif(arr[1] == 'premeno'):
            arr = np.append(arr, 0)
            arr = np.append(arr, 1)
            arr = np.append(arr, 0)
        elif(arr[1] == 'lt40'):
            arr = np.append(arr, 0)
            arr = np.append(arr, 0)
            arr = np.append(arr, 1)
            
        arr = np.delete(arr, 1)
            
        if(arr[6] == 'right_up'):
            arr = np.append(arr, 1)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            
        elif(arr[6] == 'left_up'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
        elif(arr[6] == 'left_low'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
        elif(arr[6] == 'right_low'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            arr =np.append(arr, 0)
        elif(arr[6] == 'central'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            
        arr = np.delete(arr, 6)
        processed_training_inputs = np.vstack((processed_training_inputs, arr))
        
    for row in range(len(testing_inputs)):
        
        arr = testing_inputs[row]
        if(arr[1] == 'ge40'):
            arr = np.append(arr, 1)
            arr = np.append(arr, 0)
            arr = np.append(arr, 0)
        elif(arr[1] == 'premeno'):
            arr = np.append(arr, 0)
            arr = np.append(arr, 1)
            arr = np.append(arr, 0)
        elif(arr[1] == 'lt40'):
            arr = np.append(arr, 0)
            arr = np.append(arr, 0)
            arr = np.append(arr, 1)
            
        arr = np.delete(arr, 1)
            
        if(arr[6] == 'right_up'):
            arr = np.append(arr, 1)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            
        elif(arr[6] == 'left_up'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
        elif(arr[6] == 'left_low'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
        elif(arr[6] == 'right_low'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            arr =np.append(arr, 0)
        elif(arr[6] == 'central'):
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 0)
            arr =np.append(arr, 1)
            
        arr = np.delete(arr, 6)
        processed_testing_inputs = np.vstack((processed_testing_inputs, arr))
        
    for x in range(len(training_labels)):
        if(training_labels[x] == "recurrence-events"):
            training_labels[x] = 0
        else:
            training_labels[x] = 1
            
    for x in range(len(testing_labels)):
        if(testing_labels[x] == "recurrence-events"):
            testing_labels[x] = 0
        else:
            testing_labels[x] = 1
    
    return processed_training_inputs, processed_testing_inputs, training_labels, testing_labels




def k_nearest_neighbors(predict_on, reference_points, reference_labels, k, l):
    assert len(predict_on) > 0, f"parameter predict_on needs to be of length 0 or greater"
    assert len(reference_points) > 0, f"parameter reference_points needs to be of length 0 or greater"
    assert len(reference_labels) > 0, f"parameter reference_labels needs to be of length 0 or greater"
    assert len(reference_labels) == len(reference_points), f"reference_points and reference_labels need to be the" \
                                                           f" same length"
    predictions = []
    
   
    for x in range(len(predict_on)):
        
        arr = []
        for y in range(len(reference_points)):
            arr.append(edit_distance(predict_on[x], reference_points[y], l))
        reccurence = 0
        no_reccurence =0
        arrSortedIndex = np.argsort(arr)
        for z in range(k):
            if(reference_labels[arrSortedIndex[z]] == 0):
                reccurence += 1
            else:
                no_reccurence += 1
        if(reccurence < no_reccurence):
            predictions.append(1)
        else:
            predictions.append(0)
            
    return predictions
