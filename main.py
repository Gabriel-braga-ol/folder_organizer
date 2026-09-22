from organizador import organizar_pasta
from monitor import monitorar_pasta
from pathlib import Path

caminho = Path.home() / "Downloads"

if __name__ == "__main__":
    organizar_pasta(caminho)
    monitorar_pasta(caminho)