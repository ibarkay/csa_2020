#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CS-Hacked by ibarkay.
optionsss = ['organization\nadministration\nI\nas\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\nI\nas\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\nI\nas\na\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\nI\nas\na\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\nI\nat\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\nI\nat\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\nI\nat\na\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\nI\nat\na\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\nI\nbe\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\nI\nbe\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\nI\nbe\na\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\nI\nbe\na\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\na\nas\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\na\nas\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\na\nas\na\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\na\nas\na\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\na\nat\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\na\nat\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\na\nat\na\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\na\nat\na\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\na\nbe\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\na\nbe\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'organization\nadministration\na\nbe\na\nenvironmental\nabout\naccept\nability\naccording\n', 'organization\nadministration\na\nbe\na\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\nI\nas\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\nI\nas\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\nI\nas\na\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\nI\nas\na\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\nI\nat\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\nI\nat\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\nI\nat\na\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\nI\nat\na\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\nI\nbe\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\nI\nbe\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\nI\nbe\na\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\nI\nbe\na\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\na\nas\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\na\nas\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\na\nas\na\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\na\nas\na\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\na\nat\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\na\nat\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\na\nat\na\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\na\nat\na\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\na\nbe\nI\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\na\nbe\nI\nenvironmental\nabout\nacross\nability\naccording\n', 'particularly\nadministration\na\nbe\na\nenvironmental\nabout\naccept\nability\naccording\n', 'particularly\nadministration\na\nbe\na\nenvironmental\nabout\nacross\nability\naccording\n']

from pwn import *

from arc4 import ARC4
Nrun = 0
#Global vars
for opt in optionsss:
    arc4 = ARC4('csa-mitm-key')
    host = '3.126.154.76'
    port = 80
    s = remote(host, port)
    # INIT
    print s.recv()
    # GO
    print arc4.decrypt(s.recv())
    run = True
    while run:
            #print 'sending : {}'.format(opt)

            s.send(arc4.encrypt(opt) + '\n')

            answer = arc4.decrypt(s.recv())
            print answer
            if 'No'  not in answer:
                print 'Flag found !!!'
                quit()
            # print s.recv()
            print 'run number : {}'.format(Nrun)
            Nrun += 1
            run = False
    s.close()

