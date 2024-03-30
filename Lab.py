age = int(input("Введите ваш возраст (в годах): "))
height = int(input("Введите ваш рост (в см): "))
pol = input("Введите ваш пол (М или Ж): ")

if pol == "М":
    ideal_weight = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
elif pol == "Ж":
    ideal_weight = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
else:
    print("Некорректный ввод пола. Введите 'М' или 'Ж'.")
    exit()

print("Ваш идеальный вес: {} кг".format(ideal_weight))

weight_now = float(input("Введите ваш текущий вес (в кг): "))
if weight_now > ideal_weight:
    print("Вам необходимо снизить свой вес.")
elif weight_now < ideal_weight:
    print("Вам необходимо набрать вес.")
else:
    print("У вас идеальный вес!")
