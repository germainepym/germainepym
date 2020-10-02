#Germaine Pok Yi Min
# ID: 29792802
#Task 1 :Talent Aquisition

def cost(candidates):

    total = 0
    for i in range(len(candidates)):
             
        costs = candidates[i][1] #extract the cost from the candidates eg. Tracy = 900
        total += costs # add up all the cost 
                
            
    return total

def skills(candidates):

    skill = []
    
    for i in range(len(candidates)):
        skill.append(candidates[i][0])  # appending skills of selected candidates

    b = []
    for j in skill: 
        for h in j:     # make two lists into one list
            b.append(h)
    
    final_skill = []
    for k in b:
        if k not in final_skill:    # if k(everything in b) is not in final_skill(which is empty now)
            final_skill.append(k)   # append k into final skill

    return final_skill
                

def uncovered(project, skills):

    a = []
    
    for elem in project:        
        if elem not in skills:      #if elem(everything in project) is not in skills
            a.append(elem)          #append to list a 
    return a

def best_individual_candidate(project, candidates):
    
    lst3 = []
    
    for i in range(len(candidates)):
       
        lst=[]
        lst2 = []      
       
        for k in candidates[i][0]:  
            lst2.append(k)      # append candidate's projects to lst2
            
        for l in lst2:
            if l in project:    # if elements from lst2 is in project
                lst.append(l)   # append it to lst
                            
        x = len(lst)                # to obtain spd, number of projects the candidate have
        y = x/(candidates[i][1])    # divided by their value
        lst3.append(y)
           
    spd = lst3.index(max(lst3))     #return index of maximum spd
    
    return spd

def team_of_best_individuals(project,candidates):

    lst4=[]
    
    for e in range(len(candidates)):
        
        lst3 = []
        
        for i in range(len(candidates)):
    
            lst=[]
            lst2 = []
       
            for k in candidates[i][0]:
                lst2.append(k)
            
            for l in lst2:
                if l in project:
                    lst.append(l)
                            
            x = len(lst)
            y = x/(candidates[i][1])
            lst3.append(y)

            spd = lst3.index(max(lst3))         #index of spd

        if lst3[spd] != 0:
            lst4.append(candidates.pop(spd))    #using spd, pop the index of the highest spd from the candidates list and append the value to lst4
            for r in lst4[e][0]:
                if r in project:
                    project.remove(r)       # if the project is in lst4, remove the project from the project
        else:
            pass          
                        
    return lst4

def best_team(project, candidates):
    all_possibilities = bitlists(candidates)
    team2 = []
    team3 = []
    team4 = []
    team5 = []
    final_team = []

    for i in range(len(all_possibilities)):
        team=[]
        for j in range(len(candidates)):
            if all_possibilities[i][j] == 1:        # if the lexicographic list contains one at for example [0,0,0,0,1], candidate Matt will be appended to team
                team.append(candidates[j])          # this appends individudal names, one by one without seperation 
        team2.append(team)                          # team2 contains a list according to the lexicographic list


    
    for i in range(len(team2)):   
        if uncovered(project,skills(team2[i])) == []:   #if uncovered is empty, append the list from team2 to team3
            team3.append(team2[i])                      # contains candidates that fulfill the projects required
            
    
    for i in range(len(team3)):
        team4.append(team3[i])                      #append the first list ([tracy, superman ..]) into list team4
        team5.append(cost(team4[i]))                #calculate the cost of the first list and append it to team 5

    final_value = team5.index(min(team5))           #the index of the minimum cost
    final_team.append(team3[final_value])           # append the most optimised option into final team

    
    return final_team    
    
#bitlist and lex_suc obtained from slides
#Monash(n.d.). Lec 11_Brute_Force. Retrieved from https://lms.monash.edu/pluginfile.php/8757727/mod_resource/content/1/Lec11_Brute_Force.pdf    
def bitlists(n):
    
    first = len(n)*[0]
    last = len(n)*[1]
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1])]
    return res                                 

def lex_suc(bitlst):
    
    res = bitlst[:]
    i = len(res) - 1
    while res[i] == 1:
        res[i] = 0
        i -= 1
    res[i] = 1
    return res
    

Tracy = (["matlab", "statistics", "python","tensorflow"],900)
Sandy = (["marketing", "sales"], 450)
Superman = (["python", "mysql", "marketing", "web design", "robotics"], 2000)
Daisy = (["mysql", "marketing"], 700)
Matt = (["python", "php", "web design"], 300)

candidates = [Tracy, Sandy, Superman, Daisy, Matt]
project = ["python", "web design" , "mysql", "marketing"]

##print(cost(candidates))
##print(skills(candidates))
##print(uncovered(project,skills([Tracy])))
##print(best_individual_candidate(project, candidates))
##print(team_of_best_individuals(project,candidates))
##print(best_team(project,candidates))
