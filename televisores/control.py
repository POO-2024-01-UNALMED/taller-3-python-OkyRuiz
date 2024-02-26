class Control:

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
            if (self._tv and self._tv.getEstado()):
                self._tv.setVolumen(volumen)

    def setCanal(self, canal):
            if (self.tv and self._tv.getEstado()):
                self._tv.setCanal(canal)

    #METODO SETTER Y GETTER TV
    def setTv(self, tv):
        self._tv= tv
        
    def getTv(self):
        return self._tv

    