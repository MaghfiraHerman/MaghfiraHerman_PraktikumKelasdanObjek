class Lingkaran(object):
  def __init__(self, phi, r):
    self.phi = phi
    self.jarijari = r
  def hitungKelilingLingkaran(self):
    return 2 * self.phi * self.jarijari 

def main():
   # membuat objek pertama
   Keliling1 = Lingkaran(3.14, 8)

   # menggunakan objek pertama
   print('Objek Keliling1')
   print('phi\t: ', Keliling1.phi)
   print('jarijari\t: ', Keliling1.jarijari)
   print('Keliling\t= ', Keliling1.hitungKelilingLingkaran())

    # membuat objek kedua
   Keliling2 = Lingkaran(3.14, 6)

   # menggunakan objek kedua
   print('Objek Keliling2')
   print('phi\t: ', Keliling2.phi)
   print('jarijari\t: ', Keliling2.jarijari)
   print('Keliling\t= ', Keliling2.hitungKelilingLingkaran())

if __name__ == "__main__":
   main()
