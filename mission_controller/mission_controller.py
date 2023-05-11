
import numpy as np
import asyncio

class MissionController:
    def __init__(self, robot):
        print("Creating MissionController!")
        self.robot = robot
        self.current_waypoint_idx = 0
        asyncio.create_task(self._poll_position())
        
    def set_trajectory(self, trajectory):
        self.current_waypoint_idx = 0
        self.trajectory = trajectory
        
    async def _poll_position(self):
        while True:
            position = self.robot.get_position()
            if len(self.trajectory) == 0 and self.robot.moving:
                await self._send_stop_command()
            if self.current_waypoint_idx < len(self.trajectory):
                if self.current_waypoint_idx == 0:
                    await self._send_navigation_command()
                    self.current_waypoint_idx += 1
                
                elif np.all(position == self.trajectory[self.current_waypoint_idx-1]):
                    await self._send_navigation_command()
                    self.current_waypoint_idx += 1
            await asyncio.sleep(1)
    
    async def _send_navigation_command(self):
        print(f"Sending waypoint {self.trajectory[self.current_waypoint_idx]}")
        await self.robot.set_navigation_command(self.trajectory[self.current_waypoint_idx])
    
    async def _send_stop_command(self):
        print(f"Sending stop command")
        await self.robot.stop()