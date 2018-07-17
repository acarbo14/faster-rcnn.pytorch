import numpy as np
import pickle

with open('output_test/meanAP.pkl','rb') as val_accuracy:
	val_accuracy = pickle.load(val_accuracy)

m=max(val_accuracy)
epoch = [i for i,j in enumerate(val_accuracy) if j == m]
print(m)
print(epoch)