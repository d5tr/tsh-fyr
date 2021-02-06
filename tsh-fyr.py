import random
print('''
# Thanks for use my tool #
insta : d_5tr
[1]تشفير بقاعده (محدود)
[2]تشفير عشوائي (الى 70 رمز)
''')
ch0s = int(input('enter number you went : '))
if ch0s == 2:
    lowen = 'qwertyuiopasdfghjklzxcvbnm'
    uppen = 'QWERTYUIOPASDFGHJKLZXCVBNM'                    #تشفير الى 70 رمز 
    numbers = '1234567890'
    symbols = '[]{+*/-_@$'

    all = lowen+uppen+numbers+symbols
    input('site went to hash : ')
    length = int(input('enter number : '))
    passwond = "".join(random.sample(all,length))
    print('------------------------')
    print(passwond)
    print('------------------------')

    print('do you went save in file ? (yes , no) :')
    w6 = input('enter you went :')
    if w6 == 'yes':

        opened_file = open(input('name file to save : '), 'w')

        opened_file.write(passwond)
    elif w6 == 'no':
        exit


elif ch0s == 1:
    import os 
    os.system("clear")

    while True:
        from hashlib import md5
        x = input('enter your hash :')
        y = md5(x.encode()).hexdigest()                  #تشفير بقاعده 
        print("-----------------------")
        print(y)
        print("-----------------------")
        print ('do you went save in file ? (yes , no) :')
        w4 = input('enter you went :')
        if w4 == 'yes' :
            of = open(input('enter name file :'), 'w')
            of.write(y)
        
        elif ch0s == 'no' :
            exit


else :
    print('error')                # d_5tr -- 01
    exit        




