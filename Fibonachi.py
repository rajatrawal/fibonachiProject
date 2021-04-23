f1, f2, count = 0, 1, 0
while f2 < 10000:
    count += 1
    if count > 27:
        print("Итерация больше 27. Прерываюсь.")
        break
    f1, f2 = f2, f1 + f2
    if f2 < 1000:
        continue
    print(f2)
else:
    print("Было", count, "итерации")