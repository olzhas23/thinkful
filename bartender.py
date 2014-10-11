import random
questions = {
    "strong": "Do you like your drinks strong?",
    "salty": "Do you like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

coctail_names = { "Fluffy Chinchilla" : ["Dog"], 
                  "Salty": [ "Sea-Dog"],
                  "Fluffy": [ "Sea-Cow"]
    
}

answers_set={}

def style_drink():

    """ Here we ask the customer what kind of drink he/she likes"""
    for flavor, question in questions.iteritems():
        print question, " Yes/y or not/ n?"
        answers_set[flavor]=raw_input().lower()

    return answers_set




def constract_drink(answers_set):
    drink = []
    for ingredient_type, liked in answers_set.iteritems():
        if not liked:
            continue
 
        drink.append(random.choice(ingredients[ingredient_type]))
    return drink

"""def coctail_name():
    drink_name = []
    for keys, values in coctail_names.iteritems:
        drink_name.append(random.choice(coctail_names[values]))
   
    return drink_name"""





def main():
    answers_set = style_drink()
    drink = constract_drink(answers_set)
   # d_name=coctail_name()
    print "Your drink"
    #print d_name
    for ingredient in drink:
        print "A {}".format(ingredient)
 
if __name__ == "__main__":
    main()
