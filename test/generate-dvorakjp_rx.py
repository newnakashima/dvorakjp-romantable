# coding: utf-8
from collections import OrderedDict


def main():
    f = open('romantable_original.txt')
    #  vowels_d = {'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お'}
    dual_vowels_d = {"'": 'aい', ',': 'oう', '.': 'eい', 'p': 'uう', ';': 'aん', 'q': 'oん', 'j': 'eん', 'k': 'uん', 'x': 'iん'}
    vowels_list = {'a', 'i', 'u', 'e', 'o'}
    consonants_list = ['k', 'c', 'g', 's', 'g', 't', 'd', 'n', 'h', 'f', 'b', 'p', 'm', 'y', 'r', 'w']
    contracted_sounds_list = ['y', 'w']
    conbination_key_d = {'h': ['p', 'j', 'k', 'r', 'l', 'n', 's', 'w', 'v', 'z'], 'n': ['p', 'q', 'j', 'k', 'x', 'f', 'g', 'k', 'd', 'h', 't', 'b', 'm']}

    keymap_d = {}
    for line in f.readlines():
        splited_line = line.strip().split('\t')
        keymap_d[splited_line[0]] = ''.join(splited_line[1:])
    f.close()

    print(keymap_d)

    # generate dvorakjp keymap
    dvorakjp_keymap_d = OrderedDict()
    for consonant in consonants_list:

        # consonant + vowel
        for vowel in vowels_list:
            char = consonant + vowel
            dvorakjp_keymap_d[char] = keymap_d.get(char, '')

        # consonant + contracted_sound + vowel
        for contracted_sound in contracted_sounds_list:
            for vowel in vowels_list:
                char = consonant + contracted_sound + vowel
                dvorakjp_keymap_d[char] = keymap_d.get(char, '')

    print(dvorakjp_keymap_d)
    #  f = open('test.txt', 'w')
    for key, keymap in dvorakjp_keymap_d.items():
        #  f.write('\t'.join(key, keymap))
        #  print(keymap[0])
        print('\t'.join((key, keymap)))

    #  f.close()

if __name__ == "__main__":
    main()
