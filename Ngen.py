import calendar
import os
os.system('clear')
#input

banner="""
==================================
= AU : RAMADHANI\t         =
= YT : EMON \t                 =
= GT : github.com/RmHcy07        =
= FB : MUHAMMAD ALFIKRI RAMADHANI=
==================================\t\x1b[1;96m\n\t\t\t\t\t \x1b[1;91m\x1b[1;97m
===============================
[ \x1b[1;92mSIMPLE CALLENDER NEW 2021 !\x1b[1;97m ]
==============================="""
print(banner)
print
tahun = int(input("MASUKAN TH YG ANDA INGIN CARI ? = \x1b[1;96m"))
bulan = int(input("\x1b[1;97mMASUKAN BLN YG ANDA CARI ? = \x1b[1;96m"))
# out put
print '\x1b[1;93m'
print(calendar.month(tahun, bulan))
print '\x1b[1;97m'
 