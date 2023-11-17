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

input_file = "AISearchfile535.txt"

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

algorithm_code = "GA"

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
start_time = time.time()

def display_matrix(matrix, name):
    print(name)
    for line in matrix:
        print(line)
    print("____________________________________________\n")

#New initialize condition where the population size depends on the number of cities. 
def initialize(num_cities):
    population = []
    list_of_cities = [x for x in range(num_cities)]
    if num_cities < 16:
        while len(population) < 64:
            random.shuffle(list_of_cities)
            newPopulation = list_of_cities.copy()
            population.append(newPopulation)
    elif num_cities < 32:
        while len(population) < 128:
            random.shuffle(list_of_cities)
            newPopulation = list_of_cities.copy()
            population.append(newPopulation)
    elif num_cities < 256:
        while len(population) < 128:
            random.shuffle(list_of_cities)
            newPopulation = list_of_cities.copy()
            population.append(newPopulation)
    elif num_cities > 528:
        while len(population) < 256:
            random.shuffle(list_of_cities)
            newPopulation = list_of_cities.copy()
            population.append(newPopulation)
    return population

def fitnessFunction(chromosome):
    score = 0
    for i in range(1, num_cities):
        currentCity = chromosome[i-1]
        nextCity = chromosome[i]
        score += dist_matrix[currentCity][nextCity]
    score += dist_matrix[chromosome[0]][chromosome[-1]]
    return score

def fitnessCalculation(population):
    fitness_Scores = []
    total_f = 0
    for i in range(len(population)):
        fitness_Scores.append(fitnessFunction(population[i]))
        total_f += fitness_Scores[i]
    return fitness_Scores, total_f

#Tournament Selection < Roulette wheel selection in terms of worst case runtime. The selection process will randomly put 
#two chromosomes up against each other and select the fitter one. Not as random as roulette wheel but faster since the
#best and worst runtime is always n/2

def TournamentSelection(population, fitness_Scores):
    selectedPopulation = []
    index_list = [x for x in range(len(population))]
    for n in range(len(fitness_Scores)//2):
        if num_cities > 100 and time.time() - start_time > 59:
            return False
        index1 = random.choice(index_list)
        index_list.remove(index1)
        index2 = random.choice(index_list)
        index_list.remove(index2)
        selected_chromosome_1 = fitness_Scores[index1]
        selected_chromosome_2 = fitness_Scores[index2]
        if selected_chromosome_1 < selected_chromosome_2:
            selectedPopulation.append(population[index1])
        else:
            selectedPopulation.append(population[index2])
    return selectedPopulation


def RouletteWheelSelection(population, fitness_Scores):
    r = 0
    seenPositions = []
    selectedPopulation = []
    fitnessProbabilities = fitness_probability(fitness_Scores)
    while len(selectedPopulation) < len(fitnessProbabilities)/2:
        for n in range(len(fitnessProbabilities)):
            r = random.uniform(0,1)
            if fitnessProbabilities[n] > r:
                if n not in seenPositions:
                    seenPositions.append(n)
                    selectedPopulation.append(population[n])               
            if len(selectedPopulation) == len(fitnessProbabilities)/2:
                break
    return selectedPopulation

#crossover is the same as for the basic version
def crossover(parent_1, parent_2):
    if num_cities > 100 and time.time() - start_time > 59:
            return False
    starting_index = random.randint(0, num_cities//2)
    ending_index = random.randint(num_cities//2, num_cities)

    child_1 = [-1 for i in range(num_cities)]
    child_2 = [-1 for i in range(num_cities)]
    slice_1 = parent_1[starting_index:ending_index]
    slice_2 = parent_2[starting_index:ending_index]
 
    for i in range(num_cities):
        if starting_index <= i < ending_index:
            child_2[i] = parent_1[i]
            child_1[i] = parent_2[i]
        else:
            if parent_1[i] not in slice_2:
                child_1[i] = parent_1[i]
            if parent_2[i] not in slice_1:
                child_2[i] = parent_2[i]
    
    for i in range(num_cities):
        if child_1[i] == -1:
            for j in range(num_cities):
                if child_2[j] not in child_1:
                    child_1[i] = child_2[j]
                    break
        if child_2[i] == -1:
            for j in range(num_cities):
                if child_1[j] not in child_2:
                    child_2[i] = child_1[j]
                    break
    
    return (child_1, child_2)

def replacement(population, parents):
    i = 0
    new_population = []
    while len(new_population) != len(population):
        if num_cities > 100 and time.time() - start_time > 59:
            return population
        p1 = random.randint(0, len(parents)-1)
        p2 = random.randint(0, len(parents)-1)
        
        while p2 == p1:
            p2 = random.randint(0, len(parents)-1)
        (child_1, child_2) = crossover(parents[p1], parents[p2])
        new_population.append(parents.pop(p1))
        new_population.append(parents.pop(p2-1))
        
        new_population.append(child_1)
        new_population.append(child_2)

    return new_population


def mutation(population, alpha=0.05):
    for i in range(len(population)):
        r = random.uniform(0,1)
        if r < alpha:
            index_1 = random.randint(0, num_cities-1)
            index_2 = random.randint(0, num_cities-1)
            city_1 = population[i][index_1]
            city_2 = population[i][index_2]
            population[i][index_1] = city_2
            population[i][index_2] = city_1
            

def get_best_route(population, scores):
    best_route = population[0]
    best_score = scores[0]
    for i in range(1, len(population)):
        if scores[i] < best_score:
            best_score = scores[i]
            best_route = population[i]
    return (best_route, best_score)

#This will rank the chromosomes in terms of fitness. This is important as it encourages crossovers with better paths. 
def best_chromosomes(population, fitness_Scores):
    ranked_population_fitness = sorted(fitness_Scores)
    ranked_index = 0
    ranked_population = []
    for i in range(len(population)):
        ranked_index = fitness_Scores.index(ranked_population_fitness[i])
        ranked_population.append(population[ranked_index])
    return ranked_population

def geneticAlgorithm(run, population):
    best_route = [x for x in range(num_cities)]
    best_score = 100000000000000000000000000
    count = 0
    i = 0
#Set the max iterations depending on the number of cities. This was useful when testing
#since having a higher number of max iterations means we give the algorithm I higher chance of
#breaking out of a local optimum.
    if num_cities < 16:
        max_iter = 1000
    elif num_cities < 32:
        max_iter = 2500
    elif num_cities < 64:
        max_iter = 5000
    elif num_cities < 128:
        max_iter = 10000
    elif num_cities < 256:
        max_iter = 20000
    elif num_cities > 528:
        max_iter = 25000
        
    fitness_Scores, total_score = fitnessCalculation(population)
    while count < max_iter:
        count += 1
        i += 1
        parents = TournamentSelection(population, fitness_Scores)
        population = replacement(population, parents)
        mutation(population)
        fitness_Scores, total_score = fitnessCalculation(population)

        current_best_route, current_best_score = get_best_route(population, fitness_Scores)
        if current_best_score < best_score:
            count = 0
            best_score = current_best_score
            best_route = current_best_route
        if time.time() - start_time > 59:
            break

#This is returning the top 1/8 best chromosomes into the next generation cycle which keeps the best paths.
#Doing this ensures that the edges with smaller distances stays in the population. 
    ranked_population = best_chromosomes(population, fitness_Scores)
    population = initialize(num_cities)
    for i in range(len(population)//8):
        population.pop(i)
        population.append(ranked_population[i])
    best_score = fitnessFunction(best_route)
    return best_route, best_score

def generationCycle():
    tour = [x for x in range(num_cities)]
    tour_length = fitnessFunction(tour)
    generationCycle = 0
    population = initialize(num_cities)
    while time.time() - start_time < 59:
        generationCycle += 1
        route, score = geneticAlgorithm(generationCycle, population)
        if score < tour_length:
            tour_length = score
            tour = route
    return tour, tour_length

def main():
    tour, tour_length = generationCycle()
    return tour, tour_length
    
if __name__ == "__main__":
    tour, tour_length = main()
    print(tour, tour_length, time.time() - start_time)










        
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
