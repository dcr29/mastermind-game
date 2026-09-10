# Mastermind

A Mastermind game developed in Python using Pygame.

## Overview

The goal of the game is to guess the hidden combination of colored pegs in as few attempts as possible.

After each attempt, the game indicates:

- The number of pegs with the correct color and position.
- The number of pegs with the correct color but wrong position.

## Game Modes

- **Easy:** 4 holes, 4 available colors
- **Medium:** 4 holes, 6 available colors
- **Hard:** 4 holes, 8 available colors
- **Custom:** Choose between 2 and 8 holes and 2 and 8 colors

The game keeps track of the best score for each standard game mode.

## Technologies

- Python
- Pygame
- Object-oriented programming
- Git / GitHub

## My Contribution

Developed as part of a two-person team.

My contributions included:

- Implementing game logic and interactive features.
- Developing graphical elements and buttons.
- Designing and organizing the application into dedicated classes and modules.
- Working on scene management and score handling.
- Contributing to the project architecture and development using Git and GitHub.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mastermind-game.git
cd mastermind-game
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

On macOS and Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the game with:

```bash
python code/main.py
```

## Project Structure

```text
code/
├── main.py
├── GameScene.py
├── GameGestion.py
├── SceneGestion.py
├── ScoreGestion.py
├── ColorPalette.py
├── DoneLine.py
├── DoneLineGestion.py
├── Button.py
└── ...
```
