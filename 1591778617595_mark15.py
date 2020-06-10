import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import urllib.request
import ctypes
from bs4 import BeautifulSoup
from word2number import w2n
from ctypes import windll
import string
import stat
from googlesearch import search
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from dateutil.parser import parse
import pickle
import autoit

speech = sr.Recognizer()
try:
    engine=pyttsx3.init()
except ImportError:
    print("Requested driver is not found")
except RuntimeError:
    print("Driver fails to load")
voices = engine.getProperty("voices")

greeting_dict={'hello':'hello','buddy':'buddy','high':'high'}
open_dict={'Open':'Open','Run':'Run','goto':'goto','open':'open','move':'move'}
bye_dict={'by':'by','goodbye':'goodbye','night':'night'}
social_dict={'Facebook':'https://www.facebook.com/','Twitter':'https://twitter.com/login?lang=en','WhatsApp':'WhatsApp'}
google_dict={'search':'search','option':'option','back':'back','home':'home','choose':'choose','forward':'forward'}
youtube_dict={'find':'find','play':'play','previous':'previous','pause':'pause','resume':'resume'}
month_dict={'January':'1','February':'2','March':'3','April':'4','May':'5','June':'6','July':'7','August':'8','September':'9','October':'10','Novermber':'11','December':'12'}
file_dict={}
event_dict={}

engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_10.0")
rate = engine.getProperty("rate")
engine.setProperty("rate",rate)
engine.runAndWait()

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    print('Listening...')
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass

    except sr.RequestError as e:
            print("Network Error")
    return voice_text

def is_hidden(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def getdrives():
    drives=[]
    val=windll.kernel32.GetLogicalDrives()
    for char in string.ascii_uppercase:
        if val & 1:
            drives.append(char)
        val>>=1
    return drives

def getdup_key(key, keys):
    co=0
    for k in keys:
        if key in k:
            co+=1
    return co


def find(fol):
    drives=getdrives()
    for drive in drives:
        for root,dirs,files in os.walk(drive+":\\{}\\".format(fol)):
            for f in files:
                if is_hidden(os.path.join(root,f))==False:
                    key=os.path.join(root,f).rsplit('\\')[-1]
                    file_dict.update({key+'_{}'.format(getdup_key(key,file_dict.keys())):os.path.join(root,f)})
            for dir in dirs:
                if is_hidden(os.path.join(root,dir))==False:
                    key=os.path.join(root,dir).rsplit('\\')[-1]
                    file_dict.update({key+'_{}'.format(getdup_key(key,file_dict.keys())): os.path.join(root, dir)})
    return file_dict


def google_search(google_dict,voice_note):
    for key,value in google_dict.items():
        if google_dict.get(key)==voice_note.split(' ')[0]:
            return True

def youtube_search(youtube_dict, voice_note):
    for key, value in youtube_dict.items():
        if youtube_dict.get(key) == voice_note.split(' ')[0]:
            return True


def greeting(greeting_dict,voice_note):
    for key,value in greeting_dict.items():
        if value==voice_note.split(' ')[0]:
            return True
    return False

def launch(open_dict,voice_note):
    for key,value in open_dict.items():
        if value==voice_note.split(' ')[0]:
            return True
        elif key==voice_note.split(' ')[0]:
            return True
    return False
def soc(social_dict,voice_note):
    for key,value in social_dict.items():
        if key==voice_note.split(' ')[0]:
            return True
    return False
def rem(month_dict,voice_note):
    for key,value in month_dict.items():
        if key==voice_note.split(' ')[1]:
            return value

def Thank(bye_dict,voice_note):
    for key,value in bye_dict.items():
        if value==voice_note.split(' ')[0]:
            return True
    return False


if __name__ == '__main__':
    speak_text_cmd('Welcome back sir,Mark is online and ready')
    s=[]
    a=[]
    t=''
    key1=''
    c=''
    w=''
    q=''
    b=[]
    h=[]
    y=''
    driver=''
    url=''
    while True:
        voice_note = read_voice_cmd()
        print('cmd: {}'.format(voice_note))
        if greeting(greeting_dict,voice_note):
            speak_text_cmd("Hi...Sir what's the task ......")

            continue
        elif launch(open_dict,voice_note):
            if 'desktop'in voice_note:
                speak_text_cmd("Opening Desktop")
                key = voice_note.split(' ')[1]
                key1 = "C:\\Users\\adie\\Desktop".format(key)
                print(key1)
                os.system("explorer {}\\".format(key1))
            elif 'Drive'in voice_note:
                speak_text_cmd("Opening Drive...")
                key = voice_note.split(' ')[1]
                key1= "{}:".format(key)
                os.system("explorer {}\\".format(key1))
            elif 'folder'in voice_note:
                speak_text_cmd("Opening Folder...")
                key2=str(voice_note.split(' ')[1]).capitalize()
                key1=key1+'\\' +key2
                os.system("explorer {}".format(key1))
                print(key1)
            elif 'exe'in voice_note:
                key3=str(voice_note.split(' ')[1]).capitalize()
                key1=key1+'\\'+key3
                os.system("explorer {}.exe".format(key1))
            elif 'mp3'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.mp3".format(key1))
            elif 'mp4'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.mp4".format(key1))
            elif 'pdf'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.pdf".format(key1))
            elif 'txt'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.txt".format(key1))
            elif 'png'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.png".format(key1))
            elif 'jpg'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.jpg".format(key1))
            elif 'py'in voice_note:
                key3 = str(voice_note.split(' ')[1]).capitalize()
                key1 = key1 + '\\' + key3
                os.system("explorer {}.py".format(key1))
            elif 'back'in voice_note:
                key3=''
                key3=os.path.dirname(key1)
                print(key3)
                speak_text_cmd("Moving Back....")
                os.system("explorer {}".format(key3))
                key2=key3.split(os.path.sep)
                print(key2)
                if key3=='C:\\'or'D:\\'or'F:\\':
                    key1=key2[0]
                else:
                    key1=key3
                print(key1)
            continue
        elif soc(social_dict,voice_note):
            speak_text_cmd("Sure Sir...")
            key = voice_note.split(' ')[0]
            if key=='WhatsApp':
                web_driver = webdriver.Firefox(executable_path=r"C:\\Users\\adie\\PycharmProjects\\MARK\\New folder\\geckodriver"r".exe")
                web_driver.get("https://web.whatsapp.com/")
                wait=WebDriverWait(web_driver,600)
                speak_text_cmd("Sir What Would You Like to Do")
                voice_note=read_voice_cmd()
                print(voice_note)
                if 'message'in voice_note:
                    speak_text_cmd("Sir..Contact Name....")
                    voice_note = read_voice_cmd()
                    contact = str(voice_note).capitalize()
                    print(contact)
                    speak_text_cmd("Sir..Your message...")
                    voice_note=read_voice_cmd()
                    string=voice_note
                    x_arg = '//span[contains(@title, ' + '"' + contact + '"' + ')]'
                    print(x_arg)
                    person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    print(person_title)
                    person_title.click()
                    inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
                    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
                    for i in range(1):
                        input_box.send_keys(string + Keys.ENTER)
                        time.sleep(1)
                    continue
                elif 'document'in voice_note:
                    speak_text_cmd("Sir..Contact Name....")
                    voice_note = read_voice_cmd()
                    contact = str(voice_note).capitalize()
                    print(contact)
                    x_arg = '//span[contains(@title, ' + '"' + contact + '"' + ')]'
                    print(x_arg)
                    person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    print(person_title)
                    person_title.click()
                    imp_x = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div"
                    button = wait.until(EC.presence_of_element_located((By.XPATH, imp_x)))
                    button.click()
                    wait = WebDriverWait(web_driver, 600)
                    speak_text_cmd("Sir Choose the document folder")
                    voice_note = read_voice_cmd()
                    fol=str(voice_note.split(' ')[0]).capitalize()
                    print(fol)
                    p = find(fol)
                    speak_text_cmd("Document name")
                    voice_note=read_voice_cmd()
                    x=str(voice_note)
                    print(p)
                    print(x)
                    for key,value in p.items():
                        if x in p.get(key):
                            w= value
                            break
                    print(w)
                    inp_x = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/span"
                    button1 = wait.until(EC.presence_of_element_located((By.XPATH, inp_x)))
                    button1.click()
                    time.sleep(5)
                    autoit.send('{}'.format(w))
                    autoit.send("{ENTER}")
                    inpy = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div"
                    button2 = wait.until(EC.presence_of_element_located((By.XPATH, inpy)))
                    button2.click()
                    continue
                elif 'photo'in voice_note:
                    speak_text_cmd("Sir..Contact Name....")
                    voice_note = read_voice_cmd()
                    contact = str(voice_note).capitalize()
                    print(contact)
                    x_arg = '//span[contains(@title, ' + '"' + contact + '"' + ')]'
                    print(x_arg)
                    person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    print(person_title)
                    person_title.click()
                    imp_x = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div"
                    button = wait.until(EC.presence_of_element_located((By.XPATH, imp_x)))
                    button.click()
                    speak_text_cmd("Sir Choose the image or video folder")
                    voice_note = read_voice_cmd()
                    fol = str(voice_note.split(' ')[0]).capitalize()
                    print(fol)
                    p = find(fol)
                    speak_text_cmd("Image or Video Folder")
                    voice_note = read_voice_cmd()
                    x = str(voice_note)
                    print(p)
                    print(x)
                    for key, value in p.items():
                        if x in p.get(key):
                            w = value
                            break
                    print(w)
                    inp_x = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/span"
                    button1 = wait.until(EC.presence_of_element_located((By.XPATH, inp_x)))
                    button1.click()
                    wait = WebDriverWait(web_driver, 600)
                    time.sleep(5)
                    autoit.send('{}'.format(w))
                    autoit.send("{ENTER}")
                    inpy = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div"
                    button2 = wait.until(EC.presence_of_element_located((By.XPATH, inpy)))
                    button2.click()
                    continue
                elif'contacts'in voice_note:
                    speak_text_cmd("Sir..Contact Name....")
                    voice_note = read_voice_cmd()
                    contact = str(voice_note).capitalize()
                    print(contact)
                    x_arg = '//span[contains(@title, ' + '"' + contact + '"' + ')]'
                    print(x_arg)
                    person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    print(person_title)
                    person_title.click()
                    speak_text_cmd("Name Of Conatct you want to send")
                    voice_note=read_voice_cmd()
                    t=str(voice_note).capitalize()
                    print(t)
                    imp_x = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div"
                    button = wait.until(EC.presence_of_element_located((By.XPATH, imp_x)))
                    button.click()
                    inpj="/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[4]/button/span"
                    button1= wait.until(EC.presence_of_element_located((By.XPATH, inpj)))
                    button1.click()
                    inpg="/html/body/div[1]/div/span[3]/div/span/div/div/div/div/div/div/div[1]/div/label/input"
                    button2=wait.until(EC.presence_of_element_located((By.XPATH, inpg)))
                    for i in range(1):
                        button2.send_keys(t + Keys.ENTER)
                        time.sleep(1)
                    inpu="/html/body/div[1]/div/span[3]/div/span/div/div/div/div/div/div/span/div/div/div"
                    button3 = wait.until(EC.presence_of_element_located((By.XPATH, inpu)))
                    button3.click()
                    continue
                elif 'view profile'in voice_note:
                    speak_text_cmd("Opening profile")
                    r="/html/body/div[1]/div/div/div[3]/div/header/div[1]/div"
                    button=wait.until(EC.presence_of_element_located((By.XPATH, r)))
                    button.click()
                    continue
                elif'group'in voice_note:
                    speak_text_cmd("Opening Group Window")
                    i="/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div[1]/div[2]/div/div"
                    button3 = wait.until(EC.presence_of_element_located((By.XPATH, i)))
                    button3.click()
                    l="/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input"
                    button2 = wait.until(EC.presence_of_element_located((By.XPATH, l)))
                    speak_text_cmd("Number Of Contacts Sir...")
                    voice_note=read_voice_cmd()
                    v=w2n.word_to_num(voice_note)
                    print(v)
                    speak_text_cmd("Contacts")
                    voice_note=read_voice_cmd()
                    d=str(voice_note).capitalize()
                    for s in range(v):
                        button2.send_keys(d + Keys.ENTER)
                        time.sleep(1)
                    k="/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/span/div"
                    button1=wait.until(EC.presence_of_element_located((By.XPATH, k)))
                    button1.click()
                    speak_text_cmd("Group Name Sir...")
                    voice_note=read_voice_cmd()
                    f = voice_note
                    h = "/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]"
                    button = wait.until(EC.presence_of_element_located((By.XPATH, h)))
                    for a in range(1):
                        button.send_keys(f + Keys.ENTER)
                        time.sleep(1)
                    g="/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div"
                    button4=wait.until(EC.presence_of_element_located((By.XPATH, g)))
                    button4.click()
                    continue
                elif 'view contact'in voice_note:
                    speak_text_cmd("Sir..Contact Name....")
                    voice_note = read_voice_cmd()
                    contact = str(voice_note).capitalize()
                    print(contact)
                    x_arg = '//span[contains(@title, ' + '"' + contact + '"' + ')]'
                    print(x_arg)
                    person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    print(person_title)
                    person_title.click()
                    e="/html/body/div[1]/div/div/div[4]/div/header/div[1]"
                    button= wait.until(EC.presence_of_element_located((By.XPATH, e)))
                    button.click()
                    continue
                elif 'search messages'in voice_note:
                    speak_text_cmd("Sir..Contact Name....")
                    voice_note = read_voice_cmd()
                    contact = str(voice_note).capitalize()
                    print(contact)
                    x_arg = '//span[contains(@title, ' + '"' + contact + '"' + ')]'
                    print(x_arg)
                    person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    print(person_title)
                    person_title.click()
                    k="/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[1]/div"
                    jh=wait.until(EC.presence_of_element_located((By.XPATH, k)))
                    jh.click()
                    l="/html/body/div[1]/div/div/div[2]/div[3]/span/div/div/div[1]/div/label/input"
                    j1=wait.until(EC.presence_of_element_located((By.XPATH, l)))
                    speak_text_cmd("Message Sir....")
                    z=read_voice_cmd()
                    for a in range(1):
                        button.send_keys(z + Keys.ENTER)
                        time.sleep(1)
                    continue
        elif google_search(google_dict,voice_note):
            if'search'in voice_note:
                speak_text_cmd("Launching Google Browser....")
                c=voice_note.split(' ')[1]
                webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note.split(' ')[1]))
                ip = voice_note.split(' ')[1]
                for url in search(ip, stop=20):
                    a.append(url)
                print(a)
            elif 'option' in voice_note:
                speak_text_cmd("Accessing Site.....")
                m = voice_note.split(' ')[1]
                g = w2n.word_to_num(m)
                y = a[g]
                b.append(y)
                webbrowser.open(a[g])
            elif 'choose' in voice_note:
                print(y)
                html= urllib.request.urlopen(y)
                soup = BeautifulSoup(html, features="lxml")
                tags = soup('a')
                y=y.split('/')[2]
                a=[]
                c = voice_note.split(' ')[1]
                for i,tag in enumerate(tags):
                    ans = tag.get('href', None)
                    if 'https' in ans:
                        continue
                    elif 'http' in ans:
                        continue
                    else:
                        a.append(ans)
                print(a)
                for j in a:
                    if c in str(j).lower():
                        r ='https://'+y+j
                        print(r)
                        break
                webbrowser.open(r)
                y=r
                b.append(r)
            elif 'back' in voice_note:
                l=len(b)
                webbrowser.open(b[l-1])
            elif 'forward'in voice_note:
                l=len(b)
                webbrowser.open(b[l])
            elif 'home'in voice_note:
                webbrowser.open("https://www.google.co.in/")
                continue
        elif youtube_search(youtube_dict, voice_note):
            if 'find' in voice_note:
                speak_text_cmd("Launching Youtube....")
                query=urllib.parse.quote(voice_note)
                url='https://www.youtube.com/results?search_query='+query
                webbrowser.open(url)
                res=urllib.request.urlopen(url)
                html=res.read()
                soup=BeautifulSoup(html,'html.parser')
                for v in soup.find_all(attrs={'class':'yt-uix-tile-link'}):
                   h='https://www.youtube.com'
                   j=v['href']
                   g=h+j
                   s.append(g)
            elif 'play' in voice_note:
                speak_text_cmd("Playing Video....")
                f=voice_note.split(' ')[2]
                c=w2n.word_to_num(f)
                driver = webdriver.Firefox(executable_path=r"C:\\Users\\adie\\PycharmProjects\\MARK\\New folder\\geckodriver.exe")
                driver.get(s[c])
            if 'pause' in voice_note:
                driver.execute_script('document.getElementsByTagName("video")[0].pause()')
            elif 'resume' in voice_note:
                driver.execute_script('document.getElementsByTagName("video")[0].play()')
            elif 'download'in voice_note:
                link=s[c]
                yt=YouTube(str(link))
                p=yt.streams.first()
                p.download()
                continue
            elif 'previous' in voice_note:
                webbrowser.open(url)
                continue
        elif 'lock'in voice_note:
            speak_text_cmd("Locking Your PC....")
            ctypes.windll.user32.LockWorkStation()
            continue
        elif 'set reminder'in voice_note:
            speak_text_cmd("Sir ...Please Specify the Event")
            voice_note=read_voice_cmd()
            q=voice_note
            print(q)
            speak_text_cmd("And the Event Date.....")
            voice_note=read_voice_cmd()
            print(voice_note)
            z=rem(month_dict,voice_note)
            z = w2n.word_to_num(z)
            print(z)
            k=voice_note.split(' ')[0]
            k = w2n.word_to_num(k)
            w = voice_note.split(' ')[2]
            w = w2n.word_to_num(w)
            if datetime(w,z,k)<datetime.now():
                speak_text_cmd("Date Has Elapsed Sir...")
                break
            else:
                t='{}-{}-{}'.format(w,z,k)
                print(t)
                event_dict.update({'{}'.format(q):t})
                pickle.dump(event_dict,open("save.p","wb"))
                print(event_dict)
                speak_text_cmd("Sir..Update the Timings")
                voice_note=read_voice_cmd()
                print(voice_note)
                u=voice_note.split(' ')[0]
                u=w2n.word_to_num(u)
                x=voice_note.split(' ')[2]
                x=w2n.word_to_num(x)
                r='{}:{}'.format(u,x)
                print(r)

                speak_text_cmd("Reminder has Been Set Sir....")
                continue
        elif Thank(bye_dict,voice_note):
            speak_text_cmd("Hoping to meet you soon sir...")
            exit()
        elif'Gmail'in voice_note:
            o="https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession"
            web_driver = webdriver.Firefox(executable_path=r"C:\\Users\\adie\\PycharmProjects\\MARK\\New folder\\geckodriver.exe")
            web_driver.get(o)
            imp='//*[@id="identifierId"]'
            wait=WebDriverWait(web_driver,600)
            user=wait.until(EC.presence_of_element_located((By.XPATH, imp)))
            string=""
            for i in range(1):
                user.send_keys(string + Keys.ENTER)
                time.sleep(10)
            imp1="/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input"
            passw=wait.until(EC.presence_of_element_located((By.XPATH, imp1)))
            string1=""
            for j in range(1):
                passw.send_keys(string1 + Keys.ENTER)
            speak_text_cmd("Sir What would you like to do..")
            voice_note=read_voice_cmd()
            if 'sign out'in voice_note:
                u='//*[@id="gb_71"]'
                sign = wait.until(EC.presence_of_element_located((By.XPATH, u)))
                sign.click()
            elif'compose'in voice_note:
                xp="/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div"
                button=wait.until(EC.presence_of_element_located((By.XPATH,xp)))
                button.click()
                f='//*[@id=":1f6"]'
                wait = WebDriverWait(web_driver, 600)
                si= wait.until(EC.presence_of_element_located((By.XPATH, f)))
                speak_text_cmd("Recipient Sir...")
                str1=read_voice_cmd()
                for i in range(1):
                    si.send_keys(str1 + Keys.ENTER)
                    time.sleep(10)
                speak_text_cmd("Subject...")
                v='//*[@id=":1d5"]'
                wait = WebDriverWait(web_driver, 600)
                si1 = wait.until(EC.presence_of_element_located((By.XPATH, v)))
                str2 = read_voice_cmd()
                for i in range(1):
                    si1.send_keys(str2 + Keys.ENTER)
                    time.sleep(10)
                speak_text_cmd("Your Message..")
                m='//*[@id=":1gy"]'
                wait = WebDriverWait(web_driver, 600)
                si2 = wait.until(EC.presence_of_element_located((By.XPATH, m)))
                str3 = read_voice_cmd()
                for i in range(1):
                    si2.send_keys(str3 + Keys.ENTER)
                    time.sleep(10)







                



        elif 'check reminder'in voice_note:
            event_dict = pickle.load(open("save.p", "rb"))
            print(event_dict)
            for key,value in event_dict.items():
                print(parse(value))
                print(datetime.now())
                if parse(value)==parse(datetime.now()):
                    speak_text_cmd("Sir.....today You Have an Event To Attend")
                    speak_text_cmd("Ther is a {} today sir...".format(q))
                else:
                    speak_text_cmd("No Events Today")
                    



