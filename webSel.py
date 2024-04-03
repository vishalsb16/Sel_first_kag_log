import time
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from tkinter import messagebox
import pandas as pd
from selenium.webdriver.edge.service import Service as EDG
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import numpy as np
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC

caps=DC.EDGE
caps['goog:loggingPrefs']={'browser':'ALL'}

root=Tk()
root.geometry('450x200')
root.title("Kaggle Login")

frame=Frame(root)
frame.pack()
label1=Label(frame,text="Username",width=25,relief=FLAT,height=1)
label1.grid(row=0,column=0)
entry=Entry(frame,width=30,bd=0)
entry.grid(row=0,column=1)

label2=Label(frame,text="Password",width=25,relief=FLAT,height=1)
label2.grid(row=1,column=0)
entry1=Entry(frame,width=30,bd=0)
entry1.grid(row=1,column=1)
entry1.config(show="*");
btn4=Button(frame,text="Login",command=lambda:(Submit_btn(),messagebox.showinfo("Login","Login Sucessfull")),width=25,relief=RAISED)
btn4.grid(row=2,column=1)
frame.rowconfigure(0,minsize=40)
frame.rowconfigure(1,minsize=40)
frame.rowconfigure(2,minsize=40)


load_dotenv

username=entry.get()
password=entry1.get()


def Submit_btn():
    browser = webdriver.Edge(service=EDG(EdgeChromiumDriverManager().install()))
    browser.get("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F/")

    time.sleep(3)

    u_field=browser.find_element(By.XPATH,'//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/label[1]/input')
    p_field=browser.find_element(By.XPATH,'//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/label[2]')

    u_field.send_keys(username)
    p_field.send_keys(password)
    sub_field=browser.find_element(By.XPATH,'//*[@id="site-content"]/div[2]/div[1]/div/div[1]/form/div/div[2]/button[2]/span')
    sub_field.click()

    time.sleep(5)

    logs=browser.get_log('browser')
    for log in logs:
        print(log)

    browser.quit()

root.mainloop()