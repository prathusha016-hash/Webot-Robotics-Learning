from controller import Robot

# Create the Robot instance
robot = Robot()

# Get the time step
timestep = int(robot.getBasicTimeStep())

# Get the motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set motors to velocity control mode
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Get proximity sensors
prox_sensors = []

for i in range(8):
    sensor = robot.getDevice("ps" + str(i))
    sensor.enable(timestep)
    prox_sensors.append(sensor)

# Get light sensors
light_sensors = []

for i in range(8):
    sensor = robot.getDevice("ls" + str(i))
    sensor.enable(timestep)
    light_sensors.append(sensor)

# Main simulation loop
while robot.step(timestep) != -1:
    t = robot.getTime()

    # Read proximity sensor values
    ps_values = [round(s.getValue(), 1) for s in prox_sensors]

    # Read light sensor values
    ls_values = [round(s.getValue(), 1) for s in light_sensors]

    print(f"Time: {t:.2f}s")
    print(f"Proximity (ps0-ps7): {ps_values}")
    print(f"Light (ls0-ls7): {ls_values}")
    print("-" * 50)

 