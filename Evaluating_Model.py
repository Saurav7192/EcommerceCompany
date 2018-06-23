import ML_Modeling as ML_M
import Data_Reading as DR
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
import seaborn as sns



#plotting pedicted vs real output
plt.scatter(ML_M.Y_test,ML_M.predicted_Y_test , color = "blue", label = 'data')
plt.show()

#converting into array for further calculation
Y_test = np.array(ML_M.Y_test)
Y_train = np.array(ML_M.Y_train)
predicted_Y_test = np.array(ML_M.predicted_Y_test)

#Evaluating model
print('MAE:', metrics.mean_absolute_error(Y_test,predicted_Y_test))
print('MSE:', metrics.mean_squared_error(Y_test, predicted_Y_test))
print('RMSE:', np.sqrt(metrics.mean_squared_error(Y_test, predicted_Y_test)))

sns.distplot((Y_test-predicted_Y_test),bins=50);
plt.show()
