class Person(object):
   def __init__(self, name, age, address):
      self.name = name
      self.age = age
      self.address = address

   def Display(self):
      return self.name * self.age * \
             self.address

   def cetakData(self):
      print("name\t: ", self.name)
      print("age\t: ", self.age)
      print("address\t: ", self.address)

   def cetakStudent(self):
      print("Display\t= ", self.Display())

# mendefinisikan kelas turunan (subclass)
class Student(Person):
   def __init__(self, name, age, address, per):
      self.name = name
      self.age = age
      self.address = address
      self.warna = per
   def cetakData(self):
      print("name\t: ", self.name)
      print("age\t: ", self.age)
      print("address\t: ", self.address)
      print("percentage\t: ", self.warna)

def main():
   # membuat objek Student
   Student1 = Student("Sulkarnain", 19  , "Bontolempangan", 89.88)

   # menggunakan objek
   Student1.cetakData()
   Student1.cetakDisplay()

if __name__ == "__main__":
   main()
