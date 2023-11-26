def mestrefunção(fuc, args, **kwargs, ):
    return fuc(args, **kwargs,)


nome = input("digite seu nome e daremos uma saudação")
dia2 = str(input("digite um dia da semana "))


def saudação(saudacao2):

    if dia2 == "domingo":
        print(f"hj é domingo {nome}")
    elif dia2 == "segunda-feira":
        print(f"hj é segunda-feira{nome}")
    elif dia2 == "terca-feira":
        print(f"hj é terca-feira{nome}")
    elif dia2 == "quarta-feira ":
        print(f"hj é quarta-feira{nome}")
    elif dia2 == " quinta-feira":
        print(f"hj é quinta-feira{nome}")
    elif dia2 == "sexta-feira":
        print(f"hj é sexta-feira{nome}")
    elif dia2 == " sabado":
        print(f"hj é sabado{nome}")

    else:
        print("invalid day,digite nome do dia correto")
    return saudacao2


day = int(input("digite um numero de 1-3"))


def qualhorario(dia):

    try:
        if dia == 1:
            print("bom dia")
        elif dia == 2:
            print("boa tarde")
        elif dia == 3:
            print("boa noite")
        else:
            print("numero incorreto")
            return dia

    except:
        print("erro")


qualhorario(dia=day)


print()


var = mestrefunção(saudação, qualhorario,)
print()
print(f"obrigado por usar este programa {nome} , tenha uma otima  {dia2}")
