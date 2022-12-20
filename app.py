#! /usr/bin/python3
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PlatformConstants import LINE_SEP as lsep
from custom_modules.PatternConstants import (
    is_number_only as isnumber,
    is_alpha_only as isletter,
)
from custom_modules.ArgumentManager import filtered as args, filtered_count as argsc


cus = cms["custom"]


user_input = input("Enter something:\t")
users_input_space_split = user_input.split(" ")

m_header = cus(255, 222, 0, "You Entered:")
m_body = cus(255, 255, 255, "{}".format(user_input))
msg = "{} {}{}".format(m_header, m_body, lsep)

print("Count:\t{}".format(len(users_input_space_split)))


print("{}".format(msg))
