from self_driving_car import game
import numpy as np
from neural_network import neural_network

NUM_SENSORS = 3


def play(model):
    game_demo = game.Game()
    _,state = game_demo.frame_step((2)) #action is taken as 2
    status = 1
    # while game still in progress
    while status == 1:
        qval = model.predict(state.reshape(1, 64), batch_size=1)
        action = (np.argmax(qval))  # take action with highest Q-value
        _,state = game_demo.frame_step(action)
        # x, y = game_demo.car_body.position
        # reward = game.Game.get_sonar_readings(x, y, game.Game.car_body.angle)



if __name__ == "__main__":
    saved_model = 'saved-models/164-150-100-50000-250.h5'
    model = neural_network(NUM_SENSORS, [164, 150], saved_model)
    play(model)