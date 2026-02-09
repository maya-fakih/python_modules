*This project has been created as part of the 42 curriculum by mfakih.*

# What is Polymorphism?
---
Polymorphism means "many forms." In programming, it allows objects of different types to be treated as objects of a common type.

In this project:

JSONAdapter, CSVAdapter, and StreamAdapter are all types of ProcessingPipeline

They all have the same methods (process(), add_stage())

But each processes data differently (JSON, CSV, or Stream data)

The NexusManager can work with any pipeline without knowing which specific type it is

# What are Protocols?
---
Protocols are like contracts. If a class has the methods defined in the protocol, it satisfies that protocol - no inheritance needed!

In this project:
The ProcessingStage protocol says: "Any class with a process() method can be a processing stage."
So InputStage, TransformStage, and OutputStage all work as stages because they have a process() method.

How the System Works
Three pipeline types handle different data:

JSONAdapter: Processes dictionary data

CSVAdapter: Processes string data

StreamAdapter: Processes list data

Three processing stages transform the data:

InputStage: Identifies what type of data it is

TransformStage: Processes the data based on its type

OutputStage: Displays the results appropriately

The manager (NexusManager) coordinates everything and treats all pipelines the same way

Key Features
One interface, multiple implementations: Same process() method works on JSON, CSV, and Stream data

Flexible stages: Any class with a process() method can be added as a stage

Error recovery: System handles invalid data and rec gracefully

Extensible: Easy to add new pipeline types or processing stages

Running the Project
bash
python pipeline_system.py
The system will show:

JSON data being processed as temperature readings

CSV data counting user actions

Stream data calculating averages

Error handling when invalid data is encountered

Why This Matters
This demonstrates how to build systems that are:

Easy to maintain: Changes to one part don't break others

Easy to extend: Add new formats without rewriting existing code

Flexible: Components work together through clear interfaces

Reliable: Error handling keeps the system running

