#!/usr/bin/env python3
import argparse

_DESCRIPTION = 'Test script demonstrating argparse'

parser = argparse.ArgumentParser(description=_DESCRIPTION)
msg = 'directory  (default: .)'
parser.add_argument('-d', '--directory', default='.', help=msg)
msg = 'First arbitrary integer number'
parser.add_argument('number', type=int, metavar='NUM', help=msg)
msg = 'Second arbitrary integer number'
parser.add_argument('-id', type=int, metavar='NUM', help=msg)
args = parser.parse_args()
print(f"Directory: {args.directory}")
print(f"1st Number: {args.number:d}")
print(f"2nd Number: {args.id:d}")
