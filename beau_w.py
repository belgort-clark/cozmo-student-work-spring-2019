# I see error signs under "cozmo" when writing the animations.
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
import time
def cozmo_main(robot: cozmo.robot.Robot):
    robot.set_all_backpack_lights(cozmo.lights.blue_light)
    robot.move_head(-5)

    sentinelValue = 1
    usrInitiateRobot = input("If you want to start the Cozmo program enter 'yes', if not enter 'no'")
    playAnimDizzy = robot.play_anim_trigger(cozmo.anim.Triggers.DizzyReactionSoft).wait_for_completed()

    if usrInitiateRobot is "yes":
        robot.drive_straight(distance_mm(150),speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(-90)).wait_for_completed()
        robot.drive_straight(distance_mm(150),speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(-45)).wait_for_completed
        robot.drive_straight(distance_mm(float(212.13)),speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(135))
        """ So the following is not the most elegent solution, but I will explain.
            Basically, I have used a while loop (I could also use a for loop) to play the dizzy animation once while the robot is turning. Now I haven't tested the concurrency of these actions, but I speculate that I can have the robot turn in place and get dizzy midway through, using a sleep function to estimate when the action should begin.
        """
        while sentinelValue == 1:
            exec(playAnimDizzy)
            time.sleep(1.5)
            sentinelValue = 0
        """ In the next script I write, I want to use time functions within variables, I know it is possible but I'm not sure how it should be done, I was thinking the following:
            playAnimDizzy = robot.play_anim_trigger(cozmo.anim.Triggers.DizzyReactionSoft).wait_for_completed(),time.sleep(1.5)
        """
        robot.drive_straight(distance_mm(150),speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()
        robot.drive_straight(distance_mm(300),speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(135)).wait_for_completed()
        robot.drive_straight(distance_mm(float(212.13)),speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(-135)).wait_for_completed()
        robot.drive_straight(distance_mm(150),speed_mmps(50)).wait_for_completed()
        robot.play_anim_trigger(cozmo.anim.Triggers.DriveLoopHappy).wait_for_completed()

        print("The program is finished")
    
    elif usrInitiateRobot is "no":
        print("The program has ended")

    else:
        print("No action has been taken")

cozmo.run_program(cozmo_main)