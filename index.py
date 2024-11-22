#importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase

#criar a janela principal
jan = Tk()
jan.title("WK Sistem - Login")
jan.geometry("600x350")
jan.configure(background="white")
jan.resizable(width=FALSE, height=FALSE)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/favicon.ico")

#******* Carregando imagens
logo = PhotoImage(file="icons/wk.png")

#******* Widgets ****
LeftFrame = Frame(jan, width=200, height=350, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side="left")

RightFrame = Frame(jan, width=395, height=350, bg="MIDNIGHTBLUE")
RightFrame.pack(side="right")

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

PasswordLabel = Label(RightFrame, text="Senha", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PasswordLabel.place(x=5, y=150)

PasswordEntry = Entry(RightFrame, width=30, show="•")
PasswordEntry.place(x=150, y=160)

def Login():
    User = UserEntry.get()  # Obtendo o valor digitado no campo de usuário
    Password = PasswordEntry.get()  # Obtendo o valor digitado no campo de senha

    DataBase.c.execute("""
    SELECT * FROM Users WHERE (User=? AND Password=?)
    """,(User, Password))

    #verifyLogin = DataBase.c.fetchone()

    if DataBase.c.fetchone():
        messagebox.showinfo(title="Login", message="Login efetuado com sucesso!")
        jan.destroy()
    else:
        messagebox.showerror(title="Erro", message="Usuário ou senha incorretos!")

#RegisterButton = Button(RightFrame, text="Cadastre-se", width=30, command=Register)
#RegisterButton.place(x=100, y=255)

LoginButton = Button(RightFrame, text="Login", width=30, command=Login)                  
LoginButton.place(x=100, y=255)

def Register():
    #escondendo botões
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #inserindo botões de cadastro
    NomeLabel = Label(RightFrame, text="Nome", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)
    
    NomeEntry = Entry(RightFrame, width=30)
    NomeEntry.place(x=150, y=15)

    EmailLabel = Label(RightFrame, text="Email", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=55)
    
    EmailEntry = Entry(RightFrame, width=30)
    EmailEntry.place(x=150, y=65)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PasswordEntry.get()

        if (Name =="" and Email =="" and User =="" and Password ==""):
            messagebox.showerror(title="Erro", message="Todos os campos precisam ser preenchidos!")
        else:
            DataBase.c.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
            """,(Name, Email, User, Password))

            DataBase.conn.commit()
            messagebox.showinfo(title="Cadastro", message="Cadastro realizado com sucesso!")

    SalvarRegister = Button(RightFrame, text="Salvar", width=20, command=RegisterToDataBase)                  
    SalvarRegister.place(x=180, y=290)

    def BackLogin():
        #escondendo botões de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        SalvarRegister.place(x=5000)
        VoltarRegister.place(x=5000)  

        #trazendo de votla os botões de login
        LoginButton.place(x=100)
        RegisterButton.place(x=130)

    VoltarRegister = Button(RightFrame, text="Voltar", width=20, command=BackLogin)                  
    VoltarRegister.place(x=30, y=290)         

RegisterButton = Button(RightFrame, text="Cadastrar", width=20, command=Register)                  
RegisterButton.place(x=130, y=290)

jan.mainloop()
