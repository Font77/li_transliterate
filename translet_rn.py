# -*- coding: utf_8 -*-
'''
Created on Apr 6, 2017
rాm్

@author: vimalk3
'''
import unicode_teqst
if __name__ == '__main__':
    ustr_xelugu = u'దీన్ని ప్రయత్నించడానికి, దిగువ మీ భాషను మరియు ఇన్‌పుట్ సాధనాన్ని ఎంచుకుని, టైప్ చేయడాన్ని మొదలుపెట్టండి. '
    uobj_xelugu = unicode_teqst.unicode_teqst(ustr_xelugu)
    print 'ustr_xelugu  ', uobj_xelugu.ditAqttr()

    ustr_mlyalm = u'ഞയാറാഴ്ചയായിരുന്നു നന്തന്‍കോട് ക്ലിഫ് ഹൗസിന് സമീപമുള്ള നാല് പേരെ വീട്ടിനുള്ളില്‍ മരിച്ച നിലയില്‍ കണ്ടെത്തിയത് '
    uobj_mlyalm = unicode_teqst.unicode_teqst(ustr_mlyalm)
    print 'ustr_mlyalm  ', uobj_mlyalm.ditAqttr()

    ustr_xmil = u'ஆர்கே நகரில் வெள்ளமென பாய்ந்த பணம்.. தினகரன் 6 ஆண்டு தேர்தலில் போட்டியிட தடை?'
    uobj_xmil = unicode_teqst.unicode_teqst(ustr_xmil)
    print 'ustr_xmil  ', uobj_xmil.ditAqttr()
	
    ustr_hinwi = u'अनुप्रिया वर्मा, मुंबई। जैसे धरती के गर्भ में क्या क्या छिपा है किसी को नहीं पता। लगता है ठीक वैसा ही हाल बाहुबली का है। रिलीज़ को तीन हफ़्ते से कम समय बचा है लेकिन अब भी कुछ न कुछ हैरान करने वाली ख़बरें आ रही हैं। अब मामला उस महा सीन का है, जिसके बारे में सुनकर आ चौक जाएंगे।'
    uobj_hinwi = unicode_teqst.unicode_teqst(ustr_hinwi)
    print 'ustr_hinwi  ', uobj_hinwi.ditAqttr()

    ustr_qnnARa = u'ಕಡೂರು ತಾಲೂಕಿನ ಪರಿಸ್ಥಿತಿ ಮತ್ತು ಬರಗಾಲವನ್ನು ಕಂಡು ಕ್ಷೇತ್ರದ ಅಭಿವೃದ್ಧಿ ಮಾಡಬೇಕೆಂದು ಪಣತೊಟ್ಟಿದ್ದಾರೆ ಡಾ. ನಿರಂತರ ಗಣೇಶ. ಅಲ್ಲದೇ ಕಡೂರು ತಾಲೂಕು ತೀರಾ ಹಿಂದುಳಿದ ತಾಲೂಕಾಗಿದ್ದು, ಯಾವುದೇ ಅಭಿವೃದ್ಧಿ ಕೆಲಸಗಳು ಆಗಿಲ್ಲ. ಈಗಾಗಲೇ ಇವರ ತಾತ ಎಸ್.ಎಂ. ಕೃಷ್ಣ ಕಾಂಗ್ರೆಸ್‍ಗೆ ಗುಡ್ ಬೈ ಹೇಳಿರೋದು ಇವರ ಮೇಲೆ ಯಾವ ಪರಿಣಾಣ ಬಿರೋದಿಲ್ಲ ಎಂದೂ ಹೇಳುತ್ತಿದ್ದಾರೆ.'
    uobj_qnnARa = unicode_teqst.unicode_teqst(ustr_qnnARa)
    print 'ustr_qnnARa  ', uobj_qnnARa.ditAqttr()