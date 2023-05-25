from tkinter import *
from tkinter import ttk
import requests

def get_data():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    name_w1.config(text=data["weather"][0]["main"])
    name_c1.config(text=data["weather"][0]["description"])
    name_t1.config(text=str(int(data["main"]["temp"]-273.15)))
    name_tm1.config(text=str(int(data["main"]["temp_min"]-273.15)))
    name_tmax1.config(text=str(int(data["main"]["temp_max"]-273.15)))
    name_wind1.config(text=data["wind"]["speed"])


window = Tk()
window.title("Weather App by Zain Ali")    # Creating title

window.config(bg="blue")           # giving background clolor to window

window.geometry("500x750")  #   Setting window size

name = Label(window, text="Weather App",          #Setting name of app to be displayed on window
             font=("Times New Roman",30,"bold"))

name.place(x=25,y=50,height=50,width=450)     #setting place for name 

list_city = ["Ahmadpur East","Ahmed Nager Chatha","Ali Khan Abad","Alipur","Arifwala","Attock","Bhera","Bhalwal","Bahawalnagar","Bahawalpur","Bhakkar","Burewala","Chenab Nagar","Chillianwala","Choa Saidanshah","Chakwal","Chak Jhumra","Chichawatni","Chiniot","Chishtian","Chunian","Dajkot","Daska","Davispur","Darya Khan","Dera Ghazi Khan","Dhaular","Dina","Dinga","Dhudial Chakwal","Dipalpur","Faisalabad","Fateh Jang","Ghakhar Mandi","Gojra","Gujranwala","Gujrat","Gujar Khan","Harappa","Hafizabad","Haroonabad","Hasilpur","Haveli Lakha","Islamabad","Jalalpur Jattan","Jampur","Jaranwala","Jhang","Jhelum","Jauharabad","Kallar Syedan","Kalabagh","Karor Lal Esan","Karachi","Kasur","Kamalia","Kāmoke","Khanewal","Khanpur","Khanqah Sharif","Kharian","Khushab","Kot Adu","Lahore","Lalamusa","Layyah","Lawa Chakwal","Liaquat Pur","Lodhran","Malakwal","Mamoori","Mailsi","Mandi Bahauddin","Mian Channu","Mianwali","Miani","Multan","Murree","Muridke","Mianwali Bangla","Muzaffargarh","Narowal","Nankana Sahib","Okara","Pakpattan","Pattoki","Pindi Bhattian","Pind Dadan Khan",
    "Pir Mahal","Qaimpur","Qila Didar Singh","Raiwind","Rajanpur","Rahim Yar Khan","Rawalpindi","Renala Khurd","Sadiqabad","Sagri","Sahiwal","Sambrial","Samundri","Sangla Hill","Sarai Alamgir","Sargodha",
    "Shakargarh","Sheikhupura","Shujaabad","Sialkot","Sohawa","Soianwala","Siranwali",
    "Tandlianwala","Talagang","Taxila","Toba Tek Singh","Vehari","Wah Cantonment", "Wazirabad","Yazman","Zafarwal"]                                      #list of cities to search weather for  

city_name = StringVar()
combo = ttk.Combobox(window, text="Weather App",values=list_city,          #Setting combobox for searching cities
             font=("Times New Roman",20),textvariable=city_name)
combo.place(x=25,y=120,height=50,width=450)

#Creating Weather conditions
name_w = Label(window, text="Weather climate", 
             font=("Times New Roman",17))
name_w.place(x=25,y=260,height=50,width=210)

name_w1 = Label(window, text="", 
             font=("Times New Roman",17))
name_w1.place(x=250,y=260,height=50,width=210)

name_c = Label(window, text="Weather Condition", 
             font=("Times New Roman",17))
name_c.place(x=25,y=330,height=50,width=210)

name_c1 = Label(window, text="", 
             font=("Times New Roman",17))
name_c1.place(x=250,y=330,height=50,width=210)

name_t = Label(window, text="Temperatre", 
             font=("Times New Roman",17))
name_t.place(x=25,y=400,height=50,width=210)

name_t1 = Label(window, text="", 
             font=("Times New Roman",17))
name_t1.place(x=250,y=400,height=50,width=210)

name_tm = Label(window, text="Minimum Temperatre", 
             font=("Times New Roman",17))
name_tm.place(x=25,y=470,height=50,width=210)

name_tm1 = Label(window, text="", 
             font=("Times New Roman",17))
name_tm1.place(x=250,y=470,height=50,width=210)

name_tmax = Label(window, text="Maximum Temperatre", 
             font=("Times New Roman",17))
name_tmax.place(x=25,y=540,height=50,width=210)

name_tmax1 = Label(window, text="", 
             font=("Times New Roman",17))
name_tmax1.place(x=250,y=540,height=50,width=210)

name_wind = Label(window, text="Wind", 
             font=("Times New Roman",17))
name_wind.place(x=25,y=610,height=30,width=210)

name_wind1 = Label(window, text="", 
             font=("Times New Roman",17))
name_wind1.place(x=250,y=610,height=30,width=210)

#Creating button
btn = Button(window,text="Submit",
             font=("Times New Roman",20),command=get_data)
btn.place(x=200,y=190,height=50,width=100)

info = Label(text="Weather App developed by Zain Ali",
             font=("Italic",15,"bold"))
info.place(x=800,y=300,height=50,width=400)

info1 = Label(text="Done using Tkinter-Python",
             font=("Italic",15,"bold"))
info1.place(x=800,y=360,height=50,width=400)

txt = Label(text="You can help me in improving this",
            font=("Calibri(Body)",12))
txt.place(x=800,y=430,height=30,width=400)

window.mainloop()