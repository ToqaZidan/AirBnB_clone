
# AirBnB clone - The console

The AirBnB clone project, the goal of this project is to deploy on the server a simple copy of the AirBnB website. We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

![hBnB](https://raw.githubusercontent.com/monoprosito/AirBnB_clone/feature/console/hBnB.png)

## Learning Objective

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

### Description of the command interpreter:
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:

- show
- create
- update
- destroy
- count
And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:

- Creating new objects (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Doing operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroying an object

### How to start it
These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.







## Installation

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
```
git clone https://github.com/ToqaZidan/AirBnB_clone.git
```
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

### How To use it/ Excution

- our shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

- But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
...... to be continued 




## Authors

- [Mohamed Fathy Saied](https://github.com/mohamed-Fathy1)
- [Toqa Zidan](https://github.com/ToqaZidan)
