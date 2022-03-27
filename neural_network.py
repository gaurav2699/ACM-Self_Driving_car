
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import RMSprop

def neural_network(num_sensors, params, load=False):
    model = Sequential()
    model.add(Dense(params[0], input_shape=(num_sensors,), activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(params[1], activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(3, activation='linear'))
    rms = RMSprop()
    model.compile(loss='mse', optimizer=rms)
    if load:
        model.load_weights(load)
    return model

