from dnsibl import Mhs

class Console:

    def run(self):
        site=input("\nBilgilerini öğrenmek istediğiniz site: ")
        print("\n\n")
        ornk=Mhs()
        ornk.hubele(site)



if __name__ == '__main__':
        c=Console()
        c.run()