
import numpy as np

import time

from threading import Thread

import random


class SimulatedRobot:

    def __init__(self, initial_position, update_position_callback=None):
        print("Creating SimulatedRobot!")

        self.position = initial_position
        self.update_position_callback = update_position_callback

    def get_position(self):
        return self.position

    def set_navigation_command(self, waypoint):

        print(f"Commanding robot to move to {waypoint}")

        def update():
            time.sleep(random.uniform(1.0, 2.0))

            print(f"Robot is now at {waypoint}")

            self.position = waypoint

            self.update_position_callback(waypoint)

        thread_update = Thread(target=update)


class SimulatedRobotWithCommunicationDelay:

    def __init__(self, initial_position):

        self._robot = SimulatedRobot(initial_position, self.set_position)

        self.position = initial_position

    def set_position(self, position):

        def update():
            time.sleep(random.uniform(0.0, 2.0))

            self.position = position

        thread_update = Thread(target=update)

    def get_position(self):
        return self.position

    def set_navigation_command(self, waypoint):

        print(f"Commanding robot to move to {waypoint}")

        def update():
            time.sleep(random.uniform(0.0, 2.0))

            self._robot.set_navigation_command(waypoint)

        thread_update = Thread(target=update)
