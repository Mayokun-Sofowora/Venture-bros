# Venture-bros

**Venture-bros** is a computer programming project that presents an exciting game where players navigate through various levels to achieve victory. Built initially in Python, the game includes engaging features such as a leaderboard, game-over screen, and world levels. The game's goal is to progress through increasingly difficult levels, score points, and achieve the highest rank.

## Features

- **Start Screen**: A welcoming start screen to begin your adventure.
- **Game Over Screen**: A clear indication of when the game ends.
- **Victory Screen**: Displays a success message when you win.
- **World Levels**: Navigate through different stages with varying difficulty, although this current implementation only has one world and level.
- **Leaderboard**: Track your performance and see how you rank among other players.

## Screenshots

### Start Screen
![Start Screen](https://github.com/user-attachments/assets/34644571-cf14-4ec8-bcf8-5e4eb74ea319)

### Game Over
![Game Over](https://github.com/user-attachments/assets/add9d6fe-50ef-49ce-a600-a6d5ea38948a)

### You Won!
![You Won](https://github.com/user-attachments/assets/db3b830f-f028-4105-aa8f-4c44e3ade717)

### World Level
![World Level](https://github.com/user-attachments/assets/8d5abc45-3b17-479b-817d-1f89c6c569fd)

### Leaderboard
![Leaderboard](https://github.com/user-attachments/assets/83a21376-64aa-4324-88bf-f2acabdc394e)

## Setup & Installation

Follow these steps to set up and run the game:

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/Venture-bros.git
cd Venture-bros
```

### 2. Install Dependencies

If you haven't already, make sure to install the required Python packages to run the game. In the terminal, navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

This will install the necessary dependencies, including the `pygame` package to run the game.

### 3. Run the Game

To start the game, run the `main.py` script:

```bash
python main.py
```

You should now be able to play the game and navigate through the levels!

## Future Improvements

While the current game is functional, there are many ways to improve the game with additional features and optimizations, including a potential move to **C++** for better performance:

- **C++ Optimization**: Migrating the game to C++ could provide better performance, especially for complex logic and real-time rendering. We plan to rewrite the core game mechanics in C++ to enhance speed and reduce latency.
- **Enhanced Graphics**: With C++, we can utilize powerful libraries like **SFML** or **SDL** to create more sophisticated 2D and 3D graphics for a richer experience.
- **AI Opponents**: Implement intelligent AI players to challenge users in different levels.
- **Multiplayer Support**: Add multiplayer functionality to allow users to compete with each other online.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues. Your suggestions for features or improvements are always welcome!

## Acknowledgments

- Special thanks to [Pygame](https://www.pygame.org) for providing the necessary game development tools in Python.
