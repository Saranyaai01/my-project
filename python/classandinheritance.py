class person:
    def __init__(self,name,address):
        self.Name=name
        self.loc=address
    def display(self):
        print("welcome to my program I am",self.Name,"from",self.loc)
x =person("saranya","trichy")
x.display()
class person_details(person):
    def __init__(self,name,address,lastname,age,phnum,education):
        self.lname=lastname
        self.Age=age
        self.mobile_num=phnum
        self.ug=education
        super(). __init__(name,address)
    def full_details(self):
        print("my details \n",self.Name,"\n",self.loc,"\n",self.lname,"\n",self.Age,"\n",self.mobile_num,"\n",self.ug)
x=person_details("saranya","trichy","narayanan",29,8248879007,"B.E")
x.full_details()        