__author__ = 'Olzhas'


class Bicycle:

    def __init__(self, model_name,weight,produce_cost):
        self.model_name=model_name
        self.weight=weight
        self.produce_cost=produce_cost

        return

   #class Wheels(Bicycle):

    #class Frames(Bicycle):



class Bike_Shops:

    def __init__(self,name,inventory,margin):
        self.name=name
        self.inventory=inventory
        self.margin=margin

        self.price=(self.inventory*self.margin)/self.inventory
        print self.price


class Customers:

    def __init__(self, name, fund_of_money,new_bike=True):
        self.name=name
        self.fund_of_money=fund_of_money
        self.new_bike=True




my_bike_shop=Bike_Shops("Bikes_for_evr1", 6, 20)

print ("Bike shop name is: ", my_bike_shop.name)
print ("It has :  bikes", my_bike_shop.inventory)

customer1=Customers("Mike", 200, True)
customer2=Customers("Eve", 500, True)
customer3=Customers("Bob", 1000, True)

print customer1.name

if customer1.fund_of_money >= my_bike_shop.price:
    print ("This is how many bikes  %s you can buy from %s" %(customer1.name,my_bike_shop.name))





