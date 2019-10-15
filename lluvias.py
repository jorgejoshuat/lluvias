from arrays import Array3D
import xlrd

def main():
    a3=Array3D(34,33,14)
    for anio in range(1985,2019,1):
        ruta= './Precipitacion/'+str(anio)+'Precip.xls'
        #print(ruta)
        archivo=xlrd.open_workbook(filename=ruta)        
        hoja=archivo.sheet_by_index(0)
        for r in range(1,33,1):
            for c in range(0,14,1):
                #print(hoja.cell_value(r,c), end='')                
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))
    
    print("1)Promedio de un estado en determinado mes y año \n\n2)Promedio de un estado, de un mes para todos los años \n\n3)Promedio de todos los meses en todos los años para un estado \n\n4)Promedio total de todo")
    x=int(input("\nElija el cáculo que desea realizar: "))
    if x==1:
        a=int(input("Año (1985-2019): "))
        e=int(input("Edo (1-32): "))
        m=int(input("Mes (1-12): "))
        print(f"En el estado de {a3.get_item(0,e,0)} llovió un promedio de {a3.get_item(a-1985,e,m)} centímetros cúbicos en el mes de {a3.get_item(0,0,m)} del año {a}")
    elif x==2:
        e=int(input("Edo (1-32): "))
        m=int(input("Mes (1-12): "))
        total=0
        for a in range(1985,2019,1):
            total=total+float(a3.get_item(a-1985,e,m))
        promedio=total/(a-1985)
        print(f"El promedio de lluvias de {a3.get_item(0,e,0)} en el mes {a3.get_item(0,0,m)} para todos los años es {promedio}")
    elif x==3:
        e=int(input("Edo (1-32): "))
        total=0
        for a in range(1985,2019,1):
            for m in range(1,13,1):
                total=total+float(a3.get_item(a-1985,e,m))
        promedio=total/((a-1985)*12)
        print(f"El promedio de lluvias de todos los meses de todos los años del estado de {a3.get_item(0,e,0)} es {promedio}")
    elif x==4:
        total=0
        for a in range(1985,2019,1):
            for m in range(1,13,1):
                for e in range(1,33,1):
                    total=total+float(a3.get_item(a-1985,e,m))
        promedio=total/((a-1985)*12*32)
        print(f"El promedio total de todos los estados de todos los años de todos los meses es {promedio}")
    else:
        print("opción no valida")
    
main()
