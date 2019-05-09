import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps



def cozmo_program(robot: cozmo.robot.Robot):

    robot.say_text("Beginning our journey to Step 1").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()

    robot.turn_in_place(degrees(90)).wait_for_completed()

    print("Playing Animation Trigger 2: (Ignoring the body track)")
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()


    robot.say_text("step 2").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()

    print("Playing Animation Trigger 1:")
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()

    robot.turn_in_place(degrees(135)).wait_for_completed()

    robot.say_text("step 3").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()
    

    print("Playing Animation 3:")
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()

    robot.turn_in_place(degrees(-135)).wait_for_completed()

    robot.say_text("step 4").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()

    print("Playing Animation Trigger 1:")
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession).wait_for_completed()


    robot.turn_in_place(degrees(-90)).wait_for_completed()

    robot.say_text("step 5").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()

    print("Playing Animation Trigger 2: (Ignoring the body track)")
    robot.play_anim_trigger(cozmo.anim.Triggers.CubePounceLoseSession, ignore_body_track=True).wait_for_completed()


    robot.say_text("step 6").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()

    print("Playing Animation 3:")
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()


    robot.turn_in_place(degrees(-135)).wait_for_completed()

    robot.say_text("step 7").wait_for_completed()
    
    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()
    
    print("Playing Animation 3:")
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()


    robot.turn_in_place(degrees(135)).wait_for_completed()

    robot.say_text("step 8").wait_for_completed()

    robot.drive_straight(distance_mm(200),speed_mmps(200)).wait_for_completed()

    print("Playing Animation 3:")
    robot.play_anim(name="anim_poked_giggle").wait_for_completed()


    robot.say_text("im done").wait_for_completed()

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


cozmo.run_program(cozmo_program,use_viewer=True,force_viewer_on_top=True)