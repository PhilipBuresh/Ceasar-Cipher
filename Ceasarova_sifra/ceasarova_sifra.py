text = input("Zadej text: ") #Zadáni textu
right_key = False
right_code = False

while right_key == False:   
    key = input("Zapiš klíč (číselně): ") #Zápis kliče
    if key.isnumeric():
        right_key = True
    else:
        print("Zkuste to znovu")
        continue
while right_code == False:   
    code = input("Vyber si (ENCODE / DECODE): ") #Výběr mezi ENCODE a DECODE
    code = code.lower()
    if code == "encode" or code == "decode":
        right_code = True
    else:
        print("Zkuste to znovu")
        continue
    
final_text = ""

for letter in text:
    num = ord(letter)
    if num >= 64 and num <= 91 or num >= 97 and num <= 122:
        #ENCODE----------------------------------------
        if code == "encode": 
            original_num = num
            num += int(key)
            if original_num >= 64 and original_num <= 91:
                while num >= 91:
                    help_key = num - 91
                    num = 65 + help_key
            if original_num >= 97 and original_num <= 123:
                while num >= 123:
                    help_key = num - 123
                    num = 97 + help_key
        #DECODE---------------------------------------- 
        else:
            original_num = num
            num -= int(key)
            if original_num >= 64 and original_num <= 91:
                while num <= 64:
                    help_key = 64 - num
                    num = 90 - help_key
            if original_num >= 97 and original_num <= 123:
                while num <= 96:
                    help_key = 96 - num
                    num = 122 - help_key
    final_text = final_text + chr(num)  
print(final_text) #Výsledek

