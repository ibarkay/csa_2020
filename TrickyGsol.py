#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tricky by Fabien and ibarkay.

from pwn import *
import sys
import os
import random
from collections import Counter
def seety(a,b):
    charsy = []
    for i in sorted(list(set(a))):
        for j in sorted(list(set(b))):
            if i == j:
                charsy.append(i)
    return charsy

f = open('words.txt','r')
word_list = f.read().splitlines()
f.close()

host = 'tricky-guess.csa-challenge.com'
port =  2222
s = remote(host,port)
#Global vars
NUM = 0
word1 = ''
word2 = ''
wordsTry = 0
dicy = {}
# INIT
print s.recv()
# GO
print s.recv()

while True:
    try:
        if wordsTry == 0: #Try 1
                random_word = word_list[random.randint(1,1000)]
                print "random_word: ",random_word
                word1 = random_word # check word
                s.send(random_word)
                os.system('sleep 0.3')
                NUM = int(s.recv())  #getting the right number of chars
                print "number is : " + str(NUM)
                wordsTry += 1
                dicy[word1] = NUM

                for i in word_list:
                    if len(seety(i,word1)) < NUM:
                        word_list.remove(i)
                print 'TRY #1 len pof possibales is : {}'.format(len(word_list))


        elif wordsTry == 1: # try 2
            random_word = random.choice(word_list)
            print "random_word: ", random_word
            word2 = random_word  # check word
            s.send(random_word)
            os.system('sleep 0.3')
            NUMcheck = int(s.recv())  # getting the right number of chars
            if NUMcheck > NUM:
                NUM = NUMcheck
                for i in word_list:
                    if len(seety(i, word2)) < NUM:
                        word_list.remove(i)

                print "number is : " + str(NUM)
                wordsTry += 1
                #print 'TRY #2 len pof possibales is : {}'.format(len(word_list))
                dicy[word2] = NUM
            else:
                print "number is : " + str(NUMcheck)
                wordsTry += 1
                print 'TRY #2 len pof possibales is : {}'.format(len(word_list))
                dicy[word2] = NUMcheck


        elif wordsTry >= 2 :
            random_word = random.choice(word_list)
            print "random_word: ", random_word
            word2 = random_word  # check word
            s.send(random_word)
            os.system('sleep 0.3')
            NUMcheck = int(s.recv())  # getting the right number of chars
            if NUMcheck > NUM:
                NUM = NUMcheck
            print dicy
            for i in word_list:
                for j in dicy:
                    if len(seety(i, j)) != dicy[j]: # THE MAGIC!
                        #print 'j is : {} and dicky[j] is : {}'.format(j, dicy[j])
                        try:
                            word_list.remove(i)
                        except:
                            pass

            print "number is : " + str(NUM)
            wordsTry += 1
            print 'TRY #2 len pof possibales is : {}'.format(len(word_list))
            dicy[word2] = NUMcheck

    except EOFError as error:
        print(error)
        exit()

s.close()
