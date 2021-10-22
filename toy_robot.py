#entrada posição e para onde esta apontando
entpos = str(input("insira os dados:  "))
E = entpos.split(" ")
posicao = E[1].split(",")
codx=int(posicao[0])
cody=int(posicao[1])
#confirmar se foi iniciado da maneira certa
if E[0] != 'PLACE':
    print("FAVOR INICAR OS COMANDOS COM 'PLACE'")
    entpos = str(input("insira os dados:  "))
    E = entpos.split(" ")
    posicao = E[1].split(",")
    codx=int(posicao[0])
    cody=int(posicao[1])
#confirmar se foi colocado na mesa, caso não pedir até colocar corretamente
while cody<0 or cody>4 or codx<0 or codx>4: 
    entpos = str(input("insira os dados:  "))
    E = entpos.split(" ")
    posicao = E[1].split(",")
    codx=int(posicao[0])
    cody=int(posicao[1])
    if E[0] != 'PLACE':
        print("FAVOR INICAR OS COMANDOS COM 'PLACE'")
    
else:
    #inciar variavel entrada para entrar na repetição
    entrada="EMPTY"
    #STOP APENAS PARA NÃO SER UM LOOP INFINITO
    while entrada!= "STOP":
        #confirmar se está dentro do requisito
        #NORTH, SOUTH, EAST or WEST.
        entrada = str(input())
        p = entrada.split(" ")
        if entrada=="REPORT":
            print(codx,cody,posicao[2])
        if p[0]=="PLACE":
            if len(p)==2:
                c=p[1].split(",")
                codx=int(c[0])
                cody=int(c[1])
                posicao[2]=c[2]
                while cody<0 or cody>4 or codx<0 or codx>4: 
                    entpos = str(input("insira os dados:  "))
                    E = entpos.split(" ")
                    posicao = E[1].split(",")
                    codx=int(posicao[0])
                    cody=int(posicao[1])
                    if E[0] != 'PLACE':
                        print("FAVOR INICAR OS COMANDOS COM 'PLACE'")                  
        if posicao[2] == "NORTH":
            if entrada == "MOVE":
                cody-=1
            if entrada == "LEFT":
                posicao[2]="WEST"
            if entrada == "RIGHT":
                posicao[2]="EAST"
        elif posicao[2] == "SOUTH":
            if entrada == "MOVE":
                cody+=1
            if entrada == "LEFT":
                posicao[2]="EAST"
            if entrada == "RIGHT":
                posicao[2]="WEST"
        elif posicao[2] == "EAST":
            if entrada == "MOVE":
                codx+=1
            if entrada == "LEFT":
                posicao[2]="NORTH"
            if entrada == "RIGHT":
                posicao[2]="SOUTH"
        elif posicao[2] == "WEST":
            if entrada == "MOVE":
                codx-=1
            if entrada == "LEFT":
                posicao[2]="SOUTH"
            if entrada == "RIGHT":
                posicao[2]="NORTH"
        if cody<0 or cody>4 or codx<0 or codx>4:
            print("fora da mesa movimento ignorado")
            if cody<0:
                cody=cody+1
            if cody>4:
                cody=cody-1
            if codx<0:
                codx=codx+1
            if codx>4:
                codx=codx-1
    
            
        
        



