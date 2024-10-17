# Drone Control Script using DroneKit

This script demonstrates how to control a drone using the `DroneKit` library in Python. It establishes a connection with a drone or simulator, arms the drone, takes off, navigates through predefined waypoints, and then lands. The coordinates are left as placeholders for user customization to ensure safety.

## 🛠️ Requirements

To run this script, you need:
- **Python 3.x**
- The `DroneKit` Python library, which can be installed using:
  ```bash
  pip install dronekit
A drone or simulator (like SITL) that connects over the MAVLink protocol. The connection string is set to 127.0.0.1:14550 by default, which is commonly used for simulators.
📜 Code Explanation
1. Connecting to the Drone
python
Kodu kopyala
drone = connect(connection_string, wait_ready=True, timeout=100)
This line connects the script to the drone using the provided connection string. The wait_ready=True ensures the script waits until the drone is fully ready before proceeding with any operations.

2. Arming the Drone and Taking Off
python
Kodu kopyala
def arm_and_takeoff(target_altitude):
    while not drone.is_armable:
        print("Waiting for drone to become armable.")
        time.sleep(1)
    print("Drone is now armable.")
The arm_and_takeoff function checks if the drone is ready to be armed. Once it is armable, the drone is switched to "GUIDED" mode for autonomous control. After that, it arms and takes off to the specified altitude (target_altitude).

3. Navigating to Waypoints
python
Kodu kopyala
point1 = LocationGlobalRelative(Your_latitude, Your_longitude, 5)
drone.simple_goto(point1, airspeed=1)
The drone navigates to specific GPS coordinates (latitude, longitude, altitude). The script uses placeholders (Your_latitude, Your_longitude) where the user can input their own waypoints.

4. Landing the Drone
python
Kodu kopyala
drone.mode = VehicleMode("LAND")
After navigating to all waypoints, the drone switches to "LAND" mode and begins landing.

5. Disconnecting
python
Kodu kopyala
drone.close()
The connection to the drone is closed after landing, ensuring the script finishes safely.

🚀 Usage
Install the required libraries and ensure your drone or simulator is running.
Replace the placeholder coordinates in the script with your own.
Run the script in a Python environment:
bash
Kodu kopyala
python drone_control.py
The drone will take off, navigate between the waypoints, and then land.
⚠️ Safety Notice
To avoid any unintended consequences, DO NOT use real coordinates from your location or sensitive areas directly in the script. Instead, use test coordinates in an open, safe area or a simulation environment.
