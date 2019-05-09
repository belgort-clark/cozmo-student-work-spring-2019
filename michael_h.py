import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time


def cozmo_program(robot: cozmo.robot.Robot):

    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Half),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half)  ]

    robot.say_text('Beginning leg one').wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(250)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    robot.say_text('Beginning leg two').wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(250)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()

    robot.say_text('Beginning leg three').wait_for_completed()
    robot.drive_straight(distance_mm(282.843), speed_mmps(250)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()

    robot.say_text('Beginning leg four').wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(250)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()

    robot.say_text('Beginning leg five and six').wait_for_completed()
    robot.drive_straight(distance_mm(400), speed_mmps(250)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.turn_in_place(degrees(-135)).wait_for_completed()

    robot.say_text('Beginning leg seven').wait_for_completed()
    robot.drive_straight(distance_mm(282.843), speed_mmps(250)).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.turn_in_place(degrees(135)).wait_for_completed()

    robot.say_text('Beginning leg eight').wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(250)).wait_for_completed()
    robot.say_text('I have reached the end of the line').wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.FrustratedByFailureMajor).wait_for_completed()
    robot.play_anim_trigger(cozmo.anim.Triggers.FacePlantRoll).wait_for_completed()
    # robot.play_anim_trigger(cozmo.anim.Triggers.DizzyShakeLoop).wait_for_completed()
    robot.play_song(notes, loop_count=1).wait_for_completed()

cozmo.run_program(cozmo_program,use_viewer=True, force_viewer_on_top=True)