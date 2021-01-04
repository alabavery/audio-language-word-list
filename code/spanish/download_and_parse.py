import requests
import json
import metadata_generator

_SOURCE = 'http://corpus.rae.es/frec/10000_formas.TXT'


def _get_word_from_line(line):
     # the word is the second column
    return line.split('\t')[1].strip() 


def _get_words():
    res = requests.get(_SOURCE)
    raw = res.content.decode(res.encoding)
    lines = raw.split('\n')[1:] # the first row is the headers
    return [_get_word_from_line(line) for line in lines]


def _get_metadata():
    return { "source": _SOURCE }


def main():
    return _get_words(), _get_metadata()