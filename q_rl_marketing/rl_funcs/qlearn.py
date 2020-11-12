import numpy as np
import random
from q_rl_marketing.rl_funcs.tdalg import TDAlg


class QLearn(TDAlg):
    def update(self, s, a, s_, r):
        best = self.best_action(s_)
        target = r + self.gamma*self.qs[s_][best] - self.qs[s][a]
        self.qs[s][a] += self.alpha*target