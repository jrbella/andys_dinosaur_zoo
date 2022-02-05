class Location:

    def __init__(self, location_continent, location_region):
        
        self.location_continent = location_continent
        self.location_region = location_region

        # getter

        def get_location_continent(self):
            return self.location_continent

        def get_location_region(self):
            return self.location_region
        
        # setter
        def set_location_continent(self, new_continent):
            self.location_continent = new_continent
        
        def set_location_region(self, new_region):
            self.location_region = new_region