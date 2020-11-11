def es_bisiesto(fecha=0):
    if(fecha%4==0):
        if((fecha%100!=0) or (fecha%400==0)):
            return True    
    return False