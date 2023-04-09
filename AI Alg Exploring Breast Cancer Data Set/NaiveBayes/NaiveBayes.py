import numpy as np
from Bayes_Utils import feature_names
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import type_of_target


figure = ['fig1.pdf', 'fig2.pdf', 'fig3.pdf', 'fig4.pdf', 'fig5.pdf', 'fig6.pdf']
pdf = 0

def preprocess_data(training_inputs, testing_inputs, training_labels, testing_labels):
    
    #Replace missing values with mode of data set
    for x in range(9):
        values, counts = np.unique(training_inputs[:,x].astype(str), return_counts = True)
        y = counts.argmax()
        training_inputs[(training_inputs[:,x]).astype(str) == '?', x] = values[y]
       
    for x in range(9):
        values, counts = np.unique(testing_inputs[:,x].astype(str), return_counts = True)
        y = counts.argmax()
        testing_inputs[(testing_inputs[:,x]).astype(str) == '?',x] = values[y]
    
    #Replace data with numerical values
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
    
    training_inputs[(training_inputs[:,1]).astype(str) == "ge40", 1] = 0
    training_inputs[(training_inputs[:,1]).astype(str) == "premeno", 1] = 1
    training_inputs[(training_inputs[:,1]).astype(str) == "lt40", 1] = 2
    
    testing_inputs[(testing_inputs[:,1]).astype(str) == "ge40", 1] = 0
    testing_inputs[(testing_inputs[:,1]).astype(str) == "premeno", 1] = 1
    testing_inputs[(testing_inputs[:,1]).astype(str) == "lt40", 1] = 2
    
    training_inputs[(training_inputs[:,7]).astype(str) == "right_up", 7] = 0
    training_inputs[(training_inputs[:,7]).astype(str) == "left_up", 7] = 1
    training_inputs[(training_inputs[:,7]).astype(str) == "central", 7] = 2
    training_inputs[(training_inputs[:,7]).astype(str) == "left_low", 7] = 3
    training_inputs[(training_inputs[:,7]).astype(str) == "right_low", 7] = 4
    
    testing_inputs[(testing_inputs[:,7]).astype(str) == "right_up", 7] = 0
    testing_inputs[(testing_inputs[:,7]).astype(str) == "left_up", 7] = 1
    testing_inputs[(testing_inputs[:,7]).astype(str) == "central", 7] = 2
    testing_inputs[(testing_inputs[:,7]).astype(str) == "left_low", 7] = 3
    testing_inputs[(testing_inputs[:,7]).astype(str) == "right_low", 7] = 4
    
        
    #replace labels with 0 for reccurence and 1 for non reccurence
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

    
    return training_inputs, testing_inputs, training_labels, testing_labels


def naive_bayes(training_inputs, testing_inputs, training_labels, testing_labels):
    assert len(training_inputs) > 0, f"parameter training_inputs needs to be of length 0 or greater"
    assert len(testing_inputs) > 0, f"parameter testing_inputs needs to be of length 0 or greater"
    assert len(training_labels) > 0, f"parameter training_labels needs to be of length 0 or greater"
    assert len(testing_labels) > 0, f"parameter testing_labels needs to be of length 0 or greater"
    assert len(training_inputs) == len(training_labels), f"training_inputs and training_labels need to be the same length"
    assert len(testing_inputs) == len(testing_labels), f"testing_inputs and testing_labels need to be the same length"
    global pdf
    predictions = []
    #New arrasy to seperate daat
    reccurence = np.empty((0,9))
    non_reccurence = np.empty((0,9))
    
    #count correct guesses
    correct = 0
    
    #Seperate data from reccurence and non reccurence classes
    for x in range(len(training_labels)):
        if(training_labels[x] == 0):
            reccurence = np.vstack((reccurence, training_inputs[x]))
        else:
            non_reccurence = np.vstack((non_reccurence, training_inputs[x]))
    
    #Create unique values array and counts for each variable for calculations
    RecV1, RecC1 = np.unique(reccurence[:,0], return_counts = True)
    RecV2, RecC2 = np.unique(reccurence[:,1], return_counts = True)
    RecV3, RecC3 = np.unique(reccurence[:,2], return_counts = True)
    RecV4, RecC4 = np.unique(reccurence[:,3], return_counts = True)
    RecV5, RecC5 = np.unique(reccurence[:,4], return_counts = True)
    RecV6, RecC6 = np.unique(reccurence[:,5], return_counts = True)
    RecV7, RecC7 = np.unique(reccurence[:,6], return_counts = True)
    RecV8, RecC8 = np.unique(reccurence[:,7], return_counts = True)
    RecV9, RecC9 = np.unique(reccurence[:,8], return_counts = True)
    

    NRecV1, NRecC1 = np.unique(non_reccurence[:,0], return_counts = True)
    NRecV2, NRecC2 = np.unique(non_reccurence[:,1], return_counts = True)
    NRecV3, NRecC3 = np.unique(non_reccurence[:,2], return_counts = True)
    NRecV4, NRecC4 = np.unique(non_reccurence[:,3], return_counts = True)
    NRecV5, NRecC5 = np.unique(non_reccurence[:,4], return_counts = True)
    NRecV6, NRecC6 = np.unique(non_reccurence[:,5], return_counts = True)
    NRecV7, NRecC7 = np.unique(non_reccurence[:,6], return_counts = True)
    NRecV8, NRecC8 = np.unique(non_reccurence[:,7], return_counts = True)
    NRecV9, NRecC9 = np.unique(non_reccurence[:,8], return_counts = True)
    
    #n is for divisor in reccurence
    #v is for divisor in non reccurence
    n = len(reccurence)
    v = len(non_reccurence)
    
    
    for x in range(len(testing_inputs)):
        #Calculate probability given its reccurence
        rec_prob = 1
        #Calculate naive bayes for both reccurence and non reccurence, then compare values to see what to predict
        if(np.where(RecV1 == testing_inputs[x][0])[0] == []): 
            rec_prob *= (RecC1[np.where(RecV1 == testing_inputs[x][0])[0][0]] + 1) / (n + len(RecV1))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV2 == testing_inputs[x][1])[0] == []):
            rec_prob *= (RecC2[np.where(RecV2 == testing_inputs[x][1])[0][0]] + 1) / (n + len(RecV2))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV3 == testing_inputs[x][2])[0] == []):
            rec_prob *= (RecC3[np.where(RecV3 == testing_inputs[x][2])[0][0]] + 1) / (n + len(RecV3))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV4 == testing_inputs[x][3])[0] == []):
            rec_prob *= (RecC4[np.where(RecV4 == testing_inputs[x][3])[0][0]] + 1) / (n + len(RecV4))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV5 == testing_inputs[x][4])[0] == []):
            rec_prob *= (RecC5[np.where(RecV5 == testing_inputs[x][4])[0][0]] + 1) / (n + len(RecV5))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV6 == testing_inputs[x][5])[0] == []):
            rec_prob *= (RecC6[np.where(RecV6 == testing_inputs[x][5])[0][0]] + 1) / (n + len(RecV6))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV7 == testing_inputs[x][6])[0] == []):
            rec_prob *= (RecC7[np.where(RecV7 == testing_inputs[x][6])[0][0]] + 1) / (n + len(RecV7))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV8 == testing_inputs[x][7])[0] == []): 
            rec_prob *= (RecC8[np.where(RecV8 == testing_inputs[x][7])[0][0]] + 1) / (n + len(RecV8))
        else:
            rec_prob *= 1/(n + len(RecV1))
        if(np.where(RecV9 == testing_inputs[x][8])[0] == []):
            rec_prob *= (RecC9[np.where(RecV9 == testing_inputs[x][8])[0][0]] + 1) / (n + len(RecV8))
        else:
            rec_prob *= 1/(n + len(RecV1))
        
        #Now calculate for non reccurence class
        
        non_rec_prob = 1
        if(np.where(NRecV1 == testing_inputs[x][0])[0] == []): 
            non_rec_prob *= (NRecC1[np.where(NRecV1 == testing_inputs[x][0])[0][0]] + 1) / (v + len(NRecV1))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV2 == testing_inputs[x][1])[0] == []):
            non_rec_prob *= (NRecC2[np.where(NRecV2 == testing_inputs[x][1])[0][0]] + 1) / (v + len(NRecV2))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV3 == testing_inputs[x][2])[0] == []):
            non_rec_prob *= (NRecC3[np.where(NRecV3 == testing_inputs[x][2])[0][0]] + 1) / (v + len(NRecV3))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV4 == testing_inputs[x][3])[0] == []):
            non_rec_prob *= (NRecC4[np.where(NRecV4 == testing_inputs[x][3])[0][0]] + 1) / (v + len(NRecV4))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV5 == testing_inputs[x][4])[0] == []):
            non_rec_prob *= (NRecC5[np.where(NRecV5 == testing_inputs[x][4])[0][0]] + 1) / (v + len(NRecV5))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV6 == testing_inputs[x][5])[0] == []):
            non_rec_prob *= (NRecC6[np.where(NRecV6 == testing_inputs[x][5])[0][0]] + 1) / (v + len(NRecV6))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV7 == testing_inputs[x][6])[0] == []):
            non_rec_prob *= (NRecC7[np.where(NRecV7 == testing_inputs[x][6])[0][0]] + 1) / (v + len(NRecV7))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV8 == testing_inputs[x][7])[0] == []): 
            non_rec_prob *= (NRecC8[np.where(NRecV8 == testing_inputs[x][7])[0][0]] + 1) / (v + len(NRecV8))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        if(np.where(NRecV9 == testing_inputs[x][8])[0] == []):
            non_rec_prob *= (NRecC9[np.where(NRecV9 == testing_inputs[x][8])[0][0]] + 1) / (v + len(NRecV8))
        else:
            non_rec_prob *= 1/(v + len(NRecV1))
        
        
       
        
        if(non_rec_prob > rec_prob):
            predictions.append(1)
            
            if(testing_labels[x] == 1):
                correct += 1
        else:
            predictions.append(0)
            
            if(testing_labels[x] == 0):
                correct+= 1
        #print(predictions)
                
    
    
    confusionM = confusion_matrix(testing_labels.tolist(), predictions)
    confusionMatrix = pd.DataFrame(data = confusionM, columns=['True Reccurence:0', 'True NonReccurence:1'],
                                   index = ['Predict Reccurence:0', 'Predict NonReccurence:1'])
    sea.heatmap(confusionMatrix, annot=True, fmt='d', cmap = 'YlGnBu')
    plt.savefig(figure[pdf])
    plt.clf()
    pdf += 1
        
    
    return (correct / len(testing_labels))


def cross_validation(training_inputs, testing_inputs, training_labels, testing_labels):
    data = np.concatenate((training_inputs, testing_inputs))
    label = np.concatenate((training_labels, testing_labels))
    average_rate = 0
    
    shuffeled_data,shuffled_labels = shuffle_arrays(data, label)
    #Use five fold cross validation
    splitData = np.array_split(shuffeled_data, 5)
    splitLabels = np.array_split(shuffled_labels, 5)
    
    CV = 0
    for x in range(len(splitData)):
        newTrainingInputs = np.empty((0,9))
        newTrainingLabels = []
        for y in range(len(splitData)):
            if( x != y):
                newTrainingInputs = np.concatenate((newTrainingInputs,splitData[y]))
                newTrainingLabels = np.concatenate((newTrainingLabels, splitLabels[y]))
        CV += naive_bayes(newTrainingInputs, splitData[x], newTrainingLabels, splitLabels[x])
                

    return (CV / 5)

def shuffle_arrays(data, labels):
    assert len(data) == len(labels)
    shuffled_data = np.empty(data.shape, dtype=data.dtype)
    shuffled_labels = np.empty(labels.shape, dtype=labels.dtype)
    permutation = np.random.permutation(len(data))
    for old_index, new_index in enumerate(permutation):
        shuffled_labels[new_index] = labels[old_index]
        shuffled_data[new_index] = data[old_index]
    return shuffled_data, shuffled_labels