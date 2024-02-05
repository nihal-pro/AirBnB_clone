# Airbnb project

## description of the project

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization,
  serialization and - - - - deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## description of the command interpter:

- execute console py `./console.py`
- command:

  - EOF : To Exit The program
  - quit : To Exit The program
  - help : to see The command line.
  - `Enter + empty line ` : shouldn’t execute anything

- Console v1.0:

- create: to Creates a new instance
  Usage: `create <name Class>` it will give you your id.

- show: to Prints the string representation of an instance based on the class name and id.
  Usage: `show <name Class> <id>`.

- destroy: Deletes an instance based on the class name and id
  Usage: `destroy <name Class> <id>`

- all: Prints all string representation of all instances based or not on the class name.
  Usage: `all <name Class>` or `all`.

- update: Updates an instance based on the class name and id by adding or updating attribute
  Usage: `update <name Class> <id> email "aibnb@mail.com"`

console update:

- Usage :
  <class_name>.all() : print all name insttances of class.
  <class_name>.count() : to count membre of insttances of class.
  <class_name>.show("id") : to show membre of insttance of class
  <class_name>.destroy("id") : to destroy membre of insttance of class
  <class_name>.update("id", "attribute", value) : to destroy membre of insttance of class
  <class_name>.update("id", dictionary) : to destroy membre of insttance of class
