# Seagull Scaring V2
A seagull scaring program with GUI written in Python.
By Gabriel Alonso-Holt.

The days of having me run around scaring seagulls manually are over! With Seagull Scaring, you can just start the program, choose a time to scare seagulls for, and relax as the seagulls fly away when you want.

**Before you proceed, sound effects are not included!**

Recommended settings: 2700 seconds (timer), 60 seconds (min time), 300 seconds (max time), seagull (sound).

### Install instructions
1. Unzip the program folder.
2. Set up the virtual environment and install dependencies. (see below)
3. Copy a `media.zip` to the program folder, run `main.pyw`, click "about" and then click "extract gull effects".

### Installing dependencies
1. Run this command to create a virtual environment: `python -m venv .venv`
2. Activate the environment: `.venv\Scripts\activate.bat`
3. Install dependencies: `pip install -r requirements.txt`
4. Run program: `python main.pyw`

### Config file documentation
In the program directory, there is a file called `ssv2cfg.ini`.

You may edit this file as you desire.

**All settings must go in the [main] section.**

Valid settings:
`scaring_time (int)`: How long to run the program for.

`min_time (int)`: Minimum time to wait.

`max_time (int)`: Maximum time to wait.

`default_volume (int)`: Default volume from 0-100.

`default_sound (str)`: Seagull sound to use. Valid options: seagull, sad seagull, angry seagull, confused seagull, disgust seagull, robot seagull, alarm seagull, Seagull 2, sea gull.
