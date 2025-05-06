#!/usr/bin/python

import random
import textwrap
from optparse import OptionParser


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--no-dove', help='do not display a dove', action='store_true', dest='nodove')
    parser.add_option('-l', '--smaller-dove', help='display a smaller dove', action='store_true', dest='smaller_dove')
    parser.add_option('-u', '--unicode-dove', help='display only a unicode \'🕊 \'', action='store_true', dest='unicode_dove')
    parser.add_option('-s', '--no-speech-bubble', help='do not display a speech bubble', action='store_true', dest='nospeechbubbles')
    parser.add_option('-f', '--file', dest='file', help='load verses from a specific FILE', metavar='FILE')
    (options, args) = parser.parse_args()

    # Read verse file
    if not options.file:
        try:
            verses_file = open('verses.txt')
        except FileNotFoundError:
            verses_file = open('/usr/share/biblesay/verses.txt')
    else:
        verses_file = open(options.file)

    verses = verses_file.readlines()
    verses_file.close()

    # Choose a verse
    verse = random.choice(verses)
    # Wrap the text
    verse = textwrap.wrap(verse, width=50)

    # This int is for generating the speech bubble around the text later
    longest_line = 0

    # Get the longest line
    for i in range(len(verse)):
        longest_line = len(verse[i]) if len(verse[i]) > longest_line else longest_line

    if not options.nospeechbubbles:
        # Print the top speech bubble line
        print(' ' + (longest_line + 2) * '_' + ' ');
        print('/' + (longest_line + 2) * ' ' + '\\');

    # Print the lines with vertical lines on the side for speech bubbles
    for i in range(len(verse)):
        # Add empty spaces to 'verse' until 'longest_line'
        if not options.nospeechbubbles:
            for j in range(len(verse[i]), longest_line + 1):
                verse[i] += ' '
            verse[i] = '| ' + verse[i] + '|'
        print(verse[i])

    # Print the bottom speech bubble line
    if not options.nospeechbubbles:
        print('\\' + (longest_line + 2) * '_' + '/');

    if not options.nodove:
        if options.smaller_dove:
            print(smaller_ascii_dove)
        elif options.unicode_dove:
            print('\t\\')
            print('\t 🕊')
