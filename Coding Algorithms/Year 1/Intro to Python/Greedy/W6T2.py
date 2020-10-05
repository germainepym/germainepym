##amount = int(input("What is the amount? "))
##def greedy_algorithm(amount,denoms):
##    n = len(denoms)
##    items = sorted(range(n),reverse=True)
##    result_list = [0 for i in range(len(denoms))]
##    total = 0
##    while total!=amount:
##        for i in items:
##            if total+denoms[i]<=amount:
##                total+=denoms[i]
##                result_list[i]+=1
##    return result_list
##print(greedy_algorithm(amount,[1,7,13]))
            
def best_individual_candidate(project, candidates):

    total = ()
    
    n = len(candidates)
    items = sorted(range(n),reverse=True)
    result_list = [0 for i in range(len(candidates))]
    
    while total!=project:
        for i in items:
            if total+candidates[i]<=project:
                total+=candidates[i]
                result_list[i]+=1
    return result_list

jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)

candidates = [jess, clark, john, cindy]
project = ["php", "java", "c++", "lua", "go"]

print(best_individual_candidate(project, candidates))
