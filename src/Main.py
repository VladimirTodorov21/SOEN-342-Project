from SearchCriteria import *

class Main:    
    def run(self):
        SearchCriteria.collect_user_input(SearchCriteria)
        SearchCriteria.display_user_input(SearchCriteria)

if __name__ == "__main__":
    main = Main()
    main.run()