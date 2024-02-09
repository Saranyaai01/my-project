# class person:
#     def __init__(self,name,address):
#         self.Name=name
#         self.loc=address
#     def display(self):
#         print("welcome to my program I am",self.Name,"from",self.loc)
# x =person("saranya","trichy")
# x.display()
# class person_details(person):
#     def __init__(self,name,address,lastname,age,phnum,education):
#         self.lname=lastname
#         self.Age=age
#         self.mobile_num=phnum
#         self.ug=education
#         super(). __init__(name,address)
#     def full_details(self):
#         print("my details \n",self.Name,"\n",self.loc,"\n",self.lname,"\n",self.Age,"\n",self.mobile_num,"\n",self.ug)
# x=person_details("saranya","trichy","narayanan",29,8248879007,"B.E")
# x.full_details()





# class Car:   
#     def mileage(self):   
#         pass  
  
# class Tesla(Car):   
#     def mileage(self):
#         print("***********TESLA*********")   
#         print("The mileage  is 30kmph")   
# class Suzuki(Car):   
#     def mileage(self):
#         print("************SUZUKI********")   
#         print("The mileage is 25kmph ")   
# class Duster(Car):   
#      def mileage(self):
#           print("**********DUSTER********")   
#           print("The mileage is 24kmph ") 
#           print("------------------------")   
# class Renault(Car):   
#     def mileage(self):
#             print("*********RENAULT******")   
#             print("The mileage is 27kmph ") 
               
# t= Tesla ()   
# t.mileage()   
# r = Renault()   
# r.mileage()     
# s = Suzuki()   
# s.mileage()   
# d = Duster()   
# d.mileage()  




class car:  
    def __init__(self,modelname, year):
        modelname=input("enter the model name:",modelname)
        year=input("enter the year:", year)  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car()  
c1.display()  