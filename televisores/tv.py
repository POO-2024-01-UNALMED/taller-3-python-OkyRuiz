class TV:
    _numTV=0
    def __init__(self, marca, estado):
        self._marca= marca
        self._estado= estado
        self._canal= 1
        self._volumen=1
        self._precio=500
        self._control= None

        TV._numTV+=1

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    #METODOS SET Y GET MARCA
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca=marca

    #METODOS SET Y GET CANAL
    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):
        if (self._estado==True):
            if (canal>=1 and canal<=120):
                self._canal=canal

    #METODOS SET Y GET VOLUMEN
    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if (self._estado==True):
            if (volumen>=0 and volumen<=7):
                self._volumen= volumen
    
    #METODOS SET Y GET PRECIO
    def getPrecio(self):
        return self._precio
    def setPrecio(self,precio):
        self._precio= precio

    #METODOS SET Y GET CONTROL
    def setControl(self,control):
        self._control= control
    def getControl(self):
        return self._control
    
    #METODOS PARA DEFINIR ESTADO
    def turnOn(self):
        self._estado= True
    def turnOff(self):
        self._estado= False

    def getEstado(self):
        return self._estado
    
    ##DISMINUIR Y AUMENTAR CANAL DE A UNO
    def canalDown(self):
        if (self._estado == True):
            if (self._canal>1 and self._canal<=120):
                self._canal-=1
    
    def canalUp(self):
        if (self._estado == True):
            if (self._canal>=1 and self._canal<120):
                self._canal+=1

    ##DISMINUIR Y AUMENTAR CANAL DE A UNO
    def volumenDown(self):
        if (self._estado == True):
            if (self._volumen>0 and self._canal<=7):
                self._volumen-=1
    
    def canalUp(self):
        if (self._estado == True):
            if (self._canal>=0 and self._canal<7):
                self._volumen+=1

    
