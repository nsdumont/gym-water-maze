from gymnasium.envs.registration import register
from gym_water_maze.watermazeenv import WaterMazeEnv

register(
    id="WaterMaze-v0",
    entry_point="gym_water_maze:WaterMazeEnv"
)

