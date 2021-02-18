
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[1]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[12]:

'''import matplotlib.animation as animation
x = [x1, x2, x3, x4]


axis1 = [-7.5, 2.5, 0, 0.6]
axis2 = [0, 10, 0, 0.6]
axis3 = [7, 17, 0, 0.6]
axis4 = [12, 22, 0, 0.6]
axis = [axis1, axis2, axis3, axis4]


titles = ['x1 Normal', 'x2 Gamma', 'x3 Exponential', 'Normed Frequency']


bins1 = np.arange(-7.5, 2.5, 0.2)
bins2 = np.arange(0, 10, 0.2)
bins3 = np.arange(7, 17, 0.2)
bins4 = np.arange(12, 22, 0.2)
bins = [bins1, bins2, bins3, bins4]


anno_x = [-1, 6.5, 13.5, 18.5]


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = True)
ax = [ax1, ax2, ax3, ax4]

# create the function that will do the plotting, where curr is the current frame
def update(curr):
    if curr == 100:
        a.event_source.stop()
        
# subplot with 1 row, 4 columns,for each axis
    for i in range(len(ax)):
        ax[i].cla()
        ax[i].hist(x[i][:100*curr], normed = True, bins = bins[i])
        ax[i].axis(axis[i])
        ax[i].set_title(titles[i])
        ax[i].set_ylabel('Normed Frequency')
        ax[i].set_xlabel('Value')
        ax[i].annotate('n = {}'.format(100*curr), [anno_x[i], 0.5])
    plt.tight_layout()
a = animation.FuncAnimation(fig, update, interval = 100)'''


import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


get_ipython().magic('matplotlib notebook')

n = 100
# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

    
# create the function that will do the plotting, where curr is the current frame
def update(curr):
    if curr == n: 
        a.event_source.stop()

    print (curr)
  
    # subplot with 1 row, 4 columns, and current axis is 1st subplot axes
    #plt.axis([-7, 2, 0, .6])
    plt.clf()
    ax1 = plt.subplot(2, 2, 1)
    plt.hist(x1[:curr], normed=True, bins=20, alpha=0.5)
    plt.text(x1[:curr].mean()-1.5, 0.428, 'x1 Normal')

    # subplot with 1 row, 4 columns, and current axis is 2nd subplot axes
    #plt.clf()
    plt.subplot(2, 2, 2, sharey=ax1)
    plt.hist(x2[:curr], normed=True, bins=20, alpha=0.5)
    plt.text(x2[:curr].mean()-1.5, 0.428, 'x2 Gamma')
    # subplot with 1 row, 4 columns, and current axis is 3rd subplot axes
    #plt.clf()
    plt.subplot(2, 2, 3, sharey=ax1)
    plt.hist(x3[:curr], normed=True, bins=20, alpha=0.5)
    plt.text(x3[:curr].mean()-1.5, 0.428, 'x3 Exponential')
    # subplot with 1 row, 4 columns, and current axis is 4th subplot axes
    #plt.clf()
    plt.subplot(2, 2, 4, sharey=ax1)
    plt.hist(x4[:curr], normed=True, bins=20, alpha=0.5);
    plt.text(x4[:curr].mean()-1.5, 0.428, 'x4 Uniform')
    #plt.subplots_adjust(left=None, bottom=None, right=None, top=1, wspace=None, hspace=None)

    #plt.axis([-7,21,0,0.6])

# plot the histograms
fig = plt.figure(figsize=(9,5))
#plt.subplots_adjust(left=0.25, bottom=0.25)
#fig = plt.figure()
a = animation.FuncAnimation(fig, update, interval=10)

