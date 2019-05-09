#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Make Cozmo drive in a square.

This script combines the two previous examples (02_drive_and_turn.py and
03_count.py) to make Cozmo drive in a square by going forward and turning
left 4 times in a row.
'''
import cozmo
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time


def cozmo_program(robot: cozmo.robot.Robot):
    # Use a "for loop" to repeat the indented code 4 times
    # Note: the _ variable name can be used when you don't need the value

    robot.say_text("Path one").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRooster,
        in_parallel=True)
    robot.drive_straight(distance_mm(100), speed_mmps(50),
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.say_text("Path two").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabPartyTime,
        in_parallel=True)
    robot.drive_straight(distance_mm(100), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()
    robot.say_text("Path three").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaryCozmo,
        in_parallel=True)
    robot.drive_straight(distance_mm(141), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.say_text("Path four").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRooster,
        in_parallel=True)
    robot.drive_straight(distance_mm(100), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.say_text("Path five").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRooster,
        in_parallel=True)
    robot.drive_straight(distance_mm(100), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.say_text("Path six").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRooster,
        in_parallel=True)
    robot.drive_straight(distance_mm(100), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.say_text("Path seven").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRooster,
        in_parallel=True)
    robot.drive_straight(distance_mm(141), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()
    robot.say_text("Path eight").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabRooster,
        in_parallel=True)
    robot.drive_straight(distance_mm(100), speed_mmps(50))
        should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.say_text("That is it master").wait_for_completed()
#cozmo.run_program(cozmo_program,use_viewer=True,force_viewer_on_top=True)   
cozmo.run_program(cozmo_program)