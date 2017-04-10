'''
Created on Apr 10, 2017

@author: DELL
'''

class qNNARa(object):
    ''' 
    classdocs               
    '''
    qNNARa_char_tuple = (
        u'ಾ',u'ಅ',u'ಆ', # aAa
        u'ಿ', u'ೀ', u'ಇ', u'ಈ',# iiii
        u'ು', u'ೂ', u'ಉ', u'ಊ',# uuuu
        u'ೆ', u'ೇ', u'ೈ', u'ಎ', u'ಏ', u'ಐ', u'ೖ',# eeeeeee 7 times
        u'ೊ', u'ೋ', u'ೌ', u'ಒ', u'ಓ', u'ಔ',# oooooo 6 times
        u'ಕ',# q
        u'ಕ',# q
    )

    def __init__(self, params):
        '''
        Constructor
        '''
        