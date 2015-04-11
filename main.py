#! /bin/python

import curses
from dungeon import Dungeon

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.keypad(1)
isRunning = True

caves = Dungeon(60, 8, 4, stdscr)

while isRunning:
	caves.render()		
	event = stdscr.getch()
	if event == ord('q'): break
	if event == ord('='): caves.ascend()
	if event == ord('-'): caves.descend()
	if event == ord('h'): caves.movePlayer(-1, 0)
	if event == ord('j'): caves.movePlayer(0, 1)
	if event == ord('k'): caves.movePlayer(0, -1)
	if event == ord('l'): caves.movePlayer(1, 0)

curses.endwin()


