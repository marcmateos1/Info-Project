class PlaneSpeedFuel():
    def __init__(self,code,speed,fuel):
        self.code=code
        self.speed=float(speed)
        self.fuel=float(fuel)

#nova funció: a partir d'un fixter amb el format com <airplane_list.txt>, que dona la velocitat mitjana i el consum mitjà
#per km d'un avio, a l'hora de fer el shortest path, segons l'avió que escullis et dirà el temps de vol i el combustible
#necessari. Aquí s'ha creat una classe per agrupar cada avió: té el seu codi (ex. Airbus A320 --> A320), la seva velocitat
#mitjana i el seu consum promig.