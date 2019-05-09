import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import random


def talk(robot, phrase):
    # Say the provided phrase.
    robot.say_text(phrase).wait_for_completed()


def drive(robot, distance):
    # Function drives half distance, executes animation, completes the side
    # Drive specified distance at specified speed.
    robot.drive_straight(distance_mm(distance/2), speed_mmps(50)).wait_for_completed()
    # animate(robot)
    robot.drive_straight(distance_mm(distance/2), speed_mmps(50)).wait_for_completed()


def turn(robot, required_degrees):
    # Turn degrees (positive degrees to left, negative degrees to right).
    robot.turn_in_place(degrees(required_degrees)).wait_for_completed()


def animate(robot):
    # Turn degrees (positive degrees to left, negative degrees to right).
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()


def cozmo_program(robot: cozmo.robot.Robot):
    regular_side = 304.8
    long_side = 431.05
    no_side = 0
    half_left = 45
    left = 90
    wide_left = 135
    half_right = -45
    right = -90
    wide_right = -135
    no_turn = 0

    instructionList = [
        [regular_side, left],
        [regular_side, wide_left],
        [long_side, half_right],
        [regular_side, right],
        [regular_side, no_turn],
        [regular_side, wide_right],
        [regular_side, wide_left],
        [regular_side, no_turn]
    ]

    for instruction in instructionList:
        talk(robot, str("side" + (instruction + 1))
        drive(robot, instruction[1])
        turn(robot, instruction[2])

    talk(robot, "Yippie, I'm done!")


cozmo.run_program(cozmo_program, use_viewer = True, force_viewer_on_top = True)