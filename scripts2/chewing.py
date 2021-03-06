# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# libpinyin - Library to deal with pinyin.
#
# Copyright (C) 2011 Peng Wu <alexepico@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


ASCII_CHEWING_INITIAL_LIST = [
    ("CHEWING_ZERO_INITIAL" , None),    #Zero Initial
    ("CHEWING_B" , "ㄅ"),
    ("CHEWING_C" , "ㄘ"),
    ("CHEWING_CH" , "ㄔ"),
    ("CHEWING_D" , "ㄉ"),
    ("CHEWING_F" , "ㄈ"),
    ("CHEWING_H" , "ㄏ"),
    ("CHEWING_G" , "ㄍ"),
    ("CHEWING_K" , "ㄎ"),
    ("CHEWING_J" , "ㄐ"),
    ("CHEWING_M" , "ㄇ"),
    ("CHEWING_N" , "ㄋ"),
    ("CHEWING_L" , "ㄌ"),
    ("CHEWING_R" , "ㄖ"),
    ("CHEWING_P" , "ㄆ"),
    ("CHEWING_Q" , "ㄑ"),
    ("CHEWING_S" , "ㄙ"),
    ("CHEWING_SH" , "ㄕ"),
    ("CHEWING_T" , "ㄊ"),
    ("PINYIN_W" , None),                #Invalid Chewing
    ("CHEWING_X" , "ㄒ"),
    ("PINYIN_Y" , None),                #Invalid Chewing
    ("CHEWING_Z" , "ㄗ"),
    ("CHEWING_ZH" , "ㄓ"),
]

ASCII_CHEWING_INITIAL_MAP = dict([(k, v) for k, v in ASCII_CHEWING_INITIAL_LIST if v])

CHEWING_ASCII_INITIAL_MAP = dict([(v, k) for k, v in ASCII_CHEWING_INITIAL_LIST if v])


ASCII_CHEWING_MIDDLE_LIST = [
    ("CHEWING_ZERO_MIDDLE" , None),     #Zero Middle
    ("CHEWING_I" , "ㄧ"),
    ("CHEWING_U" , "ㄨ"),
    ("CHEWING_V" , "ㄩ"),
]

ASCII_CHEWING_MIDDLE_MAP = dict([(k, v) for k, v in ASCII_CHEWING_MIDDLE_LIST if v])

CHEWING_ASCII_MIDDLE_MAP = dict([(v, k) for k, v in ASCII_CHEWING_MIDDLE_LIST if v])


ASCII_CHEWING_FINAL_LIST = [
    ("CHEWING_ZERO_FINAL" , None),      #Zero Final
    ("CHEWING_A" , "ㄚ"),
    ("CHEWING_AI" , "ㄞ"),
    ("CHEWING_AN" , "ㄢ"),
    ("CHEWING_ANG" , "ㄤ"),
    ("CHEWING_AO" , "ㄠ"),
    ("CHEWING_E" , "ㄝ"),                # merge "ㄝ" and "ㄜ"
    ("INVALID_EA" , None),               #Invalid Pinyin/Chewing
    ("CHEWING_EI" , "ㄟ"),
    ("CHEWING_EN" , "ㄣ"),
    ("CHEWING_ENG" , "ㄥ"),
    ("CHEWING_ER" , "ㄦ"),
    ("CHEWING_NG" , "ㄫ"),
    ("CHEWING_O" , "ㄛ"),
    ("PINYIN_ONG" , None),               #"ueng"
    ("CHEWING_OU" , "ㄡ"),
    ("PINYIN_IN" , None),                #"ien"
    ("PINYIN_ING" , None),               #"ieng"
]

ASCII_CHEWING_FINAL_MAP = dict([(k, v) for k, v in ASCII_CHEWING_FINAL_LIST if v])

CHEWING_ASCII_FINAL_MAP = dict([(v, k) for k, v in ASCII_CHEWING_FINAL_LIST if v])


ASCII_CHEWING_TONE_LIST = [
    ("CHEWING_ZERO_TONE" , None),     #Zero Tone
    ("CHEWING_1" , " "),
    ("CHEWING_2" , "ˊ"),
    ("CHEWING_3" , "ˇ"),
    ("CHEWING_4" , "ˋ"),
    ("CHEWING_5" , "˙"),
]

ASCII_CHEWING_TONE_MAP = dict([(k, v) for k, v in ASCII_CHEWING_TONE_LIST if v])

CHEWING_ASCII_TONE_MAP = dict([(v, k) for k, v in ASCII_CHEWING_TONE_LIST if v])

CHEWING_INITIAL_LIST = [k for k, v in ASCII_CHEWING_INITIAL_LIST]

CHEWING_MIDDLE_LIST  = [k for k, v in ASCII_CHEWING_MIDDLE_LIST]

CHEWING_FINAL_LIST   = [k for k, v in ASCII_CHEWING_FINAL_LIST]

CHEWING_TONE_LIST    = [k for k, v in ASCII_CHEWING_TONE_LIST]


def gen_entries(items, last_enum, num_enum):
    entries = []
    for enum, item in enumerate(items, start=0):
        entry = '{0} = {1}'.format(item, enum)
        entries.append(entry)

    #last enum
    entry = last_enum + ' = ' + items[-1]
    entries.append(entry)

    #num enum
    entry = num_enum + ' = ' + last_enum + ' + 1'
    entries.append(entry)

    return ",\n".join(entries)


def gen_initials():
    return gen_entries(CHEWING_INITIAL_LIST, 'CHEWING_LAST_INITIAL',
                       'CHEWING_NUMBER_OF_INITIALS')


def gen_middles():
    return gen_entries(CHEWING_MIDDLE_LIST, 'CHEWING_LAST_MIDDLE',
                       'CHEWING_NUMBER_OF_MIDDLES')


def gen_finals():
    return gen_entries(CHEWING_FINAL_LIST, 'CHEWING_LAST_FINAL',
                       'CHEWING_NUMBER_OF_FINALS')


def gen_tones():
    return gen_entries(CHEWING_TONE_LIST, 'CHEWING_LAST_TONE',
                       'CHEWING_NUMBER_OF_TONES')


### main function ###
if __name__ == "__main__":
    print(ASCII_CHEWING_INITIAL_LIST)
    print(ASCII_CHEWING_INITIAL_MAP)
    print(CHEWING_ASCII_INITIAL_MAP)

    print(ASCII_CHEWING_MIDDLE_LIST)
    print(ASCII_CHEWING_MIDDLE_MAP)
    print(CHEWING_ASCII_MIDDLE_MAP)

    print(ASCII_CHEWING_FINAL_LIST)
    print(ASCII_CHEWING_FINAL_MAP)
    print(CHEWING_ASCII_FINAL_MAP)

    print(ASCII_CHEWING_TONE_LIST)

    print(gen_initials())
    print(gen_middles())
    print(gen_finals())
    print(gen_tones())
