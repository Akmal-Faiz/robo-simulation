
import time
import numpy as np

from mission_controller.mission_controller_original import MissionController
from mission_controller.simulated_robot_original import SimulatedRobot, SimulatedRobotWithCommunicationDelay


def test_normal_operation():

    simulated_robot = SimulatedRobotWithCommunicationDelay(np.array([0.0, 0.0]))

    controller = MissionController(simulated_robot)

    # set the first trajectory

    controller.set_trajectory(np.array([[0.0, 0.0], [1.0, 0.0]]))

    time.sleep(1)

    # now set a different trajectory before the first trajectory completes

    controller.set_trajectory(np.array([[2.0, 0.0], [3.0, 0.0]]))

    time.sleep(2)

    print("Test complete")

    exit(0)


if __name__ == "__main__":
    test_normal_operation()
