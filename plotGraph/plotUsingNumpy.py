import matplotlib.pyplot as plt
import numpy as np
time_hours=np.array([1,2,3,4,5])
study_score=np.array([50,60,70,80,90])
plt.plot(time_hours,study_score,color='b',ls='-')
#plt.plot(time_hours,study_score,color='r',marker='o')
plt.scatter(time_hours,study_score,color='r',marker='o') 
plt.show()
