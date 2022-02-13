
import sys
import time 
import random
p_hp=20
p_q=0
p_xp=3
print('欢迎加入游戏世界')
time.sleep(1)
print('你的血量:'+str(p_hp))
time.sleep(1)
print('你的攻击:'+str(p_xp))
dj=['cs',]
time.sleep(1)
while True:
    zl=input('按a散步按b商店(开发中）按c战斗按d查看金币')
    if zl=='a' :
        if random.randint(0,1)==1 :
            print('你遇到了敌人')
            e_hp=random.randint(10,15)
            e_xp=random.randint(1,2)
            while p_hp>=1 and e_hp>=1:
                print('这是你的回合')
                zl=input('按a攻击按c道具按d跳过')
                if zl=='a':
                    e_hp=e_hp-p_xp
                    print('敌人血量:'+str(e_hp))
                elif zl=='c':
                    print('从1开始输入'+dj)
                    zl=input()
                    del dj[int(zl)]
                    p_hp=p_hp+10                   
                elif zl=='d':
                    print('你跳过了此回合')
                print('这是敌人的回合')
                p_hp=p_hp-e_xp
                print('你的血量:'+str(p_hp))
                if p_hp>=1 and e_hp<1:
                    print('你胜利了，')
                    
                    p_hp=p_hp+e_hp
                    p_xp=p_xp+e_xp
                    p_q=p_q+10
                    break
                elif  p_hp<1 and e_hp>=1:
                    print('你失败了')                    
                    break
                elif  p_hp<1 and e_hp<1:
                    print('你们都死翘翘了')
                    break
        else:
            print('你减到一张彩票')
            Jl=random.randint(0,100)
            print('你跑去兑奖获得了'+str(Jl)+'元')

    elif zl=='b':
        while True:        
            if p_xp>=3:
                print('欢迎来到商店')
                zl==input('按a购买加血道具按b卖加血道具按c退出')
                if zl=='a':
                    if p_q>=10:
                        dj.append('jxdj')
                        print('购买成功')
                    else:
                        print('你的钱不够哦')
                elif zl=='b':
                    if 'jxdj' in dj:
                        del dj[1]
                        p_q=p_q+9                                                   
                elif zl=='c':
                    break
            elif p_xp<3:
                print('你的等级不够哦')
    elif zl=='c':
        print('你遇到了敌人')
        print('这是你的回合')                
        zl=input('按a散步按b商店按c战斗按d查看金币')    
        if zl=='a':
            e_hp=e_hp-p_xp
            print('敌人血量:'+str(e_hp))
        elif zl=='c':
            print('从1开始输入'+dj)
            zl=input()
            del dj[int(zl)]
            p_hp=p_hp+10                   
        elif zl=='d':
            print('你跳过了此回合')
        print('这是敌人的回合')
        p_hp=p_hp-e_xp
        print('你的血量:'+str(p_hp))
        if p_hp>=1 and e_hp<1:
            print('你胜利了')
            p_hp=p_hp+e_hp
            p_xp=p_xp+e_xp
            p_q=p_q+10
            break
        elif  p_hp<1 and e_hp>=1:
            print('你失败了')                    
            break
        elif  p_hp<1 and e_hp<1:
            print('你们都死翘翘了')
            break
    elif zl=='d':
        print('你的金币为：'+str(p_q))

    

                

                




                    


