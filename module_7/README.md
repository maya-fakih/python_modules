*This project has been created as part of the 42 curriculum by mfakih.*

# DataDeck
## Master the Art of Abstract Card Architecture
What We Built
We built a modular card game engine that demonstrates key object-oriented design patterns in Python. The project is split into 5 exercises, each building on the previous one.
---
## Project Architecture
text
Repository Root (Package)
├── ex0/ - Foundation Layer (Abstract Base Classes)
├── ex1/ - Implementation Layer (Polymorphism)
├── ex2/ - Ability Layer (Multiple Inheritance)
├── ex3/ - Engine Layer (Strategy + Factory Patterns)
└── ex4/ - Platform Layer (Interface Composition)
---
## Key Concepts Learned
### 1. Running at Package Level
We run everything using:

bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
Why?

The -m flag tells Python to run a module as part of a package

This requires __init__.py files in each directory

Enables proper absolute imports between exercises: from ex0.Card import Card

Without this, Python doesn't recognize folders as packages

### 2. Abstract Base Classes (ABC)
What they are: Templates that define WHAT methods a class MUST have, but not HOW they work.

Why we used them:

Ensures every card has a play() method

Forces consistency across different card types

You cannot create an instance of an abstract class directly

### 3. Polymorphism
What it is: The same interface working with different underlying types.

In our project:

A Deck can hold Creatures, Spells, and Artifacts

The deck doesn't care what card type it is - it just calls play()

Each card type responds differently to the same method call

### 4. Multiple Inheritance
What it is: A class inheriting from more than one parent class.

In our project:

EliteCard inherits from Card, Combatable, AND Magical

Gets card properties from Card

Gets combat abilities from Combatable

Gets magic abilities from Magical

Must implement ALL abstract methods from ALL parents

### 5. Interface Segregation
What it is: Small, focused interfaces instead of one giant interface.

In our project:

Combatable only deals with combat

Magical only deals with magic

Rankable only deals with rankings

Classes pick only the interfaces they need

### 6. Strategy Pattern
What it is: Swapping algorithms/behaviors at runtime.

In our project:

GameStrategy defines how to play

AggressiveStrategy is one concrete strategy

The engine can use ANY strategy without changing its code

### 7. Abstract Factory Pattern
What it is: Creating families of related objects without specifying concrete classes.

In our project:

CardFactory defines how to create cards

FantasyCardFactory creates fantasy-themed cards

The engine asks for cards without knowing how they're made

Why This Architecture Works
Separation of Concerns
Each exercise handles ONE thing:

ex0: The card template

ex1: Different card types + deck management

ex2: Abilities through interfaces

ex3: Game rules and card creation

ex4: Competition and rankings

Extensibility
Want to add a new card theme? Create a new factory.
Want a new playstyle? Create a new strategy.
Want a new ability? Create a new interface.
No existing code breaks.

Reusability
Combatable can be used by any card that fights

Magical can be used by any spellcaster

The Deck works with ANY card type

Testability
Each piece can be tested in isolation:

Test factories with dummy strategies

Test strategies with dummy cards

Test the engine with any combination

The Big Picture
We started with a simple abstract card (ex0) and ended with a full tournament platform (ex4) where cards can:

Be played like any card

Fight like warriors

Cast spells like wizards

Earn rankings like competitors

All this without changing the core Card class from ex0 - that's the power of good abstract design!

