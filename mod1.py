from tkinter import *
root=Tk()
l1=Label(root,text='enter city ')
e1=Entry(root)
def fun():
 import requests,json
 api_key='b8de1ee1c90ee40bcb22a93b7f7c59ee'
 base_url = "http://api.openweathermap.org/data/2.5/weather?"
 city=e1.get()
 url=base_url+ "appid=" + api_key + "&q=" + city
 res=requests.get(url)
 data=res.json()
 temp=data['main']['temp']
 wind_speed=data['wind']['speed']
 latitude=data['coord']['lat']
 longitude=data['coord']['lon']
 description=data['weather'][0]['description']
 temperature='Temparature : {} kelvin'.format(temp)
 txt1.insert(0.0,temperature)
 wind='Wind Speed : {} m/s'.format(wind_speed)
 txt2.insert(0.0,wind)
 lat='Latitude : {}'.format(latitude)
 txt3.insert(0.0,lat)
 lon='Longitude : {}'.format(longitude)
 txt4.insert(0.0,lon)
 des='Description : {}'.format(description)
 txt5.insert(0.0,des)
l1.grid(row=0,sticky=W)
e1.grid(row=0,column=1)
b1=Button(root,text='GO',command=fun)
b1.grid(row=1)
txt1=Text(root,width=25,height=2,wrap=WORD)
txt1.grid(row=2,columnspan=2,sticky=W)
txt2=Text(root,width=25,height=2,wrap=WORD)
txt2.grid(row=3,columnspan=2,sticky=W)
txt3=Text(root,width=25,height=2,wrap=WORD)
txt3.grid(row=4,columnspan=2,sticky=W)
txt4=Text(root,width=25,height=2,wrap=WORD)
txt4.grid(row=5,columnspan=2,sticky=W)
txt5=Text(root,width=25,height=2,wrap=WORD)
txt5.grid(row=6,columnspan=2,sticky=W)
root.mainloop()