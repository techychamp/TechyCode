from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os,time

def main():
    global driver,clarity
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1024x1400")
    url="www.hotstar.com/tv/radhakrishn/s-1695/shukracharyas-shocking-plan/1000241527"
    # download Chrome Webdriver  
    # https://sites.google.com/a/chromium.org/chromedriver/download
    # put driver executable file in the script directory
    chrome_driver = os.path.join(os.getcwd(), "chromedriver")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)#PhantomJS()
    driver.get("https://www.cpclips.com")
    driver.get_screenshot_as_file("python-cpclips.png")
    driver.execute_script("document.querySelector('#urlForm > div > label').setAttribute('class','active')")
    inpt=driver.find_element_by_xpath('//*[@id="url"]')
    inpt.clear()
    inpt.send_keys(url)
    time.sleep(0.5)
    download=driver.find_element_by_xpath('//*[@id="download-button"]')
    download.click()
    # screenshot capture
    driver.get_screenshot_as_file("python-cpclips.png")
    time.sleep(2)
    video_src=driver.find_element_by_xpath("//*[@id='video']/ul")
    video_lst=video_src.find_elements_by_class_name("collection-item")
    clarity={}
    for i in range(1,len(video_lst)+1):
        key,value=video_lst[i-1].find_element_by_xpath(f'//*[@id="video"]/ul/li[{i}]/div/div[1]').text,(video_lst[i-1].find_element_by_xpath(f'//*[@id="video"]/ul/li[{i}]/div/div[4]/a').get_attribute('href'))[:-10]
        clarity.update({key : value})
        if(i!=0):
            if(video_lst[i].find_element_by_xpath(f'//*[@id="video"]/ul/li[{i-1}]/div/div[2]').text.strip()=="mp4"):
                break
    driver.close()
    return
main()
