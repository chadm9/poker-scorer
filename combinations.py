
lyst = [0, 1, 2, 3, 4, 5, 6]

def unique_combinations(lyst, combination=[], combinations=[]):
    #print combination
    if len(combination) == 5:
        if sorted(combination) not in combinations:
            combinations.append(sorted(combination))
        #print combinations
    for i in range(len(lyst)):
        if lyst[i] not in combination:
            combination.append(lyst[i])

            unique_combinations(lyst, combination, combinations)
            combination.pop()


    return combinations



print unique_combinations(lyst)
