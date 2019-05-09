import time
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.anim import Triggers


def main(robot: cozmo.robot.Robot):
    # first run     
    robot.say_text("I am starting").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhoa, in_parallel=True).wait_for_completed()  
    robot.drive_straight(distance_mm(200), speed_mmps(300), should_play_anim=True, in_parallel=True).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    # second run
    robot.say_text("second checkpoint").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWhew).wait_for_completed() 
    robot.drive_straight(distance_mm(200), speed_mmps(300)).wait_for_completed()
    robot.turn_in_place(degrees(495)).wait_for_completed()

    # third run
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeStop).wait_for_completed() 
    robot.say_text("third checkpoint").wait_for_completed()
    robot.drive_straight(distance_mm(283), speed_mmps(300)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()

    # fourth run
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin).wait_for_completed() 
    robot.say_text("fourth checkpoint").wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(300)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()

    # fifth run
    robot.say_text("fifth checkpoint").wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(300)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabZombie).wait_for_completed() 

    # sixth run
    robot.say_text("sixth checkpoint").wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(300)).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabAmazed).wait_for_completed() 

    # seventh run
    robot.say_text("seventh checkpoint").wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(300)).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()

    # eight run
    robot.say_text("eighth checkpoint").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CozmoSaysGetOut).wait_for_completed() 

    robot.drive_straight(distance_mm(200), speed_mmps(300)).wait_for_completed()

    # the end
    robot.say_text("I reached the end!").wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()  

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

    

cozmo.run_program(main, use_viewer=True, force_viewer_on_top=True)