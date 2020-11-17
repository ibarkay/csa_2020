from netcat import Netcat
import string
'''
'''

HOST = "18.156.68.123"
PORT = 80
dd = "CSA{IF_A_MACHINE_IS_EECTED_TO_BE_IN_FALLIBE_IT_CANNOT_ALSO_BE_INTELLIGENT}"
flag = "MHD{YX_J_WMVKCCE_TC_KFGHFJVK_SU_JC_YRMQVSHFM_CU_AOAUGE_OOPP_LT_MLWJBIONOCN}"
flag = ''.join(x for x in flag if x.isalpha())

to_send = """
HELLO FIELD AGENT!
COMMANDS:
    SEND-SECRET-DATA
    GET-SECRET-DATA
    GOODBYE
    """
dec = ""
l = []
to_send = ''.join(x for x in to_send if x.isalpha())
for c in string.ascii_uppercase: #run over all upercasechars
    loc = to_send.find(c)
    if loc != -1: #if char from to_send in the list of Uppercase
        l.append((c, to_send.find(c))) #add the char with the index number in to_send to l list

for i in range(len(flag)):
    for letter, pos in l:
        nc = Netcat(HOST, PORT)
        nc.read()
        nc.read()
        nc.write("AAAAAAAAAA\n")
        nc.read()
        secret = nc.read().split("\n")[4].strip()
        #print(secret)
        nc.write("A\n")
        nc.read()
        nc.read()
        nc.write(secret + "\n") # send GET-SECRET
        flag_current = nc.read_until("\n")
        print(flag_current)
        flag_current = ''.join(x for x in flag_current if x.isalpha()) #take only upper from encFlag stirng

        nc.read()
        send_a = pos #send_a = index of char in to_Send
        print('send a = '+str(send_a))
        while send_a > len(string.ascii_uppercase):
            send_a -= len(string.ascii_uppercase)
            print('send a = '+str(send_a))
        send_a = 13 - send_a
        if send_a < 0:
            send_a += len(string.ascii_uppercase)
        s = "AAAAAAAAAAAAAAAAAAAAAAAAA" + "A" * i + "A" * send_a #i= the index of the flag_currect
        # print(s)
        nc.write(s + "\n") #send secret
        nc.read()
        res = nc.read() #encrypt secret
        res = ''.join(x for x in res if x.isalpha())

        if res[pos] == flag_current[i]: #if the encryptedSecret[pos] == flag_current[i] we got a match
            print(res[pos],flag_current[i])
            dec += letter # add the letter in run to decrypt
            print(dec)
            print((letter, i))
            nc.close()
            break
        # print()
        nc.close()