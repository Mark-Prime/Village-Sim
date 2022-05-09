from email.policy import default
import random

class Villager:
    TOTAL = 0
    growing_pains = {
        "Child": 0.3,
        "Teenager": 1,
        "Young Adult": 2,
        "Adult": 2.5,
        "Older Adult": 3,
        "Senior": 5,
        "Elder": 7
    }
    pregnancy_pain = {
        "Teenager": 5,
        "Young Adult": 2,
        "Adult": 2,
        "Older Adult": 3
    }
    
    def __init__(self, age, birth_month):
        Villager.TOTAL += 1
        
        # TODO: Give the villager a real name.
        self._name = f"Villager {Villager.TOTAL}"
        
        self._age = age
        self._birth_month = birth_month
        
        self.is_pregnant = False
        self._months_pregnant = 0
        
        self._health = 100
        
        self._job = "Child"
        
        if 17 < self._age < 65:
            self.assign_job()
        
    def assign_job(self):
        match random.randint(1, 5):
            case 1 | 2:
                self._job = 'Hunter'
                return
            case 3 | 4:
                self._job = 'Gatherer'
                return
            case 5:
                self._job = 'Craftsman'
                return
        
    def check_birthday(self, month):
        if self._birth_month == month:
            self._age += 1
            if self._age == 18:
                self.assign_job()
                return
            
            if self._age == 65:
                self._job = 'Retired'
                return
            
    def hurt(self, amount):
        self._health -= amount
        
    def heal(self, amount):
        self._health = min(self._health + amount, 100)
        
    def eat(self):
        self.heal(random.randint(3, 5))
        
    def growing_pains(self):
        self.hurt(Villager.growing_pains[self.age])
                
    def check_pregnancy(self):
        if self.is_pregnant:
            self._months_pregnant += 1
            
            if self._months_pregnant > 8:
                self.is_pregnant = False
                
                # Pregnancy is painful
                self.hurt(Villager.pregnancy_pain[self.age])
                
                return "BIRTH"
            
            return
        
        if (random.randint(1, 100) < 2) and (12 < self._age < 65):
            self.is_pregnant = True
        
        return
                
    def aging(self, month):
        # Properly age the villager
        self.check_birthday(month)
        
        # General pain that comes with living
        self.growing_pains()
        
    def hunt(self, season, tools):
        match season:
            case "Winter":
                food = random.randint(0, 1)
            case "Spring":
                food = random.randint(0, 3)
            case "Summer":
                food = random.randint(0, 5)
            case "Fall":
                food = random.randint(0, 3)
                
        if tools:
            return food * 2, 1
        
        return food, 0
            
    def gather(self, season, tools):
        match season:
            case "Winter":
                food, resources = 0, random.randint(0, 1)
            case "Spring":
                food, resources = random.randint(0, 1), random.randint(0, 2)
            case "Summer":
                food, resources = random.randint(0, 2), random.randint(0, 3)
            case "Fall":
                food, resources = random.randint(0, 1), random.randint(0, 2)
                
        if tools:
            return round(food * 1.5), round(resources * 1.5), 1
        
        return food, resources, 0
            
    def craft(self, resources):
        tools = random.randint(0, 3)
        resources_used = random.randint(0, 6)
        if resources >= resources_used:
            return tools, resources_used
        
        return 0, 0
        
    @property
    def job(self):
        return self._job
        
    @property
    def age(self):
        match self._age:
            case self._age if self._age < 13:
                return "Child"
            case self._age if self._age < 18:
                return "Teenager"
            case self._age if self._age < 30:
                return "Young Adult"
            case self._age if self._age < 45:
                return "Adult"
            case self._age if self._age < 65:
                return "Older Adult"
            case self._age if self._age < 85:
                return "Senior"
            case self._age:
                return "Elder"