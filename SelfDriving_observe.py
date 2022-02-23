t=0
gamma = 0.9
epsilon = 1
replay = []
#stores tuples of (State, Action, Reward, Next State)
h = 0
observe = 500  # number of frames it is going to observe
training_frames = 1000  # number of frames it is going to play
# will need to increase these frames for better result

# first observe, then train
while t < training_frames:
  t += 1
  #reset weights of neural network
  model.compile(loss='mse', optimizer=rms)  

  _,state = game_state.frame_step((2))
  #initial state of the car       
        
        
  #All possible actions from that state
  qval = model.predict(state.reshape(1,num_sensors), batch_size=1)

  if (random.random() < epsilon):
    action = np.random.randint(0,4) 
    #take random action choice: 0 - up, 1 - down, 2 - left, 3 - right
  else:
    #Take maximum value of the Q values
    action = (np.argmax(qval))



#Take action, observe new state S' and record it
  reward, new_state = game_state.frame_step(state, action)

  #Experience replay storage
  if (len(replay) < buffer): 
    replay.append((state, action, reward, new_state))
  else: #if buffer full, overwrite old values
    if (h < (buffer-1)):
        h += 1
    else:
        h = 0
#Initially, we want the car to take random actions to familiarize itself with the environment 
#We use the neural network only after a certain number of frames, in this case "observe" number of frames
#Decrement epsilon only after "observe" number of frames to eventually take the help of neural network
  if (t > observe):
    decrement = 1/train_frames
    if epsilon > 0.1: #We set the lower cap for epsilon as 0.1
      epsilon -= decrement