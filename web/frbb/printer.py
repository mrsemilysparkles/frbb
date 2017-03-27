#!/usr/bin/env python
# coding: utf-8

import django_rq
from django_rq import job
from rq import Queue
from redis import Redis

from Adafruit_Thermal import *
from PIL import Image

TERMS_OF_SERVICE="""
Thanks for using
Any True Meaning,
a place to share poetry. This
service is brought to you by the
bunnies at Serious Camp, located
somewhere at Flipside.\n\n

PLEASE READ THESE TERMS AND CONDITIONS CAREFULLY.
BY CREATING AN ACCOUNT YOU AGREE TO BE BOUND BY 1ST REGIONAL 
BUNNY BANK, AS PARTIALLY DESCRIBED IN THE TERMS AND CONDITIONS BELOW. THESE TERMS AND
CONDITIONS ARE SUBJECT TO CHANGE. ANY CHANGES WILL
BE AVAILABLE UPON REQUEST FROM TIME TO TIME. IF YOU DO
NOT AGREE WITH THESE TERMS AND CONDITIONS, PLEASE CONTACT YOUR NEAREST 
1ST REGIONAL BUNNY BANK BRANCH OFFICE DURING REGULAR BUSINESS HOURS.\n\n

Unauthorized use of 1st Regional Bunny Bank's kiosk, systems, including but not limited to
unauthorized entry into 1st Regional Bunny Banks systems, misuse of account codes or any
information is strictly prohibited.\n

Applicable use is allowed as permitted by the first law of Benjamin, along with Flopsy 
and Peter control laws. With any deviation from these laws 1st Regional Bunny Bank and its
affiliate agents have a right or duty to provide , ice cream, sweets, cures, and 
champagne at branch office locations throughout Flipside.
"""

TOS_MESSAGE ="""
This message is for the designated recipient only and may contain saucy,
thoughtful, challenging, comforting or otherwise mind-expanding information
that is protected from disclosure. If you have any questions with this art,
or otherwise believe that you have received this message in error, please 
speak to a registered Bunny with Serious Camp. Any other use of this message
by you is prohibited, unless it will get you consensually laid. If the reader
of this message is not the intended recipient, you are hereby notified that
any dissemination, distribution or copying of this communication is wantonly
encouraged and might serve as good fodder for an additional deposit into the
1st Regional Bunny Bank."""


def text_format(text, length=30):
    strings = text.split()
    char_count = 0
    line = ""
    output = ""
    for counter, string in enumerate(strings):
        char_count += len(string)+1
        if char_count > length:
            char_count = len(string);
            output += line
            output += '\n'
            line = ""

        line += " " + string

        if counter == len(strings)-1:
            output += line
            output += '\n'
    return output


def print_new_account_info(account_number, pin_number, tos):
    queue = django_rq.get_queue()
    queue.enqueue(__print_new_account_info, account_number, pin_number, tos)

def print_poem(poem_text, upc):
    queue = django_rq.get_queue()
    poem = text_format(poem_text, length=29)
    queue.enqueue(__print_poem, poem, upc)

@job
def __print_new_account_info(account_number, pin_number, tos):
    printer = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=60)
    
    printer.setSize('M')
    printer.justify('C')
    printer.println("1st Regional Bunny Bank\n\n")

    printer.boldOn()
    printer.println("================================")
    printer.boldOff()

    printer.boldOn()
    printer.boldOn()
    printer.println("================================")
    printer.boldOff()
    printer.println("================================")
    printer.boldOff()
    printer.setSize('S')
    printer.justify('C')
    printer.println("Here at 1st Regional BB")
    printer.println("we're proud to provide you")
    printer.println("with words when you're")
    printer.println("struggling to find them.")
    
    printer.justify('C')
    printer.println("================================")

    printer.justify('C')
    printer.setSize('S')
    printer.println("Account #")
    printer.setSize('M')
    printer.println(account_number)
    printer.setSize('S')
    printer.println("Pin #")
    printer.setSize('M')
    printer.println(pin_number)
    printer.setSize('S')
    printer.println("================================")

    printer.justify('L')
    printer.println("\n")
    printer.println("With your new account you")
    printer.println("have the following options:")

    printer.boldOn()
    printer.println("1. Deposit")
    printer.boldOff()
    printer.println("Your balance is increased by one")
    printer.println("and the poem is printed.")

    printer.boldOn()
    printer.println("2. Withdraw Personal")
    printer.boldOff()
    printer.println("Your balance is not affected")
    printer.println("and the poems are printed")

    printer.boldOn()
    printer.println("3. Withdraw Community")
    printer.boldOff()
    printer.println("Your balance is decreased by x")
    printer.println("and the poems are printed")
    printer.println("\n\n\n")
    printer.println("--------------------------------")
    printer.println("--------------------------------")
    printer.println(text_format(TERMS_OF_SERVICE))
    printer.println("--------------------------------")

    printer.feed(30)

@job
def __print_poem(poem_text, upc):
    printer = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=60)
    printer.setSize('M')
    printer.justify('C')
    printer.println("1st Regional Bunny Bank\n\n")
    printer.println("\n")
    printer.justify('C')
    printer.println("================================")
    
    printer.justify('C')
    printer.setSize('M')
    printer.println(poem_text, length=29)
    
    printer.feed(1)
    printer.setBarcodeHeight(100)
    printer.printBarcode(upc, printer.UPC_A)

    #printer.setSize('S')
    #printer.setSize('S')
    #printer.println(text_format(TOS_MESSAGE))

    printer.feed(30)

    printer.sleep()
    printer.wake()
    printer.setDefault()


