#!/usr/bin/python
"""
Problem 2.5 from 2nd edition Giordano book. A bicycle travelling at low
velocities at constant force that transitions to higher velocities where
constant power is a more suitable representation.

Governing equations:
Eq.1 v_i+1 = v_i + F_0 / m * dt - C * p * A * v_i**2 / m	 * d t	 F_0 = P / v_T
Eq.2 v_i+1 = v_i + P / (v_i * m) * dt - C * p * A * v_i**2 / m * dt	 v_T = 7 m/s

The Euler's method uses Eq.1 when F_0*v_i < P and Eq.2 when F_0*v_i >= P
"""
import numpy as np
import matplotlib.pyplot as plt

class bicycleDrag():

	def __init__(self, F, vT, initialV, C, A, p, m, dt, maxTime):
		self.F = F
		self.vT = vT
		self.initialV = initialV
		self.P = F * vT
		self.C = C
		self.A = A
		self.p = p
		self.m = m
		self.dt = dt
		self.maxTime = maxTime

	def initialize(self):
		self.time = np.arange(0, self.maxTime, self.dt)
		self.nSteps = int(self.maxTime/self.dt)
		self.velocity = np.zeros(self.nSteps)
		self.velocity[0] = self.initialV

	def velocityCorrection(self, v):
		if self.F * v < self.P:
			print("low velocity")
			return self.F / self.m
		else:
			print("high velocity")
			return self.P/(self.m * v)

	def getVelocity(self):
		i = 0
		while i < self.nSteps -1:
			self.velocity[i+1] = self.velocity[i] + self.velocityCorrection(self.velocity[i]) * self.dt - self.C * self.A * self.p * self.velocity[i]**2 * self.dt / self.m
			i = i + 1
		return self.time, self.velocity

	def plotVelocity(self,show=True, filename="plot.pdf"):
		plt.scatter(self.time,self.velocity)
		if show:
			plt.show()
		else:
			plt.savefig(filename)

# Declaring initial Values and constants
dt = 0.05
maxTime = 20
m = 1
C = 0.5
A = 0.5
initialV = 0
F = 2
p = 1.225
vT = 7

bicycle = bicycleDrag(F, vT, initialV, C, A, p, m, dt, maxTime)
bicycle.initialize()
bicycle.getVelocity()
bicycle.plotVelocity()
print bicycle.velocity
