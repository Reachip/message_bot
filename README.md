# message_bot

The aim of this project is to provide a CLI to store dynamically some message commands with a simple CLI.

It use a markdown files to store the message contents. 
The files are stored into a path given by the ```CMD_FILES``` environnement variable.

You can give your bot token into the ```TOKEN``` environnement variable.

## CLI

## Usage

__main__.py [-h] {add,commit,list,remove} ...

## Positional arguments

{add,commit,list,remove}

| Command | Description |
| ------- | ----------- |
| add     | add a new message command |
| commit  | commit a existing message command |
| list    | list some message command |
| remove  | remove a existing message command |
    
## Optional arguments:

-h: show this help message and exit
