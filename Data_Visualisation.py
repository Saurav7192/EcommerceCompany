import Data_Reading as DR
import seaborn as sns
import matplotlib.pyplot as plt

#Relation b/w attributes
sns.swarmplot(x='Time on Website', y='Yearly Amount Spent',data = DR.data)
plt.show()

#
sns.swarmplot(x='Time on App', y='Yearly Amount Spent',data = DR.data)
plt.show()

#
sns.jointplot("Time on App", "Length of Membership", data=DR.data, kind="hex")
plt.show()

#
sns.lmplot("Length of Membership", "Yearly Amount Spent", data=DR.data)
plt.show()

#Relation b/w all atribute
sns.pairplot(DR.data)
plt.show()
