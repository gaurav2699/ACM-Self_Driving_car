import numpy as np
from neural_network import neural_network
from self_driving_car import game
import random

NUM_INPUT = 3
episilon = 1
gamma = 0.9



def deep_q_train(model, params):
    batch_size = params["batchSize"]
    buffer = params["buffer"]
    nn_params = params["nn"]
    t = 0
    game_state = game.Game()

    observe = 500  # number of frames it is going to observe
    training_frames = 1000  # number of frames it is going to play
    # will need to increase these frames for better result
    replay = []
    # first observe then train
    while t < training_frames:
        t += 1
        # let the game play for a while to learn about the environmnent
        if (t > observe):
            print("Game #: %s" % (model.i,))
            minibatch = random.sample(replay, batch_size)
            X_train, y_train = minibatch_process(model, minibatch)
            model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=1, verbose=1)
    #state = new_state
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