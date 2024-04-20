import copy
import random
import matplotlib.pyplot as plt

persons = [5, 10, 20, 30, 35]
price = range(200, 400)
theme_anime = ["Naruto", "Dragon Ball", "One Piece", "Bleach", "Attack on Titan", "My Hero Academia", "Tokyo Ghoul",
               "Death Note", "Sword Art Online", "Demon Slayer", "Black Clover", "Hunter x Hunter", "Fairy Tail",
               "One Punch"]
theme_games = ["Halo", "Free Fire", "Doom", "Mario bros", "Kirby", "Zelda", "Sonic", "Crash Bandicoot", "Spyro",
               "Resident Evil", "Final Fantasy", "Metal Gear", "Street Fighter", "Mortal Kombat", "Tekken",
               "King of Fighters", "Guilty Gear", "BlazBlue", "Dead or Alive", "Soul Calibur", "Virtua Fighter",
               "Dark Souls", "Bloodborne", "Nioh", "Sekiro", "God of War", "Uncharted", "The Last of Us"]
theme_kids = ["Pepa pig", "Miracoulus", "Paw Patrol", "Dora", "Diego", "Mickey Mouse", "Minnie Mouse", "Donald Duck",
              "Daisy Duck", "Goofy", "Pluto", "Chip and Dale", "Scrooge McDuck", "Huey, Dewey and Louie",
              "Webby Vanderquack", "Launchpad McQuack", "Gyro Gearloose", "Fenton Crackshell", "Gizmoduck",
              "Bubba the Caveduck", "Gladstone Gander", "Gosalyn Mallard", "Darkwing Duck", "Megavolt", "Quackerjack",
              "Bushroot", "Liquidator", "Negaduck", "Steelbeak", "Taurus Bulba", "F.O.W.L.", "Magica De Spell",
              "Flintheart Glomgold"]
theme_fruits = ["Apple", "Orange", "Banana", "Pear", "Peach", "Plum", "Grape", "Watermelon", "Kiwi", "Cranberry",
                "Blackberry", "Strawberry", "Raspberry", "Blueberry", "Cherry", "Pineapple", "Coconut", "Lemon", "Lime",
                "Mango", "Papaya", "Guava", "Pomegranate", "Passion Fruit", "Lychee", "Dragon Fruit", "Star Fruit",
                "Kumquat", "Persimmon", "Fig", "Apricot", "Nectarine", "Cantaloupe", "Honeydew", "Cucumber",
                "Bell Pepper", "Pumpkin"]
theme_Normal = ["Green", "Red", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White", "Gray",
                "Beige", "Maroon", "Teal", "Coral", "Lavender", "Periwinkle", "Turquoise", "Gold", "Platinum",
                "Rose Gold", "Rainbow", "Pastel"]
theme_romantic = ["Romantic Hearts", "Elegant Lace", "Vintage Roses", "Classic Elegance", "Lovebirds",
                  "Champagne Toast", "Golden Anniversary", "Diamond Dreams", "Forever Yours", "Timeless Romance",
                  "Enchanted Evening", "Whimsical Wonderland", "Passionate Pinks", "Dreamy Drapes",
                  "Celestial Serenity", "Moonlit Magic", "Fairy Tale Fantasy", "Garden of Love", "Candlelit Affair",
                  "Starry Night"]
theme_elegant = ["White Elegance", "Floral Cascade", "Fairy Tale Romance", "Royal Love", "Enchanted Garden",
                 "Candlelit Splendor", "Crystal Dreams", "Regal Affair", "Glamorous Gold", "Modern Minimalism"]

classic_flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Lemon', 'Orange', 'Mint', 'Caramel', 'Coffee']

fruits_berries = ['Strawberry', 'Lemon', 'Orange', 'Cherry', 'Blueberry', 'Raspberry', 'Pineapple', 'Banana', 'Apple',
                  'Mango', 'Grape', 'Watermelon', 'Kiwi', 'Cranberry', 'Plum']

nuts = ['Coconut', 'Almond', 'Hazelnut', 'Pistachio', 'Walnut', 'Macadamia', 'Pecan', 'Cashew', 'Chestnut']

spices_others = ['Cinnamon', 'Ginger', 'Honey', 'Maple', 'Pumpkin', 'Cotton Candy', 'Licorice']

occasions = ["Cumpleaños (Kids)", "Cumpleaños (Adtes)", "Cumpleaños (Mayor)", "Aniversario", "Boda", "Graduación"]

flavor = ['classic', 'fruits berries', 'nuts', 'spices others']


def generate_individual():
    individual = []
    individual.append(random.choice(persons))
    price_og = random.choice(price)
    individual.append(price_og)
    select_theme = random.randint(0, 6)
    print(individual[1])
    print(select_theme)
    if select_theme == 0:
        individual.append(random.choice(theme_anime))
        individual[1] = round(individual[1] * 1.5, 2)
    elif select_theme == 1:
        individual.append(random.choice(theme_games))
        individual[1] = round(individual[1] * 1.2, 2)
    elif select_theme == 2:
        individual.append(random.choice(theme_kids))
        individual[1] = round(individual[1] * 1.3, 2)
    elif select_theme == 3:
        individual.append(random.choice(theme_fruits))
        individual[1] = round(individual[1] * 1.6, 2)
    elif select_theme == 4:
        individual.append(random.choice(theme_Normal))
        individual[1] = round(individual[1] * 1.6, 2)
    elif select_theme == 5:
        individual.append(random.choice(theme_elegant))
        individual[1] = round(individual[1] * 1.6, 2)
    else:
        individual.append(random.choice(theme_romantic))
        individual[1] = round(individual[1] * 1.1, 2)
    if individual[0] == 10:
        individual[1] = individual[1] + 50
    elif individual[0] == 20:
        individual[1] = individual[1] + 100
    elif individual[0] == 30:
        individual[1] = individual[1] + 150
    elif individual[0] == 35:
        individual[1] = individual[1] + 170
    select_flavor = random.randint(0, 3)
    print(select_flavor)
    if select_flavor == 0:
        individual.append(random.choice(classic_flavors))
        individual[1] = round(individual[1] * 1.5, 2)
    elif select_flavor == 1:
        individual.append(random.choice(fruits_berries))
        individual[1] = round(individual[1] * 1.2, 2)
    elif select_flavor == 2:
        individual.append(random.choice(nuts))
        individual[1] = round(individual[1] * 1.6, 2)
    else:
        individual.append(random.choice(spices_others))
        individual[1] = round(individual[1] * 1.1, 2)
    individual.append(price_og)
    return individual


def generate_population(size_of_population):
    population = []
    for i in range(size_of_population):
        population.append(generate_individual())
    print("POPULATION", population)
    return population


def delete_prices(population):
    for i in population:
        i[1] = i[4]
    return population


def calculate_price(population):
    for i in range(len(population)):
        if population[i][0] == 10:
            population[i][1] = population[i][1] + 50
        elif population[i][0] == 20:
            population[i][1] = population[i][1] + 100
        elif population[i][0] == 30:
            population[i][1] = population[i][1] + 150
        elif population[i][0] == 35:
            population[i][1] = population[i][1] + 170

        if population[i][2] in theme_anime:
            population[i][1] = round(population[i][1] * 1.5, 2)
        elif population[i][2] in theme_games:
            population[i][1] = round(population[i][1] * 1.2, 2)
        elif population[i][2] in theme_kids:
            population[i][1] = round(population[i][1] * 1.3, 2)
        elif population[i][2] in theme_fruits:
            population[i][1] = round(population[i][1] * 1.6, 2)
        else:
            population[i][1] = round(population[i][1] * 1.1, 2)

        if population[i][3] in classic_flavors:
            population[i][1] = population[i][1] + 100
        elif population[i][3] in fruits_berries:
            population[i][1] = population[i][1] + 120
        elif population[i][3] in nuts:
            population[i][1] = population[i][1] + 70
        else:
            population[i][1] = population[i][1] + 50

    return population


def calculate_fitness(population, client):
    fitness_scores = []
    for individual in population:
        score = 0
        if individual[0] < client[0]:
            score -= 0.2  # People
        if individual[0] > client[0] + 10:
            score -= 0.2  # People
        if individual[0] >= client[0]:
            score += 0.2  # People
        if individual[1] <= client[1]:
            score += 0.2  # Price
        # Occasions
        if client[2] == 'Cumpleaños (Kids)':
            if individual[2] in theme_kids:
                score += 0.3
        elif client[2] == 'Cumpleaños (Adtes)':
            if individual[2] in theme_anime:
                score += 0.3

        elif client[2] == 'Cumpleaños (Mayor)':
            if individual[2] in theme_Normal:
                score += 0.3

        elif client[2] == 'Aniversario':
            if individual[2] in theme_romantic:
                score += 0.3

        elif client[2] == 'Boda':
            if individual[2] in theme_elegant:
                score += 0.3

        elif client[2] == 'Graduación':
            if individual[2] in theme_Normal + theme_elegant:
                score += 0.3
        # Flavor
        if client[3] == 'classic':
            if individual[3] in classic_flavors:
                score += 0.3

        elif client[3] == 'fruits berries':
            if individual[3] in fruits_berries:
                score += 0.3

        elif client[3] == 'nuts':
            if individual[3] in nuts:
                score += 0.3

        elif client[3] == 'spices others':
            if individual[3] in spices_others:
                score += 0.3

        fitness_scores.append(round(score, 1))
    print("FITNESS SCORES", fitness_scores)
    return fitness_scores


def selection(population, client):
    fitness_scores = calculate_fitness(population, client)
    sort = zip(fitness_scores, population)
    sort = sorted(sort, key=lambda x: x[0], reverse=True)
    population = [x for y, x in sort]
    if len(population) % 2 != 0:
        population_selected = population[:int(len(population) * 0.5 + 1)]
    else:
        population_selected = population[:int(len(population) * 0.5)]
    print("POPULATION SELECTED", population_selected)
    return population_selected, population


def crossover(population, population_selected):
    population_selected = delete_prices(population_selected)
    population = delete_prices(population)
    for i in range(len(population_selected)):
        point_of_crossover = random.choice(range(1, len(population[0]) - 1))
        print("POINT OF CROSSOVER", point_of_crossover)
        father = copy.copy(population_selected[i])
        mother = copy.copy(random.choice(population))
        print("FATHER", father)
        print("MOTHER", mother)
        father[point_of_crossover:-1], mother[point_of_crossover:-1] = mother[point_of_crossover:-1], father[
                                                                                                      point_of_crossover:-1]
        if point_of_crossover == 1:
            father[4] = father[1]
            mother[4] = mother[1]
        print("CHILD1", father)
        print("CHILD2", mother)
        population.append(father)
        population.append(mother)
    population = calculate_price(population)
    print("POPULATION BEFORE CROSSOVER", population)
    return population


def mutation(population, num_ind, num_gen):
    population = delete_prices(population)
    for i in population:
        if random.random() < num_ind:
            print("INDIVIDUAL", i)
            for j in i:
                if random.random() < num_gen:
                    if j == i[0]:
                        i[0] = random.choice(persons)
                    elif j == i[1]:
                        i[1] = random.choice(price)
                        i[4] = i[1]
                    elif j == i[2]:
                        select_theme = random.randint(0, 6)
                        if select_theme == 0:
                            i[2] = random.choice(theme_anime)
                        elif select_theme == 1:
                            i[2] = random.choice(theme_games)
                        elif select_theme == 2:
                            i[2] = random.choice(theme_kids)
                        elif select_theme == 3:
                            i[2] = random.choice(theme_fruits)
                        elif select_theme == 4:
                            i[2] = random.choice(theme_elegant)
                        elif select_theme == 6:
                            i[2] = random.choice(theme_romantic)
                        else:
                            i[2] = random.choice(theme_Normal)
                    elif j == i[3]:
                        select_flavor = random.randint(0, 3)
                        if select_flavor == 0:
                            i[3] = random.choice(classic_flavors)
                        elif select_flavor == 1:
                            i[3] = random.choice(fruits_berries)
                        elif select_flavor == 2:
                            i[3] = random.choice(nuts)
                        else:
                            i[3] = random.choice(spices_others)
                    elif j == i[4]:
                        i[4] = random.choice(price)
                        i[1] = i[4]
    population = calculate_price(population)
    print("POPULATION AFTER MUTATION", population)
    return population


def pruning(population, size, client):
    population = eliminate_repeated(population)
    fitness_scores = calculate_fitness(population, client)
    sort = zip(fitness_scores, population)
    sort = sorted(sort, key=lambda x: x[0], reverse=True)
    population = [x for y, x in sort]
    fss = [y for y, x in sort]
    population_select = population[0]
    print("POPULATION SELECT", population_select, fss[:3])
    print("POPULATION", len(population))
    while len(population) > size:
        individual = random.choice(population)
        if individual not in population_select:
            population.remove(individual)
    print("POPULATION", len(population))
    return population


def eliminate_repeated(population):
    poblation_no_repeated = []
    print("POBLATION ENTRA", len(population))
    for i in population:
        if i not in poblation_no_repeated:
            poblation_no_repeated.append(i)
    print("POBLATION SALE", len(poblation_no_repeated))
    return poblation_no_repeated


def genetic_algorithm(client, size, size_of_population, num_gen, num_ind, epochs):
    history = []
    worst = []
    best_individual = []
    fss_best = []
    population = generate_population(size_of_population)
    count = 0

    while True:
        if history and history[-1] >= epochs and count > 2:
            break
        else:
            best_individual.clear()
            fss_best.clear()
        population_selected, population = selection(population, client)

        population = crossover(population, population_selected)
        population = mutation(population, num_ind, num_gen)

        fss = calculate_fitness(population, client)
        sort = zip(fss, population)
        sort = sorted(sort, key=lambda x: x[0], reverse=True)
        fss = [y for y, x in sort]
        indv = [x for y, x in sort]
        print("FITNESS", fss[0])
        best_individual.append(indv[0])
        best_individual.append(indv[1])
        best_individual.append(indv[2])
        fss_best.append(fss[0])
        fss_best.append(fss[1])
        fss_best.append(fss[2])
        history.append(fss[0])
        worst.append(fss[-1])
        print("HISTORY", history)
        population = pruning(population, size, client)
        print(len(population))
        count += 1
    return population, history, fss_best, best_individual, count, worst
