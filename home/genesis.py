import random

def generate_id():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                  'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    _pname = []
    coin_flip = random.randint(0, 1)
    if coin_flip == 0:
        # indexes for consonant and vowel lists, respectively
        c_index = 0
        v_index = 0
        vow_list = [random.randrange(0, 5, 1) for i in range(6)]
        cons_list = [random.randrange(0, 19, 1) for i in range(4)]
        print(vow_list)
        for i in range(0, 11):
            if i % 2 == 0:
                _pname.append(vowels[vow_list[v_index]])
                v_index += 1
            elif i % 2 == 1:
                if i == 5:
                    _pname.append('-')
                else:
                    _pname.append(consonants[cons_list[c_index]])
                    c_index += 1
    elif coin_flip == 1:
        c_index = 0
        v_index = 0
        vow_list = [random.randrange(0, 5, 1) for i in range(4)]
        print(vow_list)
        cons_list = [random.randrange(0, 19, 1) for i in range(6)]
        for i in range(0, 11):
            if i % 2 == 0:
                _pname.append(consonants[cons_list[v_index]])
                v_index += 1
            elif i % 2 == 1:
                if i == 5:
                    _pname.append('-')
                else:
                    _pname.append(vowels[vow_list[c_index]])
                    c_index += 1
    new_proj = ''.join(_pname)
    return new_proj

