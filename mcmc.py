#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Authors: Carrie Long and Maria Paolini
#Date: November 21, 2020
#Assignment: MCMC
#Purpose: 

import seed
import random
seed(1)

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
    
def main(): 
	C19 = random.choice([True, False])
	F  = random.choice([True, False])
	C = random.choice([True, False])
	N = True
	FC = random.choice([True, False])
	FN = True
	CN = random.choice([True, False])
	print("This is the list: %d", %[C19, F, C, N, FC, FN, CN])
	
	
