from front import main_content

if __name__ == "__main__":
    try:
        app = main_content.MainContent()
        app.render()
    except KeyboardInterrupt:
        print("Aplicação encerrada pelo usuário.")
    except Exception as e:
        print(f"Erro ao executar a aplicação: {e}")