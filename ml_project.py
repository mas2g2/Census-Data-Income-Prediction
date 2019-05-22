import numpy as np
import csv
# function loads data from *.csv file to array
def load_data(filename):
    other_data = []
    with open(filename,"r") as f:
        other_data = list(csv.reader(f))
    other_data = np.array(other_data)
    for row in other_data:
        for item in row:
            if item.isdigit():
                item = float(item)
            else:
                pass
    return other_data
# Calculating Gini index
data = load_data("adult_data.csv")

half = int(len(data)/2)

first_half = data[:half,:]

second_half = data[half:,:]

# Calculate the Gini index for a split dataset
def gini_index(groups,classes):
    # Count all samples at split point
    n = float(sum([len(group) for group in groups]))
    # sum gini weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val)/size
            score += p*p
        # weight the group score by its relative size
        gini += (1.0 - score) * (size/n)
    return gini

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Select the best split point for a dataset
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_values, b_score, b_groups = 999, 999, 999, None
    for index in range(len(dataset) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
            print("{'index':",b_index,", 'value':",b_value,", 'groups':",b_groups,"}")
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

groups = [first_half,second_half]
classes = [" >50K"," <=50K"]
gini = gini_index(groups,classes)
print("Gini score: ",gini)
print("Split : ",get_split(data))
