
# QUESTION 1
class Ankara:
    def __init__(self, mood, temperature):
        self.mood = mood
        self.temperature = temperature
    def predict_pattern_changes(self):
        if self.temperature >= 20 and self.mood == "happy":
            return "Wear a light and more patterned ankara"
        
        elif self.temperature < 20 and self.mood == "sad":
            return "Wear a heavy and less patterned ankara"
        
        else:
            return "No changes in pattern"
        

# QUESTION2
class Migration:
    def __init__(self, weather_pattern, river_level, peditor_location):
        self.weather_pattern = weather_pattern
        self.river_level = river_level
        self.preditor_location =  peditor_location

    def predict_migration(self):
        river_level_in_feets = 2000
        current_weather = "rainy"
        if self.river_level == river_level_in_feets and self.weather_pattern == current_weather:
            return "Migration will not occur"
        
        else:
            return "Migration will occur"
        
    def new_location(self, current_location):
        self.current_location = current_location
        return "Migration from ${self.preditor_location} to {self.current_location}"    
    


# QUESTION3
class film:
    def __init__(self,title,cast,shooting_schedule,budget) :
        self.title= title
        self.cast=cast
        self.shooting_schedule=shooting_schedule
        self.budget=budget
class producer:
    def __init__(self):
        self.projects=[]
    def add_projects(self,film):
        self.projects.append(film)
    def remove_projects(self,film) :
        self.projects.remove(film)
    def get_project_by_title(self,title):
        for project in self.projects:
            if project.title == title:
               return project
        return None
    def get_project_cast(self,title):
        project = self.get_project_by_title(title)
        if project:
            return project.cast
        return None
    def updated_project_schedule(self,title,shooting_schedule):
        project = self.get_project_by_title(title)
        if project:
            project.shooting_schedule = shooting_schedule
    def updated_project_budget(self,title,budget) :
        project = self.get_project_by_title(title)
        if project:
            project.budget = budget



# QUESTION4
class Fruit:
    def __init__(self, type, power, effect):
        self.type = type
        self.power = power
        self.effect = effect

    
class Baobab_tree:
    def __init__(self, fruit):
        self.fruit.append(fruit) 

    def prediction(self):
        return "Type of fruit to be bored next season"   

    def fruit_power(self):
        return "type of power the fruit possesses"

    def fruit_effect(self):
        return "the effect the fruit has when consumed"   



# QUESTION5
           
class Drum:
    def __init__(self, material, size):
        self.material = material 
        self.size = size

    def playing_sound(self):
        print ("The drum")  

class Djembe (Drum):
    def playing_sound(self):
        return "The djembe with range of tones"   
       
class Talking_drum(Drum):
    def playing_sound(self):
        return "Talking drum mimics human speech"     

class Baogaraubou(Drum):
    def playing_sound(self):
        return "Baugaraubou has deep rich bass tones"  

djembe = Djembe("wood", "medium")
talking_drum = Talking_drum("animal skin", "small")
baogaraubou = Baogaraubou("metal", "large")

print(djembe.playing_sound())  
print(talking_drum.playing_sound())  
print(baogaraubou.playing_sound()) 




#...Python...Assesment2...Classes...

# 1. question 

class AncestralStories:
    def __init__(self, length, lesson, age_group): 
        self.length = length
        self.lesson = lesson
        self.age_group = age_group

    def story_details(self):
        return f"the length of the story is {self.length}, it's lesson is {self.lesson} and is ment for {self.age_group}" 


class StoryTeller(AncestralStories):
    def __init__(self, length, lesson, age_group, name):
        super().__init__(length, lesson, age_group)
        self.name = name

    def get_story_details(self):
        details = super().story_details()
        return f"{details}, and the translator is {self.name}"   


class Translator(AncestralStories):
    def __init__(self, length, lesson, age_group, name, language):
        super().__init__(length, lesson, age_group)   
        self.name = name
        self.language = language  
    def translate_story(self):
        translated = "Audience language choice"
        return f"{translated}"
    
stories = AncestralStories("long", "encouraging", "children")
print(stories.story_details())

teller = StoryTeller("small", "sad", "elders", "Bobo")
print(teller.get_story_details())

translator = Translator("medium", "Motivative", "youths", "Agogo", "swahili")
print(translator.translate_story())




# 2. question

class Recipe:
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information):
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_information = nutritional_information

    def know_recipes(self):
        return f"ingredients is {self.ingredients}, preparation time is {self.preparation_time}, cooking method is {self.cooking_method} and nutritional information is {self.nutritional_information}"    


class MoroccanRecipe(Recipe):
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information, taste, oil):
        super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
        self.taste = taste
        self.oil = oil
        

    def find_taste(self):
        return f"Moroccan food has a {self.taste} test, and is cooked using {self.oil}"   


class EthiopianRecipe(Recipe):
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information, flavour, color):
        super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
        self.flavour = flavour
        self.color = color
    

    def fing_flavour(self):
        return f"Ethiopian food is sour, has a {self.flavour} flavour and is mostly {self.color} in color"  


class Nigerianrecipe(Recipe):
    def __init__(self, ingredients, preparation_time, cooking_method, nutritional_information, preservation_method, texture):
        super().__init__(ingredients, preparation_time, cooking_method, nutritional_information)
        self.preservation_method = preservation_method
        self.texture = texture
        

    def find_texture(self):
        return f"Nigerian food has a {self.preservation_method} reservation method and is always {self.texture} in texture"          




food = Recipe("too spicy", "2 hours", "long", "too informative")    
print(food.know_recipes())

taste = MoroccanRecipe("too spicy", "2 hours", "long", "too informative", "sweet", "coconut oil")
print(taste.find_taste())

flavour = EthiopianRecipe("too spicy", "2 hours", "long", "too informative", "pungent", "brown")
print(flavour.fing_flavour())

texture = Nigerianrecipe("too spicy", "2 hours", "long", "too informative", "long", "rough")
print(texture.find_texture())




# question 3

class Species:
    def __init__(self, name, diet, lifespan, month):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.month = month

    def track(self):
        if self.month=="dry":
            return "Animal mostly moves from East to West"
        else:
            return "Animals mostly move from North to South"
        
        
class Predator(Species):
    def __init__(self, name, diet, lifespan, month, prey):
        super().__init__(name, diet, lifespan, month)
        self.prey = prey

    def track_predator(self):
        return f"The prey was {self.prey}, its diet is {self.diet} and it was born on {self.month} season"
    

class Prey(Species):
    def __init__(self, name, diet, lifespan, month, predator):
        super().__init__(name, diet, lifespan, month)
        self.predator = predator

    def track_prey(self):
        return f"The lifespan was {self.lifespan}, and the preditor was {self.predator}"
    


animal_one = Species("antelope", "grass", "10 years", "bufallo")
print(animal_one.track())

animal_two = Predator("lion", "grass", "70 years", "dry", "bear")
print(animal_two.track_predator())

animal_three = Prey("gazzel", "herbs", "50 yeras", "wet", "cheetah")
print(animal_three.track_prey())



# question4

class Festival:
    def __init__(self, musical_style, instruments, festival_lineup, schedule, stage_arrangement):
        self.musical_style = musical_style
        self.instruments = instruments
        self.festival_lineup = festival_lineup
        self.schedule = schedule
        self.stage_arrangement = stage_arrangement

    def know_instruments(self):
        return f" musical style:{self.musical_style}\n instruments:{self.instruments}\n festival lineup:{self.festival_lineup}\n schedule:{self.schedule}\n stage arangement:{self.stage_arrangement}."
    

class Artist(Festival):
    def __init__(self, musical_style, instruments, festival_lineup, schedule, stage_arrangement, name, country):
        super().__init__(musical_style, instruments, festival_lineup, schedule, stage_arrangement)  
        self.name = name
        self.country = country

    def know_artist(self):
        return f"The artist was {self.name} she comes from {self.country} her musical instrument was {self.instruments}."    
    

class Performance(Festival):
    def __init__(self, musical_style, instruments, festival_lineup, schedule, stage_arrangement, musical_theatre, magic):
        super().__init__(musical_style, instruments, festival_lineup, schedule, stage_arrangement)   
        self.musical_theatre  = musical_theatre
        self.magic = magic

    def know_performance(self):
        return f"The performance done by the artists were {self.musical_theatre} acompanied by {self.magic}."    


class Stage(Festival):
    def __init__(self, musical_style, instruments, festival_lineup, schedule, stage_arrangement, stage, theatre,):
        super().__init__(musical_style, instruments, festival_lineup, schedule, stage_arrangement) 
        self.stage = stage
        self.theatre = theatre

    def type_of_stage(self):
        return f"The type of stage used was {self.stage}, and the theatre was {self.theatre}."        




music = Festival("Digital", "piano", "long", "automatic","triangular")
print(music.know_instruments())

singer = Artist("opera", "guitar", "long", "rotation", "circular", "Amilolo", "Uganda")
print(singer.know_artist())

perform = Performance("opera", "guitar", "long", "rotation", "circular", "stand up comedy", "Illusion")
print(perform.know_performance())

stages = Stage("opera", "guitar", "long", "rotation", "oval", "thrust stages", "arena")
print(stages.type_of_stage())




# question5


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity


product1 = Product('Bread', 50, 3)
product2 = Product('Mango', 15, 5)
product3 = Product('Toothpaste', 100, 2)

total_value = 0

for product in [product1, product2, product3]:
    total_value += product.calculate_total_value()

print('Total value of all products:', total_value)



class Product:
    def __init__(self, name, price, quantity):
      self.name = name
      self.price = price
      self.quantity = quantity
    
    def calculate_total_value(self): 
      return self.price * self.quantity
 
product1 = Product('Bread', 50, 3)
product2 = Product('Mango', 15, 5)
product3 = Product('Toothpaste', 100, 2)

totalValue1 = product1.calculate_total_value()
totalValue2 = product2.calculate_total_value()
totalValue3 = product3.calculate_total_value()
print('Total value of product 1:', totalValue1)
print('Total value of product 2:', totalValue2)
print('Total value of product 3:', totalValue3)
    






