# python-autoupdate-config

This is a python implementation for an application similar to zookeeper. It keeps your config data in once place and can be updated WITHOUT a change in code. It is made for distributed systems and can be used in applications like machine learning and web apps. Your latest config data will automatically be available on all your distributed nodes using WebSockets. 

## Help Needed
```
If you are trying to learn python websockets and are willing to contribute. 
Please do send a pull request I will review it and merge it. 💖
```

## Setup (Python3.7)
```
> python -m venv python_env
> .\python_env\Scripts\activate
> pip install -r requiremenets.txt
```

## Required Tasks (❌-Not Done, ✔️-Done)
```
1) Better storage type of data ❌
2) Create a way to have an API key to access the data ❌
3) Refactoring folder structure ❌
4) Make a UI preferably just html or using Flask (like zookeeper) ❌
5) Add threading for the client using a thread pool ❌
6) Make support for hierarchical data ❌
7) Secure end points to send sensitive config data ❌
```


## How to Use?
```
Server.py:
> Starts up your single node server containing your configuration data 
(not secure look to Task 7 to help me out there)

Client.py:
> Starts a listener that gets the data and then listens to updates made to the config 
(Needs to be updated to use a thread pool so its not blocking)

Client_update.py:
> This is used to update a config file current implementation only has a CLI interface 
(If you know flask you could contribute here, or just make a regular html file anything works!)

Client_remove.py:
> This is used to remove a config field current implementation only has a CLI interface 
(If you know flask you could contribute here, or just make a regular html file anything works!)
```
