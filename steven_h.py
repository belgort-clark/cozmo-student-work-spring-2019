#!/usr/bin/env python3
import cozmo
import asyncio
import time
from cozmo.util import degrees, distance_mm, speed_mmps
def cozmo_path(robot: cozmo.robot.Robot):
    # Create an array of SongNote objects, consisting of all notes from C2 to C3_Sharp
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
    
    # 1
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    #  2
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()
    # 3
    robot.drive_straight(distance_mm(70), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    
    # 4
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    # 5
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    # 6
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    # 7
    
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(70), speed_mmps(50)).wait_for_completed()
    # 8
    robot.turn_in_place(degrees(135)).wait_for_completed()
    robot.drive_straight(distance_mm(50), speed_mmps(50)).wait_for_completed()
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()
    # Play the ascending notes
    robot.play_song(notes, loop_count=1).wait_for_completed()
cozmo.run_program(cozmo_path, use_viewer=True, force_viewer_on_top=True)