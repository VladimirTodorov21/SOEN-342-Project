from SearchCriteria import *
from ConnectionFinder import *
from ConnectionCatalog import *
import csv
class Main:    

  
             

    def run(self):
          search = SearchCriteria()
          search.collect_user_input()
          search.display_user_input()
          catalog=ConnectionCatalog()
         
          connectionFinder= ConnectionFinder(search,catalog)
          connectionFinder.findConnections()

          connection_options=len(connectionFinder.direct_connections)+len(connectionFinder.multi_stop_connections)
          if connection_options>1:
               print("\nThere are multiple connection options for your criteria. Which sort option do you want?")
               print("1. Sort by Price")
               print("2. Sort by Duration")
               choice=input("Enter 1 or 2: ").strip()

               sorting_class=search.sorting_class.lower() if search.sorting_class else "first"

               if choice=="1":
                    connectionFinder.sortPrice(sorting_class)
                    connectionFinder.sortPriceMultiStop(sorting_class)
               elif choice=="2":
                    connectionFinder.sortDuration()
                    connectionFinder.sortDurationMultiStop()
               else:
                    print("Invalid sort option.")
   
          else:
               
               print("\nOnly one connection option found, no sorting needed.")        

          connectionFinder.printConnections()

if __name__ == "__main__":
    main = Main()
    main.run()