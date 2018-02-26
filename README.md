# Shortcut-To-Exec
#### A group of `python` scripts to help make emulation easier

## Table of Contents

1. [Overview](#Overview)
1. [Prerequisites](#Prerequisites)
1. [makeBats.py](#makebats.py)
1. [makeExes.py](#makeexes.py)
1. [CreateSteamGridImage.py](#createsteamgridimage.py)
1. [TODO](#todo)


## Overview

The basic idea behind these files was to make adding emulators to Steam much easier.

Steam cannot accept shortcuts or links in the app list, only executables. So, if you have a bunch of games that run from
a command line, such as emulators, you are typically stuck having to open the app, then opening the game or other file
from within that app.

This collection uses `python` to create actual (Windows only for now) executable files to launch your emulators straight
to the game you want to play.

The main files are:

1. makeBats.py (Will be renamed in a future update)
1. makeExes.py
1. CreateSteamGridImage.py

## Prerequisites

This readme assumes you have pip installed, but is not strictly necessary, as there are other ways of installing any 
and all prerequisites.

Currently, this suite of scripts requires a few separate programs:
1. [Python 3.x](https://www.python.org/downloads/) (Tested on 3.6.3, but any version from 3.0 should work)
1. [pyinstaller](http://www.pyinstaller.org/)
    - Used in `makeExes.py`, as shown below
    - Can be installed from the website linked above or by simply using `pip install pyinstaller`

## makeBats.py

This file loops through a directory (containing your ROMs)and creates a separate `.py` file for each item in said
directory.

The `.py` file is simply a `python` script that uses the `subprocess` library to open your emulator with the game as a 
command line argument.

Currently, the directories are embedded in `makeBats.py`, but in a future update I will be adding both command line 
arguments as well as a full GUI for this suite of scripts.

## makeExes.py

Uses pyinstaller to loop through a given folder (the one that contains the scripts made with `makeBats.py`) and creates
executables from it.

Currently, the directories are embedded in `makeExes.py`, but in a future update I will be adding both command line 
arguments as well as a full GUI for this suite of scripts.

## CreateSteamGridImage.py

Creates a 920x430 Image (Double the standard resolution for Steam's Grid or Big Picture Mode) for each ROM in a given 
folder.

Uses a file called SNES.jpg as a background, with the name of the ROM centered on the image.

## TODO

1. Rewrite this file to make it easier to understand / sound more professional
2. Add GUI
3. add `images` for  each file to explain the process better