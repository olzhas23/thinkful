__author__ = 'Olzhas'
import Bicycle
import frames
import wheels



class Customers:


    """Customer class, name, fund_of_money, newbike"""
    def __init__(self, name, fund_of_money,new_bike=True):
        self.name=name
        self.fund_of_money=fund_of_money
        self.new_bike=True

class Bike_Shops(object):
    '''Bike shop

      inventory is the dictionary with names and prices of the inventory we have
      bike shop takes name, inventory and margin and returns the profit'''

    def __init__(self,name, margin,*kwargs):
        
        self.name=name
        self.margin=margin
        
        
   
        
    def prices(self):

        name_price = { }
    

        for name, cost in inventory.iteritems():
            
            name_price[name]=(cost*self.margin)/100+cost
        
        self.price=name_price
        return self.price   
    



"""@afford
def  inventory(self, *kwargs):
    This funciton takes a dictionary of sold bikes and shows the how many bikes are in inventory
    



    for name, cost in sold.iteritems():
            print sold[name]
            print sold[cost]
            
            if new_inventory[name]==sold[name]:
                    new_inventory.append=new_inventory[name]
            else:
                return new_inventory
        return new_inventory
        pass
"""

def afford(customer_name):
        """This function returns if customers can buy the bikes, and returns the bikes that are sold to them"""
        
        
        
        for name, price in my_bike_shop.prices().iteritems():
            """we iterate in bikeshop prices dictionary and compare to the fund of money that is available to the customer"""
            
            
            

            if customer_name.fund_of_money>=price:
                print "______________________________________"
                print ("Dear %s we have %s for $%s\n" %(customer_name.name,name, price))
                customer_name.fund_of_money=(customer_name.fund_of_money-price)
                print ("you bought %s and have $ %s left" %(name, customer_name.fund_of_money))
                                              
                """Here we calculate the profit that is made from the sale"""
                print "______________________________________"
                profit.append(price-inventory[name])
                print ("Bike shop profit from sale $%s" % sum(profit))

                """Here we get get a new list with the bikes sold, in order to update our inventory dictionary latter"""
                sold_bikes[name]=inventory[name]
                print sold_bikes
                print "Sold to %s %s: " %(customer_name.name, sold_bikes)
                return sold_bikes
                """We are going to use this sold_bikes to input to our bike shop instance to update the inventory"""

            else:
                pass
      



"""Global vars, dic, lists"""
profit=[] # list to calculate the total profit
remaining_inventory={ } # dic for inventory that is left
sold_bikes={ }
new_inventory = { }

""" Inventory of bikes, base price """
inventory={'Giant':200, 'GT':250, 'Bianchi':500, 'Shwinn':500}

"""Here we create a new instance my_bike_shop and pass values(name, margin, and dic of the bikes for sale)"""

my_bike_shop=Bike_Shops("Bikes for Everyone",20, inventory)


"""Here we create a new instances of customers and pass values (name, fund_of_money, willing to purchase a bike"""

customer1=Customers("Mike", 245, True)
customer2=Customers("Eve", 500, True)
customer3=Customers("Bob", 1000, True)

"""Here we pass our customer instances to function to purchase the bikes"""
afford(customer1)
afford(customer2)
afford(customer3)




