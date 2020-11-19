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
	C19 = randint(0, 1)
	F  = randint(0, 1)
	C = randint(0, 1)
	N = randint(0, 1)
	FC = randint(0, 1)
	FN = randint(0, 1)
	CN = randint(0, 1)
	print("This is the list: %s, %s, %s, %s, %s, %s, %s", %C19, %F, %C, %N, %FC, %FN, %CN)
