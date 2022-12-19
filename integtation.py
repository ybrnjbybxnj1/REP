import math
from typing import List


class Integrall:
    n: int
    y: List[float]
    x: List[float]
    crRectR: float = 0
    crRectM: float = 0
    crRectL: float = 0
    crTrap: float = 0
    crSimps: float = 0
    cr38: float = 0

    def __init__(self, n: int, y: List[float], x: List[float]):
        self.n = n
        self.y = y
        self.x = x

    def rectR(self):
        for i in range(1, self.n):
            dx = self.x[i] - self.x[i-1]
            self.crRectR += dx*self.y[i]

    def rectM(self):
        for i in range(1, self.n):
            dx = self.x[i] - self.x[i-1]
            self.crRectM += (self.y[i-1] + self.y[i]) / 2 * dx

    def rectL(self):
        for i in range(1, self.n):
            dx = self.x[i] - self.x[i-1]
            self.crRectL += dx*self.y[i-1]

    def trap(self):
        for i in range(1, self.n):
            dx = self.x[i] - self.x[i-1]
            dy = (self.y[i-1] + self.y[i]) / 2
            self.crTrap += dx * dy

    def simps(self):
        for i in range(1, self.n):
            dx = self.x[i] - self.x[i-1]
            self.crSimps += (self.y[i-1] + self.y[i] + 4* (self.y[i-1] + self.y[i]) / 2) / 6 * dx

    def f38(self):
        for i in range(1, self.n):
            dx = self.x[i] - self.x[i-1]
            self.cr38 += (self.y[i-1] + 3 * self.y[i-1] + 3 * self.y[i] + self.y[i]) / 8 * dx

    def integrateAll(self):
        self.rectR()
        self.rectM()
        self.rectL()
        self.trap()
        self.simps()
        self.f38()
