from calificaciones import *
def test_nota_teoria(c1,c2):
    print("Probando la función nota_teoria")
    media=notas_teoria(c1,c2)
    print(c1,",",c2,"==>",media)



if __name__=="__main__":
    test_nota_teoria(9.1,7.2)
    test_nota_teoria(4.0,6.0)
    test_nota_teoria(4.0,3.0)
    test_nota_teoria(None,3.0)
    test_nota_teoria(9.0,None)
    test_nota_teoria(None,None)

def test_nota_cuatrimestre(t1,t2,p):
    print("Probando la función nota_cuatrimestre")
    media_cuatrimestre=notas_cuatrimestre(t1,t2,p)
    print(t1,",",t2,"==>",media_cuatrimestre)


if __name__=="__main__":
    test_nota_cuatrimestre(9.1, 7.2, 8.1)
    test_nota_cuatrimestre(4.0, 6.0, 5.0)
    test_nota_cuatrimestre(4.0, 3.0, None)
    test_nota_cuatrimestre(None, 3.0, None)
    test_nota_cuatrimestre(9.0, None, 4.5)
    test_nota_cuatrimestre(9.0, None, None)
    test_nota_cuatrimestre(None, None, None)

def test_nota_continua(notas_teoria, notas_practica):
    print("Probando la función nota_continua")
    nota_final=nota_continua(t1,t2,p)
    print(t1,",",t2,"==>",media_cuatrimestre)


if __name__=="__main__":
    test_nota_cuatrimestre(9.1, 7.2, 8.1)
    test_nota_cuatrimestre(4.0, 6.0, 5.0)
    test_nota_cuatrimestre(4.0, 3.0, None)
    test_nota_cuatrimestre(None, 3.0, None)
    test_nota_cuatrimestre(9.0, None, 4.5)
    test_nota_cuatrimestre(9.0, None, None)
    test_nota_cuatrimestre(None, None, None)