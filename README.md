# andys_dinosaur_zoo
A terminal python game about dinosuars

## Project Scope
This program will spawn a random dinsoaur.  You will get a chance to catch the dinosaur.  If you catch the dinosaur it goes to your zoo.  A carnivore can eat you.  A herbavore can stomp you.  You can run away.  The dinsosaur can escape.


## The zoo

The zoo will have dinsosaur pens.  
The name of the zoo is the 'Dino Zoo' by default.
The user can give the zoo a custom name



## The user

The user should be able to see how many dinosaurs are in the zoo.  The user should be able to see how many carnivores or herbivores are in the zoo.  The user should be able to see how many of each type of dinosaur they have captured.


# Phase 1 Building the zoo

The user can set the name of their zoo.  The user can name the dinsosaurs.  The user can name themselves.

*  When a user adds a dinsosaur to the zoo, they get prompted if they want to name the dinosaur
 *  When a user adds a dinosaur to the zoo if there is no pen for the dinosaur create the pen with the name of the dinosaurs scientific name

# Phase 2 The dinosaur

* The Dinosaur have a scientific name
* The Dinosaurs have a custom name
* The Dinosaurs have a Type 
  * The Dinosaurs Types: 
            * Grassland ( strong to marine, weak to Mountain)
            * Mountain ( strong to grassland, weak to marine)
            * Marine ( strong to mountain, weak to Grassland)
            * Ancient ( is not strong or weak against anything)
* The Dinosaurs have a Classification
  * The Dinosaurs Classification:
    * Carnivore
    * Herbavore
* The Dinosaur has an Attack Number
* The Dinsosuar has a Defense Number
* The Dinosaur has a Health number

# Phase 3 The Player

* The Player has a name
* The Player has a team of dinosaurs
  * The team is up to 3 dinosaurs
* The Player has a location (where they are)
* The Player has a zoo

# Phase 4 Locations
* The user by default starts at home, or the name of its zoo
* Different locations can spawn different kinds of dinosaurs
  * North America
    * Canada
    * Montana
    * Texas
  * South America
    * Brazil
    * Chile
    * Argentina
  * Aisa
    * China
    * Russia
    * India
  * Europe
    * Great Britan
    * Germany
    * France
  * Africa
    * South Africa
    * Egypt
    * Ghana
  * Australia
    * East Australia
    * West Australia
  * Antartica
* A player may be in only 1 location
* When a player enters home all of their dinosaur team are healed

# Phase 5 Building the dinosaur combat engine

* The user has a dinosaur team.
* The first dinosaur on the team is always the dinosaur chosen for combat
* A user may switch a dinosaur 
* The dinosaur has an Attacking phase
* The dinosaur has a Defense phase
  * The dinosaur Attacking and Defending go into a Combat Phase
    * During the combat phase the attacking dinosaurs Attack number is added to the result of a random number between 1 and 6
    * During the combat phase the defending dinosaurs Defense number is added to the result of a random number between 1 and 6
    * If the attack is greater than the defense than subtract health from the defending dinosaur equal to the difference of the attacking attack number and the defending defense number
    * The dinosaur who is attacking becomes the defending dinosaur
    * The dinosaur who is defending becomes the attacking dinosaur
    * If the attack is greater than the defense than subtract health from the defending dinosaur
   * The Combat Phase ends
   
* After each phase health is subtracted from the losing dinosaur

# Phase 6 Building the dinosaur capture engine

* The user may attempt to capture the dinosaur
  * The capture will be determined by input: how much health the dinosaur to be captured has, against the chance of being captured (algorithm)
  * If the dinosaur is captured it is sent to the users zoo
