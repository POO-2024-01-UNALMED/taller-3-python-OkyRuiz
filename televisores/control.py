class Control:

    def __init__(self, tv=None):
        self._tv=tv 

    def enlazar(self, tv):
        self._tv= tv
        tv.setControl(self)

    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
    
    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setVolumen(self, volumen):
        if (volumen>=0 and volumen<=7):
            self._tv.setVolumen(volumen)

    def setCanal(self, canal):
        if (canal>=1 and canal<=120):
            self._tv.setCanal(canal)

    #METODO SETTER Y GETTER TV
    def setTv(self, tv):
        self._tv= tv
        
    def getTv(self):
        return self._tv

    