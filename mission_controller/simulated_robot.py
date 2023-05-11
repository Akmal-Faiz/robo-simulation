import asyncio
import numpy as np

def do_nothing(*args, **kwargs): pass

class SimulatedRobot:

    def __init__(self, initial_position, update_position_callback = asyncio.coroutine(do_nothing)):
        print("Creating SimulatedRobot!")
        self.position = initial_position
        self.destination = None
        self.moving = False
        self.move_task = None
        self.update_position_callback = update_position_callback

    def get_position(self):
        return self.position
    
    async def set_navigation_command(self, waypoint):
        print(f"Commanding robot to move to {waypoint}")
        self.destination = waypoint
        if np.all(self.position == self.destination):
            await self.update_position_callback(self.position)
            print(f"Robot is already at {self.destination}")
            return
        
        if self.move_task is not None:
            # Cancel the current movement task
            self.move_task.cancel()
            await self.move_task
        self.move_task = asyncio.create_task(self._move_to_destination())

    async def stop(self):
        if self.move_task is not None:
            # Cancel the current movement task
            self.move_task.cancel()
    
    async def _move_to_destination(self):
        self.moving = True
        try:
            while np.any(self.position != self.destination):
                await asyncio.sleep(3)     
                self.position = self.destination
                await self.update_position_callback(self.position)
                print(f"Robot has arrived {self.destination}")
        except asyncio.CancelledError:
            pass
        finally:
            self.moving = False
            
        
class SimulatedRobotWithCommunicationDelay:

    def __init__(self, initial_position):
        self._robot = SimulatedRobot(initial_position, self.set_position)
        self.position = initial_position

    async def set_position(self, position):
        print("waiting before responding...")
        await asyncio.sleep(3)
        self.position = position

    def get_position(self):
        return self.position

    async def set_navigation_command(self, waypoint):
        print("waiting before command...")
        await asyncio.sleep(3) 
        await self._robot.set_navigation_command(waypoint)
        