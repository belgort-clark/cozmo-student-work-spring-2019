import cozmo
import asyncio
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.anim import Triggers


def cozmo_program(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(0), speed_mmps(50)).wait_for_completed()
    robot.say_text("starting animation").wait_for_completed()
    for i in range(8):
        robot.play_anim_trigger(cozmo.anim.Triggers.LaserFace).wait_for_completed()
        robot.drive_straight(distance_mm(driveDistance[i]), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(turnDegree[i])).wait_for_completed()


leftNinty = 90
leftMore = 135
rightNinty = -90
rightMore = -135
noTurn = 0

squareSide = 150
squareDiagonal = squareSide*(2**(0.5))

lookLeft = "LaserFace"
lookRight = "KnockOverEyes"
lookStrait = "LaserFace"

driveDistance = [squareSide, squareSide, squareDiagonal, squareSide, squareSide, squareSide, squareDiagonal, squareSide]
turnDegree = [leftNinty, leftMore, rightMore, rightNinty, noTurn, rightMore, leftMore, noTurn]
lookEyes = [lookStrait, lookLeft, lookLeft, lookRight, lookRight, lookStrait, lookRight, lookLeft]

notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.F2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.G2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C3_Sharp, cozmo.song.NoteDurations.Quarter) ]

cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)