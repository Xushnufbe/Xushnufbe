import wikipedia
import requests
wikipedia.set_lang("Uz")
print("Xush kelibsiz")
print("bo'limlardan birini tanlang")
print("Ogohlantirish Sms bomber faqat beeline uchun")
print("1-Malumot topish")
print("2-Sms bomber")

menu = ('1','2')

usr_inp = input("bolimni tanlang: ")
if usr_inp == '1':   
    savol = input("Savolni kiriting: ")
    print(wikipedia.summary(savol))

if usr_inp == '2':   
    num = input("Numerni kiriting +998siz ")
    api = ("http://beeline.uz/restservices/api/a2/auth/998"+num+"/otp/send")
    response =   requests.get(api)
    if response:
    	print("Sms 1 sekunddan keyin boradi")
    else:
    			print("Xatolik")
