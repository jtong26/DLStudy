import numpy as np
import random

# Multi-armed Bandit game simulation
class MAB:

    def __init__(self, n, rewards, probs, flag):
        self.n = n
        self.probs = probs
        self.rewards = rewards
        self.flag = flag

    def choose_one_greedy(self):
        explore = random.random()
        if explore < 0.01:
            return np.random.randint(0, 10)
        rewards_mean = [np.mean(i) for i in self.rewards]
        return np.argmax(rewards_mean)
    
    def choose_one_improv_greedy(self):
        explore = random.random()
        total_play = sum(len(i) for i in self.rewards)
        if explore < 1/total_play:
            return np.random.randint(0, 10)
        rewards_mean = [np.mean(i) for i in self.rewards]
        return np.argmax(rewards_mean)

    def try_and_play(self):
        if self.flag == "greedy":
            choice = self.choose_one_greedy()
        elif self.flag == "improv_greedy":
            choice = self.choose_one_improv_greedy()
        prob = np.random.uniform()
        #print('choice: ', choice)
        if prob < self.probs[choice]:
            self.rewards[choice].append(1)
        else:
            self.rewards[choice].append(0)

    def get_result(self):
        for _ in range(self.n):
            self.try_and_play()
        EXCEPT_MAX_REWARD = self.n * max(self.probs)
        PLAY_MAX_REWADR = sum(sum(i) for i in self.rewards) - 10
        return EXCEPT_MAX_REWARD, PLAY_MAX_REWADR, np.array([np.mean(i) for i in self.rewards])

flag = ["greedy", "improv_greedy"]
for j in range(2):
    n = 1000
    prob = np.random.uniform(size=10)
    reward = [[1] for _ in range(10)]
    P1 = MAB(n = n, probs=prob, rewards=reward, flag=flag[j])
    a1, b1, c1 = P1.get_result()
    print(a1, b1, '\n', c1, '\n')