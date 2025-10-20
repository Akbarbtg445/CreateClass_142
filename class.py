class persegipanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

        def keliling(self):
            return 2 *(self.panjang + self.lebar)
        def luas (self):
            return self.panjang * self.lebar
        
        def __str__(self):
            return f"persegi panjang, panjang {self.panjang} cm,dan lebar {self.lebar}cm"
    try:
            panjang_input = int(input("Masukan panjang (cm):"))
            lebar_input =int(input("Masukan lebar(cm):"))

            pp = persegipanjang(panjang_input,lebar_input)
            print("keliling:",pp.keliling(),"cm")
            print("Luas:",pp.luas(),"cm^2")
    except ValueError:
         print("Input harus berupa angka.") 