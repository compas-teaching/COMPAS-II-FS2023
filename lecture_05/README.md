# COMPAS II: Robot control with COMPAS RRC

Online non-real time control of industrial robots.

Components of an RRC deployment.

Communication primitives (blocking, futures, cyclic).

Instructions.

Multi controller & location coordination.

👉 [Slides](https://docs.google.com/presentation/d/1dLaqzAVe4KJIF0qUSySq08IEOWcyTXgnXLCuTqLFaGk/edit?usp=sharing)
🤖 [GoFa station PackNGo file](https://nextcloud.ethz.ch/s/ngy7Hz2AK6dLPrR)
📜 [Quiz assignment](https://forms.gle/yaVm9z7XSexmf6pZ9)

## Examples

Before running this examples, you have to connect to a robot controller. Either a real one, or a simulated one.

To run a simulated one, use the following instructions (only Windows, unfortunately):

1. Install [ABB RobotStudio](https://new.abb.com/products/robotics/robotstudio) (see [more installation notes here](https://github.com/compas-rrc/compas_rrc_start#robotstudio))
2. Install [ABB GoFa robot station](https://nextcloud.ethz.ch/s/ngy7Hz2AK6dLPrR) (`Pack&Go .rspag` files are installed simply by opening them from RobotStudio).
3. Start (`compose up`) our [docker containers](../docker/gofa-noetic/docker-compose.yml)

* Communication
  * [Hello World](701_hello_world.py)
  * [Send instruction](702_send.py)
  * [Send instruction with feedback (blocking)](703_send_and_wait.py)
  * [Send instruction with deferred feedback (non-blocking)](704_send_and_wait_in_the_future.py)

* Basic setup
  * [Set tool](705_set_tool.py)
  * [Set work object](706_set_work_object.py)
  * [Set acceleration](707_set_acceleration.py)
  * [Set max speed](708_set_max_speed.py)

* Motion instructions
  * [Get/Move to frame](709_get_and_move_to_frames.py)
  * [Get/Move to joints (Configuration)](710_get_and_move_to_joints.py)
  * [Get/Move to Robtarget](711_get_and_move_to_robtarget.py)
  * [Move to home configuration](712_move_to_home.py)

* Utilities
  * [No-op/ping](713_no-op.py)
  * [Print Text on flex pendant](714_print_text.py)
  * [Wait time](715_wait_time.py)
  * [Stop/Pause program](716_stop.py)
  * [Stopwatch on the robot](717_watch.py)
  * [Custom instruction](718_custom_instruction.py)

* Input/Output signals
  * [Read analog input](719_input_analog.py)
  * [Read digital input](720_input_digital.py)
  * [Read group input](721_input_group.py)
  * [Set analog output](722_output_analog.py)
  * [Set digital output](723_output_digital.py)
  * [Set group output](724_output_group.py)

