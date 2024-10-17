from dronekit import connect, VehicleMode, LocationGlobalRelative 
import time

# Connection string for the drone (e.g., SITL or real drone)
connection_string = "127.0.0.1:14550"

# Connect to the drone
drone = connect(connection_string, wait_ready=True, timeout=100)

# Countdown before starting the flight
countdown = 5
while countdown > 0:
    print("Flight starting in:", countdown)
    countdown -= 1
    time.sleep(1)

# Function to arm the drone and take off
def arm_and_takeoff(target_altitude):
    # Wait until the drone is ready to be armed
    while not drone.is_armable:
        print("Waiting for drone to become armable.")
        time.sleep(1)
    print("Drone is now armable.")

    # Switch the drone to GUIDED mode for autonomous control
    drone.mode = VehicleMode("GUIDED")
    while drone.mode != 'GUIDED':
        print('Switching to GUIDED mode...')
        time.sleep(1.5)

    print("GUIDED mode activated.")

    # Arm the drone
    drone.armed = True
    while not drone.armed:
        print("Waiting for drone to arm.")
        time.sleep(1)

    print("Drone armed. Starting takeoff.")

    # Perform takeoff
    drone.simple_takeoff(target_altitude)

    # Wait until the drone reaches the target altitude (within a margin)
    while drone.location.global_relative_frame.alt <= target_altitude * 0.94:
        print("Current altitude: {}".format(drone.location.global_relative_frame.alt))
        time.sleep(0.5)

    print("Takeoff completed.")

# Execute the arm and takeoff function
arm_and_takeoff(5)

# Wait for 10 seconds before moving to the first waypoint
time.sleep(10)

# Move to first waypoint
print("Moving to the first waypoint in 10 seconds...")
# Insert your coordinates here
point1 = LocationGlobalRelative(Your_latitude, Your_longitude, 5)
drone.simple_goto(point1, airspeed=1)

# Wait 30 seconds at the first waypoint
time.sleep(30)

# Move to second waypoint
print("Moving to the second waypoint...")
# Insert your coordinates here
point2 = LocationGlobalRelative(Your_latitude, Your_longitude, 5)
drone.simple_goto(point2, airspeed=1)

# Wait another 30 seconds
time.sleep(30)

# Set airspeed for next movements
print("Airspeed set to 1 m/s.")
drone.airspeed = 1

# Move to third waypoint
print("Moving to the third waypoint...")
# Insert your coordinates here
point3 = LocationGlobalRelative(Your_latitude, Your_longitude, 5)
drone.simple_goto(point3, groundspeed=1)

# Wait 30 seconds at the third waypoint
time.sleep(30)

# Land the drone
print("Initiating landing...")
drone.mode = VehicleMode("LAND")

# Close the connection after landing
print("Disarming and closing connection.")
drone.close()
