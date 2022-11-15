import rlgym
from stable_baselines3 import PPO

#Make the default rlgym environment
env = rlgym.make()

#Initialize PPO from stable_baselines3
model = PPO("MlpPolicy", env=env, verbose=1)

#Train our agent!
model.learn(total_timesteps=int(1e6))