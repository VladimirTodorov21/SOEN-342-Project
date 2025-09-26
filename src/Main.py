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
          connectionFinder.printConnections()

if __name__ == "__main__":
    main = Main()
    main.run()