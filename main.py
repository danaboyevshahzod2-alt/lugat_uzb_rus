lugat = {
    "быть": "bo‘lmoq",
    "мочь": "qodir bo‘lmoq",
    "скаэать": "aytmoq"
}

while True:
    print("\n1. So‘zni tarjima qilish")
    print("2. Yangi so‘z qo‘shish")
    print("3. Chiqish")

    tanlov = input("Tanlang (1/2/3): ")

    if tanlov == "1":
        a = input("So'zni kiriting: ")
        if a in lugat:
            print(f"Tarjimasi: {lugat[a]}")
        elif a in lugat.values():
            for k, v in lugat.items():
                if v == a:
                    print(f"Ruscha: {k}")
        else:
            print("Bunday so‘z yo‘q")

    elif tanlov == "2":
        ruscha = input("Ruscha so‘z: ")
        uzbekcha = input("O‘zbekcha tarjimasi: ")
        lugat[ruscha] = uzbekcha
        print(f"So‘z qo‘shildi: {ruscha} -> {uzbekcha}")

    elif tanlov == "3":
        print("Dastur yakunlandi")
        break

    else:
        print("Noto‘g‘ri tanlov")