############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
import os
import sys
import time
import random

############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES WILL NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############

input_file = "AISearchfile175.txt"

############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

##### begin change 1 #####
the_particular_city_file_folder = "city-files"
path_for_city_files = "../" + the_particular_city_file_folder
##### end change 1   #####
    
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the folder '" + the_particular_city_file_folder + "'.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")


############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############

############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME, E.G., 'abcd12'.
############

##### begin change 2 #####
the_particular_alg_codes_and_tariffs = "alg_codes_and_tariffs.txt"
path_for_alg_codes_and_tariffs = "../" + the_particular_alg_codes_and_tariffs
##### end change 2   #####

code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############

my_user_name = "tkmb68"

############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############

my_first_name = "Sidharth"
my_last_name = "Rao"

############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############

algorithm_code = "AC"

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############

import math
import time


start_time = time.time()

number_of_ants = num_cities


def display_matrix(matrix, name):
    print(name)
    for line in matrix:
        print(line)
    print("_________________________________________\n")

def initialize(number_of_ants):
    list_of_cities = [0 for x in range(number_of_ants)]
    unvisited_cities = [0 for x in range(number_of_ants)]
    for i in range(number_of_ants):
        city = random.randint(0, num_cities-1)

        list_of_cities[i] = [city]
        unvisited_cities[i] = list(range(num_cities))
        unvisited_cities[i].remove(city)
    return list_of_cities, unvisited_cities

def fitnessFunction(route):
    score = 0
    for i in range(1, num_cities):
        currentCity = route[i-1]
        nextCity = route[i]
        score += dist_matrix[currentCity][nextCity]
    score += dist_matrix[route[0]][route[-1]]
    return score

#finding minimum distance of the next city for the nearest neighbour algorithm.
def findingMinimum(unvisited_cities, line):
    minimum = max(line)
    city = line.index(minimum)
    for i in unvisited_cities:
        distance = line[i]
        if distance < minimum:
            minimum = distance
            city = i
    return city

#Nearest Neighbour Algorithm for giving the value for Lnn.
def NearestNeighbourAlgorithm(starting_city, dist_matrix):
    route = [starting_city]
    unvisited_cities = [x for x in range(num_cities)]
    unvisited_cities.remove(starting_city)
    line = dist_matrix[starting_city]
    for i in range(num_cities-1):
        city = findingMinimum(unvisited_cities, line)
        route.append(city)
        if city not in unvisited_cities:
            break
        unvisited_cities.remove(city)
        line = dist_matrix[city]
    return route

def fitnessCalculation(population):
    fitness_Scores = []
    for i in range(len(population)):
        fitness_Scores.append(fitnessFunction(population[i]))

    return fitness_Scores

#Lnn computes the nearest neighbour for all the lines in the distance matrix 
def Lnn():
    lnn_routes = []
    for n in range(num_cities):
        lnn_routes.append(NearestNeighbourAlgorithm(n, dist_matrix))
    fitness_scores = fitnessCalculation(lnn_routes)
    minFitness = min(fitness_scores)
    selectedVal = 1/minFitness
    return selectedVal

#The initial pheromone concentration is equal to the number of ants divided by the best route from the Nearest neighbour
#algorithm

def initial_pheromone_matrix(pheromone_amount = number_of_ants/Lnn()):
    pheromone_line = []
    pheromone_matrix = []
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone_line.append(pheromone_amount)
        pheromone_matrix.append(pheromone_line)
        pheromone_line = []
    return pheromone_matrix



def allFitness(matrix):
    fitList = []
    for i in range(number_of_ants):
         a = fitnessFunction(matrix[i])
         fitList.append(a)
    return fitList

#Heuristic Desirability Matrix is for computing the Heuristic Desirability (HD) of all the distances.
#This is implemented in the probability function as a higher HD will increase the chance of an ant selecting the route.
#This favours the shortest distances.
def heuristicDesirabilityMatrix(dist_matrix):
    heuristic_desirability = 0
    line = []
    heuristic_desirability_matrix = []
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                if dist_matrix[i][j] != 0:
                    heuristic_desirability = 1/dist_matrix[i][j]
                else:
                    heuristic_desirability = 1
                line.append(heuristic_desirability)
            else:
                line.append(0)
        heuristic_desirability_matrix.append(line)
        line = []
    return heuristic_desirability_matrix

#Probability function with the added Heuristic desirability of all the distances.
#cities with a higher heuristicly desirable distance and pheromone concentration are more likely to be selected.
#favours shorter distances and the shortest distances have the highest HD
#this increases the chance of breaking out of a local optimum. 
def probabilityFunction(i, j, heuristic_desirability_matrix, pheromone_matrix, unvisited_cities, alpha=1.3, beta = 2.2):
    total = 0
    heuristic_desirability_total = 0
    denominator = 0
    for m in unvisited_cities:
        total = pheromone_matrix[i][m] ** alpha
        heuristic_desirability_total = heuristic_desirability_matrix[i][m] ** beta
        denominator += total * heuristic_desirability_total
    if denominator == 0:
        denominator = 0.00000000000001
    numerator = ((pheromone_matrix[i][j])**alpha)*((heuristic_desirability_matrix[i][j])**beta)
    probability = numerator/denominator
    return probability

def selection(ant_city_list, unvisited_cities, n , pheromone_matrix,heuristic_desirability_matrix):
    probabilities = {}
    count = 0
    for j in unvisited_cities[n]:
        probability_ij = probabilityFunction(ant_city_list[n][-1], j, heuristic_desirability_matrix, pheromone_matrix, unvisited_cities[n])
        probabilities[j] = probability_ij
    while True:
        for city, prob in probabilities.items():
            if prob > random.random():
                return city
    return city


def update_ants(ant_city_list, unvisited_cities, pheromone_matrix, heuristic_desirability_matrix, number_of_ants):
    for n in range(number_of_ants):
        city = selection(ant_city_list, unvisited_cities, n, pheromone_matrix, heuristic_desirability_matrix)
        ant_city_list[n].append(city)
        unvisited_cities[n].remove(city)


def all_ant_paths(ant_city_list, unvisited_cities, pheromone_matrix, heuristic_desirability_matrix, number_of_ants):
    for i in range(num_cities - 1):
        update_ants(ant_city_list, unvisited_cities, pheromone_matrix, heuristic_desirability_matrix, number_of_ants)


#decay rate is fixed to 20%
def decayRate(pheromone_matrix, peta = 0.2):
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone_matrix[i][j] = (1 - peta) * pheromone_matrix[i][j]

#this function will deposit pheromones based on the rank of the ant as well as
#the size of the distance.
#As I mention later in the RankedEAS function, the added weight of the pheromone
#will decrease as the index of the ranked_pheromone_weight increases.
#This is a form of reinforcement learning where ants are now "competing" with
#each other in order the get the best routes as the ants with the higher ranking
#tend to leave behind a higher concentration of pheromones. 
#If the length of distance is lower then more pheromones are deposited. 
def inverseDeposit(pheromone_matrix, dist_matrix, ant_city_list):
    ranked_pheromone_weight = RankedEAS(pheromone_matrix, ant_city_list)
    ant_index_list = antRanking(ant_city_list)
    for x in range(number_of_ants):
        for y in range(num_cities):
            depositVal = pheromone_matrix[y][y]
            ant = ant_city_list[ant_index_list[x]]
            weight = ranked_pheromone_weight[x]
            city1 = ant[y]
            city2 = ant[y-1]
            val = dist_matrix[city1][city2]
            if val == 0:
                val = 1
            selected_val = 1/val
            depositVal *= selected_val
            pheromone_matrix[city1][city2] += depositVal + weight
            pheromone_matrix[city2][city1] += depositVal + weight
            
#starting points and re_initialize are not used in the final enhanced version since
#I found that in testing: if each ant starts at a random city then we don't discount the possibility
#of the optimal route starting from the city that was not included.
#that too, random starting generation produced a faster runtime. 
def startingPoints(ant_city_list):
    start_points = []
    for i in range(number_of_ants):
        ant = ant_city_list[i]
        startingPoint = ant[0]
        start_points.append(startingPoint)
    return start_points

def re_initialize(number_of_ants, ant_city_list, unvistied_cities):
    list_of_cities = [0 for x in range(number_of_ants)]
    unvisited_cities = [0 for x in range(number_of_ants)]
    for i in range(number_of_ants):
        start_points = startingPoints(ant_city_list)
        city = start_points[i]
        list_of_cities[i] = [start_points[i]]
        unvisited_cities[i] = list(range(num_cities))
        unvisited_cities[i].remove(city)
    return list_of_cities, unvisited_cities

def get_best_route(ant_city_list, scores):
    best_route = ant_city_list[0]
    best_score = scores[0]
    for i in range(1, len(ant_city_list)):
        if scores[i] < best_score:
            best_score = scores[i]
            best_route = ant_city_list[i]
    return (best_route, best_score)

#ant ranking is the function used to return all the ants ranked on the criteria of the shortest tour lenght.
def antRanking(ant_city_list):
    ant_score_list = fitnessCalculation(ant_city_list)
    ranked_ant_score_list = sorted(ant_score_list)
    ant_index_list = []
    for i in range(number_of_ants):
        ant_index_list.append(ant_score_list.index(ranked_ant_score_list[i]))
    return ant_index_list

#This version of the ranked elitist ant system involves ranking all of the ants and concentrating the pheromone
#based off the rank of the ant. 
def RankedEAS(pheromone_matrix, ant_city_list):
    ranked_pheromone_weight = []
    for i in range(number_of_ants):
        #pheromone_matrix[i][i] is never changed in the pheromone matrix and is the starting pheromone
        #where initial pheromone deposit = number of ants/ Lnn
        depositVal = pheromone_matrix[i][i]
        #the ranked pheromone weight will decrease as i increases
        ranked_pheromone_weight.append(depositVal/(i+1))
    return ranked_pheromone_weight
    

def main():
    max_iter = 0
    best_score = 0
    best_route = []
    tour = [x for x in range(num_cities)]
    tour_length = fitnessFunction(tour)
    ant_city_list, unvisited_cities = initialize(number_of_ants)
    pheromone_matrix = initial_pheromone_matrix()
    heuristic_desirability_matrix = heuristicDesirabilityMatrix(dist_matrix)
    all_ant_paths(ant_city_list, unvisited_cities, pheromone_matrix, heuristic_desirability_matrix, number_of_ants)
    if num_cities > 100 and time.time() - start_time > 59:
        return tour, tour_length
    fitness_list = allFitness(ant_city_list)
    current_best_route, current_best_score = get_best_route(ant_city_list, fitness_list)
    if num_cities > 100 and time.time() - start_time > 59:
        return tour, tour_length
    if current_best_score < best_score:
            count = 0
            best_score = current_best_score
            best_route = current_best_route
    if num_cities > 100 and time.time() - start_time > 59:
        return tour, tour_length
    inverseDeposit(pheromone_matrix, dist_matrix, ant_city_list)
    decayRate(pheromone_matrix, peta = 0.2)
    while max_iter < num_cities**2 and time.time() - start_time < 59:
        max_iter += 1
        ant_city_list, unvisited_cities = initialize(number_of_ants)
        if num_cities > 100 and time.time() - start_time > 59:
            return tour, tour_length
        all_ant_paths(ant_city_list, unvisited_cities, pheromone_matrix, heuristic_desirability_matrix, number_of_ants)
        if num_cities > 100 and time.time() - start_time > 59:
            return tour, tour_length
        inverseDeposit(pheromone_matrix, dist_matrix, ant_city_list)
        if num_cities > 100 and time.time() - start_time > 59:
            return tour, tour_length
        decayRate(pheromone_matrix, peta = 0.2)
        fitness_list = allFitness(ant_city_list)
        current_best_route, current_best_score = get_best_route(ant_city_list, fitness_list)
        if current_best_score < tour_length:
            max_iter = 0
            tour_length = current_best_score
            tour = current_best_route
    return tour, tour_length

if __name__ == "__main__":
    tour, tour_length = main()
    print(tour, tour_length, round((time.time() - start_time), 3), "seconds")
    


############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############

############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S,
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATA AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############

############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")
    
    











    


