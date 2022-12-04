import os
import sys
from stable_baselines3 import PPO
import pathlib
from rlgym.utils.action_parsers.discrete_act import DiscreteAction


class Agent:
    def __init__(self):
        _path = pathlib.Path('E:\Code\RLRLGym\type1_policy\rl_model_104000000_steps.zip').parent.resolve()
        custom_objects = {
            "lr_schedule": 0.00001,
            "clip_range": 0.02,
            "n_envs": 1,
            "device": "cpu"
        }

        self.actor = PPO.load('E:/Code/RLRLGym/trained_model/rl_model_99999968_steps.zip', custom_objects = custom_objects)
        self.parser = DiscreteAction()
        pass

    def get_discrete(self, index, val):
        if index < 5:
            return val - 1
        else:
            return val

    def act(self, state):
        # Evaluate your model here
        action = self.actor.predict(state, deterministic = False)
        x = self.parser.parse_actions(action[0], state)
        print(x)

        return x
