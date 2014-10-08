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

answers_set=[]

def style_drink(*args):

    """ Here we ask the customer what kind of drink he/she likes"""

    keys_list=questions.keys() # here we take keys from the ingredients list and make a new list from keys only
    print "The flavors available : ", keys_list  # here we let the customer know what flavors available
    values_list=questions.values()  # we break down the dictionary for keys and values because its easier to manipulate it

    for i in range(len(questions)):   # loop to get the answers to the quesitons

            print values_list[i]
            answer = raw_input("Yes or Not?")

            
            if answer=="yes" or answer=="y":

                answers_set.append(True)      # if answer is YES, we make a new set with values True and False

                print answers_set

            elif answer=="not" or answer=="no":
                answers_set.append(False)
                print  answers_set

            
            else:
                print "You entry is invalid"
    return answers_set   # this is what the function returns set with True or False answers for the questions



def constract_drink(*args):
    """ Here we make a drink from the answers we get from the customer"""


    keys_ingredients=ingredients.keys()     # set of keys
    values_ingredients=ingredients.values()  # set of values

    answers_set=style_drink()

    drink=[]


    for True in answers_set:
            if True:
                drink.append(random.choice(values_ingredients))

                print "This is the drink", drink
            else:
                pass









if __name__=='__main__':

        constract_drink()
