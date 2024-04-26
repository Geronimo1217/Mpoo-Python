
import time
 
class Televisao:
    def __init__(self):
        self.ligado = False
        self.canal_atual = 1
        self.volume_atual = 10


    def mudar_canal(self, novo_canal):
        if  not self.ligado:
            print(f"Canal Atual antes da alteração {self.canal_atual}")
            self.canal_atual = novo_canal
            print(f"Canal alterado  {novo_canal}")
        else:
            print("A TV está desligada")

    def aumentar_volume(self):
        if not self.ligado:
            self.volume_atual += 1
            print(f"Volume aumentado para {self.volume_atual}")
        else:
            print("A TV está desligada")

    def diminuir_volume(self):
        if not self.ligado:
            self.volume_atual -= 1
            print(f"Volume diminuído para {self.volume_atual}")
        else:
            print("A TV está desligada")
    def listar_canal(self):
        if  not self.ligado:
            self.canal_atual 
            print(f"Listar o canal atual  {self.canal_atual}")
        else:
            print("A TV está desligada : ")
            
###
tv01 = Televisao()
def main():
    while True:
        print("\n"*1)
        print("-----------OPÇÕES ---------")
        print("1 - mudar canal")
        print("2 - Aumentar volume")
        print("3 - Diminuir volume")
        print("4 - Listar os canais ")
        print("5 - desligar\n ---------------")
        selec = input("Selecionar: ")
        if selec == "1":
            canal = input("Selecionar: qual canal vc quer escolher: ")
            tv01.mudar_canal(canal)  # mudaCanal()

        elif selec == "2":
            tv01.aumentar_volume() # mudaVolume()
        elif selec == "3":
            tv01.diminuir_volume()

        elif selec == "4":
            print("Listando os canais...")
            tv01.listar_canal()
        elif selec == "5":
            print("Desligando ...")
            break
        else:
            print("Selecione uma opção válida!")

        time.sleep(2)




main()