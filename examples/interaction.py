import rlgym

env = rlgym.make()

while True:
    obs = env.reset()
    done = False

    while not done:
      #Here we sample a random action. If you have an agent, you would get an action from it here.
      action = env.action_space.sample() 
      
      next_obs, reward, done, gameinfo = env.step(action)
      
      obs = next_obs

      print(action)
    


