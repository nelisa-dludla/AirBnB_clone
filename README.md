# Hbnb

This project is an Airbnb clone developed as part of a ALX programming assignment. 
The goal is to implement various functionalities such as creating and managing instances of different classes, 
serializing and deserializing data, and building a command-line interpreter to interact with the system.

## Command Interpreter - console.py

The command interpreter, `console.py`, serves as the entry point for interacting with the Airbnb clone. 
It utilizes the `cmd` module and provides a set of commands for managing different aspects of the application.

### How to Start the Command Interpreter

To start the command interpreter, run the following command in your terminal:

```bash
python console.py
```

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands:

- `quit` or `EOF`: Exit the program.
- `help`: Display the help message with a list of available commands.

### Examples

1. Creating a new User:

```bash
(hbnb) create User
```

2. Showing all instances of a class:

```bash
(hbnb) all User
```

3. Updating an instance:

```bash
(hbnb) update User <instance_id> first_name "John"
```

4. Destroying an instance:

```bash
(hbnb) destroy User <instance_id>
```

5. Displaying information about an instance:

```bash
(hbnb) show User <instance_id>
```

## Additional Classes

The project includes several classes that inheirt from the `BaseModel` class, each representing different entities in the Airbnb clone:

- State
- City
- Amenity
- Place
- Review

## File Storage

The project includes a `FileStorage` class responsible for serializing instances to a JSON file and deserializing JSON files to instances.

## Unit Tests

All files, classes and functions have been thoroughly tested with unit tests. The test files are located in the `tests/` directory.

### How to Run Unit Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover tests
```
