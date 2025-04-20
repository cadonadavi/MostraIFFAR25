from start_menu import mostrar_menu
import jogo
import creditos

if __name__ == "__main__":
    estado = "menu"

    while True:
        if estado == "menu":
            estado = mostrar_menu()
        elif estado == "jogo":
            estado = jogo.executar()
        elif estado == "créditos":
            estado = creditos.executar_creditos()