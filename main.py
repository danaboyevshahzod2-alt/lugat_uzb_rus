while True:
   a=input('sozni kiriting')

   lugat ={"быть": 'bolmoq',
        'мочь':'qodir bolmoq'}
   if a in lugat.values():
       for k, v in lugat.items():
           if v == a:
               print(k)
   else:
       print('bunday soz yoq')