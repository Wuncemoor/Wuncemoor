from scipy.cluster.vq import kmeans,vq,whiten
from numpy import vstack, array
from numpy.random import rand

#data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))

