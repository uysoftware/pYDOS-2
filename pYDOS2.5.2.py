from random import*
import time,os
print("*"*10+"M106-dos**********")
time.sleep(5)
print("Please choose:1=Start M106-dos Normally 2=Turn off.")
u = int(input())
if u == 1:
    space = "\ "
    sp="*"
    s=" "
    i = "a"
    ia = "\033[36m欢迎使用M106DOS-Version 2.5.2！"
    data="""
        
             **         **     ***  ******  *******
            *  *       *  *      *  *    *  *
           *    *     *    *     *  *    *  *     
          *      *   *      *    *  *    *  *******
         *        * *        *   *  *    *  *     *
        *          *          *  *  ******  *******
    """
    print(data)
    print("Version 2.5.2")
    time.sleep(2)
    print("             "*75)
    print(ia)
    if i == "A" or "a":
        print("M106-DOS已准备就绪。")
        time.sleep(0.8)
        print("M106-DOS加载:",randint(1,99),"%")
        time.sleep(0.1)
        print("M106-DOS加载:",100,"%")
        time.sleep(0.1)
        i = "b"
        if i == "A" or "a" or "b" or "B":
            time.sleep(0.1)
            print("C:\ ")
            while 1 < 2:
                i = input("\033[32m你可以输入'M106-dos'去查看关于M106-DOS的文件；\n'system'可以查看电脑里的系统；\n'run'可以查看电脑里的选项。例如文件管理器，重置电脑等；\n'BIOS'可以开启安全模式（网络安全模式、iPv4，iPv6）\n'exit'可以结束进程并关闭M106DOS;\n'version'可以查看版本/升级")
                if i == "version":
                    print("版本：Version2.5.2，版本号：21CORI26025202")
                   
                elif i == "M106-dos":
                    for i in range(35):
                        print("C:\M106-dos\M106DosDoc.dll")
                elif i == "exit":
                    break
                elif i== "BIOS":
                    print("1=IPV4,2=IPV6,3=Safe Mode,4=Safe Mode with Network;")
                    sd = int(input(":"))
                    print("Loading M106-dos-------------")
                    time.sleep(2)
                    print("'exit'can finish BIOS.")
                    sf = input()
                    if sf == "exit":
                        pass
                elif i == "system":
                    print("C:\M106-dos\ ")
                elif i == "run":
                    print("\033[33m运行窗口:")
                    time.sleep(0.2)
                    i = input("你可以输入'explorer'去浏览电脑里的文件，但不能删除、更改；\n'return'可以返回第一页\n  'off'可以关闭M106-DOS；\n'reset'可以修复你的M106-DOS并且重启M106-DOS；\n 你可以输入'all'去使用Apps\n请选择:\033[0m")
                    if i == "explorer":
                        print("C:\ ")
                        d = input("下一步:")
                        time.sleep(0.2)
                        print("C:\ ",d)
                        s = input("下一步:")
                        print("C:\ ",d,space,s)
                        f = input("下一步:")
                        print("C:\ ",d,space,s,space,f)
                        g = input("下一步:")
                        print("C:\ ",d,space,s,space,f,space,g)
                        a = input("下一步:")
                        print("C:\ ",d,space,s,space,f,space,g,space,a)
                    elif i == "return":
                        pass
                    elif i == "all":
                        n = int(input("1=计算器 2=返回："))
                        if n == 1:
                            print("1=+、2=-、3=x、4=/")
                            i = input(":")
                            first = int(input("第一个数"))
                            second = int(input("第二个数"))
                            if i == "1":
                                print(first+second)
                            elif i == "2":
                                print(first-second)
                            elif i == "3":
                                print(first*second)
                            elif i == str(4):
                                print(first/second)
                        else:
                            pass
                    elif i == "off":
                        break 
                    elif i == "reset":
                        pass
else:
    print()
