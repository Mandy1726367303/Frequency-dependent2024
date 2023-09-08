#Python code implementing simulations of a stochastic branching process model of tumour growth and mutation
# accumulations, under purifying selection (PS) from the immune system due to randomly
# arising antigenic mutations. This code corresponds to an ideal population/measurement, with no measurement
# noise (but intrinsic stochasticity) and user-defined detection limit for mutations.
#    @Author: Shaoqing Chen (chenshaoqingstu.xmu.edu.cn)

import numpy as np
from scipy.special import comb
from copy import deepcopy
import matplotlib.pyplot as plt

b = 0.5 # Cell proliferation rate
mut_rate = 5 # Tumor mutation rate
db = 0.1 # Basal death rate
cutoff =0 # Immunogenicity threshold
s = -0.8 # Negative selection intensity
mutations = {}
sumA = {}

# Define negative selection
def sel_strength(N, E):
    return s if (E/(E+N+1e-9))> cutoff else 0

def birth_rate(cells, N, E):
    return b


def total_death_rate(cells, N, E):
    ss = sel_strength(N, E)
    return sum([cell.death_rate(ss) for cell in cells]) / len(cells)


class Cell:
    def __init__(self, mutation=[]):
        self.mutation = mutation

# Define the accumulative antigenicity as cell antigenicity
    def sumA(self):
        mutation = self.mutation
        suma = sum([mutations[i][0] for i in mutation])
        return suma

    def death_rate(self, s):
        sumA = self.sumA()

# Set the death rate of tumor cells to basal death rate if no antigenic mutation are accumulated
        if sumA < cutoff:
            return db

# A tumor cell's death rate depends on its antigenicity and the selection intensity
        else:return (1 + s * sumA) * (db - 1) + 1


class Reaction:
    def __init__(self, rate=0., num_lefts=None, num_rights=None, index=None):
        self.rate = rate
        assert len(num_lefts) == len(num_rights)
        self.num_lefts = np.array(num_lefts)
        self.num_rights = np.array(num_rights)
        self.num_diff = self.num_rights - self.num_lefts
        self.index = index

    def combine(self, n, s):
        return np.prod(comb(n, s))

    def propensity(self, n, cells, N, E):
        return self.rate(cells, N, E) * self.combine(n, self.num_lefts)


class System:
    def __init__(self, num_elements, inits=None, N=10, E=0, max_cell=100000):
        assert num_elements > 0
        self.num_elements = num_elements
        self.reactions = []
        self.N = N
        self.E = E
        self.log = {'N': [N], 'E': [E]}
        self.max_cell = max_cell
        if inits is None:
            self.n = [np.ones(self.num_elements)]
            self.cells = [Cell()]

        else:
            self.n = [np.array(inits)]
            self.cells = [Cell() for _ in range(int(self.n[0][0]))]

    def add_reaction(self, rate=0., num_lefts=None, num_rights=None, index=None):
        assert len(num_lefts) == self.num_elements
        assert len(num_rights) == self.num_elements
        self.reactions.append(Reaction(rate, num_lefts, num_rights, index=index))

# Simulate tumor evolution
    def evolute(self, steps):

        self.t = [0]

# The generation of antigenic mutations following a Poisson distribution
        def mutation(cell):
            new_mut_num = round(0.1 * (np.random.poisson(mut_rate)))
            new_mut_id = [max(mutations.keys(), default=0) + i + 1 for i in range(new_mut_num)]

# Mutation antigenicity sampled from a exponential distribution with mean value set to 0.2
            anti_val = [np.random.exponential(0.2) for _ in range(new_mut_num)]
            for i, new_mut in enumerate(new_mut_id):
                mutations.update({new_mut: [anti_val[i], 0]})
            cell.mutation += new_mut_id
            return cell, new_mut_id

# Cell proliferation and recording mutations
        def proliferate():
            divide_cell = np.random.choice(self.cells)
            dau1, new_mut1 = mutation(deepcopy(divide_cell))
            dau2, new_mut2 = mutation(deepcopy(divide_cell))

            for mut in new_mut1 + new_mut2:
                mutations[mut][1] += 1
            for mut in divide_cell.mutation:
                mutations[mut][1] += 1
            self.cells.remove(divide_cell)
            self.cells.append(dau1)
            self.cells.append(dau2)
            if divide_cell.sumA() < cutoff:
                self.N -= 1

                if dau1.sumA() < cutoff:
                    self.N += 1
                else:
                    self.E += 1
                if dau2.sumA() < cutoff:
                    self.N += 1
                else:
                    self.E += 1
            else:
                self.E -= 1
                if dau1.sumA() < cutoff:
                    self.N += 1
                else:
                    self.E += 1
                if dau2.sumA() < cutoff:
                    self.N += 1
                else:
                    self.E += 1

# Cell death and removing mutations
        def death():
            s = sel_strength(self.N, self.E)
            deathp = np.array([cell.death_rate(s) for cell in self.cells])
            deathp = deathp / sum(deathp)
            death_cell = np.random.choice(self.cells, p=deathp)
            if death_cell.sumA() < cutoff:
                self.N -= 1
            else:
                self.E -= 1
            for mut in death_cell.mutation:
                mutations[mut][1] -= 1
            self.cells.remove(death_cell)

        for i in range(steps):
            A = np.array([rec.propensity(self.n[-1], self.cells, self.N, self.E)
                          for rec in self.reactions])
            A0 = A.sum()
            A /= A0
            t0 = -np.log(np.random.random()) / A0
            self.t.append(self.t[-1] + t0)
            react = np.random.choice(self.reactions, p=A)
            self.n.append(self.n[-1] + react.num_diff)
            switch = {0: proliferate, 1: death}
            switch.get(react.index)()
            self.log['N'].append(self.N)
            self.log['E'].append(self.E)

# Exit simulation until the tumor reached a predefined size or elimination
            if self.N + self.E >= self.max_cell  or self.N + self.E < 1 :
                break


system = System(1, np.array([100]))
system.add_reaction(birth_rate, [1], [2], index=0)
system.add_reaction(total_death_rate, [1], [0], index=1)
system.evolute(500000000)
pop_size = np.array(system.n).reshape(1, -1)[0]
E = system.log['E']
N = system.log['N']
np.savetxt('p_PS.txt', pop_size, fmt='%d', delimiter=',')
np.savetxt('t_PS.txt', system.t, delimiter=',')
mutation_num = np.array([0, 0])
for i in mutations:
    mutation_num = np.vstack((mutation_num, [mutations[i][0], mutations[i][1]]))
mutation_num = mutation_num[1:, :]
np.savetxt('m_PS.txt', mutation_num)
