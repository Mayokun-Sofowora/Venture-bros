This site contains the project documentation for the
`Venture Bros` project, this project is a clone of the super mario bros
made for a semester project.
[Build Your Python Project Documentation With MkDocs](
    https://realpython.com/python-project-documentation-with-mkdocs/).
Its aim is to give you a framework to build your
project documentation using Python, MkDocs,
mkdocstrings, and the Material for MkDocs theme.

## Table Of Contents

The documentation follows the best practice for
project documentation as described by Daniele Procida
in the [Diátaxis documentation framework](https://diataxis.fr/)
and consists of four separate parts:

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference.md)
4. [Explanation](explanation.md)

Quickly find what you're looking for depending on
your use case by looking at the different pages.

## Project Overview

::: BGObject
Description: BGObject module represents the objects in the background of the game.
Usage: The BGObject module is used in creating background object in the Map module.

::: Camera
Description: Camera module represents the camera used to control the viewport and helps in handling movement.
Usage: The Camera module is used effectively in the Map module, helps in the players movement and stops when the player reaches the flag.

::: CoinDebris
Description: CoinDebris module is a child class of the Debris class and represents the debris of coins when it is spawned from the question blocks.
Usage: The CoinDebris module is used in the Map module for the spawning and generation of the coins.

::: Const
Description: Const module is where the global constants are defined.
Usage: The content of the const is used througout the project.

::: Core
Description: Core module represents the main game engine of the game.
Usage: The Core class is where the players keyboard input is handled and the map and menu manager is generated and handled.

::: Debris
Description: Debris module is a base class that represents the debris of objects in the game.
Usage: The Debris class is the parent class that coin-debris and platform-debris inherit from.

::: Entity
Description: Entity module is a base class that represents the entity objects in the game.
Usage: The Entity class is the a parent class to the mobs and some objects like the flowers and mushroom.

::: Event
Description: Event module represents the game events of the and their effects.
Usage: The Event class is used in the Map module and handles what happens when the player wins the game or when the player looses the game. 

::: Filesystem
Description: Filesystem module manages the loading of all the files in the game.
Usage: The filesystem is used throughout the game and handles the file loading.

::: Fireball
Description: Fireball module is a child class of Entity and represents the fireball object for when the player gets the level up ability.
Usage: The fireball class used in the Map module and gives the player the ability to shoot fireball, when they level up with the flower.

::: Flag
Description: Flag module is a child class of Entity and class represents the flag and flag pole object in the game.
Usage: The flag class used in the Map module, represents the flag and flag pole at the end of the game, representing the player has won the game.

::: Flower
Description: Describe the Core module and its significance in the game, such as managing game logic or handling events.
Usage: The flower class used in the Map module, gives the player a level up ability.

::: GameScreen
Description: GameScreen module represents the game screen display. 
Usage: The gamescreen used in the Map module is where the game is played, and renders the player and its attributes like the player's lives, player's scores coins collected and time left.

::: Goombas
Description: Goombas module is a child of the Entity class and represents an enemy in the game called Goombas.
Usage: The goombas class is used in the Map module, creates the goombas' entity.

::: Koopa
Description: Koopa module is a child of the Entity class and represents an enemy found in the game called koopa.
Usage: The koopa class is used in the Map module, creates the koopa's entity.

::: LeaderboardMenu
Description: LeaderboardMenu module represents the leaderboard menu screen state in the game, where a players can save their score and names.
Usage: The lLeaderboardMenu class is managed in the menu manager, this is where players can save their highscores a game.

::: LoadingMenu
Description: LoadingMenu module represents the loading menu in the game.
Usage: The loading menu is managed in the menu manager, is a short loading screen between states of the game, it is used when the game starts and when it ends.

::: MainMenu
Description: MainMenu module represents the main menu screen and state in the game.
Usage: The main menu is the intro screen of the game where the user can choose to start the game or go to the leaderboard.

::: Map
Description: Map module represents the map object, it contains all the tiles, mobs and player. 
Usage: The map class is where all entities and player object are stored, it is also used to create an instance of the map.

::: MenuManager
Description: MenuManager module where the different game menus are managed and updated.
Usage: The menu manager class is used in the Core module to manage the menu states of the game.

::: Mushroom
Description: Mushroom module is a child class for the Entity class that represents the mushroom objects in the game.
Usage: The mushroom class used in the Map module, gives the player a level up ability.

::: Platform
Description: Platform module represents a platform blocks in the game.
Usage: The platform class used in the Map module, is used for creating platforms.

::: PlatformDebris
Description: PlatformDebris module is a child class of the Debris class, that represents the debris that appears when a platform block is destroyed.
Usage: The PlatformDebris class is used in the Map module for the effect of when the platform blocks are destroyed.

::: Player
Description: Player module represents the player character object in the game.
Usage: The player class is used in the Map module and creates the player object, it also handles the player's movement and attributes.

::: Schnoopas
Description: Schnoopas module is a child of the Entity class and represents an enemy found in the game called schnoopas.
Usage: The Schnoopas class is used in the Map module, creates the Schnoopas' entity.

::: Sound
Description: Sound module represents the sound and music in the game and where it is managed.
Usage: The sound class is where the sound and music of the game is managed using separate threads.

::: Text
Description: Text module represents the text ojects used in the game
Usage: The text class is used for creating texts that are used throughout the game. It is used in the Map, MainMenu, LeaderboardMenu, and LoadingMenu.

::: Tube
Description: Tube module represents the tube objects of the game's platform.
Usage: The tube used in the Map class is used as an object in the game's platform.

## Acknowledgements

I want to thank my house plants for providing me with
a negligible amount of oxygen each day. Also, I want
to thank the sun for providing more than half of their
nourishment free of charge.