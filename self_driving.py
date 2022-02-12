# %%
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import RMSprop

# %%
model = Sequential()
model.add(Dense(150, input_dim=784, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='linear'))
rms = RMSprop()
model.compile(loss='mse', optimizer=rms)

# %%
model.summary