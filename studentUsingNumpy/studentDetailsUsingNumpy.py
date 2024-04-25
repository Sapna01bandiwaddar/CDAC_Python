import matplotlib.pyplot as plt
import numpy as np
sub=np.array(["maths","science","history","english","art"]) score=np.array([85,70,75,90,80])
colour=(['red','blue','pink','black','orange'])
plt.bar(sub,score)
plt.title("Students Performance") plt.ylabel("score")
plt.xlabel("Subject")
plt.grid(c='gray',lw=1,ls='--')
plt.bar(sub,score,color=colour) 
plt.show()
