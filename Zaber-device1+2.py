from zaber_motion import Units, Library
from zaber_motion.ascii import Connection
import asyncio

Library.enable_device_db_store()

with Connection.open_serial_port("COM7") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device_v = device_list[0]  # h = horizontal
    device_h = device_list[1]  # v = vertical

    axis_h = device_h.get_axis(1)  # get axis 1 out of 1 for device_v
    axis_v = device_v.get_axis(1)  # get axis 1 out of 1 for device_h


    def place_on_sample(h, v):
        axis_h.move_relative(h, Units.LENGTH_MILLIMETRES)
        axis_v.move_relative(v, Units.LENGTH_MILLIMETRES)


    def place_off_sample():
        axis_v.home(wait_until_idle=False)
        axis_h.home(wait_until_idle=False)



    if axis_v.is_homed():
        pass
    else:
        axis_v.home()

    if axis_h.is_homed():
        pass
    else:
        axis_h.home()


    place_on_sample(100, 100)
    place_off_sample()

    position_axis_h = axis_h.get_position(Units.LENGTH_MILLIMETRES)
    # print(position_axis_h)
