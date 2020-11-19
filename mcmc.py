#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Carrie Long and Maria Paolini
#Date: November 21, 2020
#Assignment: MCMC
#Purpose: 

import random
from random import choice
from random import seed


#Returns True with probability p, and False with probability 1-p
def prob(p):
  if random.random() < p:
    return True
  else:
    return False

#Conditional prob. for COVID-19 and fever
def C19_given_F(C19, F):
  if C19 == True:
    F = prob(0.886)
  else:
    F = prob(0.114)

#Conditional prob. for COVID-19 and cough
def C19_given_C(C19, C):
  if C19 == True:
    C = prob(0.907)
  else:
    C = prob(0.093)

#Conditional prob. for COVID-19 and nausea
#def C19_given_N(C19, N):
#  if C19 == True:
#    N = prob(0.747)
#  else:
#    N = prob(0.253)
    
#Conditional prob. for fever and cough
def F_given_C(F, C):
	if F == True:
		if C == False:
			C = prob(0.826)
		else:
			C = prob(0.727)
	else:
		if C == False:
			C = prob(0.174)
		else:
			C = prob(0.273)
			
#Conditional prob. for fever and cough
def C_given_F(C, F):
	if C == True:
		if F == False:
			F = prob(0.6)
		else:
			F = prob(0.457)
	else:
		if F == False:
			F = prob(0.4)
		else:
			F = prob(0.543)
			
#Conditional prob. for cough and nausea			
def N_given_C(N, C):
	if N == True:
		if C == False:
			C = prob(0.853)
		else:
			C = prob(0.644)
	else:
		if C == False:
			C = prob(0.147)
		else:
			C = prob(0.356)

#Conditional prob. for cough and nausea
def C_given_N(C, N):
	if C == True:
		if N == False:
			N = prob(0.894)
		else:
			N = prob(0.724)
	else:
		if N == False:
			N = prob(0.106)
		else:
			N = prob(0.276)
	
random.seed()
C19 = random.choice([True, False])
F  = random.choice([True, False])
C = random.choice([True, False])
N = True
FC = random.choice([True, False])
FN = True
CN = random.choice([True, False])
list = [C19, F, C, N, FC, FN, CN]
print("This is the list: " + str(list))
print("Hello World")
	
	
