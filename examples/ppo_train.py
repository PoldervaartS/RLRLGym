# import the gym and stable baselines 3 libraries
import rlgym
from stable_baselines3.ppo import PPO
from rlgym_tools.sb3_utils import SB3SingleInstanceEnv

# setup the RLGym environment
gym_env = rlgym.make(use_injector=True, self_play=True)

# wrap the RLGym environment with the single instance wrapper
env = SB3SingleInstanceEnv(gym_env)

# create a PPO instance and start learning
learner = PPO(policy="MlpPolicy", env=env, verbose=1)
learner.learn(1_000_000)