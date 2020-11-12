import numpy as np
import random
from collections import defaultdict
from q_rl_marketing.config import *


def choose_action():
    return random.choice(marketing_options)


def make_dict():
    return {a: 0 for a in marketing_options}


class TDAlg:
    def __init__(self, actions, qs=None, policy=None, eps=.05, gamma=1, alpha=1, max_time=None):
        self.actions = actions
        if qs is None:
            self.qs = defaultdict(make_dict)
        else:
            self.qs = qs
        if policy is None:
            self.policy = defaultdict(choose_action)
        else:
            self.policy = policy
        self.eps = eps
        self.gamma = gamma
        self.alpha = alpha
        self.max_time = max_time
        self.state = None
        self.ep = 0
        self.time = 0
        self.ep_log = []
        self.r_log = []

    def get_action(self, state, m_choices=None):
        if m_choices is None:
            m_choices = self.actions
        if random.random() < self.eps:
            choice = random.choice(m_choices)
        else:
            choice = self.best_action(state, m_choices)
        return choice

    def best_action(self, state, m_choices=None):
        if m_choices is None:
            m_choices = self.actions
        max_choice = max([self.qs[state][a] for a in m_choices])
        choices = [a for a in m_choices if self.qs[state][a] == max_choice]
        best_action = random.choice(choices)
        return best_action

    def update_policy(self):
        for state in self.policy:
            self.policy[state] = self.best_action(state)

    def run_episode(self):
        if (self.max_time is not None and self.time <= self.max_time) or self.max_time is None:
            old_count = self.time
            cum_reward = self.update()
            self.ep_log.extend([self.ep for _ in range(self.time - old_count)])
            self.ep += 1
            if len(self.r_log) > 0:
                self.r_log.append(self.r_log[-1] + cum_reward)
            else:
                self.r_log.append(cum_reward)
        else:
            pass
