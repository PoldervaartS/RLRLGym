from rlgym.utils.gamestates import GameState, PlayerData
from rlgym.utils.reward_functions import RewardFunction
from rlgym.utils.reward_functions.combined_reward import CombinedReward
import numpy as np
from typing import Tuple

class myCustomRewards(RewardFunction):

    def __init__(self, rewardType, reward_functions: Tuple[RewardFunction, ...], REWARDINCREASESTEP = 10000000, gamma = 0.9):
        super().__init__()
        # reward functions should be passed in order from simplest to most complex
        # rewardType 0 means all, 1 means build up, 2 means just the current value?
        self.rewardType = rewardType
        self.rewardUseCounter = 0
        self.REWARDINCREASESTEP = REWARDINCREASESTEP # 10 million
        self.reward_functions = reward_functions
        self.gamma = 0.9
        print(self.reward_functions)
        if rewardType == 0:
            self.currentRewardToUse = CombinedReward(reward_functions)
        else:
            print((reward_functions[0]))
            self.currentRewardToUse = CombinedReward([reward_functions[0]])
        print("Current Rewards: ", self.currentRewardToUse)

    def incrementRewardIndexUsed(self):
        """
        Redefine the base combined reward if type 1 to now include the other. Type 2 to only be the new values. 
        
        """
        # capped for array out of bounds
        rewardIndex = min(len(self.reward_functions) - 1, self.rewardUseCounter // self.REWARDINCREASESTEP)
        
        if self.rewardType == 1:
            # reward importance gradually descent
            self.currentRewardToUse = CombinedReward(self.reward_functions[0: rewardIndex + 1], [self.gamma**x for x in range(rewardIndex, -1, -1)])
        elif self.rewardType == 2:
            self.currentRewardToUse = CombinedReward(self.reward_functions[rewardIndex])
        print("Current Rewards: ", self.currentRewardToUse)



    def reset(self, initial_state: GameState):
        """
        Function to be called each time the environment is reset. This is meant to enable users to design stateful reward
        functions that maintain information about the game throughout an episode to determine a reward.

        :param initial_state: The initial state of the reset environment.
        """
        self.currentRewardToUse.reset(initial_state)

    def get_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        """
        Function to compute the reward for a player. This function is given a player argument, and it is expected that
        the reward returned by this function will be for that player.

        :param player: Player to compute the reward for.
        :param state: The current state of the game.
        :param previous_action: The action taken at the previous environment step.

        :return: A reward for the player provided.
        """
        self.rewardUseCounter += 1
        if self.rewardUseCounter > 0 and self.rewardUseCounter % self.REWARDINCREASESTEP == 0:
            self.incrementRewardIndexUsed()
        return self.currentRewardToUse.get_reward(player, state, previous_action)

    def get_final_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        """
        Function to compute the reward for a player at the final step of an episode. This will be called only once, when
        it is determined that the current state is a terminal one. This may be useful for sparse reward signals that only
        produce a value at the final step of an environment. By default, the regular get_reward is used.

        :param player: Player to compute the reward for.
        :param state: The current state of the game.
        :param previous_action: The action taken at the previous environment step.

        :return: A reward for the player provided.
        """

        print(f'Rewards Count: {self.rewardUseCounter}') 
        return self.currentRewardToUse.get_final_reward(player, state, previous_action)
