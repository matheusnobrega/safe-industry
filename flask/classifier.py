import math
import numpy as np
from config import *

def dist(attr1, attr2):
  distance = 0
  for i in range(len(attr1)):
    distance += (float(attr1[i]) - float(attr2[i]))**2
  return math.sqrt(distance)

def knn(k, training_data, training_label, new_data):
  distances = [dist(training_point, new_data) for training_point in training_data]
  distances = np.array(distances, dtype=np.float32)

  nearest_neighbor_ids = distances.argsort()[:k]
  training_label = np.array(training_label)
  nearest_neighbor_rings = training_label[nearest_neighbor_ids].tolist()

  return max(set(nearest_neighbor_rings), key = nearest_neighbor_rings.count)


