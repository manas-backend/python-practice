pin = '1111'
balans = 100000000
print("Tilni tanlang: ")
print("1. O'zbek tili")
print("2. Русский язык")
print("3. English")
lang_code = int(input("Tanlang|Выберите|Choose: "))

if lang_code == 1:
    lang = 'uz'
elif lang_code == 2:
    lang = 'ru'
elif lang_code == 3:
    lang = 'en'
else:
    print("Xato / Ошибка  / Error.")
    exit() 


pin_input = input("PIN KOD ")
if pin_input != pin:
    print("XXX")
    exit()
    
if lang == 'uz':
        print("""
      1. Balansni ko'rish
      2. Naqd pul yechish
      3. Pul kiritish
      4. Pin kodni almashtirish
      5. Kommunal to'lovlar 
      6. SMS xabarnoma
      """)    
        n = int(input("Tanlang: "))
        match n:
            case 1:
                print(f"Sizning balansingiz: {balans} so'm")  
            case 2:
                print("""
              1. 50000   4. 400000
              2. 100000  5. 800000
              3. 200000  6. Boshqa summa
              """)
                withdraw_input = int(input("Tanlang: "))
                match withdraw_input:
                    case 1:
                        if balans < 50000:
                            print("Balansda yetarli mablag' mavjud emas.")
                        else:
                            balans -= 50000
                        print("Xizmatlarimizdan foydalanganingiz uchun rahmat.")
    
                    case 2:
                        if balans < 100000:
                            print("Balansda yetarli mablag' mavjud emas.")
                        else:
                            balans -= 100000
                        print("Xizmatlarimizdan foydalanganingiz uchun rahmat.")
                    case 3:
                        if balans < 200000:
                            print("Balansda yetarli mablag' mavjud emas.")
                        else:
                            balans -= 200000
                        print("Xizmatlarimizdan foydalanganingiz uchun rahmat.")
                    case 4:
                        if balans < 400000:  
                            print("Balansda yetarli mablag' mavjud emas.")
                        else:
                            balans -= 400000  
                        print("Xizmatlarimizdan foydalanganingiz uchun rahmat.")
                    case 5:
                        if balans < 800000:
                            print("Balansda yetarli mablag' mavjud emas.")
                        else:
                            balans -= 800000
                        print("Xizmatlarimizdan foydalanganingiz uchun rahmat.")
                    case 6:
                        withdraw_input = int(input("Yechiladigan mablag'ni kiriting: "))  
                        if balans < withdraw_input:
                            print("Balansda yetarli mablag' mavjud emas.")
                        else:
                            balans -= withdraw_input  
                        print("Xizmatlarimizdan foydalanganingiz uchun rahmat.")   
            case 3:
                withdraw_input = int(input("Kiritmoqchi bo'lgan summangizni kiriting: "))
                print (f"{withdraw_input + balans}\nSumma muvoffaqiyatli qo'shildi") 
            case 4:
                yangi_pin = int(input("O'zgartirmoqchi bo'lgan pin kodni kiriting: "))
                if  yangi_pin < 1000 or  yangi_pin < 9999:
                    print (f"{yangi_pin}\nPin kod muvoffaqiyatli o'zgartirildi: ")
                else:
                    print ("Xato kiritildi\n1000 va 9999 oralig'idagi sonni kiriting") 
            case 5:
                print("""
                      
        1. Suv uchun to'lov
        2. Gaz uchun to'lov
        3. Chiroq uchun to'lov
                    
                    """)
                withdraw_input = int(input("Tanlang: "))
    
                summa = int (input("To'lmamoqchi bo'lgan summangizni kiriting: "))
                if balans < summa:
                    print ("Balansda yetarli mablag' mavjud emas")
                else:
                    print ("Muvoffaqiyatli to'landi") 
            case 6:
                print (f"M bank\n02.12.2025\n18:00\nSizning balansingizda qolgan summa: {balans} \nXizmatlarimizdan foydalanganiz uchun rahmat")         
if lang == 'ru':
        print("""
      1. Просмотр баланса 
      2. Снятие наличных 
      3. Внести деньги 
      4. Сменить пин-код
      5. Коммунальные платежи
      6. SMS-уведомления 
      """)    
        n = int(input("Выберите "))
        match n:
            case 1:
                print(f"Ваш баланс  {balans} сум")  
            case 2:
                print("""
              1. 50000   4. 400000
              2. 100000  5. 800000
              3. 200000  6. Другая сумма
              """)
                withdraw_input = int(input("Выберите: "))
                match withdraw_input:
                    case 1:
                        if balans < 50000:
                            print("На балансе недостаточно средств. ")
                        else:
                            balans -= 50000
                        print("Спасибо за использование наших услуг.")
                    case 2:
                        if balans < 100000:
                            print("На балансе недостаточно средств.")
                        else:
                            balans -= 100000
                        print("Спасибо за использование наших услуг.")
                    case 3:
                        if balans < 200000:
                            print("На балансе недостаточно средств.")
                        else:
                            balans -= 200000
                        print("Спасибо за использование наших услуг.")
                    case 4:
                        if balans < 400000:  
                            print("На балансе недостаточно средств.")
                        else:
                            balans -= 400000  
                        print("Спасибо за использование наших услуг.")
                    case 5:
                        if balans < 800000:
                            print("На балансе недостаточно средств.")
                        else:
                            balans -= 800000
                        print("Спасибо за использование наших услуг.")
                    case 6:
                        withdraw_input = int(input("Введите сумму для снятия: "))  
                        if balans < withdraw_input:
                            print("На балансе недостаточно средств.")
                        else:
                            balans -= withdraw_input  
                        print("Спасибо за использование наших услуг.")   
            case 3:
                withdraw_input = int(input("Введите сумму, которую хотите внести : "))
                print (f"{withdraw_input + balans}\nСумма успешно добавлена ") 
            case 4:
                yangi_pin = int(input("Введите пин-код, который хотите изменить : "))
                if  yangi_pin < 1000 or  yangi_pin < 9999:
                    print (f"{yangi_pin}\nПин-код успешно изменён : ")
                else:
                    print ("Введено неправильно \nВведите число от 1000 до 9999 ") 
            case 5:
                print("""
            1. Оплата за воду
            2. Оплата за газ
            3. Оплата за электричество
                     """)
                withdraw_input = int(input("Выберите: "))
                summa = int(input("Введите сумму, которую хотите оплатить: "))
                if balans < summa:
                    print("На балансе недостаточно средств")
                else:
                    print("Оплата успешно выполнена")

            case 6:
                print(f"M bank\n02.12.2025\n18:00\nНа вашем балансе осталось: {balans} сум\nСпасибо, что пользуетесь нашими услугами")
        
if lang == 'en':
        print("""
      1. Check balance
      2. Withdraw cash
      3. Deposit money
      4. Change PIN code
      5. Utility payments
      6. SMS notification
      """)
        n = int(input("Choose: "))
        match n:
            case 1:
                print(f"Your balance: {balans} sum")  
            case 2:
                print("""
              1. 50000   4. 400000
              2. 100000  5. 800000
              3. 200000  6. Other amount
              """)
                withdraw_input = int(input("Choose: "))
                match withdraw_input:
                    case 1:
                        if balans < 50000:
                            print("Insufficient funds.")
                        else:
                            balans -= 50000
                        print("Thank you for using our services.")
                    case 2:
                        if balans < 100000:
                            print("Insufficient funds.")
                        else:
                            balans -= 100000
                        print("Thank you for using our services.")
                    case 3:
                        if balans < 200000:
                            print("Insufficient funds.")
                        else:
                            balans -= 200000
                        print("Thank you for using our services.")
                    case 4:
                        if balans < 400000:  
                            print("Insufficient funds.")
                        else:
                            balans -= 400000  
                        print("Thank you for using our services.")
                    case 5:
                        if balans < 800000:
                            print("Insufficient funds.")
                        else:
                            balans -= 800000
                        print("Thank you for using our services.")
                    case 6:
                        withdraw_input = int(input("— Enter the amount to withdraw: "))  
                        if balans < withdraw_input:
                            print("Insufficient funds.")
                        else:
                            balans -= withdraw_input  
                            print("Thank you for using our services.")   
            case 3:
                withdraw_input = int(input("Enter the amount to deposit: "))
                print (f"{withdraw_input + balans}\nAmount successfully added") 
            case 4:
                yangi_pin = int(input("Enter the PIN code you want to change: "))
                if  yangi_pin < 1000 or  yangi_pin < 9999:
                    print (f"{yangi_pin}\nPIN code successfully changed: ")
                else:
                    print ("Incorrect input\nEnter a number between 1000 and 9999")
            case 5:
                print("""
            1. Payment for water
            2. Payment for gas
            3. Payment for electricity
                """)
                withdraw_input = int(input("Choose: "))
                amount = int(input("Enter the amount you want to pay: "))
                if balans < amount:
                    print("Insufficient balance")
                else:
                    print("Payment successful")
            case 6:
                print(f"M bank\n02.12.2025\n18:00\nRemaining balance: {balans} sum\nThank you for using our services")


