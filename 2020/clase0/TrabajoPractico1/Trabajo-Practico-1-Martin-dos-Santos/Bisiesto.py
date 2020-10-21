def esBisiesto(fecha=0):
    if(fecha%4==0):
        if((fecha%100!=0) or (fecha%400==0)):
            return True   
        else: 
            return False
    else:
        return False