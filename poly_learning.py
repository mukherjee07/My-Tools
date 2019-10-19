
'''
Author: Krishnendu Mukherjee
Affiliation: The State University of New York at Buffalo
Objective: To test different Machine Learning models like ANN, Random Forest, Polynomial, SVR etc. to obtain a single model which will map 
geometry of a system to its -----> single point energy [ i.e. we want to by-pass the physics behind it ]
for this we have training data for 100 conformers for each combination of NTCDA + 'n' Li/Li+ where 'n' ---> [1,24]
and each conformer has on an average 100 geometric optimisation cycles. So 100 * 100 = 10k data points for each combination of NTCDA + 'n'
we expect to reduce the total time for calculation by atleast 75%, and the remaining 25% would consist of --> (20% time for computational chemistry
i.e. DFT modeling and the rest 5% for machine-learning)

Input variable: The geometry of Li atoms in x, y and z coordinates (standard cartesian coordinates)
output variable: Single Point Energy in hartree
'''
# calling all the essential libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def PL(n):
	#importing the dataset
	#n = 3 ### This corresponds to number of Li atoms
	lim1 = 2
	lim2 = (2 + (3*n))
	lim3 = (3 + (3*n))
	dataset = pd.read_csv('trj_mapper'+ str(n) +'.csv', delimiter=',')

	# The independent variables

	x = dataset.iloc[:, lim1:lim2].values # x has all the coordinates
	#y = dataset.iloc[:, 3].values
	#z = dataset.iloc[:, 4].values

	# the dependent variables      # This has energy
	e = dataset.iloc[:, lim2:lim3].values
	#print (x),(e)

	# Splitting the data into training set and test set
	from sklearn.model_selection import train_test_split 
	x_train, x_test, y_train, y_test = train_test_split(x, e, test_size = 0.20, random_state = 0)
	# print (x_train)

	# Feature scaling
	from sklearn.preprocessing import StandardScaler
	sc_x = StandardScaler()
	x_train = sc_x.fit_transform(x_train)
	x_test = sc_x.fit_transform(x_test)

	sc_y = StandardScaler()
	y_train = sc_y.fit_transform(y_train)
	y_test = sc_y.fit_transform(y_test)

	# Now our training and test set are ready and scaled, now we can go ahead with the machine learning phase
	'''
	# Fitting Linear model to our dataset
	'''
	from sklearn.linear_model import LinearRegression
	lin_reg = LinearRegression()
	model = lin_reg.fit(x_train,y_train)
	#print (lin_reg.predict(x_test))
	# Predicting the score from Linear Regression
	print ("Score for Linear Regression with "),n,(" Li's is "), (model.score(x_test,y_test))
	#print (model.summary())

	from sklearn.preprocessing import PolynomialFeatures
	poly_reg = PolynomialFeatures(degree = 3)
	x_poly = poly_reg.fit_transform(x_train)
	lin_reg2 = LinearRegression()
	model2 = lin_reg2.fit(x_poly,y_train)
	x_test = poly_reg.fit_transform(x_test)

	# Fitting Support vector Regression to the dataset
	'''from sklearn.svm import SVR
	sv_reg = SVR(kernel = 'rbf')
	model3 = sv_reg.fit(x_train, y_train)
	'''
	# 
	print ("Score for Polynomial Regression with "),n,(" Li's is "), (model2.score(x_test,y_test))
	'''print ("Score for Support Vector Regression:"), (model3.score(x_test,y_test))
	print (sv_reg.predict(x_test))
	#Fitting Random Forest regression
	#print (X)
	'''

for i in range(6,10,1):
	PL(i+1)

