
// QUESTION1
class Ankara{
    constructor(temperature, mood){
        this.temperature = temperature
        this.mood = mood
    }
    getColor(){

    if(this.temperature >= 20 && this.mood < 5){
        return `Wear a light clothe`;
    }

    else{
        return `Wear a heavy clothe`;
    }
}
}


clothe = new Ankara(15, 2)    
console.log(clothe.getColor());


// // QUESTION2
class Migration{
    constructor(weatherPattern, riverlevel){
        this.weatherPattern = weatherPattern
        this.riverlevel = riverlevel
    }
    migration(){
        if(this.weatherPattern == "dry" && this.riverlevel == "low" ){
            console.log("Weather is high");
        }

        else{
            console.log("Weather is low");
        }
    }
}
const migrationInstance = new
Migration("dry", "low");
migrationInstance.migration()


// QUESTION4
class Baobab{
    constructor(season,fruitType,power){
        this.season=season
        this.fruitType=fruitType
        this.power=power
    }
    predictFruitType(){
        if (this.season=="dry"){
            console.log(this.fruitType="small");
            console.log(this.power=0);
        }
        else if(this.season=="wet"){
            console.log(this.fruitType="large");
            console.log(this.power=1);
        }
        else{
            return "Unable to predict changes"
        }    
    }
    predictEffect(){
        if (this.power==0){
            return "The person can fly"
        }
        else if (this.power==1){
            return "The person can sing"
        }
    }
    }
 
 
 let baobab1=new Baobab("dry","large",0)
 baobab1.predictFruitType()
 console.log(baobab1.predictEffect())   



// QUESTION5
class Drum{
    constructor(material,size){
        this.material=material
        this.size=size
    }
    getSound(){
        console.log(`${this.constructor.name}is of ${this.size }size and is made of ${this.material} and makes ${this.sound}`)
    }
}
 class Djembe extends Drum{
    sound="wide range of tones"
 }


class TalkingDrum extends Drum{
    sound="Mimic human speech"
 }


class Bougaraubou extends Drum{
    sound="Produces deep rich bass tones"
 }


let  drum3=new Bougaraubou("leather","big")
drum3.getSound() 
let  drum2=new TalkingDrum("skin","medium")
drum2.getSound()
let  drum1=new Djembe("wooden","small")
drum1.getSound()



// ...JavaScript...

class AncestralStories{
    constructor(length, lesson, ageGroup){
        this.length = length
        this.lesson = lesson
        this.ageGroup = ageGroup
    }
    storyDetails(){
        return `the length of the story is ${this.length}, it's lesson is ${this.lesson} and is ment for ${this.ageGroup}`
    }
}
class StoryTeller extends AncestralStories{
    constructor(length, lesson, ageGroup, name){
        super(length, lesson, ageGroup)
        this.name = name
    
    }
    getStoryDetails(){
        details = super.getStoryDetails()
        return `${details}, and the translator is ${this.name}`  
    }    
}

class Translator extends AncestralStories{
    constructor(length, lesson, ageGroup, name, language){
      super(length, lesson, ageGroup)   
        this.name = name
        this.language = language  
    }
    translateStory(){
        translated = "Audience language choice"
        return `translated swahili`
    }
}        
    
stories = new AncestralStories("long", "encouraging", "children")
console.log(stories.storyDetails());

teller = new StoryTeller("small", "sad", "elders", "Bobo")
console.log(teller.storyDetails());

translated = new Translator("medium", "Motivative", "youths", "Agogo", "swahili")
console.log(translated.translateStory());




// question 2

class Recipe{
    constructor(ingredients, preparation_time, cooking_method, nutritional_information){
        this.ingredients = ingredients
        this.preparation_time = preparation_time
        this.cooking_method = cooking_method
        this.nutritional_information = nutritional_information
    }
    know_recipes(){
        return `ingredients is ${this.ingredients}, preparation time is ${this.preparation_time}, cooking method is ${this.cooking_method} and nutritional information is ${this.nutritional_information}`    
    }
}
class MoroccanRecipe extends Recipe{
    constructor(ingredients, preparation_time, cooking_method, nutritional_information, taste, oil){
        super(ingredients, preparation_time, cooking_method, nutritional_information)
        this.taste = taste
        this.oil = oil
    } 

    find_taste(){
        return `Moroccan food a ${this.taste} test, and is cooked using ${this.oil}`   
    }
}

class EthiopianRecipe extends Recipe{
    constructor(ingredients, preparation_time, cooking_method, nutritional_information, flavour, color){
        super(ingredients, preparation_time, cooking_method, nutritional_information)
        this.flavour = flavour
        this.color = color
    }

    find_flavour(){
        return `Ethiopian food is sour, has a ${this.flavour} flavour and is mostly ${this.color} in color` 
    }
}
class Nigerianrecipe extends Recipe{
    constructor(ingredients, preparation_time, cooking_method, nutritional_information, preservation_method, texture){
        super(ingredients, preparation_time, cooking_method, nutritional_information)
        this.preservation_method = preservation_method
        this.texture = texture       
    }
    find_texture(){
        return `Nigerian food has a ${this.preservation_method} reservation method and is always ${this.texture} in texture`
    }        
}



food = new Recipe("too spicy", "2 hours", "long", "too informative")    
console.log(food.know_recipes());

taste = new MoroccanRecipe("too spicy", "2 hours", "long", "too informative", "sweet", "coconut oil")
console.log(taste.find_taste());

flavour = new EthiopianRecipe("too spicy", "2 hours", "long", "too informative", "pungent", "brown")
console.log(flavour.find_flavour());

texture = new Nigerianrecipe("too spicy", "2 hours", "long", "too informative", "long", "rough")
console.log(texture.find_texture());



// question 3

class Species{
    constructor(name, diet, lifespan, month){
        this.name = name
        this.diet = diet
        this.lifespan = lifespan
        this.month = month
    }

    track(){
        if (this.month == "dry"){
            return "Animal mostly moves from East to West"
        }
        else{
            return "Animals mostly move from North to South"
        }
    }
} 
        
class Predator extends Species{
    constructor(name, diet, lifespan, month, prey){
        super(name, diet, lifespan, month)
        this.prey = prey
    }

    track_predator(){
        return `The prey was ${this.prey}, its diet is ${this.diet} and it was born on ${this.month} season`
    }
}
    

class Prey extends Species{
    constructor(name, diet, lifespan, month, predator){
        super(name, diet, lifespan, month)
        this.predator = predator
    }

    track_prey(){
        return `The lifespan was ${this.lifespan}, and the preditor was ${this.predator}`
    }
}


animal_one = new Species("antelope", "grass", "10 years", "bufallo")
console.log(animal_one.track())

animal_two = new Predator("lion", "grass", "70 years", "dry", "bear")
console.log(animal_two.track_predator())

animal_three = new Prey("gazzel", "herbs", "50 yeras", "wet", "cheetah")
console.log(animal_three.track_prey())



// question 4

class Festival{
    constructor(musical_style, instruments, festival_lineup, schedule, stage_arrangement){
        this.musical_style = musical_style
        this.instruments = instruments
        this.festival_lineup = festival_lineup
        this.schedule = schedule
        this.stage_arrangement = stage_arrangement
    }

    know_instruments(){
        return `musical style:${this.musical_style}\n instruments:${this.instruments}\n festival lineup:${this.festival_lineup}\n schedule:${this.schedule}\n stage arangement:${this.stage_arrangement}.`
    }
}
    

class Artist extends Festival{
    constructor(musical_style, instruments, festival_lineup, schedule, stage_arrangement, name, country){
        super(musical_style, instruments, festival_lineup, schedule, stage_arrangement)  
        this.name = name
        this.country = country
    }

    know_artist(){
        return `The artist was ${this.name} she comes from ${this.country} her musical instrument was ${this.instruments}.`
    }   
}
    

class Performance extends Festival{
    constructor(musical_style, instruments, festival_lineup, schedule, stage_arrangement, musical_theatre, magic){
        super(musical_style, instruments, festival_lineup, schedule, stage_arrangement)   
        this.musical_theatre  = musical_theatre
        this.magic = magic
    }

    know_performance(){
        return `The performance done by the artists were ${this.musical_theatre} acompanied by ${this.magic}.`
    }
} 


class Stage extends Festival{
    constructor(musical_style, instruments, festival_lineup, schedule, stage_arrangement, stage, theatre,){
        super(musical_style, instruments, festival_lineup, schedule, stage_arrangement) 
        this.stage = stage
        this.theatre = theatre
    }

    type_of_stage(){
        return `The type of stage used was ${this.stage}, and the theatre was ${this.theatre}.`
    } 
}    




music = new Festival("Digital", "piano", "long", "automatic","triangular")
console.log(music.know_instruments())

singer = new Artist("opera", "guitar", "long", "rotation", "circular", "Amilolo", "Uganda")
console.log(singer.know_artist())

perform = new Performance("opera", "guitar", "long", "rotation", "circular", "stand up comedy", "Illusion")
console.log(perform.know_performance())

stages = new Stage("opera", "guitar", "long", "rotation", "oval", "thrust stages", "arena")
console.log(stages.type_of_stage())



// question5






class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
    calculateTotalValue() {
      return this.price * this.quantity;
    }
  }

  const product1 = new Product('Bread', 50, 3);
  const product2 = new Product('Mango', 15, 5);
  const product3 = new Product('Toothpaste', 100, 2);

  const totalValue1 = product1.calculateTotalValue();
  const totalValue2 = product2.calculateTotalValue();
  const totalValue3 = product3.calculateTotalValue();
  console.log('Total value of product 1:', totalValue1);
  console.log('Total value of product 2:', totalValue2);
  console.log('Total value of product 3:', totalValue3);

