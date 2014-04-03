tobiont
=======


Create a creature/evolution simulation in the vein of Conway's Game of Life and the many evolution simulators that arose afterward. The proposed simulation should strive to maximize the freedom of action of the the creature through a large scale dynamic simulation board and a large instruction set for the creatures.

I premise the project on the theory that evolution simulators that I've seen suffer from limited complexity which in turn limits the complexity or range of behaviors/states which can arise from the simulation, resulting in them too quickly arriving at end-state equilibrium or an optimally competitive variant of the creature. By increasing the complexity of the simulation I hope to see more advance or interesting behaviors or patterns arise from the creatures.

The specific core goals will be the following:

- A simulated creature who can execute a modern programing language equivalent instruction set, which is to say they're commands/ability code should have the same capabilities as a modern high level programming language. Including loops, logic branching, variables.

- A large and dynamic game board with localized differences such as food/resource types or availability and changes over time such as increasing or decreasing resource generation. This is all to differentiated biomes to encourage specialization of the creature.

- Optimization. A key to a complex simulation is getting it to run quickly enough to be useful. The subsystems and system design work required for a fast simulation will be a core of the work on this project including fast interpretation of creature code.
