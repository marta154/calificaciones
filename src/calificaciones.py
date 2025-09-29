def notas_teoria(c1,c2):
    c1=convierte_none(c1)
    c2=convierte_none(c2)
    return (c1+c2)/2

def convierte_none(n):
    if n is None:
        n=0
    return n

def notas_cuatrimestre(t1,t2,p):
    t1=convierte_none(t1)
    t2=convierte_none(t2)
    p=convierte_none(p)
    if (t1+t2+p)/3 >= 4:
        nota_cuatrimestre =  0,15 * t1 + 0,15 * t2 + 0,7 * p
    else:
        nota_cuatrimestre= 0
    return nota_cuatrimestre

def nota_continua(notas_teoria, notas_practica):
    n1=notas_cuatrimestre(notas_teoria[0],notas_teoria[1],notas_practica[0] )
    n2=notas_cuatrimestre( notas_teoria[2], notas_teoria[3], notas_practica[1])
    if n1 >= 5 and n2  >= 5:
        nota= (n1+n2)/2
    else:
        nota=min(4, (n1+n2)/2)
    return  nota



