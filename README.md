# MemoryCardGame-master

## Introduction
This is a Python-based memory card game implemented using the graphics library. The game requires the player to match pairs of cards with identical symbols. It features different game modes (Images Mode or Numbers Mode) and difficulty levels (Easy, Normal, and Hard). The player earns keys by successfully matching pairs, aiming to collect all keys within the least moves and time possible.

## Features
- **Game Modes**: Players can choose between Images Mode or Numbers Mode.
- **Difficulty Levels**: Three difficulty levels are available: Easy, Normal, and Hard.
- **Interactive Interface**: The game provides a user-friendly graphical interface for seamless gameplay.
- **Sound Effects**: Interactive sound effects enhance the gaming experience, including background music and click sounds.
- **Pause Functionality**: Players can pause the game at any time and resume later.
- **Scoreboard**: After completing the game, players can view their performance and rankings.
- **Exit Button**: Allows players to exit the game at any time.

## Requirements
- Python (for running the script)
- `graphics`, `random`, `time`, `platform`, `pygame`, `tkinter` libraries
- Sound files in `mp3` format for background music and sound effects
- Image files in `png` format for graphics

## File Structure
- **`main.py`**: Python script containing the game implementation.
- **`bg.png`**: Background image file.
- **`card.png`**: Image file for card with symbols (for Numbers Mode).
- **`cardback.png`**: Image file for the back of the card.
- **`cardopen.mp3`**: Sound file for card opening.
- **`card_close.mp3`**: Sound file for card closing.
- **`click_sound.mp3`**: Sound file for click interactions.
- **`exit_button.png`**: Image file for the exit button.
- **`hard.png`**, **`normal.png`**, **`easy.png`**: Image files for difficulty selection buttons.
- **`imagesmode.png`**, **`numbersmode.png`**: Image files for game mode selection buttons.
- **`jbm_music.mp3`**: Background music file.
- **`logo.png`**: Image file for game logo.
- **`pause_button.png`**: Image file for pause button.
- **`sound.png`**: Image file for sound control button.

## Installation
1. Make sure you have Python installed on your system.
2. Install the required libraries using pip:
3. Place the script (`main.py`) and all associated files in the same directory.
4. Ensure the sound and image files are accessible to the script.
5. Run the script using the command:




## Technical Details

### Function Definitions

#### `Pause_function(win)`
Description: Pauses the game and displays a message. Resumes the game upon user interaction.

#### `quit_game(win)`
Description: Closes the game window and exits the program.

#### `get_user_response(response_var, user_response)`
Description: Sets the user's response and closes the dialogue box.

#### `ask_yn(ynMessage)`
Description: Displays a Yes/No dialogue box and returns the user's response.

#### `ExitButton(win)`
Description: Displays an exit button on the game window. Closes the game upon clicking the button.

#### `sound_button_function()`
Description: Toggles sound effects on/off and displays corresponding messages.

#### `welcome_music()`
Description: Plays background music upon starting the game.

#### `click_music()`
Description: Plays a click sound effect upon user interaction.

#### `card_music()`
Description: Plays a sound effect when a card is opened.

#### `card_close()`
Description: Plays a sound effect when a card is closed.

#### `OsCheck()`
Description: Checks if the operating system is Windows.

#### `Welcome(win)`
Description: Displays the welcome screen and prompts the user to start the game.

#### `GameModePick(win)`
Description: Allows the user to select the game mode (Images Mode or Numbers Mode).

#### `Difficult(win)`
Description: Allows the user to select the difficulty level (Easy, Normal, or Hard).

#### `Init(win)`
Description: Initializes the game by prompting the user to enter their name and starting the timer.

#### `ReadPicturesNames(t, gamemode)`
Description: Returns the file name of the card image based on the game mode and card type.

#### `DrawPictures(path, p, win, gamemode)`
Description: Draws card images on the game window.

#### `DrawText(p, win, num_list, clicked_card)`
Description: Draws text on the card image.

#### `ScoreBoard(win, move, key, mouse)`
Description: Displays the scoreboard showing the number of moves, keys collected, and mouse clicks.

#### `GameBoard(win, username, gamemode, difficult)`
Description: Draws the game board with card images based on the selected game mode and difficulty level.

#### `DecideWhichCard(x, y, card_point1, card_point2 , difficult)`
Description: Determines which card is clicked based on mouse coordinates.

#### `HasItBeenClickedBefore(clicked_card, exposed)`
Description: Checks if a card has been clicked before.

#### `CheckMacthes(c1, c2, num_list)`
Description: Checks if the symbols on two cards match.

#### `Reuslt(win, gametime, username, difficult)`
Description: Displays the game result including player time and rankings.

#### `InsertInsideTheTopPlayer(username, gametime, move, difficult)`
Description: Inserts the player's performance into the top player list.

#### `Main()`
Description: Main function that orchestrates the entire gameplay loop.


