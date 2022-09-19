def crear_palabra_vacia(palabra_secreta) :
    x=list(palabra_secreta)
    print(x)
    for i in range(0,len(x)):
        x[i]='*'
    #print(x)
    palSecret = "".join(x)
    #print(palSecret)
    return palSecret
crear_palabra_vacia("hola")