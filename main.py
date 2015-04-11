#! /bin/python

import curses
from level import Level

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)
isRunning = True

test = Level(20, 5, stdscr)

try:

	while isRunning:
		test.render()	
		event = stdscr.getch()
		if event == ord('q'): break

	curses.endwin()

except Exception as e:
	curses.endwin()
	print(e)

