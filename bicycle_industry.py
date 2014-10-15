__author__ = 'Olzhas'
import Bicycle
import frames
import wheels



class Customers:

    def __init__(self, name, fund_of_money,new_bike=True):
        self.name=name
        self.fund_of_money=fund_of_money
        self.new_bike=True

class Bike_Shops(object):

      #"""inventory is the dictionary with names and prices of the inventory we have"""
      # bike shop takes name, inventory and margin and returns the profit

    def __init__(self,name, margin,*kwargs):
        
        self.name=name
        self.margin=margin
        
        
   
        
    def prices(self):

        name_price = { }
    

        for name, cost in inventory.iteritems():
            
            name_price[name]=(cost*self.margin)/100+cost
        
        self.price=name_price
        return self.price   
    


class Shop_Inventory(Bike_Shops):

    def  inventory(self, key):
        new_inventory={ }

        for name, cost in inventory.iteritems():
            print inventory[name]
            print inventory[cost]
            
            if new_inventory[name]==key:
                    del(new_inventory[name])
            else:
                return new_inventory
        return new_inventory
        pass
      
def afford(customer_name):
        
        
        
        for name, price in my_bike_shop.prices().iteritems():
            
            
            

            if customer_name.fund_of_money>=price:
                print "______________________________________"
                print ("Dear %s we have %s for $%s\n" %(customer_name.name,name, price))
                customer_name.fund_of_money=(customer_name.fund_of_money-price)
                print ("you bought %s and have $ %s left" %(name, customer_name.fund_of_money))
                                              
                
                print "______________________________________"
                profit.append(price-inventory[name])
                print ("Bike shop profit is $%s" % sum(profit))

                sold_bikes[name]=inventory[name]
                print "Sold to %s %s: " %(customer_name.name, sold_bikes)
                return sold_bikes
            else:
                pass
      




profit=[]
remaining_inventory={ }
sold_bikes={ }

inventory={'Giant':200, 'GT':250, 'Bianchi':500, 'Shwinn':500}


my_bike_shop=Bike_Shops("Bikes for Everyone",20, inventory)



customer1=Customers("Mike", 245, True)
customer2=Customers("Eve", 500, True)
customer3=Customers("Bob", 1000, True)

afford(customer1)
afford(customer2)
afford(customer3)



