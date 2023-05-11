import asyncio
import numpy as np

from mission_controller.mission_controller import MissionController
from mission_controller.simulated_robot import SimulatedRobot, SimulatedRobotWithCommunicationDelay


async def test_normal_operation():
    # expected output:
    # Creating SimulatedRobot!
    # Creating MissionController!
    # Sending waypoint [1. 0.]
    # Commanding robot to move to [1. 0.]
    # Robot has arrived [1. 0.]
    # Sending waypoint [2. 0.]
    # Commanding robot to move to [2. 0.]
    # Robot has arrived [2. 0.]
    # Test complete
    simulated_robot = SimulatedRobot(np.array([0.0, 0.0]))

    controller = MissionController(simulated_robot)

    # set the first trajectory
    controller.set_trajectory(np.array([[1.0, 0.0], [2.0, 0.0]]))

    while controller.current_waypoint_idx < len(controller.trajectory) or simulated_robot.moving:
        await asyncio.sleep(1)
    print("Test complete")

async def test_interrupt_operation():
    # expected output:
    # Creating SimulatedRobot!
    # Creating MissionController!
    # Sending waypoint [1. 0.]
    # Commanding robot to move to [1. 0.]
    # Sending waypoint [3. 0.]
    # Commanding robot to move to [3. 0.]
    # Robot has arrived [3. 0.]
    # Sending waypoint [4. 0.]
    # Commanding robot to move to [4. 0.]
    # Robot has arrived [4. 0.]
    simulated_robot = SimulatedRobot(np.array([0.0, 0.0]))

    controller = MissionController(simulated_robot)

    # set the first trajectory
    controller.set_trajectory(np.array([[1.0, 0.0], [2.0, 0.0]]))
    
    # sleep for a while
    await asyncio.sleep(1)
    
    # interrupt the movement
    controller.set_trajectory(np.array([[3.0, 0.0], [4.0, 0.0]]))

    while controller.current_waypoint_idx < len(controller.trajectory) or simulated_robot.moving:
        await asyncio.sleep(1)
    print("Test complete")

async def test_already_at_waypoint():
    # expected output:
    # Creating SimulatedRobot!
    # Creating MissionController!
    # Sending waypoint [1. 0.]
    # Commanding robot to move to [1. 0.]
    # Robot is already at [1. 0.]
    # Sending waypoint [1. 0.]
    # Commanding robot to move to [1. 0.]
    # Robot is already at [1. 0.]
    # Test complete
    simulated_robot = SimulatedRobot(np.array([1.0, 0.0]))

    controller = MissionController(simulated_robot)

    # set the trajectory to start and end at the initial position
    controller.set_trajectory(np.array([[1.0, 0.0], [1.0, 0.0]]))

    while controller.current_waypoint_idx < len(controller.trajectory) or simulated_robot.moving:
        await asyncio.sleep(1)
    print("Test complete")

async def test_interrupt_with_none():
    # expected output:
    # Creating SimulatedRobot!
    # Creating MissionController!
    # Sending waypoint [2. 0.]
    # Commanding robot to move to [2. 0.]
    # Sending stop command
    # Test complete
    simulated_robot = SimulatedRobot(np.array([1.0, 0.0]))

    controller = MissionController(simulated_robot)

    # # set the trajectory to start and end at the initial position
    controller.set_trajectory(np.array([[2.0, 0.0], [5.0, 0.0]]))
    await asyncio.sleep(1)
    controller.set_trajectory(np.array([]))
    # await asyncio.sleep(1)
    # controller.set_trajectory(np.array([[2.0, 0.0], [5.0, 0.0]]))

    while controller.current_waypoint_idx < len(controller.trajectory) or simulated_robot.moving:
        await asyncio.sleep(1)
    print("Test complete")

if __name__ == "__main__":
    # asyncio.run(test_normal_operation())
    # asyncio.run(test_interrupt_operation())
    # asyncio.run(test_already_at_waypoint())
    asyncio.run(test_interrupt_with_none())
    
    