
This is a code debugging/refactoring exercise, it is meant to take 1-2 hours.

The program is intended as a simple service to release waypoints one at a time to a robot in a way that allows changes/cancellations. 

For example, the process could be:

* The robot begins with coordinates (2, 1). 
* We submit a trajectory with points ((4, 3), (5, 3)).
* The robot starts to move to (4, 3).
* We submit a trajectory with points ((3, 3), (5, 4)).
* The robot starts to move to (3, 3) instead of (4, 3).
* The robot arrives at (3, 3), and starts to move towards (5, 4).
* The robot receives a trajectory with points ().
* The robot stops.

(In the real world this might be done with something like ROS, but we minimized external dependencies for this exercise.)

Task:

* Expand the test set as needed.
* Debug the program to resolve inconsistencies.
* Add basic input validation to improve robustness.
* Refactor the code to improve readability, maintainability.


Scoring is based on:

* How many bugs/other issues are fixed.
* Overall structure of the final code.

It does not depend on adding new features, using a particular testing framework, adding very detailed documentation etc.


Notes:

* Currently it is based on python threading (with many bugs added), but you can rewrite using whatever methodology 
  you're comfortable with (e.g. async python).

* If you are unfamiliar with python, feel free to write an equivalent program in a language of your choosing.

