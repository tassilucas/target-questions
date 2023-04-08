import json
import numpy as np

file = open('datasets/dados.json')
df = json.load(file)

'''
Considering that all days which have 0 as revenue are
either hollidays or weekends.
'''
def higher_revenue():
    return sorted(df, key=lambda df: df['valor'], reverse=True)[0]['dia']

def lower_revenue():
    revenue = sorted(df, key=lambda df: df['valor'])

    for data in revenue:
        if data['valor'] > 0:
            return data['dia']

# Excluding from mean the days with 0 revenue
def mean_revenue():
    filtered = [d for d in df if d['valor'] > 0]
    return sum([n['valor'] for n in filtered]) / len(filtered)

def above_mean():
    mean = mean_revenue()
    count = 0

    for d in df:
        if d['valor'] > mean:
            count = count + 1

    return count

# Question 1
print("Dia de maior faturamento")
print(higher_revenue())

# Question 2
print("Dia de menor faturamento")
print(lower_revenue())

# Question 3
print("Numero de dias com faturamento maior que media mensal")
print(above_mean())
