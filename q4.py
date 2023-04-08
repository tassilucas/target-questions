
states = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88,
          'ES': 27165.48, 'Outros': 19849.53}

def print_percents():
    for k, v in states.items():
        print("{}: {}%".format(k, 100 * round(v / sum(states.values()), 2)))

print_percents()
