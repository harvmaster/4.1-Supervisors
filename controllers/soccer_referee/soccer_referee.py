"""soccer_referee controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Supervisor

# create the Robot instance.
supervisor = Supervisor()

ball = supervisor.getFromDef("BALL")
trans_field = ball.getField("translation")

# get the time step of the current world.
timestep = 32

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
while supervisor.step(timestep) != -1:
    values = trans_field.getSFVec3f()
    print("Ball is at position: %g %g %g" % (values[0], values[1], values[2]))
    
    if values[0] > 4.5 or values[0] < -4.5:
        if values[2] < 0.75 and values[2] > -0.75:
            INITIAL = [0, 0.113, 0]
            trans_field.setSFVec3f(INITIAL)
            ball.resetPhysics()
        else:
            if values[0] > 4.5:
                ball.setVelocity([0,0,0])
                trans_field.setSFVec3f([ 4.5, 0.113, round(values[2], 2) ])
                ball.resetPhysics()
            else:
                ball.setVelocity([0,0,0])
                trans_field.setSFVec3f([ -4.5, 0.113, round(values[2], 2) ])
                ball.resetPhysics()
    if (values[2] > 3 or values[2] < -3):
        if values[2] > 3:
            ball.setVelocity([0,0,0])
            trans_field.setSFVec3f([round(values[0], 2),0.113, 3])
            ball.resetPhysics()
        else:
            ball.setVelocity([0,0,0])
            trans_field.setSFVec3f([round(values[0], 2),0.113, -3])
            ball.resetPhysics()