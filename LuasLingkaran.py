class Lingkaran(object):
  def __init__(self, phi, r):
    self.phi = phi
    self.jarijari = r
  def hitungLuasLingkaran(self):
    return self.phi * self.jarijari * self.jarijari 

def main():
   # membuat objek pertama
   Luas1 = Lingkaran(3.14, 6)

   # menggunakan objek pertama
   print('Objek Luas1')
   print('phi\t: ', Luas1.phi)
   print('jarijari\t: ', Luas1.jarijari)
   print('Luas\t= ', Luas1.hitungLuasLingkaran())

    # membuat objek kedua
   Luas2 = Lingkaran(3.14, 8)

   # menggunakan objek kedua
   print('Objek Luas2')
   print('phi\t: ', Luas2.phi)
   print('jarijari\t: ', Luas2.jarijari)
   print('Luas\t= ', Luas2.hitungLuasLingkaran())

if __name__ == "__main__":
   main()
