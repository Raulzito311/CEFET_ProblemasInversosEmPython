import numpy as np

# Configurações do algoritmo de Evolução Diferencial
def evolucaoDiferencial(fObj, bounds, nPop=20, genCount=1000, F=0.8, CR=0.7):
    min, max = bounds
    pop = np.random.uniform(min, max, nPop)
    results = np.array([fObj([x]) for x in pop])
    
    for gen in range(genCount):
        trialPop = np.copy(pop)

        # Mutation
        mutantPop = []

        for i in range(nPop):
            indexes = list(range(nPop))
            indexes.remove(i)
            r1, r2, r3 = np.random.choice(indexes, 3, replace=False)
            
            mutant = pop[r1] + F * (pop[r2] - pop[r3])
            mutant = np.clip(mutant, min, max)

            mutantPop.append(mutant)
        
        #Crossover
        randI = np.random.choice(list(range(nPop)), 1)
        
        for i in range(nPop):
            if i == randI or np.random.rand() <= CR:
                trialPop[i] = mutantPop[i]

        # Selection
        trialResults = np.array([fObj([x]) for x in trialPop])

        # if (np.average(trialResults) < np.average(results)):
        #     pop = trialPop
        #     results = trialResults

        for i in range(nPop):
            if (trialResults[i] < results[i]):
                pop[i] = trialPop[i]
                results[i] = trialResults[i]

        bestI = np.argmin(results)
        bestX = pop[bestI]
        bestFx = results[bestI]
        print(f"Gen: {gen} | Best x: {bestX} | Best F(x): {bestFx}")

    # Retorna o melhor indivíduo encontrado
    bestI = np.argmin(results)
    bestX = pop[bestI]
    bestFx = results[bestI]

    return bestX, bestFx
