"""Example utility module.

Please use a file like this one to add extra functions.

"""
import numpy as np

def exampleFunction():
    """Example of user-defined function.

    """
    x = -1
    return x

def circularTrajectory(origin, radius, waypoints, cycles):
    num_waypoints = 150 * cycles
    cx, cy, cz = origin[0], origin[1], origin[2]

    start_angle = np.arctan2(waypoints[0][1] - cy, waypoints[0][0] - cx)

    for i in np.linspace(start_angle, start_angle + cycles*2*np.pi, num_waypoints, endpoint=False):
        x = cx + radius * np.cos(i)
        y = cy + radius * np.sin(i)
        waypoints.append((x, y, cz))

    return waypoints