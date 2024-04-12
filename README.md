## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `my_bot` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).

🔽 NEW 🔽
---------------------------------------------------------------------------------------------

## Robots Soccer Game 🤖

To try the 2-player robots soccer game, use the command: `ros2 launch my_bot soccer_game.launch.py world:=<soccer.world path>`

To control the 2 robots you may either use the `teleop_twist_keyboard` or `teleop_twist_joy` nodes depending on your preference, don't forget to add `--ros-args --remap cmd_vel:=/<bot1 or bot2 for both robots>/cmd_vel`
![Screenshot from 2024-04-12 23-02-58](https://github.com/MennaMagdie/my_bot/assets/73966691/6ba4391f-c556-42d2-81fe-69d1eb74a5f8)
