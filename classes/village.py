from classes.villager import Villager
import random

class Village():
    def __init__(self, name, population):
        self._name = name
        self._year = 0
        self._month = 1
        self._villagers = [Villager(random.randint(0, 100), random.randint(1, 12)) for _ in range(population)]
        self._food = 1000
        self._tools = 100
        self._resources = 100
        
    def __str__(self):
        return f"{self._name} has {self.population} people."
        
    def grow(self, amount):
        for _ in range(amount):
            self._villagers.append(Villager(random.randint(0, 100), random.randint(1, 12)))
            
    def kill(self, index):
        villager = self._villagers.pop(index)
        print(f"{villager._name} has died as a(n) {villager.age}")
            
    def purge(self, amount):
        for _ in range(amount):
            self._villagers.pop(random.randint(1, self.population - 1))
            
    def census(self):
        census = {}
        
        for villager in self._villagers:
            if villager.age not in census.keys():
                census[villager.age] = 0
                
            census[villager.age] += 1
        
        print(census)
        
    def feed_villagers(self, villager):
        if self._food > 0:
            villager.eat()
            self._food -= 1
            return
        
        # Hunger pains
        villager.growing_pains()
        
    def do_job(self, villager):
        match villager.job:
            case "Hunter":
                food, tools_used = villager.hunt(self.season, self._tools)
                self._food += food
                self._tools -= tools_used
            case "Gatherer":
                food, resources, tools_used = villager.gather(self.season, self._tools)
                self._food += food
                self._resources += resources
                self._tools -= tools_used
            case "Craftsman":
                tools, resources_used = villager.craft(self._resources)
                self._tools += tools
                self._resources -= resources_used
            
    def advance_month(self):
        self._month += 1

        if self._month > 12:
            self._month = 1
            self._year += 1

            self.census()

        for i, villager in enumerate(self._villagers):
            villager.aging(self._month)
            
            self.feed_villagers(villager)
            
            self.do_job(villager)

            if villager.check_pregnancy() == "BIRTH":
                self._villagers.append(Villager(0, self._month))

            if villager._health <= 0:
                self.kill(i)
                
    
    def is_alive(self):
        return self.population > 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def date(self):
        return f"{self._month}-{self._year}"
    
    @property
    def season(self):
        match self._month:
            case self._month if self._month < 3:
                return "Winter"
            case self._month if self._month < 6:
                return "Spring"
            case self._month if self._month < 9:
                return "Summer"
            case self._month if self._month < 12:
                return "Fall"
            case self._month if self._month == 12:
                return "Winter"
        
    @property
    def population(self):
        return self._villagers.__len__()