import pyaudio,pydub,cv2,numpy as np
import time
import concurrent.futures
loc="E:/MOVIE COLLECTION/Mersal/Neethanae Lyric - Mersal 1080p HD.mp4"
audio=pydub.AudioSegment.from_file(loc)
cap = cv2.VideoCapture(loc)
if (cap.isOpened()== False): 
    print("Error opening video file")
output=pyaudio.PyAudio()
output=output.open(format=pyaudio.get_format_from_width(audio.sample_width),
		 channels=audio.channels,
		 rate=audio.frame_rate,
		 output=True)
length = audio.duration_seconds
playchunk = audio[0.0:length*1000.0]
control=[False,100.0]
#data=pydub.utils.make_chunks(playchunk, 50)
data=playchunk
def play(data):
        for i in range(len(data)):
            output.write((data[i]-(60-(60*(control[1]/100.0))))._data)
            if control[0]==True:
                break
        return 1
def disp(cap):
        global stop
        while(cap.isOpened()): 
            ret, frame = cap.read() 
            if ret == True:
                cv2.imshow('Frame', frame)
                t=cv2.waitKey(int(cap.get(5)-1))
                if t & 0xFF == ord('q'):
                    control[0]=True
                    break
                elif (t & 0xFF == ord("w") and control[1]<150.0):
                    control[1]+=1
                elif (t & 0xFF == ord("s") and control[1]>-1.0):
                    control[1]-=1
            else:
                break
        return 1
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as s:
        s.submit(disp,cap)
        s.submit(play,data)
#cap.release()
cv2.destroyAllWindows()
