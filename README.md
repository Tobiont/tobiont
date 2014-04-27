tobiont
=======

#Overview
Tobiot is an evolution simulation which attempts to go beyond the existing or previously do research in this area and create a simulation where very complex behaviors can arise. This is achieved in a few specific ways:
The simulated creature’s logic or brain will run a full, turing-complete, instruction set which parallels a modern high-level programming language.
This simulation gameboard will be large and dynamic to create differentiation and specialization pressures in the simulated creatures.

###History
[Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life) was interesting because of the dynamism and complexity that arose from a simulation with very succinct and simple rules. As simulators grew more advanced they more frequently modeled themselves on real-world biological systems and due to that increasing complexity they also reduced in scope due to computing power. Eventually simulations were attempting to model a few dozen creatures at most and if they were run for any length of time, the simulations quickly reached a stable end-state equilibrium and progress no further.

While some research is still being done on Conway’s Game of Life, and biologists are certainly still using models to analyse and predict real world ecologies, little research is still being done or has been done on life simulators in the last decade.

###Goals
The primary goal of this project are to see if more complex behaviors will arise from an evolution simulation if we increase the simulation’s complexity. To catalog those behaviors and try to find parallels to the real world or unique new behaviors not found in nature.

A hypothetical example of some things we may look for:
Do behaviors of simulated creatures begin to fall into common predator-prey relationships
Do recognizable real world programming patterns ever arise from the simulated creature’s code
###Non-Goals
When neccessary this simulation will adopt real world paradigms such as the need for creatures to eat. But we are not attempting to create a simulation which mirrors real life or overly adopts real world patterns without reason.

As an example, a requirement to eat may be adopted for the purpose of applying selection pressure on the simulated creature. Without some pressures on the creatures, they would just be running random code to no end. But in contrast we may choose to not implement any kind of physics for the simulation if the only goal of physics is to mirror reality.

##Top level systems
###Gameboard
The gameboard should be a square grid upon which the creatures act. It is responsible for generating food for the creatures and for handling movement on the game board grid. The gameboard can be described as a taxonomy of large regions which contain local biomes which are made up of individual gameboard cells. Each cell is a tile of the grid which may or may not contain one creature.

The gameboard should generate resources variably based on regional and local variables. For example a region may simulate ‘seasons’ by increasing and diminishing overall resource production in a long cycle, and this regional season will affect the overall output of all biomes in the region

An individual biome may vary resource production in many ways based on unique patterns. For example a biome may generate resources like ‘rain’ which constantly dribbles out small amounts all over the biome. Or it may resemble the ocean bottom’s thermal vents by having a few very productive spouts of resources in a fixed places and a pattern of spreading accumulates resources out from the spouts.

Biomes should also have the ability to manipulate objects upon them. For example a biome might resemble a river by moving tiles in a certain direction every few tics. 

###Creature
The creature should be an autonomous object on the gameboard who will be capable of moving, interacting with the game board, and interacting with other creatures in proximity to itself.

A creature will operate based on a list of code or code-like instructions and ‘run’ these instructions to perform actions. 

####Instruction set
Each individual creature should have an instruction set or code that defines how it operates. This should include standard high level programming language idioms such as Branching statements, loops, etc. Details below.

List of command words (elements of the language):  if, else, for and while loops, break, creating temporary variables, assigning values to variables, AND, OR, NOT, = 
	
More artificial commands: eat, move, attack 

Based on external or internal factors, the Creature’s code should be manipulatable

##Ancillary Systems
###Monitor/Visualizer
Takes the raw gameboard and renders the activity in a human readable manner. The purposes is to provide a tool for developers to monitor the simulation’s activity.

###Creature Optimizer
Due to the randomness of mutation, each creature’s instruction set is naturally going to contain a lot of cruft and commands which are essentially useless or no-ops. The optimizer will take a creature’s instruction set and render it down to fast implementation code; reducing ‘no op’ commands to a sleep command, simplifying loops, etc. This allows the simulation to run faster while preserving continuous time for the creature in ticks.

###Simulation Analyzer
Keeps track of each generation of creature, their instruction sets, lineages, and populations. The purpose here is to enable the analysis of instruction sets to see which creatures were most effective, and to capture any interesting behaviors.

##Specific Requirements
###Creature:
- Can move on the game board
- Can consume resources
- Can reproduce (create a new empty creature)
- Can transfer code to its young or other creatures
- Can “see” the spaces on the gameboard around it
- Can attack other creatures (delete their code)
- Is programmable

###Gameboard:
- Generates resources
- Defines biomes and ‘weather’ through the biome-specific resource generation method.
- Handles Creature movement

###Monitor:
- Displays gameboard
- Displays population, time
- Has controls for setting the initial conditions of the simulation
- Has controls for starting and stopping the simulation, changing the speed

###Creature Optimizer:
- Cuts out bad syntax
- Simplifies verbose code
- Defines a metric for the difference between two creatures’ code
  - Defines some minimum difference between creatures of different “species”

###Simulation Analyzer:
- Keeps track of evolutionary trees:
  - Tracks lineages and the time at which each species develops
  - Notes average lifespan of each species
  - Tracks the population of each species
