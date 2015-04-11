#! /bin/python

import curses
from dungeon import Dungeon

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)
isRunning = True

caves = Dungeon(60, 8, 3, stdscr)

try:

	while isRunning:
		caves.render()		
		event = stdscr.getch()
		if event == ord('q'): break
		if event == ord('='): caves.ascend()
		if event == ord('-'): caves.descend()

	curses.endwin()

except Exception as e:
	curses.endwin()
	print(e)

