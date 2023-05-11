# Understanding of the Program

## MissionController class
- Instantiated with a robot.
- Trajectory can be modified at any time.
- Polls every second and does the following
    - Sleep for 1s, before getting the robot's current position
    - If the trajectory is newly set, i.e. `(current_waypoint_idx=0)`, send a navigation command to the first waypoint
    - If the robot is already at the current destination waypoint, send a navigation command to the next waypoint.

## SimulatedRobot class
- Instantiated with an initial position and a callback function(to be called when the robot's position is updated)
- When the robot receives a navigation command, it starts a thread and runs the update function
    - The update function sleeps for some time (to simulate travelling presumably) and updates the robot's position

## SimulatedRobotWithCommunicationDelay class
- This class implements the same methods as the SimulatedRobot class, with an additional `set_position` method.
- The class is instantiated with a SimulatedRobot object as one of the properties, where the set_position method is passed as the update_position_callback function
- The set_position method adds a delay before commanding the robot to move and before updating its position.

# Bugs

## mission_controller.py:
- The expression `self.trajectory[:, self.current_waypoint_idx]` takes the 2nd element of each of the waypoints, instead of the i<sup>th</sup> waypoint.
- It should also compare to the previous waypoint instead of the current
- The current_waypoint_index can go beyond the size of the trajectory, leading to IndexError
- Unable to handle an empty trajectory.

## simulated_robot.py
- Threads are never started
- update_position_callback defaults to None, which can cause an error when it is called
- There is no need to simulate travel if the robot is already at the waypoint when given the command
- interrupting the robot with a new command doesnt work

## test.py
- the program can exit while waiting for the robot to complete moving.


# Report
- Used `asyncio` as I'm more familiar with it.
- Fixed the above bugs
- Added interruption to the robot, using the `moving` flag and `move_task` task
- Unable to properly simulate delay in communications
- removed random sleeps for more consistent testing
    - Possible to replace hardcoded time to distance based time.
