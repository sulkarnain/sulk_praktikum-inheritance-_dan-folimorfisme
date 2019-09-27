# mendefinisikan kelas Bapak
class Hyaman(object):
   def __init__(self, fhira):
      self.fhira = fhira
   def cetakfhira(self):
      print("fhira = ", self.fhira)

# mendefinisikan kelas Ibu
class Nurbaya(object):
   def __init__(self, adhymulya):
      self.adhymulya = adhymulya
   def cetakadhymulya(self):
      print("adhymulya = ", self.adhymulya)

# mendefinisikan kelas turunan
class Anak(Hyaman, Nurbaya):
   def __init__(self, fhira, adhymulya, kasmawati):
      # memanggil Hyaman.__init__()
      Hyaman.__init__(self, fhira)
      # memanggil Nurbaya.__init__()
      Nurbaya.__init__(self, adhymulya)
      self.kasmawati = kasmawati
   def cetakkasmawati(self):
      print("kasmawati = ", self.kasmawati)

def main():
   # membuat objek dari kelas Sulkarnain
   obj = Anak ("saya selalu siap", "dalam menghadapi", "tantangan baru")

   # memanggil metode kelas Hyaman dari obj
   obj.cetakfhira()

   # memanggil metode kelas Nurbaya dari obj
   obj.cetakadhymulya()

   # memanggil metode kelas Sulkarnain
   obj.cetakkasmawati()

if __name__ == "__main__":
   main()
