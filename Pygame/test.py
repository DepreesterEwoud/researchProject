import GameEnv
import pygame
import numpy as np
from ddqn_keras import DQAgent
from collections import deque
import random, math

TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 10000
REPLACE_TARGET = 50 

game = GameEnv.RacingEnv()
state = game.reset()
REPLAY_MEMORY_CAPACITY = 20000

agent = DQAgent(replayCapacity=REPLAY_MEMORY_CAPACITY, outputShape=8)



def run():
    # reset the parameters
    DISCOUNT = 0.90
    BATCH_SIZE = 256  # How many steps (samples) to use for training
    UPDATE_TARGET_INTERVAL = 500
    EPSILON = 0.99 # Exploration percentage
    MIN_EPSILON = 0.01
    DECAY = 0.9999
    EPISODE_AMOUNT = 200

    updateCounter = 0
    rewardHistory = []
    epsilonHistory = []
    for e in range(EPISODE_AMOUNT):
        #print("Resetten")
        episodeReward = 0
        stepCounter = 0  # count the number of successful steps within the episode
        state = game.reset() #reset env 

        #print(state.shape)
        done = False
        epsilonHistory.append(EPSILON)

        while not done:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return

            if random.random() <= EPSILON:
                action = random.randint(0,8)
                #print(action)
            else:
                print("polleke")
                #state_addapted = generate_state_frame_stack_from_queue(state)
                print(type(state))
                state = np.asarray(state)
                state = state.reshape(1,-1)
                print(state)
                print(state.shape)
                qValues = agent.policy_network_predict(state)
                action = np.argmax(qValues[0])
                print(action)
                

            newState, reward, done = game.step(action)
            #print(newState, reward, done)
            stepCounter +=1

            # store step in replay memory
            step = (state, action, reward, newState, done)
            agent.addToReplayMemory(step)
            state = newState
            #print(state)
            episodeReward += reward
            # When enough steps in replay memory -> train policy network
            if len(agent.memory) >= (BATCH_SIZE):
                EPSILON = DECAY * EPSILON
                if EPSILON < MIN_EPSILON:
                    EPSILON = MIN_EPSILON
                # sample minibatch from replay memory
                print("memory > batch")
                miniBatch = agent.sampleFromReplayMemory(BATCH_SIZE)
                """ miniBatch_states = np.array(list(zip(*miniBatch))[0], dtype=object)
                print(len(miniBatch_states))
                for i in 256:
                    #print(miniBatch_states[i])
                    miniBatch_states[i] = np.asarray(miniBatch_states[i])
                #print(np.array(miniBatch_states))
                print(miniBatch_states)
                print(type(miniBatch_states))
                print(type(miniBatch_states[0]))
                miniBatch_actions = np.array(list(zip(*miniBatch))[1], dtype = int)
                miniBatch_rewards = np.array(list(zip(*miniBatch))[2], dtype = float)
                miniBatch_next_state = np.array(list(zip(*miniBatch))[3], dtype =object)
                miniBatch_done = np.array(list(zip(*miniBatch))[4],dtype=bool) """
                miniBatch_states = []
                miniBatch_next_state = []
                y = []
                """ miniBatch_states = np.asarray([np.asarray(i[0]).astype(float) for i in miniBatch],dtype=object)
                print(miniBatch_states)
                miniBatch_actions = np.array([i[1] for i in miniBatch])
                #print(len(miniBatch_actions))
                miniBatch_rewards = np.array([i[2] for i in miniBatch])
                miniBatch_next_state = np.asarray([np.asarray(i[3]) for i in miniBatch])
                miniBatch_done = np.array([i[4] for i in miniBatch]) """
                NoneType = type(None)
                for i in miniBatch:
                    if type(i[0]) == NoneType:
                        state = np.asarray([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]).astype(np.float)
                    else: state = np.asarray(i[0]).astype(np.float)
                    state = state.reshape(1,-1)
                    miniBatch_states.append(state)
                    state_state = agent.policy_network_predict_from_batch(state)
                    y.append(state_state)
                    #miniBatch_states.append(state)

                    #print(i[3])
                    if type(i[3]) == NoneType:
                        next_state = np.asarray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
                    else: next_state = np.asarray(i[3])
                    next_state = next_state.reshape(1,-1)
                    next_state = agent.target_network_predict(next_state)
                    miniBatch_next_state.append(next_state)
                
                #y = agent.policy_network_predict_from_batch(miniBatch_states)
                print(y.shape)
                #next_state_q_values = agent.target_network_predict(miniBatch_next_state)
                max_q_next_state = np.max(miniBatch_next_state,axis=1)

                for i in range(BATCH_SIZE):
                    if miniBatch_done[i]:
                        #print("done")
                        y[i] = miniBatch_rewards[i]
                    else:
                        y[i] = miniBatch_rewards[i] + DISCOUNT *  max_q_next_state[i]
                        #y[i] = y[i].tolist()
                        #y[i] = np.asarray(y[i])
                        #y[i] = np.argmax(y[i])
                        #y[i] = y[i].astype(np.int32)
                    
                        
                        #y[i,miniBatch_actions[i]] = miniBatch_rewards[i] + DISCOUNT *  max_q_next_state[i]
                y = np.asarray(y)
                print(type(y))
                #print(y)
                #print(miniBatch_states)
                print(type(miniBatch_states))
                agent.policy_model.fit(miniBatch_states, y, batch_size=BATCH_SIZE, verbose = 0)
            else:
                continue
            if updateCounter == UPDATE_TARGET_INTERVAL:
                agent.update_target_network()
                updateCounter = 0
            updateCounter += 1
        print('episodeReward for episode ', e, '= ', episodeReward, 'with epsilon = ', EPSILON)
        #env.render()
        rewardHistory.append(episodeReward)

run()        
