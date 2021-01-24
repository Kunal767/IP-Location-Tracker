from tkinter import *
from tkinter import PhotoImage
import json
import os
import urllib3
from tkinter import messagebox
import folium
import webbrowser

root =  Tk()
root.geometry("600x500")
root.title("IP Location Tracker")
root.config(bg="grey")
root.iconbitmap("Location.ico")
root.resizable(False, False)

def location_find():
    try:
        ip_input = input_ip_entry.get()
        url = "http://ip-api.com/json/" + ip_input
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        values = json.loads(response.data)
        lati = float(values['lat'])
        longi = float(values['lon'])
        country.set(values['country'])
        city.set(values['city'])
        region.set(values['region'])
        time.set(values['timezone'])
        isp.set(values['isp'])

        fg = folium.FeatureGroup("IP Tracker")
        fg.add_child(folium.GeoJson(data=(open("india_states.json", 'r', encoding="utf-8-sig").read())))
        fg.add_child(folium.Marker(location=[lati, longi], popup="This is Your Location"))

        map = folium.Map(location=[lati, longi], zoom_start=7)
        map.add_child(fg)
        map.save("map.html")
    except EXCEPTION as e:
        messagebox.askretrycancel("Error", "Please Enter a Valid IP Address")


title = Label(root, text="IP Location Tracker", bg="grey", fg="white", font=("ubuntu", 20), pady="20px")
title.pack(anchor="center")

input_ip = Label(root, text="Enter any IP Address :- ", bg="grey", fg="cyan", font=("ubuntu", 14))
input_ip.place(x="30px", y="70px")

def on_click(e):
    btn_finder['bg'] = "white"
    btn_finder['fg'] = "black"

def on_leave(e):
    btn_finder['bg'] = "brown"
    btn_finder['fg'] = "white"

input_ip_entry = Entry(root, bg="beige", fg="black", font=("ubuntu", 14), width=25)
input_ip_entry.place(x="200px", y="71px")

btn_finder = Button(root, text="Find Location", bg="brown", fg="white", font=("ubuntu", 15), cursor="hand2", command=location_find)
btn_finder.bind("<Enter>", on_click)
btn_finder.bind("<Leave>", on_leave)
btn_finder.place(x="170px", y="110px")

country_label = Label(root, text="Country :- ", bg="grey", fg="lime", font=("ubuntu", 14))
country_label.place(x="80px", y="160px")

country = StringVar()
country_entry = Entry(root, textvariable=country, fg="brown", state="readonly", width=23, font=("ubuntu", 14))
country_entry.place(x="160px", y="162px")

region_label = Label(root, text="Region :- ", bg="grey", fg="lime", font=("ubuntu", 14))
region_label.place(x="80px", y="190px")

region = StringVar()
region_entry = Entry(root, textvariable=region, fg="brown", state="readonly", width=23, font=("ubuntu", 14))
region_entry.place(x="160px", y="192px")

city_label = Label(root, text="City :- ", bg="grey", fg="lime", font=("ubuntu", 14))
city_label.place(x="80px", y="220px")

city = StringVar()
city_entry = Entry(root, textvariable=city, fg="brown", state="readonly", width=23, font=("ubuntu", 14))
city_entry.place(x="160px", y="222px")

time_label = Label(root, text="TimeZone :- ", bg="grey", fg="lime", font=("ubuntu", 14))
time_label.place(x="80px", y="250px")

time = StringVar()
time_entry = Entry(root, textvariable=time, fg="brown", state="readonly", width=23, font=("ubuntu", 14))
time_entry.place(x="160px", y="252px")

isp_label = Label(root, text="ISP :- ", bg="grey", fg="lime", font=("ubuntu", 14))
isp_label.place(x="80px", y="280px")

isp = StringVar()
isp_entry = Entry(root, textvariable=isp, fg="brown", state="readonly", width=23, font=("ubuntu", 14))
isp_entry.place(x="160px", y="282px")

def btn_mapclick():
    try:
        webbrowser.open("map.html")
    except Exception as e:
        messagebox.askretrycancel("A Problem Has Been Occured", "Please First Find Your IP then Press this Button")

btn_map = Button(root, text="Show Location On Map", bg="black", fg="white", font=("ubuntu", 15), cursor="hand2", command=btn_mapclick)
btn_map.place(x="130px", y="320px")

root.mainloop()