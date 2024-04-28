#Возможно, что нужна программа
#IDLE Python Shell
#Но я, если нужно,
#Переведу игру в .exe
#Специально для вас :)
####ЧТОБЫ РАБОТАЛИ СОХРАНЕНИЯ, НЕОБХОДИМО ВЫЙТИ КОМАНДОЙ "ВЫЙТИ" ВО ВРЕМЯ БОЯ####




import random
import time
import winsound
import sys

mana= 100
wins= 0
deaths= 0
hero_hp = 10
hero_power=1
hp_drawn=0
varn_type= [None,"Слизень","Скелет","Зомби","Сталкер","Тёмный слизень","Боб"]
rep= 1
money= 10
namelessfuncl= 0
shop_pass=0
time_now= time.time()
timeingame=0
proof=0
rand_gen=0
level=1
skip=0
kh=0
class File:
    def savecreate(self):
        global savemana,savewins,savetime,saverep,savemoney,savehp,savepower,saverand_gen
        savemana= open("SSG1.txt","w+");
        savewins= open("SSG2.txt","w+");
        savetime= open("SSG3.txt","w+");
        saverep= open("SSG4.txt","w+");
        savemoney= open("SSG5.txt","w+");
        savehp= open("SSG6.txt","w+");
        savepower= open("SSG7.txt","w+");
        saverand_gen= open("SSG8.txt","w+");

    def shifter(self):
        global timeingame
        timeingame=int(timeingame+time.time()-time_now)
        global rand_gen
        rand_gen= (timeingame*wins+rep+money-hero_hp-mana-hero_power)*17
    def save(self):
        global rand_gen,savemana,savewins,savetime,saverep,savemoney,savehp,savepower,saverand_gen
        savemana.write(str(mana))
        savewins.write(str(wins))
        savetime.write(str(timeingame))
        saverep.write(str(rep))
        savemoney.write(str(money))
        savehp.write(str(hero_hp))
        savepower.write(str(hero_power))
        saverand_gen.write(str(rand_gen))
        savemana.close()
        saverand_gen.close()
        savewins.close()
        savetime.close()
        saverep.close()
        savemoney.close()
        savehp.close()
        savepower.close()
    def load(self):
        global rand_gen,mana,wins,timeingame,rep,money,hero_hp,hero_power
        with open("SSG1.txt","r") as a:
            mana= int(a.read())
        with open("SSG2.txt","r")as b:
            wins= int(b.read())
        with open("SSG3.txt","r") as c:
            timeingame= int(c.read())
        with open("SSG4.txt","r") as d:
            rep= int(d.read())
        with open("SSG5.txt","r") as e:
            money= int(e.read())
        with open("SSG6.txt","r") as f:
            hero_hp=int(f.read())
        with open("SSG7.txt","r") as g:
            hero_power=int(g.read())
        with open("SSG8.txt","r") as h:
            proof=float(h.read())
        if proof== (timeingame*wins+rep+money-hero_hp-mana-hero_power)*17:
            input()
        else:
            with open("SSG1.txt","w") as a:
                a.write("0")
            with open("SSG2.txt","w")as b:
                b.write("0")
            with open("SSG3.txt","w") as c:    
                c.write("0")
            with open("SSG4.txt","w") as d:
                d.write("0")
            with open("SSG5.txt","w") as e:
                e.write("0")
            with open("SSG6.txt","w") as f:
                f.write("0")
            with open("SSG7.txt","w") as g:
                g.write("0")
            print("Грязный читер!")
            input()
            sys.exit(1)
saven= File()
try:
    saven.load()
    skip=1
except:  
    saven.savecreate()
while True:
    print("|▓▓                  |")
    time.sleep(0.2)
    print("|▓▓▓▓                |")
    time.sleep(0.1)
    print("|▓▓▓▓▓▓              |")
    time.sleep(0.1)
    print("|▓▓▓▓▓▓▓▓            |")
    time.sleep(2)
    print("|▓▓▓▓▓▓▓▓▓▓          |")
    time.sleep(1.6)
    print("|▓▓▓▓▓▓▓▓▓▓▓▓        |")

    print("|▓▓▓▓▓▓▓▓▓▓▓▓▓▓      |")

    print("|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    |")

    print("|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  |")
    time.sleep(1)
    print("|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|")
    print("Done!")
    time.sleep(0.5)
    break
    
        
class Shop:
    def __init__(self):
        global rep
        global kh
        self.mana_mon= random.randint(1,30)-rep+kh*2
        self.dam_mon= random.randint(5, 20)-rep+kh*2
        self.spesh_mon= random.randint(40,80)-rep+kh*2
        self.all_mon=random.randint(6, 50)-rep+kh*2
    def buy_item(self):
        global money
        global mana
        global hero_power,level
        print("Приветствую у себя в магазине, путник! Я, как самый порядочный Боб- Боб, готов предложить некоторые товары!")
        while True:
            com1=input( "Что бы ты хотел?\n Команды: пока,цены, товары, репутация, деньги, уровень\n> ")
            if com1== "цены":
                print( f"Сегодня цены такие: мана- {self.mana_mon} кромеров, обновление меча- {self.dam_mon} кромеров, ну а если всё сразу, то {self.all_mon} кромеров!")
            elif com1 == "товары" :
                items=input("Что бы ты хотел купить у меня?\n> ")
                if items== "мана":
                    if money>=self.mana_mon:
                        print("Приятно с тобой иметь дело!")
                        mana= mana+ 25
                        money= money- self.mana_mon
                        continue
                    else:
                        print("Жаль, но деньи всё же нужны!")
                        continue

                    
                if items== "меч" or items=="обновление меча":
                    if money>= self.dam_mon:
                        print("Хороша у тебя обновка! Ещё что- то?")
                        hero_power= hero_power+ 1
                        money= money- self.dam_mon
                        continue
                    else:
                        print("Надеюсь, это не грабёж? Шучу! Это мои обычные цены!")
                        continue

                if items== "всё":
                    if money>=self.all_mon:
                        print("Неудевительно! Популярный товар, знаешь ли.")
                        hero_power= hero_power+ 1
                        mana= mana+ 25
                        money= money-self.all_mon
                    else:
                        print("Богатство и сила требуют жертв!")
                        continue
            elif com1== "репутация":
                print(f"Твоя скидка составляет {rep} кромеров. Делай выводы!")
                continue
            elif com1== "деньги":
                print(f"У тебя всего {money} кромеров! Да у моего сапога запасов больше!")
                continue
            elif com1== "пока":
                print("Давай, удачи! Принеси побольше денег мне в казну, безымянный!Чтобы снова меня встретить, напиши во врмя боя \"магазин\"!")
                time.sleep(0.3)
                break
            elif com1=="уровень":
                global kh,level
                while level>=10:
                    level-=10
                    kh+=1
                if level==1:
                    print(f"┌|██|  |  |  |  |  |  |  |  |┘\n                 {kh} LvL!")
                elif level==2:
                    print(f"┌|██|██|  |  |  |  |  |  |  |┘\n                 {kh} LvL!")
                elif level==3:
                    print(f"┌|██|██|██|  |  |  |  |  |  |┘\n                 {kh} LvL!")
                elif level==4:
                    print(f"┌|██|██|██|██|  |  |  |  |  |┘\n                 {kh} LvL!")
                elif level==5:
                    print(f"┌|██|██|██|██|██|  |  |  |  |┘\n                 {kh} LvL!")
                elif level==6:
                    print(f"┌|██|██|██|██|██|██|  |  |  |┘\n                 {kh} LvL!")
                elif level==7:
                    print(f"┌|██|██|██|██|██|██|██|  |  |┘\n                 {kh} LvL!")
                elif level==8:
                    print(f"┌|██|██|██|██|██|██|██|██|  |┘\n                 {kh} LvL!")
                elif level==9:
                    print(f"┌|██|██|██|██|██|██|██|██|██|┘\n                 {kh} LvL!")
                elif level==0:
                    print(f"┌|  |  |  |  |  |  |  |  |  |┘\n                 {kh} LvL!")
class Varn:
    def __init__(self,hp,power):
        global varn_type,level,kh
        self.heal_points= hp+kh
        self.varn_type = varn_type[random.randint(1,6)]
        self.power_of_attack= power+ kh
        print(f"Перед вами материализовался враг- {self.varn_type}!")
        print(f"У него {hp+kh} хп и {power+kh} Силы!")

    def attack(self):
        global hero_hp,kh
        ran= random.randint(1,3)
        if ran == 1 or ran == 2:
            hero_hp= hero_hp- self.power_of_attack
        else:
            print("Вы успешно уклонились!")
            return
        
        global deaths
        if hero_hp <= 0:
            print("Потрачено")
            deaths= 1
            input()
            sys.exit(1)
            return deaths
        else:
            print(f"Уффф! Враг нанёс {self.power_of_attack} Урона!У вас осталось {hero_hp} Хп!")
            

    def take_damage(self):
        global hero_power
        global wins
        global rep
        global money,kh, level
        ran1= random.randint(1,3)
        if ran1==1 or ran1== 2:
            self.heal_points-= hero_power
        else:
            print("Какое несчастье! Враг уклонился!")
            return
        if self.heal_points <=0:
            level+=1
            wins= wins+1
            rep=rep+1
            money+=random.randint(1,10) +self.power_of_attack*2+kh   
            print(f"Вы убили врага! У вас {wins} побед! Уровень сейчас:{kh}/{level}")
            
            
            return wins
        else:
            print(f"Удар нанесён, у врага {self.heal_points} хп!")

def heal_self():
     global hero_hp
     global mana
     if mana>= 25:
          hero_hp += 5
          mana-= 25
          print(f"Вас исцелила магическая аура! Теперь у вас {hero_hp} хп!")
     else:
         print("Недостаточно маны!")

def give_mon():
    global money
    global rep
    money-=10
    if money<0:
        money=0
    rep-=1
    print(f"Вы откупились. Пострадали: ваша репутация({rep}) и кромеры ({money})!")

def shop():
    shop= Shop()
    shop.buy_item()
        
if skip!=1:
    var1= Varn(3,1)
    time.sleep(1)
    print("У вас есть несколько вариантов действий: Удар, Лечение, Отплатиться.\n Давайте рассмотрим основы ведения боя.\n Перед вами враг типа " ,var1.varn_type, ". Не бойтесь, он слабеникий. \n Попробуйте ударить его, введя в строку ' Атаковать' или 'Ат'")
    while True:
        func1= input("> ")
        if func1== "атаковать" or func1== "ат":
            time.sleep(0.3)
            var1.take_damage()
            time.sleep(0.3)
            break
        else:
            continue

    print("Замечателно! У вас есть два варианта исхода вашей аттаки: Уклон врага и ваше попадание. Во втором случае вы нанесёте врагу урон, который прописан у вас по сюжету, но не беспокойтесь, его можно увеличить в магазинах.\n Осторожно!, кажется враг хочет нанести вам урон! Хотите увидеть, что будет дальше?")
    while True:
        func1= input("> ")
        if func1== "да":
            time.sleep(0.3)
            var1.attack()
            time.sleep(0.3)
            break
        else:
            continue
    print("Фух, пронесло! Вы тоже можете уклоняться, так что, надеюсь, вы уклонились. Но если же в бою вы получили урон, можно восстановить себе немного хп, используюя ману. Просто напишите 'Мана' и получите несколько единиц здоровья")
    while True:
        func1= input("> ")
        if func1== "мана":
            time.sleep(0.3)
            heal_self()
            time.sleep(0.3)
            break
        else:
            continue
    print("Лечение это, конечно, хорошо, но запасы вашей маны не бесконечны. Так что используйте выданную вам силу с умом! А Восстановление ману можно купить также у продовца в магазине.")
    time.sleep(1)
    print("Есть ещё вариант отплаты от врага за внутреигровую валюту. Это не очень хорошо складывается на вашем уровне репутации, так что будьте аккуратны! Введите 'откуп' или 'отк' для проверки функции.")
    while True:
        func1= input("> ")
        if func1== "откуп" or func1== "отк":
            time.sleep(0.3)
            give_mon()
            time.sleep(0.3)
            break
        else:
            continue
    print("Ну вот и всё! На этом основное обучение закончено! Об остальном вам расскажут остальные НИПы, которых довольно много в нашей прекрасной игре! Удачи тебе, путник!")
    input("> ")
    shop()
while True:
    winsl=wins+ 1
    k= random.randint(1,10)
    l= random.randint(1,3)
    var1= Varn(k,l)
    if shop_pass==1:
        shop_pass=0
        shop()
        time.sleep(0.3)
    
    while True:

        while True:
            func1= input("> ")
            if func1== "атаковать" or func1== "ат":
                time.sleep(0.3)
                var1.take_damage()
                time.sleep(0.3)
                break
            elif func1== "мана":
                time.sleep(0.3)
                heal_self()
                time.sleep(0.3)
                break
            elif func1== "откуп" or func1== "отк":
                time.sleep(0.3)
                give_mon()
                time.sleep(0.3)
                namelessfuncl= 1
                break
            elif func1== "магазин":
                shop_pass=1
                print("Вы достали телефон и набрали номер.")
                time.sleep(0.3)
                print(".")
                time.sleep(0.3)
                print("..")
                time.sleep(0.3)
                print("...")
                time.sleep(0.3)
                print("Кажется, вы дозвонились.")
                print("> ")
                time.sleep(0.9)
                print("А, нет, вы ошиблись.")
                time.sleep(0.3)
                print(".")
                time.sleep(0.3)
                print("..")
                time.sleep(0.3)
                print("...")
                time.sleep(0.3)
                print("Вас услышали. После этой драки вас встретит продавец Боб- Боб!")
                break
            elif func1== "выйти":
                exit= input("Вы уверены?\n> ")
                if exit== "да":
                    saven.savecreate()
                    saven.shifter()
                    saven.save()
                    sys.exit(1)
                else:
                    continue
            else:
                continue
        if namelessfuncl==1:
            namelessfuncl=0
            break
        elif wins== winsl:
            while level>=10:
                level-=10
                kh+=1 
            break
        else:            
            time.sleep(0.3)
            var1.attack()
            time.sleep(0.3)
        
        
        


    
