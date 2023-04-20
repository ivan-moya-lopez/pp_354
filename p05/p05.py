#!/usr/bin/env python
# coding: utf-8

# # Abrimos el archivo.

# In[4]:


import pandas as pd
data = pd.read_csv('heart_data_21x12.csv', engine='python')


# # Mostramos las 5 primeras filas
# 

# In[7]:


data.head()


# # Generamos 4 Numeros aleatorios

# In[15]:



import random
aleatorios=random.sample(range(1,11),4)
# Variables predictoras
a=aleatorios[0]
b=aleatorios[1]
c=aleatorios[2]
d=aleatorios[3]
print(a,b,c,d)


# # Variables predictoras con columnas aleatorias.
# 

# In[16]:



X=data.iloc[:,[a,b,c,d]]
X.info()


# # variable a predecir

# In[31]:


Y=data.iloc[:,12]


# # Importamos las librerias para el graficar el arbol

# In[32]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


# In[23]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size = 0.8, random_state = 0)


# In[28]:


arbol = DecisionTreeClassifier(max_depth=4)


# In[29]:


arbol_diabetes = arbol.fit(X_train,Y_train)


# # Graficamos el arbol de decision.

# In[33]:


plt.figure("Arbol de decision",figsize=[12,8])
plot_tree(arbol,fontsize=10, filled=True, feature_names=list(X.columns.values),class_names = list(Y.values))
plt.show()


# In[ ]:




