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

answers_set={}

def style_drink():

    """ Here we ask the customer what kind of drink he/she likes"""
    for flavor, question in questions.iteritems():
        print question, " Yes/y or not/ n?"
        answers_set[flavor]=raw_input().lower()

    return answers_set




def constract_drink(answers_set):
    """ Here we make a drink from the answers we get from the customer"""


    drink=[]
    print "Drink has"
    for flavors, answers in ingredients.iteritems():


         for True in ingredients.iteritems():
            if True:
                drink.append(random.choice(values_ingredients[True]))

            else:
                pass
    print format(drink)








if __name__=='__main__':

        constract_drink()
