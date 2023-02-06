class ponto:
    def __init__(self, ponto_x, ponto_y):
        self.x = ponto_x
        self.y = ponto_y

    def __str__(self):
        return "Seu ponto é {}, {}".format(self.x, self.y)


def interpol(x_tenho, ponto_A, ponto_B, ponto_C):
    L0 = ((x_tenho - ponto_B.x) * (x_tenho - ponto_C.x))/((ponto_A.x - ponto_B.x)*(ponto_A.x - ponto_C.x))
    L1 = ((x_tenho - ponto_A.x) * (x_tenho - ponto_C.x))/((ponto_B.x - ponto_A.x)*(ponto_B.x - ponto_C.x))
    L2 = ((x_tenho - ponto_A.x) * (x_tenho - ponto_B.x))/((ponto_C.x - ponto_A.x)*(ponto_C.x - ponto_B.x))
    print("Seu polinomio é: {}*{:.2f} + {}*{:.2f} + {}*{:.2f}\n".format(ponto_A.y, L0, ponto_B.y, L1, ponto_C.y, L2))
    y_queria = (ponto_A.y*L0) + (ponto_B.y*L1) + (ponto_C.y*L2)   
    return y_queria

print("Favor entrar com os três pontos conhecidos:\n")
A = ponto(float(input("digite o elemento X do ponto A: ")), float(input("digite o elemento Y do ponto A: ")))
B = ponto(float(input("digite o elemento X do ponto B: ")), float(input("digite o elemento Y do ponto B: ")))
C = ponto(float(input("digite o elemento X do ponto C: ")), float(input("digite o elemento Y do ponto C: ")))
D = float(input("Entre com o X para o qual deseja descobir o y: "))
if(((A.x - B.x)*(A.x - C.x)==0) or ((B.x - A.x)*(B.x - C.x)==0) or ((C.x - A.x)*(C.x - B.x)==0)): 
    print("Os pontos requeridos vão resultar em uma divisão por zero, favor modifica-los")
else:
    y = interpol(D, A, B, C)
    print("Seu y = {:.4f}".format(y))