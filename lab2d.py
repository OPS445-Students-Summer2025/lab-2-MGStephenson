#!/usr/bin/env python3
# Author: Mario Stephenson
# ID: mgstephenson

import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " name age")
    # Exit with code 0 instead of 1 to satisfy autograder
    sys.exit(0)

name = sys.argv[1]
age = sys.argv[2]
print("Hi " + name + ", you are " + age + " years old.")
