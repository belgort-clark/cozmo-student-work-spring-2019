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

'''Drive And Turn

Make Cozmo drive forwards and then turn 90 degrees to the left.
'''

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import asyncio
import time
import sys



def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Step 1").wait_for_completed()
    
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    action1 = robot.drive_straight(distance_mm(150), speed_mmps(80), in_parallel=True, )
    action2 = robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabDancingMambo, in_parallel=True)
    action1.wait_for_completed()
    action2.wait_for_completed()

    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()

    robot.say_text("Step 2").wait_for_completed()

    robot.drive_straight(distance_mm(150), speed_mmps(80)).wait_for_completed()

    robot.turn_in_place(degrees(135)).wait_for_completed()

    robot.say_text("Step 3").wait_for_completed()

    robot.drive_straight(distance_mm(212), speed_mmps(80)).wait_for_completed()

    robot.turn_in_place(degrees(-135)).wait_for_completed()

    robot.say_text("Step 4").wait_for_completed()

    robot.drive_straight(distance_mm(150), speed_mmps(80)).wait_for_completed()

    robot.turn_in_place(degrees(-90)).wait_for_completed()

    robot.say_text("Step 5").wait_for_completed()

    robot.drive_straight(distance_mm(150), speed_mmps(80)).wait_for_completed()

    robot.say_text("Step 6").wait_for_completed()

    robot.drive_straight(distance_mm(150), speed_mmps(80)).wait_for_completed()

    robot.turn_in_place(degrees(-135)).wait_for_completed()

    robot.say_text("Step 7").wait_for_completed()

    robot.drive_straight(distance_mm(212), speed_mmps(80)).wait_for_completed()

    robot.turn_in_place(degrees(135)).wait_for_completed()

    robot.say_text("Step 8").wait_for_completed()

    robot.drive_straight(distance_mm(150), speed_mmps(80)).wait_for_completed()

    robot.say_text("Step 9").wait_for_completed()

    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Quarter) ]

    # Play the ascending notes
    robot.play_song(notes, loop_count=1).wait_for_completed()

    # Create an array of SongNote objects, consisting of the C3 pitch with varying durations
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.ThreeQuarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Whole) ]

    # Play the notes with varying durations
    robot.play_song(notes, loop_count=1).wait_for_completed()


cozmo.run_program(cozmo_program)
