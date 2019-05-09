#!/usr/bin/env python3

'''
Author: James Owen
May 4 2019
Performs 8 traversals which consist of the following:
* announce the traversal number
* start an animation without waiting for it to stop
* perform the traversal
* turn
The camera should be running while all of this happens
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
import math
height = 500
width = 500
diagonal = math.sqrt(height**2 + height**2)

distances = [height, width, diagonal, height, width, width, diagonal, width]
animations = [cozmo.anim.Triggers.CubePounceWinSession,
              cozmo.anim.Triggers.CubePounceLoseSession,
              cozmo.anim.Triggers.CubePounceWinHand,
              cozmo.anim.Triggers.DemoSpeedTapCozmoLose,
              cozmo.anim.Triggers.DizzyReactionMedium,
              cozmo.anim.Triggers.DizzyShakeLoop,
              cozmo.anim.Triggers.DriveEndAngry,
              cozmo.anim.Triggers.DriveEndHappy
              ]
turns = [90, 90 + 45, -90 - 45, -90, 0, -90 - 45, 90 + 45, 0]


def announce(robot, step_number):
    robot.say_text("Step number %d" % step_number).wait_for_completed()


def animate(robot, step_number):
    return robot.play_anim_trigger(animations[step_number-1], loop_count=5, ignore_body_track=False, in_parallel=True)


def travel(robot, step_number):
    return robot.drive_straight(distance_mm(distances[step_number-1]), speed_mmps(50), in_parallel=True, should_play_anim=True)


def turn(robot, step_number):
    robot.turn_in_place(degrees(turns[step_number-1])).wait_for_completed()


def traverse(robot, step_number):
    announce(robot, step_number)
    traveling = travel(robot, step_number)
    time.sleep(0.5)
    animating = animate(robot, step_number)
    traveling.wait_for_completed()
    animating.wait_for_completed()
    turn(robot, step_number)


def play_song(robot):
    notes2 = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2,
                            cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2_Sharp,
                            cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2,
                            cozmo.song.NoteDurations.Quarter)]
    for i in range(2):
        robot.play_song(notes2, loop_count=1).wait_for_completed()
        notes2.reverse()
        robot.play_song(notes2, loop_count=1).wait_for_completed()
        notes2.reverse()
    robot.move_head(5)


def cozmo_program(robot: cozmo.robot.Robot):
    for i in range(1, 9):
        traverse(robot, step_number=i)
    play_song(robot)


cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)