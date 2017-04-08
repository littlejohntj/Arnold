#!/usr/bin/env python
# coding: utf-8

# This function makes a list each line of a textfile.
# The textfile should contain a collection of potential 
# usable words for a username, such as animals, female names,
# male names, etc.

from __future__ import print_function
import string
import sys


def names(ffile):
	f=open(ffile, 'r')

	tot=sum(1 for _ in f)
	f.close()
	f=open(ffile, 'r')
	newfile=[]
	for i in range(0,tot):

		newfile=newfile+[f.readline().lower().strip()]

	return newfile