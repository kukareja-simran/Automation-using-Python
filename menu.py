#!/usr/bin/python3

import os
os.system("clear")
while True:
        os.system("clear")
        os.system("tput setaf  2")
        print("\t\t=====================================================")
        os.system("tput setaf  4")
        os.system("tput bold")
        print("\t\t\t*******Automation Using Python*******\t\t")
        os.system("tput setaf  1")
        print("\t\t=====================================================")
        os.system("tput setaf  7")

        print("""
        \n
       \t\t\t\t Press 1  : Docker
       \t\t\t\t Press 2  : AWS
       \t\t\t\t Press 3  : LVM
       \t\t\t\t Press 4  : Hadoop Cluster
       \t\t\t\t Press 5  : Python interpreter
       \t\t\t\t Press 6  : Remote Server
       \t\t\t\t Press 7  : Webserver
       \t\t\t\t Press 8  : Linux Commands
       \t\t\t\t Press 0  : Exit
        """)
        ch  = input("\t\t\t\tEnter your Choice: ")
        os.system("clear")
        if int(ch) == 1:
             os.system("python3 docker.py")
        elif int(ch) == 2:
             os.system("python3 aws.py")
        elif int(ch) == 3:
             os.system("python3 lvm.py")
        elif int(ch) == 4:
             os.system("python3 hadoop1.py")
        elif int(ch) == 5:
             os.system("python3 py_interpreter.py")
        elif int(ch) == 6:
             os.system("python3 ssh.py")
        elif int(ch) == 7:
            print("Configuring Web server...")
            os.system("yum install httpd -y")
            os.system("systemctl start httpd")
            os.system("cp index.html /var/www/html/")
            os.system("systemctl stop firewalld")
            os.system("setenforce 0")
            os.system("firefox")
        elif int(ch) == 8:
            while True:
                os.system("tput setaf 3")
                print("\t\t=======================================================================")
                os.system("tput setaf  2")
                print("\t\t\t********************Linux Automation********************\t\t")
                os.system("tput setaf  6")
                print("\t\t=======================================================================")
                os.system("tput setaf 7")
                print("\t\t\t\tWelcome to linux terminal...")
                print("""
                \t\tPress 1 : Linux Command
                \t\tPress 2 : Go abck to main menu
                """)
                cmd = input("\t\t\t\tEnter your choice: ")
                if int(cmd) == 1:
                    command = input("\t\t\t\tEnter linux command: ")
                    os.system("{0}".format(command))
                elif int(cmd) == 2:
                    break
        elif int(ch) == 0:
            exit()
        else:
            print("Try again")









