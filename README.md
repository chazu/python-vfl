# View Builder - Playing with libtcod and python

[![Build Status](https://drone.itscoming.run/api/badges/chazu/python-vfl/status.svg?ref=refs/heads/master)](https://drone.itscoming.run/chazu/python-vfl)

Goal - make a constraint-based TUI editor for TUI apps. Also a bunch of other crap lives in here for now. Oops.

## TODO
 - Write parser for Extended VFL
 - Write API on top of parser(s)
 - add linter

## DONE
 - Get cursor drag-to-draw-rectangle working in all four quadrants
 - Add nose tests (or whatever is hot now in pyland)
 - Clean up rendering during rectangle drawing
 - Figure out why unit test for normalize_points is passing erroneously
 - Write PEG parser for VFL
