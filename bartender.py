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

coctail_names = { "Fluffy Chinchilla" : ["Dogydog","Cat-Smile"], 
                  "Salty":  ["Seawater", "Sea-mouse"],
                  "Fluffy": ["Splash", "Old Style"]
    
}

answers={}

def style_drink():

    """ Here we ask the customer what kind of drink he/she likes"""
    for flavor, question in questions.iteritems():
        print question, " Yes/y or not/ n?"
        answers[flavor]=raw_input().lower()
        

    return answers




def constract_drink(answers):
    drink = []
    for ingredient_type, liked in answers.iteritems():
        if liked=="yes" or liked=="y":
             drink.append(random.choice(ingredients[ingredient_type]))
        else:
            pass
        
    return drink

def coctail_name(drink):
    drink_name = []
    for keys, values in coctail_names.iteritems():
        drink_name.append(random.choice(coctail_names[keys]))
        
   
    return drink_name

def customer_name():
    
    print "What is your name?"
    customer=raw_input().lower()
    return customer



def main():
    
    drink_name=""
    
    count=0
    answers = style_drink()
    drink = constract_drink(answers)
    drink_name=coctail_name(drink)

    
    



    while count<num_customers:
                        customer=customer_name()
                        count+=1
                        

    print "Your drink name is "

    while count==0:
                    print (''.join(map(str,random.choice(drink_name))))
                    count +=1
    

        
    for ingredient in drink:
                print "A {}".format(ingredient)
         
if __name__ == "__main__":
    customer={}    
    
    
    count_m=0

    print "How many customers in the bar right now?"
    num_customers=int(raw_input())

    while count_m<num_customers:

                        main()
                        count_m+=1

