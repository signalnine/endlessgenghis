#!/usr/bin/env python3

import pronouncing
import sys
import random

file1 = open('famous_ppl.txt', 'r') 
people = file1.readlines() 
random.shuffle(people)

file2 = open('euphemisms.txt', 'r')
euphemisms = file2.readlines()
random.shuffle(euphemisms)

for person in people:
    for euphemism in euphemisms:
        person = person.rstrip()
        last_name = person.split(" ")[-1]
        for p in pronouncing.rhymes(last_name.rstrip()): 
            last = euphemism.split(" ")[-1]
            if p == last.rstrip() and last_name.lower() != last.rstrip():
                euphemism = euphemism.rstrip()
                print(f'♫ I get a little bit {person} / Don\'t want you to {euphemism} / ♪ With nobody else but me')
