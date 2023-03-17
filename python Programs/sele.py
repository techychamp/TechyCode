from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os,time

class drive():
    def __init__(self,url):
        self.url=url
        self.out=[]
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1024x1400")
        chrome_driver = os.path.join(os.getcwd(), "chromedriver")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        self.caller()
    def connect(self,recu=1):
        if(self.url_change()!=1):
            if(recu%30==0):
                return 0
            self.driver.get(self.url)
            return self.connect(recu+1)
        else:
            self.url=self.driver.current_url
            return 1
    def url_change(self,cnt=20,recu=0):
        if(self.url!=self.driver.current_url):
            if(recu%cnt==0):
                return 0
            time.sleep(0.2)
            return self.url_change(cnt,recu+1)
        else:
            print(self.driver.current_url)
            return 1
    def caller(self):
        self.connect()
        self.driver.get_screenshot_as_file("python-cpclips.png")
        self.driver.execute_script("document.querySelector('#urlForm > div > label').setAttribute('class','active')")
        inpt=self.driver.find_element_by_xpath('//*[@id="url"]')
        inpt.clear()
        inpt.send_keys(url)
        while(self.url_change(30)==0):
            self.driver.find_element_by_xpath('//*[@id="download-button"]').click()
        video_src=self.driver.find_element_by_xpath("//*[@id='video']/ul")
        video_lst=video_src.find_elements_by_class_name("collection-item")
        self.clarity={}
        for i in range(1,len(video_lst)+1):
            key,value=video_lst[i-1].find_element_by_xpath(f'//*[@id="video"]/ul/li[{i}]/div/div[1]').text,(video_lst[i-1].find_element_by_xpath(f'//*[@id="video"]/ul/li[{i}]/div/div[4]/a').get_attribute('href'))[:-10]
            self.clarity.update({key : value})
            if(i!=0):
                if(video_lst[i].find_element_by_xpath(f'//*[@id="video"]/ul/li[{i-1}]/div/div[2]').text.strip()=="mp4"):
                    break
    def execute(self,cmd):
        if(cmd[0]=="url"):
            self.url=cmd[1]
            self.connect()
            return True
        elif(cmd[0]=="Element"):
            return self.selector(cmd[1])
        elif(cmd[0]=="Elements"):
            return self.selector(cmd[1],1)
        elif(cmd[0]=="write"):
            (self.execute((cmd[1].split(",")[0]).split(":",1))).send_keys(cmd[1].split(",")[1])
            return True
        elif(cmd[0]=="clear"):
            (self.execute((cmd[1].split(",")[0]).split(":",1))).clear()
            return True
        elif(cmd[0]=="click"):
            (self.execute((cmd[1].split(",")[0]).split(":",1))).click()
            return True
        elif(cmd[0]=="url_changed"):
            while(self.url_change(20)==0):
                self.execute(cmd[1].split(":",1))
            return True
        elif(cmd[0]=="script"):
            return self.driver.execute_script(eval(cmd))
        elif(cmd[0]=="scrnsht"):
            return self.driver.get_screenshot_as_file("screenshot.png")
        elif(cmd[0]=="out"):
            self.out.append(self.execute(cmd[1].split(":",1)))
    def selector(self,arg,m=0):
        if(m==0):
            m=self.driver.find_element
        else:
            m=self.driver.find_elements
        if(len(arg)!=0):
            elem=""
            if(arg[0]=="#"):
                return m(by="id",value=arg)
            if(arg[0]=="."):
                return m(by="class",value=arg)
            if(arg[:3]=="//*"):
                return m(by="xpath",value=arg)
    def seperator(self,arg):
        dta=arg.split("\n")
        dta=list(map(lambda x:(x.split(":",1))if(x.find(":"))else(tuple(x)),dta))
        for i in dta:
            self.execute(dta)
    def __del__(self):
        self.driver.close()
s=drive("https://www.cpclips.com")
