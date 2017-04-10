# -*- coding: utf_8 -*-
'''
Created on Apr 6, 2017
rాm్

@author: vimalk3
'''
import unicode_teqst
if __name__ == '__main__':
    ustr = u"ಈ ಹಿಂದೆ ನದಿಯಲ್ಲಿ ನೀರು ತುಂಬಿ ಹರಿಯುತ್ತಿತ್ತು. ಇಲ್ಲಿನ ಜನರು ಈ ನದಿ ನೀರನ್ನೇ ಕುಡಿಯಲು ಬಳಸುತ್ತಿದ್ದರು. ಆದರೆ ಈಗ ಪಯಸ್ವಿನಿ ನದಿಯನ್ನ ನೋಡಿ ನೀವೇ ಕಣ್ಣೀರು ಹಾಕುತ್ತೀರಾ. ಬಿಸಿಲಿನ ತಾಪಕ್ಕೆ ನೀರು ಕಡಿಮೆಯಾಗಿದೆ. ಇದ್ದ ಅಲ್ಪ ಸ್ವಲ್ಪ ನೀರು ಕಲ್ಮಶಗೊಂಡಿದೆ.[ನಾಳೆ ತಂದೆಯ ಅಸ್ಥಿ ವಿಸರ್ಜನೆಗೆ ಐಶ್ವರ್ಯಾ ರೈ ದಂಪತಿ ಮಂಗಳೂರಿಗೆ]"
# adbarw maxadi xpraqi biww mೇle qೈ jೋdisiwLe raQi!
    uobj = unicode_teqst.unicode_teqst(ustr)
    unilist = [0xdc20,0xdc21,0xdc30]
    unistrar = ''.join((unichr(x)) for x in unilist)
    print unistrar
    print unichr(unilist[0])
#     print uobj.hinditr()
    print uobj.qnnRatr()
