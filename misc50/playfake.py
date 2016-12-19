from random import randint, choice
from string import ascii_uppercase
from hashlib import md5
from secret import msg, key, ctxt2, msg_m

assert (len(key) == 5) and key.isalpha() and key.isupper()

# "msg" is a meaningful English sentence.
assert all(x.isalpha() or x.isspace() for x in msg)
assert "SharifCTF" in msg
assert "contest" in msg

LIN = 'B'
LOUT = 'P'
 
def make_key(key_str):
    #print("key in func:",key_str)
    
    key_str += ascii_uppercase
    #print("key after ascii_uppercase:",key_str)
    key_str = key_str.replace(' ', '').upper().replace(LIN, LOUT)
    #print ("key after replace:",key_str,key_str[1]*2)
    #print(type(key_str))
    seen = set()
    #print(seen)
    seen_add = seen.add
    #print(seen_add)
    return [x for x in key_str if not (x in seen or seen_add(x))]
 
 

 
def make_message(msg):
    #print("msg:",msg)
    msg = msg.replace(' ', '').upper().replace(LIN, LOUT)
    #print("msg after replace:",msg)
    outp = ''
    i = 0
    while True:
        if i+1 >= len(msg):
            if i == len(msg)-1:
                outp += msg[i]
            break
        if msg[i] == msg[i+1]:
            outp += msg[i] + 'Y'
            i += 1
        else:
            outp += msg[i] + msg[i+1]
            i += 2
    if len(outp) % 2 == 1:
        outp += 'Y'
    #print("OUTP:",outp)
    return outp

def get_pos(key, letter):
    i = key.index(letter)
    return (i//5, i%5)

def get_letter(key, i, j):
    i %= 5
    j %= 5
    return key[5*i + j]


def playfair_enc(key, msg):
    #print("key is:",key,"message is:",msg)
    assert len(msg) % 2 == 0
    assert len(key) == 25
    ctxt = ''
    
    for i in range(0, len(msg), 2):
        # print(i)
        r0, c0 = get_pos(key, msg[i])

        r1, c1 = get_pos(key, msg[i+1])
        if r0 == r1:
            ctxt += get_letter(key, r0+1, c0+1) + get_letter(key, r1+1, c1+1)
        elif c0 == c1:
            ctxt += get_letter(key, r0-1, c0-1) + get_letter(key, r1-1, c1-1)
        else:
            ctxt += get_letter(key, r0+1, c1-1) + get_letter(key, r1+1, c0-1)
    return ctxt

def playfair_dec(key, ctxt2):
    #print("key is:",key,"ctxt2 is:",ctxt2)
    assert len(ctxt2) % 2 == 0
    assert len(key) == 25
    msg_m = ''
    
    for i in range(0, len(ctxt2), 2):
        # print(i)
        r0, c0 = get_pos(key, ctxt2[i])

        r1, c1 = get_pos(key, ctxt2[i+1])
        if r0 == r1:
            msg_m += get_letter(key, r0-1, c0-1) + get_letter(key, r1-1, c1-1)
        elif c0 == c1:
            msg_m += get_letter(key, r0+1, c0+1) + get_letter(key, r1+1, c1+1)
        else:
            msg_m += get_letter(key, r0-1, c1+1) + get_letter(key, r1-1, c0+1)
    return msg_m

def make_flag(msg):
    return 'SharifCTF{%s}' % md5(msg.replace(' ', '').upper().encode('ASCII')).hexdigest()
 
if __name__ == '__main__':
    key = make_key(key)
    #print("key finally:",key)
    msg2 = make_message(msg)
    ctxt = playfair_enc(key, msg2)
    #print(type(ctxt))
    print(ctxt)     # KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR
    
    #ctxt2 = [KPDPDGYJXNUSOIGOJDUSUQGFSHJUGIEAXJZUQVDKSCMQKXIR]
    #print("in main:",ctxt2)
    #msg_m = playfair_dec(key,ctxt2)
    print("message _M:",msg_m)
    #print(len(msg_m))
    #print(len(ctxt2))
    #ctxt3 = playfair_enc(key, msg_m)
    #print("this is ctxt3:",ctxt3)
    #msg_m2 = playfair_dec(key,msg_m)
    #print("msg_m2",msg_m2)

    
    # Notice that flag is generated using "msg", not "msg2".
    # After decryption, you get "msg2".
    # You must manually add spaces and perform other required changes to get "msg".
    
    flag = make_flag(msg_m)
    print(flag)


def brute_force():
    # if __name__ == '__main__':
        report=10000
        count=0
        for i in ascii_uppercase:
               ali = ascii_uppercase.replace(i,'')
               for j in ali:
                       alj = ali.replace(j,'')                        
                       for k in alj:
                               alk = alj.replace(k,'')                        
                               for l in alk:
                                       alL = alk.replace(l,'')                 
                                       for m in alL:
                                            count+=1
                                            if count%report ==0:
                                                print(count//report)
                                            rval=playfair_dec(make_key(i+j+k+l+m),ctxt2)
                                                #print(rval)
                                            if ("SHARIFCTF" in rval) and ("CONTEST" in rval):
                                                print("found candidate: %s"%rval)














