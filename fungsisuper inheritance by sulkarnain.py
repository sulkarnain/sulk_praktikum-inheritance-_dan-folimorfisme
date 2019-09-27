class Person(object):
   def __init__(self, name, age, address):
      self.name = name
      self.age = age
      self.address = address

   def  Display(self):
      return self.name * self.age * \
             self.address

   def cetakData(self):
      print("name\t: ", self.name)
      print("age\t: ", self.age)
      print("tinggi\t: ", self.address)

   def cetakDisplay(self):
      print(" Display\t= ", self. Display())

# mendefinisikan kelas turunan (subclass)
class Student(Person):
   def __init__(self, name, age, address, percentage):
      # memanggil Student.__init__()
      super(Student, self).__init__(name, age, address)
      # menambah atribut baru
      self.percentage = percentage
      
   def cetakData(self):
      # memanggil Kotak.cetakData()
      super(Student, self).cetakData()
      print("percentage\t: ", self.percentage)

def main():
   # membuat objek Student
   Student1 = Student("Sulkarnain", 19, "Bontolempangan", 89.88)

   # menggunakan objek
   Student1.cetakData()
   Student1.cetakDisplay()

if __name__ == "__main__":
   main()
