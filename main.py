lugat = {
    "быть": "bo‘lmoq",
    "мочь": "qodir bo‘lmoq",
    "скаэать": "aytmoq",
    'apple':'olma'
}



while True:
    print('agar inglizcha lug\'at qoshishni xohlasangiz 1 raqamini bosing')
    print('agar ruscha lug\'at qoshishni xohlasangiz 2 raqamini bosing')
    print('agar sizga uzbekcha sozning inglizchasi,'
          ' \nkerak bolyaptima lug\'atingizdagi 3 raqamini bosing')
    print('agar sizga uzbekcha sozning ruschasi,'
          ' \nkerak bolyaptima lug\'atingizdagi 4 raqamini bosing')
    print('bu dasturni toxtatingni xohlasangiz 5 ni bosing')
    tanlov=int(input('birini tanlang iltimos '))
    if tanlov==1:
       a=input('inglizcha soz kiriting')
       b=input('uzbekcha tarjimasini kiriting')

       if  a not in lugat and b not in lugat.values():
           lugat[a]=b
           print(f"So‘z qo‘shildi: {a} -> {b}")
       else:
            print("Bu so‘z lugatda mavjud!")
    elif tanlov==2:
        ruscha=input('ruscha soz kiriting')
        tarjima=input('uzbekcha tarjimasi')
        if ruscha not in lugat and tarjima not in lugat.values():
            lugat[ruscha] = tarjima
            print(f"So‘z qo‘shildi: {ruscha} -> {tarjima}")
        else:
            print("Bu so‘z lugatda mavjud!")
    elif tanlov==3:
        uzbekcha=input('siz xohlagan uzbekcha soz kiriting')
        topildi=False
        for i,v in lugat.items():
            if uzbekcha==v:
                print(f"Tarjimalari: {i}")
                topildi=True
        if not topildi:
            print('Bunday soz yo‘q sizning lugatingizda')
    elif tanlov==4:
        uzb_soz=input('ozbekcha soz kiring men sizga ruschasini '
                      '\nchiqarib beraman lugatingizdagi')
        topildi = False
        for i,v in lugat.items():
            if uzb_soz==v:
                print(f"Tarjimalari: {i}")
        if not topildi:
            print('Bunday soz yo‘q sizning lugatingizda')
    elif tanlov==5:
        print('dastur yakunlandi')
        break
    else:
        print('natogri tanlov')