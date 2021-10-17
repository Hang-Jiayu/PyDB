import os
import shutil
import base64

#=======================================================
class PyDB():
    def __init__(self):
        self.__main_db=''
        self.__user=''

        if not "PyDB" in os.listdir("D:/"):
            try:
                os.makedirs("D:/"+"./PyDB"+"./Database")
                os.makedirs("D:/"+"./PyDB"+"./user")
                os.makedirs("C:/"+"./Py-Tools"+"./PyDB"+"./version")
                if len(self.__turn("C:/Py-Tools/PyDB/version/version.hjy"))==1:
                    with open("C:/Py-Tools/PyDB/version/version.hjy",mode="w",encoding="gbk") as f:
                        version='{"Py-Tools":"PyDB","Version":"1.0.2"}'
                        by=version.encode("utf-8")
                        t_insert=base64.b64encode(by).decode("utf-8")
                        f.write(t_insert+'%e')
                else:
                    with open("C:/Py-Tools/PyDB/version/version.hjy",mode="a",encoding="gbk") as f:
                        version='{"Py-Tools":"PyDB","Version":"1.0.2"}'
                        by=version.encode("utf-8")
                        t_insert=base64.b64encode(by).decode("utf-8")
                        f.write(t_insert+'%e')
            except:
                try:
                    if len(self.__turn("C:/Py-Tools/PyDB/version/version.hjy"))==1:
                        with open("C:/Py-Tools/PyDB/version/version.hjy",mode="w",encoding="gbk") as f:
                            version='{"Py-Tools":"PyDB","Version":"1.0.2","Database_path":"'+self.__db+'"}'
                            by=version.encode("utf-8")
                            t_insert=base64.b64encode(by).decode("utf-8")
                            f.write(t_insert+'%e')
                    else:
                        with open("C:/Py-Tools/PyDB/version/version.hjy",mode="a",encoding="gbk") as f:
                            version='{"Py-Tools":"PyDB","Version":"1.0.2","Database_path":"'+self.__db+'"}'
                            by=version.encode("utf-8")
                            t_insert=base64.b64encode(by).decode("utf-8")
                            f.write(t_insert+'%e')
                except:
                    self.__db="D:/PyDB"
            self.__db="D:/PyDB"
        self.__db="D:/PyDB"

#--------------------------------------------------
    def __turn(self,file,lengh=None):
        with open("D:/"+file,mode='r',encoding='gbk') as f:
            a=f.readline()
            a=a.split("%e")
            ready=[]
            if lengh==None:
                for i in a:
                    by=i.encode("utf-8")
                    by=base64.b64decode(by).decode("utf-8")
                    try:
                        ready.append(eval(by))
                    except:
                        continue
                return ready
            else:
                if lengh[1]=="*":
                    for i in a:
                        by=i.encode("utf-8")
                        by=base64.b64decode(by).decode("utf-8")
                        try:
                            be_found=eval(by)
                            for i in be_found:
                                if lengh[0] in be_found[i]:
                                    ready.append(be_found)
                        except:
                            continue
                else:
                    times=0
                    for i in a:
                        by=i.encode("utf-8")
                        by=base64.b64decode(by).decode("utf-8")
                        try:
                            be_found=eval(by)
                            for i in be_found:
                                if lengh[0] in be_found[i]:
                                    ready.append(be_found)
                                    times+=1
                        except:
                            continue
                        if times==lengh[1]:
                            break
                return ready

    def __saveToJSON(self,dicObject,file):
        with open("D:/PyDB/"+file,mode='a',encoding="gbk") as f:
            if type(dicObject)!=str:
                dicObject=str(dicObject)
            by=dicObject.encode("utf-8")
            t_insert=base64.b64encode(by).decode("utf-8")
            f.write(t_insert+'%e')
            return True
    #----------------------------------------------
    def __resave(self,dicObject,file)->None:
        with open("D:/PyDB/"+file,mode='w',encoding="gbk") as f:
            if type(dicObject)!=str:
                dicObject=str(dicObject)
            by=dicObject.encode("utf-8")
            t_insert=base64.b64encode(by).decode("utf-8")
            f.write(t_insert+'%e')
        #=======================================================

    def about(self)->None:
        print(" PyDB Details:")
        print(" Server version: 1.0.2 PyDB Server.")
        print(" Copyright @ Hang Jiayu.")
        print(" Powered by @ Hang Jiayu")

    def log_in(self,username:str,password:str)->bool:

        if os.listdir("D:/PyDB/user")==[]:
            self.__saveToJSON("{'Name':'"+username+"','Password':'"+password+"','Jurisdiction':'Root'}","user/"+username+".hjy")
            os.makedirs("D:\PyDB\Database"+".\\"+username)
            self.__user={"Name":username,"Password":password,"Jurisdiction":'Root'}
        else:
            self.__T_O_F=False
            for i in os.listdir(self.__db+r"\user"):
                if i[0]!="#":
                    u=self.__turn("PyDB\\user\\"+i)[0]
                    if u["Name"]==username:
                        if u["Password"]==password:
                            self.__T_O_F=True
                            break
            if self.__T_O_F==True:
                self.__user=u
        return True

    def ch_db(self,database:str)->bool:
        if not self.__user=='':
            self.__T_O_F=False
            if database in os.listdir(self.__db+"\Database\\"+self.__user["Name"]):
                self.__T_O_F=True
                self.__main_db=database
                return True
            else:
                return False
        else:
            return False

    def cr_db(self,database:str)->bool:
        if not self.__user=='':
            if database not in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]):
                os.makedirs(self.__db+"\Database\\"+self.__user["Name"]+"\\"+'./'+database)
                return True
            else:
                return False
        else:
            return False

    def Clean_db(self,databasename:str)->bool:
        if not self.__user=='':
            if databasename in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]):
                shutil.rmtree("D:/PyDB/DataBase/"+self.__user["Name"]+"/"+databasename)
                return True
            else:
                return False
        else:
            return False

    def sh_db(self)->bool or list:
        if not self.__user=='':
            a=os.listdir(self.__db+"\Database\\"+self.__user["Name"])
            for i in range(len(a)):
                if "#" in a[i][0]:
                    a.pop(i)
            return a
        else:
            return False

    def sh_tb(self)->bool or list:
        if not self.__user=='':
            a=os.listdir(self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db)
            for i in range(len(a)):
                a[i]=a[i].replace(".hjy",'')
                if "#" in a[i][0]:
                    a.pop(i)
            return a
        else:
            return False

    def cr_tb(self,name:str,lengh:list)->bool:
        if not self.__user=='':
            if self.__main_db!='':
                if lengh!=[]:
                    if not name+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                        a={}
                        for i in range(len(lengh)):
                            a.setdefault(lengh[i],lengh[i])
                        self.__resave(str(a),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+name+'.hjy')
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

    def Clean_tb(self,tablename:str)->bool:
        if not self.__user=='':
            if self.__main_db!='':
                if tablename+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                    os.remove("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+".hjy")
                    return True
                else:
                    return False
        else:
            return False

    def query(self,tablename:str,mode:str or int=None,lengh:list=None)->bool or list:
        if not self.__user=='':
            if self.__main_db!='':
                if tablename+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                    if mode==None:
                        a=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                        a.pop(0)
                        return a
                    else:
                        try:
                            a=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy',[lengh,mode])
                            a.pop(0)
                            return a
                        except:
                            return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def insert(self,tablename:str,listobject:list,mode:str or int=None)->bool:
        if not self.__user=='':
            if self.__main_db!='':
                if listobject!=[]:
                    if tablename+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                        head=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')[0]
                        long=0
                        for i in head:
                            long+=1
                        if long==len(listobject) and type(listobject)==list and type(mode)==str or int:
                            long=0
                            heads={}
                            for i in head:
                                heads.setdefault(head[i],listobject[long])
                                long+=1
                            dictobject=str(heads)


                            if mode==None or mode=="end":
                                self.__saveToJSON(dictobject,"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True

                            elif mode=="top":
                                body=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                self.__resave(str(body[0]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                self.__saveToJSON(dictobject,"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                body.pop(0)

                                for i in body:
                                    self.__saveToJSON(str(i),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True

                            else:
                                try:
                                    locate=int(mode)
                                    if 0<locate<len(self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')):
                                        body=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                        self.__resave(str(body[0]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                        body=body.pop(0)
                                        for i in range(len(body)):
                                            if i+1==locate:
                                                self.__saveToJSON(dictobject,"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                            self.__saveToJSON(i,"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    else:
                                        return False
                                except:
                                    return False

                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def del_db(self,databasename:str)->bool:
        if self.__user!='':
            y_o_n=False
            for i in os.listdir(self.__db+"\Database\\"+self.__user["Name"]):
                if databasename in i:
                    if not "#" in i[0]:
                        y_o_n=True
            if y_o_n==True:
                os.rename(self.__db+"\Database\\"+self.__user["Name"]+"\\"+databasename,self.__db+"\Database\\"+self.__user["Name"]+"\#"+databasename)
                return True
            else:
                return False
        else:
            return False

    def del_tb(self,tablename:str)->bool:
        if self.__user!='' and self.__main_db!='':
            y_o_n=False
            for i in os.listdir(self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db):
                if tablename+".hjy" in i:
                    if not "#" in i:
                        y_o_n=True
            if y_o_n==True:
                os.renames(self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db+"\\"+tablename+".hjy",self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db+"\\"+"#"+tablename+".hjy")
                return True
            else:
                return False
        else:
            return False

    def rec_db(self,databasename:str)->bool:
        if self.__user!='':
            y_o_n=False
            for i in os.listdir(self.__db+"\Database\\"+self.__user["Name"]):
                if databasename in i:
                    if "#"+databasename==i:
                        y_o_n=True
            if y_o_n==True:
                os.rename(self.__db+"\Database\\"+self.__user["Name"]+"\\#"+databasename,self.__db+"\Database\\"+self.__user["Name"]+"\\"+databasename)
                return True
            else:
                return False
        else:
            return False

    def rec_tb(self,tablename:str)->bool:
        if self.__user!='':
            y_o_n=False
            for i in os.listdir(self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db):
                if tablename+".hjy" in i:
                    if "#"+tablename+".hjy"==i:
                        y_o_n=True
            if y_o_n==True:
                os.renames(self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db+"\\#"+tablename+".hjy",self.__db+"\Database\\"+self.__user["Name"]+"\\"+self.__main_db+"\\"+tablename+".hjy")
                return True
            else:
                return False
        else:
            return False

    def ch_data(self,tablename:str,newdata:list,olddict:list=None,oldstr:list=None,index:list=None,mode:int=None)->bool:
        if not self.__user=='':
            if self.__main_db!='':
                if newdata!=[]:
                    if tablename+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                        old=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                        if True:
                            #==================================================================================================================
                            if index!=None and olddict==None and mode==None and oldstr==None:
                                for i in newdata:
                                    for h in index:
                                        if h=='|':
                                            break
                                        old[h]=i
                                for i in range(len(old)):
                                    if i==0:
                                        self.__resave(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    else:
                                        self.__saveToJSON(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True
                            #==================================================================================================================
                            elif index==None and olddict!=None and oldstr==None and mode!=None:
                                if mode==0:
                                    for j in newdata:
                                        for i in olddict:
                                            if i=="|":
                                                break
                                            for h in range(len(old)):
                                                if old[h]==i:
                                                    old[h]=j

                                else:
                                    long=0
                                    for j in newdata:
                                        if long==mode:
                                            break
                                        for i in olddict:
                                            if i=="|":
                                                break
                                            for h in range(len(old)):
                                                if old[h]==i:
                                                    old[h]=j
                                                    long+=1

                                for i in range(len(old)):
                                    if i==0:
                                        self.__resave(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    else:
                                        self.__saveToJSON(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True
                            #==================================================================================================================
                            elif index==None and olddict==None and oldstr!=None and mode!=None:
                                if mode==0:
                                    for i in newdata:
                                        for h in oldstr:
                                            if h=="|":
                                                break
                                            for j in range(len(old)):
                                                for k in h:
                                                    for l in old[j]:
                                                        if k==l:
                                                            if h[k] in old[j][l]:
                                                                old[j][l]=i[l]
                                else:
                                    long=0
                                    for i in newdata:
                                        if long==mode:
                                            break
                                        for h in oldstr:
                                            if h=="|":
                                                break
                                            for j in range(len(old)):
                                                for k in h:
                                                    for l in old[j]:
                                                        if k==l:
                                                            if str(h[k]) in str(old[j][l]):
                                                                old[j][l]=i[l]
                                                                long+=1
                                for i in range(len(old)):
                                    if i==0:
                                        self.__resave(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    else:
                                        self.__saveToJSON(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def cr_user(self,username:str,password:str,jurisdiction:str)->bool:
        if self.__user!='':
            if self.__user["Jurisdiction"]=="Root":
                if username+".hjy" not in os.listdir(self.__db+r"/user/"):
                    if jurisdiction!="Root":
                        if jurisdiction=="Admin" or jurisdiction=="Simple":
                            os.makedirs("D:\PyDB\Database"+".\\"+username)
                            self.__resave({"Name":username,"Password":password,"Jurisdiction":jurisdiction},"user/"+username+".hjy")
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def sh_user(self)->bool or str:
        a=os.listdir(self.__db+r"/user/")
        print(a)
        if not a==[]:
            for i in range(len(a)):
                if a[i][0]=="#":
                    a.pop(i)
                    continue
                a[i]=a[i].replace(".hjy",'')

        return a

    def repass(self,username:str,newpass:str)->bool:
        if self.__user!='':
            if username+".hjy" in os.listdir(self.__db+r"/user/"):
                if self.__user["Jurisdiction"]=="Root":
                    for i in os.listdir(self.__db+r"\user"):
                        u=self.__turn("PyDB\\user\\"+i)[0]
                        if u["Name"]==username:
                            break
                    jurisdiction=u["Jurisdiction"]
                    self.__resave({"Name":username,"Password":newpass,"Jurisdiction":jurisdiction},"user/"+username+".hjy")
                    return True
                elif self.__user["Jurisdiction"]=="Admin" and self.__turn(self.__db+r"/user/"+username+".hjy")[0]["Jurisdiction"]=="Simple":
                    for i in os.listdir(self.__db+r"\user"):
                        u=self.__turn("PyDB\\user\\"+i)[0]
                        if u["Name"]==username:
                            break
                    jurisdiction=u["Jurisdiction"]
                    self.__resave({"Name":username,"Password":newpass,"Jurisdiction":jurisdiction},"user/"+username+".hjy")
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def Del_user(self,username:str)->bool:
        if self.__user!='':
            if username+".hjy" in os.listdir(self.__db+r"/user/"):
                if self.__user["Jurisdiction"]=="Root":
                    os.remove(self.__db+r"/user/"+username+".hjy")
                    shutil.rmtree(self.__db+r"/Database/"+username)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def del_data(self,tablename:str,olddict:list=None,oldstr:list=None,index:list=None,mode:int=None)->bool:
        if not self.__user=='':
            if self.__main_db!='':
                if True:
                    if tablename+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                        old=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                        if True:
                            del_index=[]
                            #==================================================================================================================
                            if index!=None and olddict==None and mode==None and oldstr==None:
                                for i in range(len(old)):
                                    if i==0:
                                        self.__resave(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    elif i in index:
                                        self.__saveToJSON("#"+str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True
                            #==================================================================================================================
                            elif index==None and olddict!=None and oldstr==None and mode!=None:
                                if mode==0:
                                    for i in olddict:
                                        for h in range(len(old)):
                                            if old[h]==i:
                                                del_index.append(h)

                                else:
                                    long=0
                                    for i in olddict:
                                        if long==mode:
                                            break
                                        for h in range(len(old)):
                                            if old[h]==i:
                                                del_index.append(h)
                                                long+=1

                                for i in range(len(old)):
                                    if i==0:
                                        self.__resave(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    elif i in del_index:
                                        self.__saveToJSON("#"+str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True
                            #==================================================================================================================
                            elif index==None and olddict==None and oldstr!=None and mode!=None:
                                if mode==0:
                                    for h in oldstr:
                                        for j in range(len(old)):
                                            for k in h:
                                                for l in old[j]:
                                                    if k==l:
                                                        if h[k] in old[j][l]:
                                                            del_index.append(j)
                                else:
                                    long=0
                                    for h in oldstr:
                                        if long==mode:
                                            break
                                        for j in range(len(old)):
                                            for k in h:
                                                for l in old[j]:
                                                    if k==l:
                                                        if str(h[k]) in str(old[j][l]):
                                                            del_index.append(j)
                                                            long+=1
                                for i in range(len(old)):
                                    if i==0:
                                        self.__resave(str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                    elif i in del_index:
                                        self.__saveToJSON("#"+str(old[i]),"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                                return True
                            else:
                                return False
                    else:
                        return False
            else:
                return False
        else:
            return False

    def ch_head(self,tablename:str,newhead:list)->bool:
        if self.__user!='':
            if self.__main_db!='':
                if tablename+".hjy" in os.listdir("D:/PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db):
                    old=self.__turn("PyDB/DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                    oldhead=[]
                    newlist=[]
                    for i in old[0]:
                        oldhead.append(i)
                    if len(newhead)==len(oldhead):
                        for i in range(len(old)):
                            new={}
                            if i==0:
                                for i in newhead:
                                    new.setdefault(i,i)
                                newlist.append(new)
                                continue
                            for j in range(len(oldhead)):
                                new.setdefault(newhead[j],old[i][oldhead[j]])
                            newlist.append(new)
                        for i in range(len(newlist)):
                            if i==0:
                                self.__resave(newlist[0],"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                            else:
                                self.__saveToJSON(newlist[i],"DataBase/"+self.__user["Name"]+'/'+self.__main_db+"/"+tablename+'.hjy')
                        return True
