# import section
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
from cozmo.anim import Triggers
import asyncio
# bot code section
def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Program initializing.").wait_for_completed()
    
    for i in range(2):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabAmazed).wait_for_completed()
    
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.turn_in_place(degrees(45)).wait_for_completed()
    
    robot.drive_straight(distance_mm(300), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabAmazed).wait_for_completed()
    
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    for i in range(2):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        
        robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabAmazed).wait_for_completed()
        
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed() 
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(75)).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(75)).wait_for_completed()
    robot.say_text("Song engaged!").wait_for_completed()
    # Song Section
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half)
    ]
    robot.play_song(notes, loop_count=1).wait_for_completed()
    
    robot.say_text("Program shutting down.").wait_for_completed()
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)