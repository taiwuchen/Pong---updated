# Pygame Pong

This is a simple implementation of the classic Pong game using Pygame.

## Description

This game offers both Player vs Player (PvP) and Player vs AI modes. Players can choose the game mode and set the maximum score to win. The game features a menu system, pause functionality, and a game-over screen.

## Features

- Two game modes: Player vs Player and Player vs AI
- Customizable max score (1-20)
- Pause menu with options to restart or return to main menu
- Game over screen with option to play again or return to main menu

## Requirements

- Python 3.x
- Pygame

## Installation

1. Ensure you have Python installed on your system.
2. Install Pygame by running:
3. Download the game script (e.g., `pong.py`).

## How to Play

1. Run the script:
   python pong.py
2. Use the menu to select game mode and set max score.
3. Controls:
- Player vs Player mode:
  - Left paddle: W (up) and S (down)
  - Right paddle: Up Arrow (up) and Down Arrow (down)
- Player vs AI mode:
  - Player paddle: Up Arrow (up) and Down Arrow (down)
- Press SPACE to pause/unpause the game
- Press ESC during gameplay to open the pause menu

## Game States

- MENU: Main menu for selecting game mode
- SCORE_SELECT: Set the maximum score
- PLAYING: Active gameplay
- PAUSED: Game is paused
- GAME_OVER: Displays the winner and options to replay or return to menu
- PAUSE_MENU: Options to restart, return to main menu, or resume

## Customization

You can easily modify game parameters such as window size, paddle size, ball speed, etc. by adjusting the constants at the beginning of the script.
