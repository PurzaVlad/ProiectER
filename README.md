# Moving Circle Game

This project is a simple game where a circular object moves in any direction within a defined square space, avoiding obstacles. The game is built using Python and provides a basic framework for game development.

## Project Structure

```
moving-circle-py
├── src
│   ├── main.py          # Entry point of the application
│   ├── proiectER.py     # Additional game logic and utility functions
│   ├── game.py          # Manages game logic and environment
│   ├── settings.py      # Configuration settings for the game
│   ├── entities         # Contains game entities
│   │   ├── __init__.py  # Initializes the entities package
│   │   ├── circle.py    # Circle class for the moving object
│   │   └── obstacle.py  # Obstacle class for collision detection
│   └── physics          # Contains physics-related logic
│       ├── __init__.py  # Initializes the physics package
│       └── collision.py  # Collision detection functions
├── tests                # Contains unit tests
│   └── test_collision.py # Tests for collision detection logic
├── requirements.txt     # Project dependencies
├── pyproject.toml       # Project configuration
├── .gitignore           # Files to ignore in version control
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd moving-circle-py
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the game:
   ```
   python src/main.py
   ```

## Usage

- Use the arrow keys to move the circular object around the screen.
- Avoid hitting the obstacles that are placed within the game area.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the game.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.# ProiectER
