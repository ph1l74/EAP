''' 
Emulation of a Video Pojector

by Rupert Powell 10-8-15
'''
class proj:
    '''
    This module controls the video projector
    
    Methods:
    function('PWR_ON') Turns proj ON and returns status
    function('PWR_OFF') Turns proj OFF and returns status
    function('INP_1-4') Changes proj input 1-4 and returns status
    function('PMT_ON') Turns proj video mute ON and returns status
    function('PMT_OFF') Turns proj video mute OFF and returns status
       
    '''
    def __init__ (self):
        '''
        
        '''
        pass

    def control(self, function) :
        if function[:3] == 'PWR' :
            if 'on' in function.lower() :
                return('Power ON')
            elif 'off' in function.lower() :
                return('Power OFF')
            else:
                return 'ERR1'
        elif function[:3] == 'INP':
            inp = function[3:]
            return 'Input ' + inp
        elif function[:3] == 'PMT':
            if 'on' in function.lower() :
                return 'Picture mute on'
            elif 'off' in function.lower() :
                return 'Picture mute off'
            else :
                return 'ERR2'
        else :
            return('ERR0')
        
        