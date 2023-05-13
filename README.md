# DK's A* Snake game

This project was a school projects aimed to learn and try to develop an A* algorithm.

It has both classic A* and "virtual" A* which first tries virtually if it's possible to eat the food,
and if not, he tries another way, which in case of success is used for the real snake.

## How to use?

Run the main.py program. In there you can configure if you want to play normal snake game or you want to let the A* do it's thing.
This can be set by setting the `set_mode` attribute to mode `1` - Manual play; `2` - Astar autoplay; `3` - Astar with Forward Checking autoplay.
