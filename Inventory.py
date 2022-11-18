class Item:
    def __init__(self,qnt,valor,descricao,marca):
        self.qnt = qnt
        self.valor = valor
        self.descricao = descricao
        self.marca = marca

class Inversor_Solar_Fotovoltaico(Item):
    pass

micro_inversor_151506_4 = Inversor_Solar_Fotovoltaico(0,2998,"SUN2000G3-US-220 2KW MONOFASICO 220V 4MPPT MONITORAMENTO","DEYE")

inversor_hibrido_177342_2 = Inversor_Solar_Fotovoltaico(0,8639,"SUN-3K-SG04LP1-EU 3KW MONOFASICO 220V MPPT MONITORAMENTO","DEYE")

inversor_hibrido_177343_6 = Inversor_Solar_Fotovoltaico(0,10879,"SUN-5K-SG04LP1-EU 5KW MONOFASICO 220V 2MPPT MONITORAMENTO","DEYE")

inversor_hibrido_177346_8 = Inversor_Solar_Fotovoltaico(0,19719,"SUN-8K-SG04LP1-EU 8KW MONOFASICO 127/220V 2MPPT MONITORAMENTO","DEYE")

inversor_hibrido_177345_4 = Inversor_Solar_Fotovoltaico(0,24139,"SUN-10K-SG04LP1-EU 10KW TRIFASICO 380V 2MPPT MONITORAMENTO","DEYE")

inversor_on_grid_68207_0 = Inversor_Solar_Fotovoltaico(0,2229,"MIC 1500 TL-X 1.5KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT")

inversor_on_grid_68208_4 = Inversor_Solar_Fotovoltaico(0,2449,"MIC 2000 TL-X 2KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT")

inversor_on_grid_68210_5 = Inversor_Solar_Fotovoltaico(0,2539,"MIC 2500 TL-X 2.5KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT")

inversor_on_grid_68211_9 = Inversor_Solar_Fotovoltaico(0,2719,"MIC 3000 TL-X 3KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT")

inversor_on_grid_68202_0 = Inversor_Solar_Fotovoltaico(0,3509,"MIC 3000 TL-X 3KW MONOFASICO 220V 2MPPT MONITORAMENTO","GROWATT")

print(micro_inversor_151506_4.descricao)
