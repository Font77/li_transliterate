# -*- coding: utf_8 -*-
'''
Created on Apr 6, 2017
రియా
@author: vimalk3
'''
import re
import sys

class unicode_teqst(object):
    '''
    classdocs
    '''
    inglisstr = (
        'qQgG' + 'cCjJn' + 'tTdDn' +
        'xXwWn' + 'pfbBm' + 'yrRlLl' +
        'vSssh' + 'aAa' + 'iiii' + 'uuuu' +
        'eeee' + 'eeee' + 'ooo' + 'ooo' + 'NNNN' + 'jf'
    )	
    mlyalmstr = (
        u'കഖഗഘ' + u'ചഛജഝഞ' + u'ടഠഡഢണ' +
        u'തഥദധന' + u'പഫബഭമ' + u'യരറലളഴ' +
        u'വശഷസഹ' + u'ാഅആ' + u'ിീഇഈ' + u'ുൂഉഊ' +
        u'െേൈഎ' + u'ഏഐee' + u'ൊോൌഒഓഔ' + u'ങങNN'
    )
    bNgalistr = (
        u'কখগঘ' + u'চছজঝঞ' + u'টঠডঢণ' +
        u'তথদধন' + u'পফবভম' + u'যরRলLl' +
        u'vশষসহ' + u'াঅআ' + u'িীইঈ' + u'ুূউঊ' +
        u'েৈএঐ' + u'eeee' + u'োৌওঔৗo' + u'ঙNNN'
    )
    uRiyastr = (
        u'କଖଗଘ' + u'ଚଛଜଝଞ' + u'ଟଠଡଢଣ' +
        u'ତଥଦଧନ' + u'ପଫବଭମ' + u'ଯରRଲଳl' +
        u'ଵଶଷସହ' + u'ାଅଆ' + u'ିୀଇଈ' + u'ୁୂଉଊ' +
        u'ୖେଏଐ ' + u'ୈeee' + u'ୗୌୋଓଔo' + u'ଙNNN'
    )
    pnjabistr = (
        u'ਕਖਗਘ' + u'ਚਛਜਝਞ' + u'ਟਠਡਢਣ' +
        u'ਤਥਦਧਨ' + u'ਪਫਬਭਮ' + u'ਯਰRਲਲ਼l' +
        u'ਵਸ਼sਸਹ' + u'ਾਅਆ' + u'ਿੀੲi' + u'ੁੂੳu' +
        u'ੇੈਏਐ' + u'eeee' + u'ੋੌਓਔoo' + u'ਙNNN'
    )
    gujraxistr = (
        u'કખગઘ' + u'ચછજઝઞ' + u'ટઠડઢણ' +
        u'તથદધન' + u'પફબભમ' + u'યરRલળl' +
        u'વશષસહ' + u'ાઅઆ' + u'િીઇઈ' + u'ુૂઉઊ' +
        u'ેૈએઐ' + u'ૅઍee' + u'ોૌૉઓઔઑ' + u'ઙNNN'
    )
    xmilstr = (
        u'கQgG' + u'ஙன' + u'சCஜJஞ' + u'டTdDண' +
        u'தXwWந' + u'பfbBம' + u'யரறலளழ' +
        u'வஶஷஸஹ' + u'ாஅஆ' + u'ிீஇஈ' + u'ுூஉஊ' +
        u'ெேைஎஏஐee' + u'ொோௌஓஔ' + u'ௗ' + u'்ஙனN'
    )
    hinwistr = (
        u'कखगघ' + u'चछजझञ' + u'टठडढण'
        u'तथदधन'  + u'पफबभम' + u'यरड़लळऴ' +
        u'वशषसह' +u'ाअआ' + u'िीइई' + u'ुूउऊ' +
        u'ेैएऐ'+ u'ॆएऍऎ' + u'ोौओऔ' + u'ॊऒ' + u'ंंNN' + u'ज़फ़'
    )
    xelugustr = (
        u'కఖగఘ' + u'చఛజఝఞ' + u'టఠడఢణ' +
        u'తథదధన' + u'పఫబభమ' + u'యరఱలళఌ' + u'వశసషహ' +
        u'ాఅఆ' + u'ిీఇఈ' +u'ుూఉఊ' +
        u'ెేైఎ' + u'ౖెఏఐ' + u'ొోౌఒఓఔ' + u'ంఙNN'
    )
    qnARastr = (
        u'ಕಖಗಘ' + u'ಚಛಜಝಞ' + u'ಟಠಡಢಣ' +
		u'ತಥದಧನ' + u'ಪಫಬಭಮ' + u'ಯರಱಳಌೡ' +
		u'ವಶಷಸಹ' + u'ಆಅಾ' + u'ಿೀಇಈ' + u'ುೂಉಊ' +
		u'ೆೇೈಎ' + u'ಏಏಐೖ' + u'ೊೋೌಒಓಔ' + u'ಙಙNN'
    )

    def __init__(self, uteqst):
        '''
        Constructor
        '''
        self.uteqst = uteqst

    def tr(self, string1, string2, source, option=''):
        """Replace or remove specific characters.
    
        If not given option, then replace all characters in string1 with
        the character in the same position in string2.
    
        Following options are available:
            c   Replace all complemented characters in string1 with
                the character in the same position in string2.
            d   Delete all characters in string1.
            s   Squeeze all characters in string1.
            cs  Squeeze all the characters in string2 besides "c" replacement.
            ds  Delete all characters in string1. Squeeze all characters
                in string2.
            cd  Delete all complemented characters in string1.
    
        Params:
            <unicode> string1
            <unicode> string2
            <unicode> source
            <basestring> option
        Return:
            <unicode> translated_source
        """
    
        def is_valid_type(source):
            return isinstance(source, unicode)
    
        def make_char_list(source):
            char_list = []
            back_slash = False
            hyphen = False
            for char in source:
                if char == '\\':
                    if not back_slash:
                        back_slash = True
                        continue
                elif char == '-' and not back_slash:
                    hyphen = True
                    continue
                elif hyphen:
                    start = char_list[-1] + 1
                    char_list += range(start, ord(char))
                char_list.append(ord(char))
                back_slash = False
                hyphen = False
            return char_list
    
        def to_unichr(char_list):
            return map(unichr, char_list)
    
        def squeeze(from_list, source):
            for char in from_list:
                squeeze_pattern = re.compile('%s{2,}' % char)
                source = squeeze_pattern.sub(char, source)
            return source
    
        def translate(from_list, to_list, source):
            translate_dict = dict(zip(from_list, to_list))
            return source.translate(translate_dict)
    
        if not is_valid_type(source):
            raise TypeError('source string must be unicode')
    
        if option == 's':
            from_list = make_char_list(string1)
            from_list = to_unichr(from_list)
            return squeeze(from_list, source)
        elif 'c' in option:
            from_list = make_char_list(string1)
            from_list = to_unichr(from_list)
            from_list = [ord(c) for c in set(source) - set(from_list)]
            if 'd' in option:
                to_list = [None for i in from_list]
            else:
                to_list = [string2[-1] for i in from_list]
            source = translate(from_list, to_list, source)
            if 's' in option:
                source = squeeze(to_list, source)
            return source
        elif 'd' in option:
            from_list = make_char_list(string1)
            to_list = [None for i in from_list]
            source = translate(from_list, to_list, source)
            if 's' in option:
                to_list = make_char_list(string2)
                to_list = to_unichr(to_list)
                source = squeeze(to_list, source)
            return source
        else:
            from_list = make_char_list(string1)
            to_list = make_char_list(string2)
            to_list = to_unichr(to_list)
            return translate(from_list, to_list, source)

    def hinwitr(self):            
        hinwiteqst = self.tr(self.hinwistr, self.inglisstr, self.uteqst)
        hinwiteqst = hinwiteqst.replace(u'्','')
        hinwiteqst = hinwiteqst.replace(u'़','')
        return hinwiteqst
    def gujraxitr(self):            
        gujraxiteqst = self.tr(self.gujraxistr, self.inglisstr, self.uteqst)
        gujraxiteqst = gujraxiteqst.replace(u'्','')
        gujraxiteqst = gujraxiteqst.replace(u'़','')
        return gujraxiteqst
    def pnjabitr(self):            
        pnjabiteqst = self.tr(self.pnjabistr, self.inglisstr, self.uteqst)
        pnjabiteqst = pnjabiteqst.replace(u'्','')
        pnjabiteqst = pnjabiteqst.replace(u'़','')
        return pnjabiteqst
    def bNgalitr(self):            
        bNgaliteqst = self.tr(self.bNgalistr, self.inglisstr, self.uteqst)
        bNgaliteqst = bNgaliteqst.replace(u'्','')
        bNgaliteqst = bNgaliteqst.replace(u'़','')
        return bNgaliteqst
    def uRiyatr(self):            
        uRiyateqst = self.tr(self.uRiyastr, self.inglisstr, self.uteqst)
        uRiyateqst = uRiyateqst.replace(u'्','')
        uRiyateqst = uRiyateqst.replace(u'़','')
        return uRiyateqst
    def xmiltr(self):        
        xmilteqst = self.tr(self.xmilstr, self.inglisstr, self.uteqst)
        xmilteqst = xmilteqst.replace(u'','') #
        return xmilteqst
    def xelugutr(self):        
        xeluguteqst = self.tr(self.xelugustr, self.inglisstr, self.uteqst)
        xeluguteqst = xeluguteqst.replace(u'్','')
        return xeluguteqst
    def mlyalmtr(self):        
        mlyalmteqst = self.tr(self.mlyalmstr, self.inglisstr, self.uteqst)
        mlyalmteqst = mlyalmteqst.replace(u'്','')
        return mlyalmteqst
    def qnARatr(self):        
        qnARateqst = self.tr(self.qnARastr, self.inglisstr, self.uteqst)
        qnARateqst = qnARateqst.replace(u'್','')
        qnARateqst = qnARateqst.replace(u'ೃ','')
        qnARateqst = qnARateqst.replace(u'ಂ','')
        return qnARateqst

    def ditAqttr(self):
        trfnq = None        
        qaunt = 0
        if self.uteqst[0] in self.hinwistr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.hinwistr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.hinwistr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.hinwistr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.hinwitr

        qaunt = 0
        if self.uteqst[0] in self.gujraxistr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.gujraxistr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.gujraxistr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.gujraxistr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.gujraxitr

        qaunt = 0
        if self.uteqst[0] in self.pnjabistr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.pnjabistr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.pnjabistr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.pnjabistr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.pnjabitr

        qaunt = 0
        if self.uteqst[0] in self.bNgalistr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.bNgalistr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.bNgalistr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.bNgalistr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.bNgalitr

        qaunt = 0
        if self.uteqst[0] in self.uRiyastr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.uRiyastr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.uRiyastr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.uRiyastr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.uRiyatr

        qaunt = 0
        if self.uteqst[0] in self.xmilstr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.xmilstr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.xmilstr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.xmilstr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.xmiltr

        qaunt = 0
        if self.uteqst[0] in self.xelugustr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.xelugustr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.xelugustr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.xelugustr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.xelugutr

        qaunt = 0
        if self.uteqst[0] in self.mlyalmstr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.mlyalmstr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.mlyalmstr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.mlyalmstr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.mlyalmtr

        qaunt = 0
        if self.uteqst[0] in self.qnARastr:
            qaunt = qaunt + 1
        if self.uteqst[1] in self.qnARastr:
            qaunt = qaunt + 1
        if self.uteqst[2] in self.qnARastr:
            qaunt = qaunt + 1
        if self.uteqst[3] in self.qnARastr:
            qaunt = qaunt + 1
        if qaunt >= 2:
            trfnq = self.qnARatr

        return trfnq()
