senhas = [  input("1° - Usuario Cadastre sua primeira senha: "),
            input("2° - Usuario Cadastre sua segunda senha: "),
            input("3° - Usuario Cadastre sua terceira senha: "),
            input("4° - Usuario Cadastre sua quarta senha: ")]



input("=============LOGIN==============")

login1 = input("Nome do usuario: ")
login = input("Digite sua senha: ")

for senha in senhas:
    if login == senha:
       senha == login

       print(login1,"==> Seja Bem Vindo!")

    else:

        print("Usuario Não Cadastrado!")

