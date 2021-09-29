import json
import os
import sys
import time
import shutil
import locale
#-----------------------


def turn(file):
    with open(file,mode='r',encoding='utf-8') as f:
        a=f.readline()
        a=a.split('","')
        b=[]
        for i in range(len(a)):
            if i <= len(a)-2:
                b.append(json.loads(a[i]))
        return b
def saveToJSON(dicObject,file):
    flag=False
    '''if type(dicObject)!=dict:
        print('dict')
        return flag'''
    try:
        j_file=open("./PyDB/"+file,'a')
        json.dump(dicObject,j_file,ensure_ascii=False)
        flag=True
    except:
        print('写数据出错!')
    finally:
        if flag:
            j_file.close()
    return flag
#=========================
def GetFromJSON(filename):
    flag=False
    dicObject={}
    try:
        way="./PyDB/"+filename
        j_file=open(way,'r')
        dicObject=json.load(j_file)
        flag=True
    except:
        flag=False
    finally:
        if flag:
            j_file.close()
        elif flag==False:
            return False
    return dicObject

#----------------------------------------
def DBhelp():
    if language=="English":
        print("Command list:")
        print("|Command             |Explain                                         |")
        print("-----------------------------------------------------------------------")
        print("|@choose             |Choose a database to use.                       |")
        print("|@create table       |Generate a table under the current database.    |")

        if host["Jurisdiction"]=="Root" or host["Jurisdiction"]=="Hang Jiayu":
            print("|@create user        |Create a new user.                              |")
        print("|@c or @continue     |Clear the current input statement.              |")
        print("|@create database    |Create a database according to the boot.        |")
        print("|@del table          |Delete a table.                                 |")
        print("|@del database       |Delete a database.                              |")
        print("|@exit               |Exit the program.                               |")
        print("|@h or @help         |Get the command list.                           |")
        print("|@insert             |Insert data into a table.                       |")
        print("|@show users         |View all users.                                 |")
        print("|@show tables        |View tables under the current database.         |")
        print("|@show database      |View the database under the current user.       |")
        print("|@query              |Query data in the selected table.               |")
        print()
    elif language=="中文":
        print("指令列表:")
        print("|指令                 |功能                                             |")
        print("-----------------------------------------------------------------------")
        print("|@choose             |选择一个进行操作的数据库。                            |")
        print("|@create table       |在当前数据库下创建一个表格。                          |")

        if host["Jurisdiction"]=="Root" or host["Jurisdiction"]=="Hang Jiayu":
            print("|@create user        |创建一个新用户。                                   |")
        print("|@c or @continue     |清除当前输入的语句。                                |")
        print("|@create database    |创建一个数据库。                                   |")
        print("|@del table          |创建一个表格。                                     |")
        print("|@del database       |删除数据库。                                       |")
        print("|@exit               |退出程序。                                        |")
        print("|@h or @help         |获取指令列表。                                     |")
        print("|@insert             |将数据插入表格。                                   |")
        print("|@show users         |获取所有用户。                                     |")
        print("|@show tables        |获取当前数据库下所有表格。                           |")
        print("|@show database      |获取当前数据库下所有数据库。                          |")
        print("|@query              |在选择的表格中查询数据。                             |")
        print()





#----------------------------------------
if __name__ == '__main__':

    folder=''
    a=locale.getdefaultlocale()
    if not "PyDB" in os.listdir():
        os.makedirs('./PyDB'+'./user')
        os.makedirs('./PyDB'+'./DataBase')
        os.makedirs("./PyDB"+"./Language")
        if a[0]=='en_US':
            b={"Language":"English"}
            with open("PyDB/Language/language.json",'w') as j_file:
                json.dump(b,j_file,ensure_ascii=False)
        elif a[0]=="zh_CN":
            b={"Language":"English"}
            with open("PyDB/Language/language.json",'w') as j_file:
                json.dump(b,j_file,ensure_ascii=False)


    if "PyDB" in os.listdir():
        language=GetFromJSON("Language/language.json")
        if language["Language"]=='English':
            print("| Welcome to PyDB Monitor.")
            print("| Server version: 1.0.0 PyDB Server.")
            print("| Add '@' at the beginning of the statement.")
            print("| Type '@help' or '@h' for help.Type '@continue' or '@c' to clear the current input statement.\n")
            print("PyDB>Welcome to PyDB!"+"\n")
        elif language["Language"]=="中文":
            print("| 欢迎使用PyDB.")
            print("| 服务版本: 1.0.0 PyDB Server.")
            print("| 在每行语句前添加 '@' 。")
            print("| 输入 '@help' 或 '@h' 获取帮助。输入 '@continue' 或 '@c' 清除当前输入的语句。\n")
            print("提示>欢迎使用PyDB!"+"\n")

    #----------------------------------------------------Sing in
    while True:
        language=GetFromJSON("Language/language.json")
        if language["Language"]=="English":
            if not "PyDB" in os.listdir():
                language=input("PyDB>Please choose your language.(English/中文)\nLanguage>")
                if language=="English":
                    a={"Language":language}
                    saveToJSON(a,"Language/language.json")
                    j_file=open("./PyDB/Language/language.json",'w')
                    json.dump(a,j_file,ensure_ascii=False)
                    j_file.close()
                    print("PyDB> There are no users yet :( ...  Let's create one! :) \n")
                    admin=input("PyDB>  Please enter your User Name!\nAdministrator>")
                    Pass=input("PyDB> Please enter your password!\nPassword>")
                    RePass=input("PyDB> Please enter your password again!\nPassword>")
                    if Pass==RePass:
                        info={
                            'Name':admin,'Password':Pass,'Jurisdiction':'Root'
                        }
                        saveToJSON(info,'user/'+admin+'.json')
                        print("\nSuccess>Congratulations, account creation succeeded!\n")
                        host=GetFromJSON("user/"+admin+".json")
                        os.makedirs('./PyDB'+'./DataBase'+'./'+admin)
                        break
                    else:
                        while True:
                            print('PyDB>The two passwords you entered are different. Please try again.')
                            Pass=input("PyDB> Please enter your password!\nPassword>")
                            RePass=input("PyDB> Please enter your password again!\nPassword>")
                            if Pass==RePass:
                                info={
                                    'User':admin,'Password':Pass,'Jurisdiction':'Root'
                                }
                                saveToJSON(info,'user/'+admin+'.json')
                                print("\nSuccess>Congratulations, account creation succeeded!\n")
                                host=GetFromJSON("user/"+admin+".json")
                                os.makedirs('./PyDB'+'./DataBase'+'./'+admin)
                                break
                            break
                elif language=="中文":
                    a={"Language":language}
                    saveToJSON(a,"Language/language.json")
                    j_file=open("./PyDB/Language/language.json",'w')
                    json.dump(a,j_file,ensure_ascii=False)
                    j_file.close()
            else:
                if language=="English":
                    while True:
                        admin=input('User name>')
                        if admin=="@exit":
                            print("PyDB>Thank you for your use~ :) Bye!")
                            time.sleep(3)
                            sys.exit()
                        user_n=os.listdir("PyDB/user/")
                        yesorno=False
                        for i in user_n:
                            if GetFromJSON("user/"+i)["Name"]==admin:
                                yesorno=True
                                break
                        if yesorno!=True:
                            print("Error>Sorry, there is no such user.Please try again.")
                        else:
                            host=GetFromJSON("user/"+admin+".json")
                            break
                    Pass=input('Password>')
                    if Pass=="@exit":
                        print("PyDB>Thank you for your use~ :) Bye!")
                        time.sleep(3)
                        sys.exit()
                    if host["Password"]!=Pass:
                        print("Error>Password error, please try again!")
                        Pass=input('Password>')
                        host=GetFromJSON("user/"+admin+".json")
                        if host["Password"]!=Pass:
                            print("Error>Password error, please try again!")
                            Pass=input('Password>')
                            host=GetFromJSON("user/"+admin+".json")
                            if host['Password']!=Pass:
                                print("Error>You have made three consecutive errors. Please try again later.")
                                time.sleep(3)
                                sys.exit()
                            else:
                                print("\n"+"PyDB>Welcome,"+admin+'!\n')
                                break
                        else:
                            print("\n"+"PyDB>Welcome,"+admin+'!\n')
                            break
                    else:
                        print("\n"+"PyDB>Welcome,"+admin+'!\n')
                        break



                elif language=="中文":
                    while True:
                        admin=input('用户名>')
                        if admin=="@exit":
                            print("提示>感谢您的使用~ :) 再见!")
                            time.sleep(3)
                            sys.exit()
                        user_n=os.listdir("PyDB/user/")
                        yesorno=False
                        for i in user_n:
                            if GetFromJSON("user/"+i)["Name"]==admin:
                                yesorno=True
                                break
                        if yesorno!=True:
                            print("错误>没有这个用户，请重试！")
                        else:
                            host=GetFromJSON("user/"+admin+".json")
                            break
                    Pass=input('密码>')
                    if Pass=="@exit":
                        print("提示>T感谢您的使用~ :) 再见!")
                        time.sleep(3)
                        sys.exit()
                    if host["Password"]!=Pass:
                        print("错误>密码错误，请重试！")
                        Pass=input('密码>')
                        host=GetFromJSON("user/"+admin+".json")
                        if host["Password"]!=Pass:
                            print("错误>密码错误，请重试！")
                            Pass=input('密码>')
                            host=GetFromJSON("user/"+admin+".json")
                            if host['Password']!=Pass:
                                print("错误>您已经连续三次密码错误，请稍后再试！")
                                time.sleep(3)
                                sys.exit()
                            else:
                                print("\n"+"提示>欢迎回来,"+admin+'!\n')
                                break
                        else:
                            print("\n"+"提示>欢迎回来,"+admin+'!\n')
                            break
                    else:
                        print("\n"+"提示>欢迎回来,"+admin+'!\n')
                        break


        elif language["Language"]=="中文":
            if len(os.listdir('./PyDB/user'))==0:
                language=input("提示>请选择您的语言！(English/中文)\n语言>")




                if language=="English":
                    a={"Language":"English"}
                    saveToJSON(a,"Language/language.json")
                    j_file=open("./PyDB/Language/language.json",'w')
                    json.dump(a,j_file,ensure_ascii=False)
                    j_file.close()
                    print("PyDB> There are no users yet :( ...  Let's create one! :) \n")
                    admin=input("PyDB>  Please enter your User Name!\nAdministrator>")
                    Pass=input("PyDB> Please enter your password!\nPassword>")
                    RePass=input("PyDB> Please enter your password again!\nPassword>")
                    if Pass==RePass:
                        info={
                            'Name':admin,'Password':Pass,'Jurisdiction':'Root'
                        }
                        saveToJSON(info,'user/'+admin+'.json')
                        print("\nSuccess>Congratulations, account creation succeeded!\n")
                        host=GetFromJSON("user/"+admin+".json")
                        os.makedirs('./PyDB'+'./DataBase'+'./'+admin)
                        break
                    else:
                        while True:
                            print('PyDB>The two passwords you entered are different. Please try again.')
                            Pass=input("PyDB> Please enter your password!\nPassword>")
                            RePass=input("PyDB> Please enter your password again!\nPassword>")
                            if Pass==RePass:
                                info={
                                    'User':admin,'Password':Pass,'Jurisdiction':'Root'
                                }
                                saveToJSON(info,'user/'+admin+'.json')
                                print("\nSuccess>Congratulations, account creation succeeded!\n")
                                host=GetFromJSON("user/"+admin+".json")
                                os.makedirs('./PyDB'+'./DataBase'+'./'+admin)
                                break
                            break




                elif language=="中文":
                    print("提示> 暂时还没有用户 :( ...  让我们来创建一个吧！ :) \n")
                    admin=input("提示>  请输入用户名！\n管理员>")
                    Pass=input("提示> 请输入密码！\n密码>")
                    RePass=input("提示> 请再次输入密码！\n密码>")
                    if Pass==RePass:
                        info={
                            'Name':admin,'Password':Pass,'Jurisdiction':'Root'
                        }
                        saveToJSON(info,'user/'+admin+'.json')
                        print("\n成功>恭喜，成功创建用户！\n")
                        host=GetFromJSON("user/"+admin+".json")
                        os.makedirs('./PyDB'+'./DataBase'+'./'+admin)
                        break
                    else:
                        while True:
                            print('提示>两次输入的密码不一致，请重试！')
                            Pass=input("提示> 请输入密码！\n密码>")
                            RePass=input("提示> 请再次输入密码！\n密码>")
                            if Pass==RePass:
                                info={
                                    'User':admin,'Password':Pass,'Jurisdiction':'Root'
                                }
                                saveToJSON(info,'user/'+admin+'.json')
                                print("\n成功>恭喜，成功创建用户！\n")
                                host=GetFromJSON("user/"+admin+".json")
                                os.makedirs('./PyDB'+'./DataBase'+'./'+admin)
                                break
                            break



                else:
                    if language=="中文":
                        while True:
                            admin=input('用户名>')
                            if admin=="@exit":
                                print("提示>感谢您的使用~ :) 再见!")
                                time.sleep(3)
                                sys.exit()
                            user_n=os.listdir("PyDB/user/")
                            yesorno=False
                            for i in user_n:
                                if GetFromJSON("user/"+i)["Name"]==admin:
                                    yesorno=True
                                    break
                            if yesorno!=True:
                                print("错误>没有这个用户，请重试！")
                            else:
                                host=GetFromJSON("user/"+admin+".json")
                                break
                        Pass=input('密码>')
                        if Pass=="@exit":
                            print("提示>T感谢您的使用~ :) 再见!")
                            time.sleep(3)
                            sys.exit()
                        if host["Password"]!=Pass:
                            print("错误>密码错误，请重试！")
                            Pass=input('密码>')
                            host=GetFromJSON("user/"+admin+".json")
                            if host["Password"]!=Pass:
                                print("错误>密码错误，请重试！")
                                Pass=input('密码>')
                                host=GetFromJSON("user/"+admin+".json")
                                if host['Password']!=Pass:
                                    print("错误>您已经连续三次密码错误，请稍后再试！")
                                    time.sleep(3)
                                    sys.exit()
                                else:
                                    print("\n"+"提示>欢迎回来,"+admin+'!\n')
                                    break
                            else:
                                print("\n"+"提示>欢迎回来,"+admin+'!\n')
                                break
                        else:
                            print("\n"+"提示>欢迎回来,"+admin+'!\n')
                            break
                    if language=="English":
                        while True:
                            admin=input('User name>')
                            if admin=="@exit":
                                print("PyDB>Thank you for your use~ :) Bye!")
                                time.sleep(3)
                                sys.exit()
                            user_n=os.listdir("PyDB/user/")
                            yesorno=False
                            for i in user_n:
                                if GetFromJSON("user/"+i)["Name"]==admin:
                                    yesorno=True
                                    break
                            if yesorno!=True:
                                print("Error>Sorry, there is no such user.Please try again.")
                            else:
                                host=GetFromJSON("user/"+admin+".json")
                                break
                        Pass=input('Password>')
                        if Pass=="@exit":
                            print("PyDB>Thank you for your use~ :) Bye!")
                            time.sleep(3)
                            sys.exit()
                        if host["Password"]!=Pass:
                            print("Error>Password error, please try again!")
                            Pass=input('Password>')
                            host=GetFromJSON("user/"+admin+".json")
                            if host["Password"]!=Pass:
                                print("Error>Password error, please try again!")
                                Pass=input('Password>')
                                host=GetFromJSON("user/"+admin+".json")
                                if host['Password']!=Pass:
                                    print("Error>You have made three consecutive errors. Please try again later.")
                                    time.sleep(3)
                                    sys.exit()
                                else:
                                    print("\n"+"PyDB>Welcome,"+admin+'!\n')
                                    break
                            else:
                                print("\n"+"PyDB>Welcome,"+admin+'!\n')
                                break
                        else:
                            print("\n"+"PyDB>Welcome,"+admin+'!\n')
                            break





    jurisdiction=host["Jurisdiction"]
    maindatabase=''



    #-----------------------------------------------------------Console(English)
    if language=="English":
        while True:
            user_e=input('PyDB>')
            User_database_path="PyDB/DataBase/"+admin

            #----------------------------------------------Help
            if user_e=='@h' or user_e=='@help':
                DBhelp()
            #----------------------------------------------continue
            if user_e=='@c' or user_e=='@continue':
                continue
            #----------------------------------------------Exit
            elif user_e=='@exit':
                print("PyDB>Thank you for your use~ :) Bye!")
                time.sleep(3)
                sys.exit()
            #----------------------------------------------Choose Database
            elif user_e=='@choose':
                maindatabase=input('Select>')
                find=os.listdir(User_database_path)
                yesorno=False
                for i in find:
                    if i==maindatabase:
                        yesorno=True
                if yesorno==False:
                    print("Error>This database does not exist.\n")
                else:
                    print('PyDB>Database changed.\n')
            #----------------------------------------------Show Database
            elif user_e=="@show database":
                database_num=os.listdir(User_database_path)
                databases=''
                if database_num==[]:
                    print("PyDB>There is no database yet. Use '@create database' to create one!\n")
                else:
                    for i in range(len(database_num)):
                        if i<len(database_num)-1:
                            databases+=database_num[i]+','
                        else:
                            databases+=database_num[i]
                    print(" | "+databases+' |')
            #----------------------------------------------Create Database
            elif user_e=="@create database":

                database_num=os.listdir(User_database_path)
                basename=input("PyDB>Please enter the Name of the Database.\nCreate>")
                os.makedirs('./PyDB'+'./DataBase'+'./'+admin+'./'+basename)
                print("Success>Database creation succeeded!\n")
            #----------------------------------------------Create Table
            elif user_e=="@create table":
                if maindatabase=='':
                    print("PyDB>Please choose a database first!\n")
                else:
                    tablename=input('PyDB>Please enter the name of the table.\nCreate>')
                    database_path=os.listdir('PyDB/Database/'+admin+'/'+maindatabase)
                    yesorno=False
                    for i in database_path:
                        i=i.replace(".json",'')
                        if i==tablename:
                            yesorno=True
                    if yesorno==True:
                        print("Error>This table already exists.\n")
                    else:
                        columns=input("PyDB>Please enter the title of each column.\nCreate>")
                        columns=columns.split(',')
                        column_dict={}
                        for i in range(len(columns)):
                            column_dict.setdefault(str(i+1),columns[i])
                        print("Success>Successfully created the table!\n")
                        saveToJSON(column_dict,'Database/'+admin+'/'+maindatabase+'/'+tablename+'.json')
                        saveToJSON(',','Database/'+admin+'/'+maindatabase+'/'+tablename+'.json')
            #----------------------------------------------show tables
            elif user_e=="@show tables":
                if maindatabase=='':
                    print("PyDB>Please choose a database first!\n")
                else:
                    database_path=os.listdir('PyDB/Database/'+admin+'/'+maindatabase)
                    if database_path==[]:
                        print("PyDB>There is no table yet. Use '@create table' to create one!\n")
                    else:
                        show_tables=''
                        for i in range(len(database_path)):
                            toshow=database_path[i]
                            if i<len(database_path)-1:

                                show_tables+=toshow.replace('.json','')+','
                            else:
                                show_tables+=toshow.replace('.json','')
                        print(' | '+show_tables+' |\n')
            #----------------------------------------------delete database
            elif user_e=="@del database":
                del_base=input("PyDB>Please enter the name of the database to delete.\nDelete>")
                database_path=os.listdir('PyDB/Database/'+admin)
                yesorno=False
                for i in database_path:
                    if i==del_base:
                        yesorno=True
                if yesorno==False:
                    print("Error>This database doesn't exists.\n")
                else:
                    database_path=os.listdir('PyDB/Database/'+admin+'/'+del_base)
                    if database_path==[]:
                        if maindatabase==del_base:
                            maindatabase=''
                        os.rmdir('PyDB/Database/'+admin+'/'+del_base)
                        print("Success> Successfully deleted this database!\n")
                    else:
                        while True:
                            sure=input("\nPyDB>Are you sure to delete?This database is not empty!(Y/N)\nDelete>")
                            if sure=='Y' or sure=='y':
                                shutil.rmtree('PyDB/Database/'+admin+'/'+del_base)
                                print('Success> Successfully deleted this database!')
                                if maindatabase==del_base:
                                    maindatabase=''
                                break
                            elif sure=='N' or sure=='n':
                                print('PyDB> Cancel deletion.\n')
                                break
            #----------------------------------------------insert data
            elif user_e=="@insert":
                if maindatabase=='':
                    print("PyDB>Please choose a database first!")
                else:
                    insert_table=input("PyDB>Please choose a table.\nInsert>")
                    find=os.listdir(User_database_path+'/'+maindatabase)
                    yesorno=False
                    for i in find:
                        if i==insert_table+'.json':
                            yesorno=True
                    if yesorno==False:
                        print("Error>Sorry, this form does not exist.\n")
                    else:
                        toshow=turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json')[0]
                        toshow=str(toshow).replace('{','')
                        toshow=toshow.replace('}','')
                        toshow=toshow.replace("'",'')
                        print("PyDB>The titles of the columns are |"+toshow+'|.')
                        toinsert=input("PyDB>Please enter the data to insert!\nInsert>")
                        toinsert=toinsert.split(',')
                        toshow=turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json')[0]
                        listshow=list(toshow)
                        tosave={}
                        if len(toinsert)==len(listshow):
                            for i in range(len(list(toshow))):
                                head=toshow[listshow[i]]
                                tosave.setdefault(head,toinsert[i])
                            waytos=input("PyDB>Please choose the way to insert!\nInsert>")
                            if waytos=='end':
                                try:
                                    saveToJSON(tosave,'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    print("Success>Successfully inserted data!\n")
                                except:
                                    print("Error>There is some thing wrong with saving it!\n")
                            elif waytos=='top':
                                try:
                                    lastin=turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json')
                                    with open(User_database_path+'/'+maindatabase+'/'+insert_table+'.json',mode='w',encoding='utf-8') as f:
                                        json.dump(lastin[0],f)
                                        lastin.pop(0)
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(tosave,'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    for i in range(len(lastin)):
                                        saveToJSON(lastin[i],'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                        saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    print("Success>Successfully inserted data!\n")
                                except:
                                    print("Error>There is some thing wrong with saving it!\n")
                            elif len(turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json'))==int(waytos):
                                try:
                                    saveToJSON(tosave,'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    print("Success>Successfully inserted data!\n")
                                except:
                                    print("Error>There is some thing wrong with saving it!\n")
                            elif int(waytos)==1:
                                try:
                                    lastin=turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json')
                                    with open(User_database_path+'/'+maindatabase+'/'+insert_table+'.json',mode='w',encoding='utf-8') as f:
                                        json.dump(lastin[0],f)
                                        lastin.pop(0)
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(tosave,'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    for i in range(len(lastin)):
                                        saveToJSON(lastin[i],'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                        saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    print("Success>Successfully inserted data!\n")
                                except:
                                    print("Error>There is some thing wrong with saving it!\n")
                            elif 1<int(waytos)<len(turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json')):
                                inwaytos=int(waytos)
                                try:
                                    lastin=turn(User_database_path+'/'+maindatabase+'/'+insert_table+'.json')
                                    with open(User_database_path+'/'+maindatabase+'/'+insert_table+'.json',mode='w',encoding='utf-8') as f:
                                        json.dump(lastin[0],f)
                                        for i in range(inwaytos):
                                            lastin.pop(i)
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(tosave,'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    for i in range(len(lastin)):
                                        saveToJSON(lastin[i],'DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                        saveToJSON(',','DataBase/'+admin+'/'+maindatabase+'/'+insert_table+'.json')
                                    print("Success>Successfully inserted data!\n")
                                except:
                                    print("Error>There is some thing wrong with saving it!\n")
                        else:
                            print('Error>The information entered is incorrect!\n')
            #----------------------------------------------delete table
            elif user_e=="@del table":
                if maindatabase=='':
                    print("PyDB>Please choose a database first!\n")
                    continue
                del_base=input("PyDB>Please enter the name of the table to delete.\nDelete>")
                del_base=del_base+'.json'
                database_path=os.listdir('PyDB/Database/'+admin+'/'+maindatabase)
                yesorno=False
                for i in database_path:
                    if i==del_base:
                        yesorno=True
                if yesorno==False:
                    print("Error>This table doesn't exists.\n")
                else:
                    while True:
                        sure=input("\nPyDB>Are you sure to delete?(Y/N)\nDelete>")
                        if sure=='Y' or sure=='y':
                            os.remove('PyDB/Database/'+admin+'/'+maindatabase+'/'+del_base)
                            print('Success> Successfully deleted this table!\n')
                            break
                        elif sure=='N' or sure=='n':
                            print('PyDB> Cancel deletion.\n')
                            break
                    #----------------------------------------------create user
            elif user_e=='@create user':
                if jurisdiction=='Root' or jurisdiction=='Hang Jiayu':
                    a=''
                else:
                    print("PyDB>Sorry, your permission is not enough!\n")
                    continue
                user_name=input("PyDB>Please enter the name,the password and the jurisdiction of the user!\nCreate>")
                user_name=user_name.split(',')
                if len(user_name)!=3:
                    print("Error>Wrong information entered!\n")
                yesorno=False
                for i in range(1):
                    if user_name[2]=='Admin' or user_name=='Simple' or user_name=="Administrator":
                        yesorno=True
                    if user_name=="Root" or user_name=='root':
                        yesorno=False
                        print("Error>Sorry, you can't create a root user.\n")
                        continue
                if yesorno==False:
                    print("Error>Wrong information entered!\n")
                    continue
                repass=input("PyDB>Please enter the password again!\nCreate>")
                if repass!=user_name[1]:
                    print("Error>The passwords entered twice are inconsistent!\n")
                    continue
                yesorno=False
                for i in os.listdir('PyDB/user'):
                    if i.replace('.json','')==user_name[0]:
                        print("Error>This user already exists!\n")
                        yesorno=True
                        break
                if yesorno==True:
                    continue
                new_user={
                    "Name":user_name[0],"Password":user_name[1],'Jurisdiction':user_name[2]
                }
                saveToJSON(new_user,'user/'+user_name[0]+'.json')
                print("Success>Successfully created new user!\n")
            #----------------------------------------------show users
            elif user_e=="@show users":
                users=''
                for i in os.listdir("PyDB/user"):
                    users+='| '+i.replace('.json','')+' '
                print(users+'|\n')
            #----------------------------------------------query data
            elif user_e=="@query":
                if maindatabase=='':
                    print("PyDB>Please choose a database first!\n")
                    continue
                e_s_d=input("PyDB>Please enter the table to query.\nQuery>")
                yesorno=False
                for i in os.listdir(User_database_path+'/'+maindatabase):
                    if i==e_s_d+'.json':
                        yesorno=True
                if yesorno==False:
                    print("Error>This table doesn't exists.\n")
                    continue
                show_data=turn(User_database_path+'/'+maindatabase+'/'+e_s_d+'.json')
                lenvalue=[]
                waytoquery=input("PyDB>Please enter the query method.\nQuery>")
                if waytoquery=='*':
                    for i in range(len(show_data)):
                        ti=0
                        for h in show_data[i]:

                            if i==0:
                                lenvalue.append(0)
                            if len(show_data[i][h])>lenvalue[ti]:
                                lenvalue[ti]=len(show_data[i][h])
                            ti+=1
                    yesorno=False
                    print()
                    for i in range(len(show_data)):
                        head=''
                        body=''
                        ti=0
                        for h in show_data[i]:
                            if i == 0:
                                yesorno=True
                                head+='  | '+show_data[i][h]+(lenvalue[ti]+1-len(show_data[i][h]))*' '
                            else:
                                body+="  | "+show_data[i][h]+(lenvalue[ti]+1-len(show_data[i][h]))*' '
                            ti+=1
                        if yesorno==True:
                            print(head+'|')
                            print('  '+(len(head)-1)*'-')
                            yesorno=False
                        else:
                            print(body+'|')
                    print()
                else:
                    waytoquery=waytoquery.split(',')
                    if len(waytoquery)!=2:
                        print("Error>The input data is incorrect!\n")
                        continue
                    else:
                        if waytoquery[0]=="*":
                            testlen=[]
                            for i in range(len(show_data)):
                                ti=0
                                yesornoB=False
                                for h in show_data[i]:
                                    if i==0:
                                        lenvalue.append(0)
                                        testlen.append(0)
                                    if len(show_data[i][h])>lenvalue[ti]:
                                        testlen[ti]=len(show_data[i][h])
                                    if show_data[i][h]==waytoquery[1]:
                                        yesornoB=True
                                    ti+=1
                                    if yesornoB==True:
                                        lenvalue=testlen
                            yesorno=False
                            print()
                            for i in range(len(show_data)):
                                head=''
                                body=''
                                ti=0
                                yesornoB=False
                                for h in show_data[i]:
                                    if i == 0:
                                        yesorno=True
                                        head+='  | '+show_data[i][h]+(lenvalue[ti]+1-len(show_data[i][h]))*' '
                                    else:
                                        body+="  | "+show_data[i][h]+(lenvalue[ti]+1-len(show_data[i][h]))*' '
                                    ti+=1
                                    if show_data[i][h]==waytoquery[1]:
                                        yesornoB=True

                                if yesorno==True:
                                    print(head+'|')
                                    print('  '+(len(head)-1)*'-')
                                    yesorno=False
                                elif yesornoB==True:
                                    print(body+'|')
                            if yesornoB==False:
                                print("  |Nothing here...|")
                            print()

            #----------------------------------------------change data

