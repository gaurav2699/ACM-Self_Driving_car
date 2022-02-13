from neural_network import  neural_network
from self_driving_car import game
NUM_INPUT = 3

def deep_q_train(model, params):
    batch_size = params["batchSize"]
    buffer = params["buffer"]
    nn_params = params["nn"]
    t = 0

    game_state = game.Game()

    observe = 500 # number of frames it is going to observe 
    training_frames=1000 # number of frames it is going to play 
    # will need to increase these frames for better result

    
    #first observe then train
    while t<training_frames:
        t+=1
        # do something
        if(t>observe):
            # train

if __name__ == "__main__":
    nn_param = [164, 150]
    params = {
        "batchSize": 100,
        "buffer": 50000,
        "nn": nn_param
    }
    model = neural_network(NUM_INPUT, nn_param)
    deep_q_train(model, params)