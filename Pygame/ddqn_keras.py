import gym
import random
import numpy as np
import matplotlib.pyplot as plt
import collections

# Import Tensorflow libraries

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import cv2

from tensorflow.keras.models import load_model


from IPython.display import HTML
from IPython.display import clear_output

# disable eager execution (optimization)
#from tensorflow.python.framework.ops import disable_eager_execution
#disable_eager_execution()

class DQAgent:
    def __init__(self, replayCapacity, outputShape):
        ## Initialize replay memory
        self.capacity = replayCapacity
        self.memory = collections.deque(maxlen=100000)
        self.populated = False
        ## Policiy model
        self.outputShape = outputShape
        self.policy_model = self.buildNetwork()

        ## Target model
        self.target_model = self.buildNetwork()
        #self.target_model.set_weights(self.policy_model.get_weights())

    def addToReplayMemory(self, step):
        self.step = step
        self.memory.append(self.step)

    def sampleFromReplayMemory(self, batchSize):
        self.batchSize = batchSize
        if self.batchSize > len(self.memory):
            self.populated = False
            return self.populated
        else:
            return random.sample(self.memory, self.batchSize)


    def buildNetwork(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(256, activation=tf.nn.relu)) #prev 256 
        model.add(tf.keras.layers.Dense(self.outputShape, activation=tf.nn.softmax))
        model.compile(loss = "mse", optimizer="adam")
        return model

    def policy_network_fit(self,batch, batchSize):
        self.batchSize = batchSize
        self.batch = batch


    def policy_network_predict(self, state):
        self.state = state
        #print(self.state)
        self.qPolicy = self.policy_model.predict(self.state)
        return self.qPolicy
    def policy_network_predict_from_batch(self, state):
        self.state = state
        #print(self.state)
        self.qPolicy = self.policy_model.predict(self.state)
        return self.qPolicy
    
    def policy_network_predictnieuw(self, state):
        self.state = state
        #self.state = state.reshape(1,96,96,3)
        #self.state = np.expand_dims(state,axis=0)
        #print("Policy network shape = ",self.state.shape)
        #self.qPolicy = np.expand_dims(self.state,axis=0)
        self.qPolicy = self.policy_model.predict(np.expand_dims(self.state,axis=0))
        return self.qPolicy

    def target_network_predict(self, state):
        self.state = state
        self.qTarget = self.target_model.predict(self.state)
        return self.qTarget

    def update_target_network(self):
        self.target_model.set_weights(self.policy_model.get_weights())
    