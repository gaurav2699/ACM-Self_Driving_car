from neural_network import  neural_network
from self_driving_car import game
NUM_INPUT = 3

def deep_q_train(model, params):
    batch_size = params["batchSize"]
    buffer = params["buffer"]
    nn_params = params["nn"]
    t = 0
    episilon = 1
    gamma = 0.9
    game_state = game.Game()

    observe = 500 # number of frames it is going to observe 
    training_frames=1000 # number of frames it is going to play 
    # will need to increase these frames for better result

    
    #first observe then train
    while t<training_frames:
        t+=1
        # let the game play for a while to learn about the environmnent
        if(t>observe):
            # train the game using the finding of the observation, update the weights, and keep observing

if __name__ == "__main__":
    nn_param = [164, 150]
    params = {
        "batchSize": 100,
        "buffer": 500,
        "nn": nn_param
    }


    model = neural_network(NUM_INPUT, nn_param)
    deep_q_train(model, params)