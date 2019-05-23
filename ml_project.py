import numpy as np
import csv
from random import seed, randrange
from math import sqrt


# function loads data from *.csv file to array
def load_data(filename):
    dataset = list()
    with open(filename,"r") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            dataset.append(row)
    return dataset
# This function splits the dataset into k folds
# Here our dataset is partitioned into k equalsized subsamples
# Of the k subsamples, a single subsample is retained as the validation data
# for testing the model , and the remaining k - 1 subsamples are used as training
# data. 
def k_fold_cross_validation(dataset, k_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_shape = int(len(dataset)/k_folds)
    for i in range(k_folds):
        fold = list()
        while len(fold) < fold_shape:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

# Split dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    # init 2 empty lists for storing split datasubsets
    left, right = list(), list()
    # for every row
    for row in dataset:
        # if the value at that row is less than the given value
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Calculate accuracy percentage
def score(actual, predicted):
    # how many correct predictions?
    correct = 0
    # for each actual label
    for i in range(len(actual)):
        # if actual matches predicted label
        if actual[i] == predicted[i]:
            correct += 1
    return correct/float(len(actual)) * 100.0

# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset,algorithm, k_folds, *args):
    folds = k_fold_cross_validation(dataset,k_folds)
    scores = list()

    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set,[])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = score(actual,predicted)
        scores.append(accuracy)
    return scores

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

# Select the best split point for a dataset
# Exhaustive greedy algorithm
def get_split(dataset, n_features):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    features = list()
    while len(features) < n_features:
        index = randrange(len(dataset[0]) - 1)
        if index not in features:
            features.append(index)
    for index in features:
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_scores:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
    return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

def split(node, max_depth, min_size, n_features, depth):
    left, right = node['groups']
    del(node['groups'])
    if not left or not right: 
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left, n_features)
        split(node['left'], max_depth, min_size,n_features, depth+1)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right, n_features)
        split(node['right'], max_depth, min_size, n_features, depth+1)

# Build a decision tree
def build_tree(train, max_depth, min_size, n_features):
    root = get_split(train, n_features)
    split(root, max_depth, min_size, n_features, 1)
    return root

# Make a prediction
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'],dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'],dict):
            return predict(node['right'], row)
        else:
            return node['right']

# Create a random subsample from the dataset with replacement
def subsample(dataset, ratio):
    sample = list()
    n_sample = round(len(dataset)*ratio)
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample

# Make a prediction with a list of bagged trees
def bagging_predict(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predictions), key=predictions.count)

# Random Forest Algorithm
def random_forest(train, test, max_depth, min_size, sample_size, n_trees, n_features):
    trees = list()
    for i in range(n_trees):
        sample = subsample(train, sample_size)
        tree = build_tree(sample, max_depth, min_size, n_features)
        trees.append(tree)
    predictions = [bagging_predict(trees, row) for row in test]
    return (predictions)

seed(1)
data = load_data("adult_data.csv")
n_folds = 5
max_depth = 10
min_size = 1
samples_size = 1.0
n_features = int(sqrt(len(data) - 1))
for n_trees in [1,5,10]:
    scores = evaluate_algorithm(data, random_forest, n_folds, max_depth, min_size, samples_size, n_trees, n_features)
    print('Trees: %d' % n_trees)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
