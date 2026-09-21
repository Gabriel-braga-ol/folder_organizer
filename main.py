from organizador import organizar_pasta
from monitor import monitorar_pasta
from pathlib import Path

caminho = Path.home() / "Desktop" / "testeOrganizador"

organizar_pasta(caminho)

if __name__ == "__main__":
    monitorar_pasta(caminho)