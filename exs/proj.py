''' 
Emulation of a Video Pojector

by Rupert Powell 10-8-15
'''
#from ex7 import BtnPON, BtnPOFF, BtnIn1, BtnIn2, BtnIn3, BtnIn4, BtnMuteON, BtnMuteOFF
class devProj:
    '''
    This module controls the video projector
    
    Methods:
    function('PWR_ON') Turns proj ON and returns status
    function('PWR_OFF') Turns proj OFF and returns status
    function('INP_1-4') Changes proj input 1-4 and returns status
    function('PMT_ON') Turns proj video mute ON and returns status
    function('PMT_OFF') Turns proj video mute OFF and returns status
       
    '''
    def __init__ (self, name):
        self.name = name

    def control(function) :
        if function[:3] == 'PWR' :
            if 'on' in function.lower() :
                return 'Power ON'
            elif 'off' in function.lower() :
                return'Power OFF'
            else:
                return'ERR1'
        elif function[:3] == 'INP':
            inp = function[4:]
            return'Input ' + inp
        elif function[:3] == 'PMT':
            if 'on' in function.lower() :
                return'Picture mute on'
            elif 'off' in function.lower() :
                return'Picture mute off'
            else :
                return'ERR2'
        else :
            return'ERR0'

    def feedback (function):
        #global BtnPON, BtnPOFF, BtnIn1, BtnIn2, BtnIn3, BtnIn4, BtnMuteON, BtnMuteOFF
        if function[:5] == 'Power':
            if 'on' in function.lower():
                BtnPON.configure(highlightcolor="red")
                BtnPOFF.configure(highlightcolor="white")
            elif 'off' in function.lower():
                BtnPON.configure(highlightcolor="white")
                BtnPOFF.configure(highlightcolor="red")
#            else:
#                return'ERR1'
#        elif function[:3] == 'INP':
#            inp = function[3:]
#            return'Input ' + inp
#        elif function[:3] == 'PMT':
#            if 'on' in function.lower() :
#                return'Picture mute on'
#            elif 'off' in function.lower() :
#                return'Picture mute off'
#            else :
#                return'ERR2'
#        else :
#            return'ERR0'