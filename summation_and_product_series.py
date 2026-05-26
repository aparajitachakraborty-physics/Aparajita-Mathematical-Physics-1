# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:30:35 2026

@author: APARAJITA CHAKRABORTY
"""

# =======================================================
# NBU Syllabus: Dynamic Summation and Product Series Engine
# =======================================================

# 1. INPUT AREA: Collect dynamic variable from the keyboard 
print("--- Interactive Mathematical Series Calculator ---")
x = float(input("Enter the base numerical value (x):"))
N = int(input("Enter the maximum upper limit power (N):"))

# 2. INITIALIZATION AREA: Set up the tracking variables
sum_total = 0       # Summation loops always start tracking at 0
product_total = 1   # Product loops must always start tracking at 1

# 3. COMPUTATIONAL AREA: Execute thr sequential logic loops

# Loop A: Calculating the Summation of the Squares Series 
for n in range(1, N + 1):
    sum_term = n * n
    sum_total = sum_total + sum_term
    
# LoopB: Calculating the Expoential Product Series
for n in range(1, N + 1):
    product_term = x ** n
    product_total = product_total * product_term
    
# 4. OUTPUT AREA: Print the final results to the user console
print("\n================ CALCULSTED RESULTS ================")
print("1. Total Summation (1^2 + 2^2 + ... + N^2) = ", sum_total)
print("2. Total Product (x^1 * x^2 * ... * x^N) =", product_total)
print("===============================================")
