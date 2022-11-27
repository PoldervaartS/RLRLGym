from rlgym.utils.reward_functions import RewardFunction
from rlgym.utils import math
from rlgym.utils.gamestates import GameState, PlayerData
import numpy as np


class CustomReward(RewardFunction):
  def reset(self, initial_state: GameState):
    pass

  def get_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
    linear_velocity = player.car_data.linear_velocity
    reward = math.vecmag(linear_velocity)
    
    return reward
    
  def get_final_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
    return 0