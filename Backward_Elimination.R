if (FALSE) {
#Backward Elimination 
#Author: Krishnendu Mukherjee
#Affiliation: University of Buffalo, The State University of New York
#Objective: To create a ML model which can identify the statistically significant dependent variable 
#for dependent variable to be: Single Point Energy
#Indepedent variables: X,Y and Z coordinates of independent Li coordinates.
}
### Importing the dataset ###
dataset = read.csv('trj_mapper2.csv', sep = ',')
## Splitting the dataset into training and test
library(caTools)
set.seed(123)
split = sample.split(dataset$Energy, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE )
test_set = subset(dataset, split == FALSE )
## Feature Scaling
#training_set = scale(training_set)
#test_set = scale(test_set)
## Fitting multiple linear regression to the training set 
regressor = lm(formula = Energy ~ ., data = training_set)
### Predicting the test set results
y_pred = predict(regressor, newdata = test_set )
## Building the optimal model using backward elimination
regressor = lm(formula = Energy ~ X1 + Z1 + Y2 + Z2, data = dataset )
summary(regressor)

