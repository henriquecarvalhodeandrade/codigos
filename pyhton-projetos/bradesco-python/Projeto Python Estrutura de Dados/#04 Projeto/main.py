from GUI import *
import backend as core

class AppController:
    def __init__(self, app):
        self.app = app
        self.selected = None

        # Vincular eventos e configurar comandos dos botões
        self.app.listClientes.bind('<<ListboxSelect>>', self.getSelectedRow)
        self.app.btnViewAll.configure(command=self.view_command)
        self.app.btnBuscar.configure(command=self.search_command)
        self.app.btnInserir.configure(command=self.insert_command)
        self.app.btnUpdate.configure(command=self.update_command)
        self.app.btnDel.configure(command=self.del_command)
        self.app.btnClose.configure(command=self.app.window.destroy)

    def view_command(self):
        '''Comando para visualizar todos os registros'''
        try:
            rows = core.view()
            self.app.listClientes.delete(0, END)
            for r in rows:
                self.app.listClientes.insert(END, r)
        except Exception as e:
            print(f"Erro ao visualizar registros: {e}")

    def search_command(self):
        '''Comando para buscar registros'''
        try:
            self.app.listClientes.delete(0, END)
            rows = core.search(self.app.txtNome.get(), self.app.txtSobrenome.get(), self.app.txtEmail.get(), self.app.txtCPF.get())
            for r in rows:
                self.app.listClientes.insert(END, r)
        except Exception as e:
            print(f"Erro ao buscar registros: {e}")

    def insert_command(self):
        '''Comando para inserir um novo registro'''
        try:
            core.insert(self.app.txtNome.get(), self.app.txtSobrenome.get(), self.app.txtEmail.get(), self.app.txtCPF.get())
            self.view_command()
        except Exception as e:
            print(f"Erro ao inserir registro: {e}")

    def update_command(self):
        '''Comando para atualizar o registro selecionado'''
        try:
            core.update(self.selected[0], self.app.txtNome.get(), self.app.txtSobrenome.get(), self.app.txtEmail.get(), self.app.txtCPF.get())
            self.view_command()
        except Exception as e:
            print(f"Erro ao atualizar registro: {e}")

    def del_command(self):
        '''Comando para deletar o registro selecionado'''
        try:
            id = self.selected[0]
            core.delete(id)
            self.view_command()
        except Exception as e:
            print(f"Erro ao deletar registro: {e}")

    def getSelectedRow(self, event):
        '''Obtém a linha selecionada na Listbox'''
        try:
            index = self.app.listClientes.curselection()[0]
            self.selected = self.app.listClientes.get(index)
            self.app.entNome.delete(0, END)
            self.app.entNome.insert(END, self.selected[1])
            self.app.entSobrenome.delete(0, END)
            self.app.entSobrenome.insert(END, self.selected[2])
            self.app.entEmail.delete(0, END)
            self.app.entEmail.insert(END, self.selected[3])
            self.app.entCPF.delete(0, END)
            self.app.entCPF.insert(END, self.selected[4])
        except IndexError:
            pass  # Ignore caso nenhuma linha esteja selecionada

def main():
    app = Gui()
    AppController(app)
    app.run()

if __name__ == "__main__":
    main()
