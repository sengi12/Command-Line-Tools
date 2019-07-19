## Bandit Walkthrough (0-34)

#### Level 0:

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

`password: bandit0`

#### Level 0 > Level 1

```bash
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

#### Level 1 > Level 2

```bash
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```

#### Level 2 > Level 3

```bash
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

#### Levle 3 > Level 4

```bash
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 16  2018 .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

#### Level 4 > Level 5

```bash
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls -la
total 48
drwxr-xr-x 2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file00
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file01
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file02
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file03
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file04
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file05
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file06
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file07
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file08
-rw-r----- 1 bandit5 bandit4   33 Oct 16  2018 -file09
bandit4@bandit:~/inhere$ file ./-*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

#### Level 5 > Level 6

```bash
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls -la
total 88
drwxr-x--- 22 root bandit5 4096 Oct 16  2018 .
drwxr-xr-x  3 root root    4096 Oct 16  2018 ..
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere00
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere01
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere02
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere03
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere04
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere05
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere06
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere07
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere08
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere09
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere10
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere11
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere12
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere13
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere14
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere15
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere16
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere17
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere18
drwxr-x---  2 root bandit5 4096 Oct 16  2018 maybehere19
bandit5@bandit:~/inhere$ find ./ -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

#### Level 6 > Level 7

```bash
bandit6@bandit:~$ ls
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

#### Level 7 > Level 8

```bash
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ cat data.txt | grep millionth
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

#### Level 8 > Level 9

```bash
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

#### Level 9 > Level 10

```bash
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ strings data.txt | grep '='
2========== the
========== password
>t=	yP
rV~dHm=
========== isa
=FQ?P\U
=	F[
pb=x
J;m=
=)$=
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
iv8!=
```

#### Level 10 > Level 11

```bash
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

#### Level 11 > Level 12

```bash
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt | tr a-zA-Z n-za-mN-ZA-M
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

#### Level 12 > Level 13

```bash
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ file data.txt
data.txt: ASCII text
bandit12@bandit:~$ mkdir /tmp/stw
bandit12@bandit:~$ cd /tmp/stw
bandit12@bandit:/tmp/stw$ xxd -r ~/data.txt > data.txt
bandit12@bandit:/tmp/stw$ file data.txt
data.txt: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/stw$ zcat data.txt > new
bandit12@bandit:/tmp/stw$ ls
data.txt  new
bandit12@bandit:/tmp/stw$ file new
new: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/stw$ bzip2 -d new
bzip2: Can't guess original name for new -- using new.out
bandit12@bandit:/tmp/stw$ ls
data.txt  new.out
bandit12@bandit:/tmp/stw$ file new.out
new.out: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/stw$ zcat new.out > evenNewer
bandit12@bandit:/tmp/stw$ ls
data.txt  evenNewer  new.out
bandit12@bandit:/tmp/stw$ file evenNewer
evenNewer: POSIX tar archive (GNU)
bandit12@bandit:/tmp/stw$ tar -xvf evenNewer
data5.bin
bandit12@bandit:/tmp/stw$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/stw$ tar -xvf data5.bin
data6.bin
bandit12@bandit:/tmp/stw$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/stw$ bzip2 -d data6.bin
bzip2: Can't guess original name for data6.bin -- using data6.bin.out
bandit12@bandit:/tmp/stw$ ls
data5.bin  data6.bin.out  data.txt  evenNewer  new.out
bandit12@bandit:/tmp/stw$ file data6.bin.out
data6.bin.out: POSIX tar archive (GNU)
bandit12@bandit:/tmp/stw$ tar -xvf data6.bin.out
data8.bin
bandit12@bandit:/tmp/stw$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/stw$ zcat data8.bin > newest
bandit12@bandit:/tmp/stw$ ls
data5.bin  data6.bin.out  data8.bin  data.txt  evenNewer  newest  new.out
bandit12@bandit:/tmp/stw$ file newest
newest: ASCII text
bandit12@bandit:/tmp/stw$ cat newest
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

#### Level 13 > Level 14

```bash
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
Could not create directory '/home/bandit13/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit13/.ssh/known_hosts).
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

#### Level 14 > Level 15

```bash
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr

Connection closed by foreign host.
```

#### Level 15 > Level 16

```bash
bandit15@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEBadydTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMTkwMjI3MDg1MTQ5WhcNMjAwMjI3MDg1MTQ5WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMyEZzRA
+5ll7Ap2bwla+8x39mTviZKqrjnmLuTZj1U3mugt3G2JI5loXyjnFxlXnHUGy/xI
OiACFOEJCce2VIkarMa1Cy13wtGuLoZxjcYSAIMzIOPykCh9+FJ89Tt1TIVXmO0C
TJaxFMhKdX0ALZlxjN1+xoZgeOtN7yfhprjjAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBACNP1/t8pfANluA2MuoxCAkie0bDCUL/ZV7FDaH1YUAEG7wEZVFJ
Pt8+6L8HkLYcuCPtjc2uxA8yEiqS7fiYRU26PmrQXzm09W0ah1pq+7NGMLKz596B
AIpiTkVpA7YCUvGcYvz6yXS202e2GbLOulF2l9kx6hhhBCWubeqh2IjR
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 70C2FD5AAD61D9B3D703D795E73F1A3F03F7E26A5A06BCA11C432CAC8F47A676
    Session-ID-ctx:
    Master-Key: D0520F9863B1041ADC76611C749DA98DA2919ED0222A4B4CE107886D432DC53F4E5831C502DAB5A41A675C71E8F972D0
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - df 12 86 44 83 09 d4 62-75 55 25 0c f8 4f 2c 53   ...D...buU%..O,S
    0010 - f4 26 47 23 20 44 e5 8d-5a bb aa 04 e4 f4 ae 7f   .&G# D..Z.......
    0020 - 61 26 24 4b 9f be fb 0a-c8 14 f6 02 7c d4 fa ad   a&$K........|...
    0030 - cb 28 54 0b 92 f2 2d ec-71 3a 61 4e d7 44 ad fd   .(T...-.q:aN.D..
    0040 - 82 c1 50 e4 f1 9b cd d7-6d a3 14 36 a5 88 58 90   ..P.....m..6..X.
    0050 - da c8 bd f0 59 95 dc 5e-c9 80 11 35 2b dd 9c 08   ....Y..^...5+...
    0060 - 1d c5 27 5a 6b 2b 56 4d-63 8c a0 33 a5 2e ee 93   ..'Zk+VMc..3....
    0070 - ff 27 05 05 4e b8 15 f6-86 45 45 f1 99 a2 6c 22   .'..N....EE...l"
    0080 - 72 8d 1d 40 1e d1 2c a0-c9 03 35 01 b2 a9 c4 5f   r..@..,...5...._
    0090 - 79 ce 8a 40 bb 05 39 22-a0 36 7b d5 80 c3 ce 56   y..@..9".6{....V

    Start Time: 1563501441
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd

closed
```

#### Level 16 > Level 17

```bash
bandit16@bandit:~$ nmap -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-07-19 04:09 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00033s latency).
Not shown: 999 closed ports
PORT      STATE SERVICE
31518/tcp open  unknown
31790/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
bandit16@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEFAEx+jANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMTkwNjAzMTk0NzM1WhcNMjAwNjAyMTk0NzM1WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAOtGIwGZ
orvQkbT7OmgRlOcpO89Qe67Sflvo+HkEWkBTHkk8kHDb5C/AZewts9hK3e/xHzfW
dKtev84q0uD9MZGn9V8fpzg7cE/WpF4AORkncch18hKsAxzkcedPRwOp0Ds4Z7iu
7lCk49eQQUxFQGmce7LI+2liISdl/2SxGnM/AgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAGTkwYZlA64cYJ9A/fVrNmRHJzULqj/rNslQP35Ur7OmJ2UpMMEd
noMwf5Kqr4c3ib0mDjBPEyNKnIapy78Fb47BGGBgQCRryDXXxQL76hLfM+hzQ6dS
dKQ5/A5QK/PUV4+yUO9jIB1Xi2r8+A41Oo4VIp2vzIFWwsh68oX7VFUM
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: B4C8E210D50D32E838C6725B1004184DCCDAC18F9D21FB92326FBE9EBD7BFFB6
    Session-ID-ctx:
    Master-Key: 7CB79E03F151F4937AAF39AE5BC9FE1A3EA70B706E680FFC30D5EE4FB4A8790125A30BCD11ACB21931C09DFA196DBCB2
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 60 b9 89 77 48 27 be de-42 fa 15 d9 21 20 46 54   `..wH'..B...! FT
    0010 - 1f 9f 40 f8 cd 61 e7 7e-b1 54 7b d0 a7 b2 e5 a4   ..@..a.~.T{.....
    0020 - 9b 55 da 01 4e 50 4b af-76 09 90 38 99 7b 1c 19   .U..NPK.v..8.{..
    0030 - 3e 23 2f 74 81 00 ab 01-59 49 f6 be ff 6e ef 4f   >#/t....YI...n.O
    0040 - e7 9f af 01 f6 18 93 df-a3 69 24 a8 b2 7d 3a ed   .........i$..}:.
    0050 - 02 05 9c 4a ed 66 a4 c3-62 37 31 9f f1 22 6d 7d   ...J.f..b71.."m}
    0060 - 47 11 44 9e 0b ea 16 5b-f2 32 36 67 63 17 ba 6c   G.D....[.26gc..l
    0070 - 3a bc 76 aa 2d cb 9c 02-71 3b 8a f8 60 87 01 f9   :.v.-...q;..`...
    0080 - e6 4c bd 5d fb ad 21 3a-cf 0a 50 8a a1 36 5b 17   .L.]..!:..P..6[.
    0090 - 12 b5 9f a1 17 9b 3b 07-12 95 72 14 12 b4 7f 7e   ......;...r....~

    Start Time: 1563502183
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
bandit16@bandit:~$ mkdir /tmp/sos
bandit16@bandit:~$ cd /tmp/sos
bandit16@bandit:/tmp/sos$ touch sshkey.private
bandit16@bandit:/tmp/sos$ vi sshkey.private
bandit16@bandit:/tmp/sos$ chmod 600 sshkey.private
bandit16@bandit:/tmp/sos$ ssh -i sshkey.private bandit17@localhost
Could not create directory '/home/bandit16/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit16/.ssh/known_hosts).
bandit17@bandit:~$
```

#### Level 17 > Level 18

```bash
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
---
> hlbSBPAWJmL6WFDb06gpTx1pPButblOA
```

#### Level 18 > Level 19

```bash
Enjoy your stay!

Byebye !
Connection to bandit.labs.overthewire.org closed.
ssh bandit18@bandit.labs.overthewire.org -p2220 cat readme
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit18@bandit.labs.overthewire.org's password:
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

#### Level 19 > Level 20

```bash
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id
bandit19@bandit:~$ ./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
bandit19@bandit:~$ ./bandit20-do whoami
bandit20
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

#### Level 20 > Level 21

```bash

```

#### Level 21 > Level 22

```bash

```

#### Level 22 > Level 23

```bash

```

#### Level 23 > Level 24

```bash

```

#### Level 24 > Level 25

```bash

```

#### Level 25 > Level 26

```bash

```

#### Level 26 > Level 27

```bash

```

#### Level 27 > Level 28

```bash

```

#### Level 28 > Level 29

```bash

```

#### Level 29 > Level 30

```bash

```

#### Level 30 > Level 31

```bash

```

#### Level 31 > Level 32

```bash

```

#### Level 32 > Level 33

```bash

```

#### Level 33 > Level 34

```bash

```