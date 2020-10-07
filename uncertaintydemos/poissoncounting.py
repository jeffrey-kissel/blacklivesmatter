# monte carlo demo
import numpy as np
import matplotlib.pyplot as plt

cm = plt.get_cmap('gist_rainbow')
cmblack = plt.get_cmap('ocean')

ndatapoints = np.array([10, 100, 1000,10000, 100000, 1000000])
ndists = len(ndatapoints)

alls = []
allupper = []
alllower = []

for iCount, thisCount in enumerate(ndatapoints):
    thiss = np.random.poisson(10., size=thisCount)
    thislower = np.percentile(thiss, 16.0, axis=0)
    thisupper = np.percentile(thiss, 84.0, axis=0)
    
    alls.append(thiss)
    alllower.append(thislower)
    allupper.append(thisupper)

plt.figure()
for n in range(0,ndists):
    count, bins, ignored = plt.hist(alls[n], range(20), normed=True, alpha=0.5, color=cm(n/ndists),label='Count = {}, Unc = 10 +{:.3f}/-{:.3f}'.format(ndatapoints[n], allupper[n],alllower[n]))
    plt.axvline(allupper[n],ls='--',color=cmblack(n/ndists))
    plt.axvline(alllower[n],ls='--',color=cmblack(n/ndists))
plt.title("Poisson distribution with mean of 10")
plt.legend()
plt.show()
