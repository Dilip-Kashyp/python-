class progarammer:
    def __init__(self,name, product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"The Name of progarammer is {self.name} and product is {self.product}");
harry = progarammer ("harry","Skype")
Dilip = progarammer ("Dilip","Student")
harry.getinfo()
Dilip.getinfo()