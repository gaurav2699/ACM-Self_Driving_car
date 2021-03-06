import numpy as np
from neural_network import neural_network
from self_driving_car import game
import random

NUM_INPUT = 3
gamma = 0.9



def deep_q_train(model, params):
    epsilon = 1
    batch_size = params["batchSize"]
    buffer = params["buffer"]
    nn_params = params["nn"]
    t = 0
    game_state = game.Game()

    observe = 500  # number of frames it is going to observe
    training_frames = 1000  # number of frames it is going to play
    # will need to increase these frames for better result
    replay = []
    max_car_distance = 0
    car_distance = 0
    _,state = game_state.frame_step((2))
    # first observe then train
    while t < training_frames:
        print(t)
        t += 1
        #reset weights of neural network
        # model.compile(loss='mse', optimizer=rms)  
        car_distance+=1
         #initial state of the car 
        
        
        #All possible actions from that state
        qval = model.predict(state, batch_size=1)

        if (random.random() < epsilon):
            action = np.random.randint(0,3) 
         #take random action choice: 0 - up, 1 - down, 2 - left, 3 - right
        else:
            #Take maximum value of the Q values
            action = (np.argmax(qval))

        #Take action, observe new state S' and record it
        reward, new_state = game_state.frame_step(action)

        #Experience replay storage
        if (len(replay) < buffer): 
           replay.append((state, action, reward, new_state))
        else: #if buffer full, overwrite old values
            replay.pop(0)
            replay.append((state, action, reward, new_state))

#Initially, we want the car to take random actions to familiarize itself with the environment 
#We use the neural network only after a certain number of frames, in this case "observe" number of frames
#Decrement epsilon only after "observe" number of frames to eventually take the help of neural network
        if (t > observe):
            decrement = 1/training_frames
            if epsilon > 0.1: #We set the lower cap for epsilon as 0.1
                epsilon -= decrement
            minibatch = random.sample(replay, batch_size)
            X_train, y_train = minibatch_process(model, minibatch)
            model.fit(X_train, y_train, batch_size=batch_size, epochs=1, verbose=1)
    state = new_state
    if reward==-500:
        print(car_distance)
        if car_distance > max_car_distance:
            max_car_distance = car_distance
        if t % 250 == 0:
            model.save_weights('saved-models/' + filename + '-' +
                               str(t) + '.h5',
                               overwrite=True)
            print(("Saving model %s - %d" % (filename, t)))
    # train the game using the finding of the observation, update the weights, and keep observing

def minibatch_process(model, minibatch):
    X_train = []  # state s of each memory
    y_train = []  # updates target values from minibatch
    for memory in minibatch:
        # Get max_Q(S',a)
        old_state, action, reward, new_state = memory
        old_qval = model.predict(old_state.reshape(1, NUM_INPUT), batch_size=1)
        newQ = model.predict(new_state.reshape(1, NUM_INPUT), batch_size=1)
        maxQ = np.max(newQ)
        y = np.zeros((1, 3))
        y[:] = old_qval[:]
        if reward == -500:  # non-terminal state
            update = (reward + (gamma * maxQ))
        else:  # terminal state
            update = reward
        y[0][action] = update
        X_train.append(old_state.reshape(NUM_INPUT, ))
        y_train.append(y.reshape(3, ))

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    
    return X_train,y_train


if __name__ == "__main__":
    nn_param = [164, 150]
    params = {
        "batchSize": 100,
        "buffer": 500,
        "nn": nn_param
    }

    model = neural_network(NUM_INPUT, nn_param)
    deep_q_train(model, params)
   # minibatch_process(model,minibatch,params)
