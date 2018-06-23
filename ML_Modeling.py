import Data_Reading as DR
from sklearn.model_selection import train_test_split
from sklearn import linear_model

#indexing and droping useless attribute
X = DR.data.ix[:,3:7]
#print(X)

Y = DR.data.ix[:,7:]
#print(Y)


#Splitting dataset into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=101)


# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, Y_train)

# regression coefficients
print('Coefficients: \n', reg.coef_)

#prediction on test data
predicted_Y_test = reg.predict(X_test)

