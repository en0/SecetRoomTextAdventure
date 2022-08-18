# TheSecretRoom

A text based adventure game.

## Goal

Create a small text based adventure game in python.

The game will take the player through a house to find a secret room. The player will need to examine
objects in the scene to find tools that will allow them to progress.

### Game Play

The game will provide a step based cycle.

Step 1: The player will be given a description of their current location.
Step 2: The player will be given a list of actions that they can do.
Step 3: The player will select an action by typing it into a prompt.

Depending on the command, the system will branch in one of 3 directions:

Action GO:
Step 4: the system will update the player's locations details
Goto Step 1

Action EXAMINE:
Step 4: the system will provide details about the object being examine.
Goto Step 3

Action USE:
Step 4: the system will attempt to use a inventory item on an object.
Step 5: The system will update the available list of actions if needed
Goto Step 3


Actions:

- go [direction]
- examine [object]
- use [item] on object

# Design

Taking the above game play as the only source of business requirements, lets outline the different
components of the system.

## Core

These are components of the system that directly solve the game rules.

### Entities:

These are fundimentally abstract types

- Player
- Room
- Object
- Item

### Use Cases

- Player Moves Use Case
- Player Examines Use Case
- Player Uses Use Case

## Infra

These are components of the system that apply to how we interact with the game.

### Console

...

