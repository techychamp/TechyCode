import pyaudio,pydub,threading
class Audio():
        def __init__(self,url):
                self.__audio__= pydub.AudioSegment.from_file(url)
                self.length= len(self.__audio__)
                self.volume= 100.0
                self.counter=0
                self.fps=8
                self.audio=self.__audio__
                stream=pyaudio.PyAudio()
                self.__stream__=stream.open(format=pyaudio.get_format_from_width(self.__audio__.sample_width),
                                   channels=self.__audio__.channels,
                                   rate=self.__audio__.frame_rate,
                                   output=True)
        def play(self):
                self.__stream__.write((self.__audio__[self.counter]-(60-(60*(self.volume/100.0))))._data)
                self.counter+=1
        def play_n(self):
                self.__stream__.write((self.__audio__[self.fps*self.counter:self.fps*(self.counter+1)]-(60-(60*(self.volume/100.0))))._data)
                self.counter+=self.fps
                

