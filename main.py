import os
from modules import nmap_scan, web_enum, nikto_scan, exploit_finder, report

def menu():
    while True:
        os.system("clear")  # ou "cls" no Windows
        print("=== Pentest Automator ===")
        print("1. Reconhecimento (Nmap)")
        print("2. Enumeração de Diretórios (Gobuster)")
        print("3. Scanner Web (Nikto)")
        print("4. Buscar Exploits (Searchsploit)")
        print("5. Gerar Relatório Final")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            target = input("Alvo (IP ou domínio): ")
            nmap_scan.run(target)
        elif escolha == "2":
            url = input("URL para enumeração (ex: http://example.com): ")
            web_enum.run(url)
        elif escolha == "3":
            url = input("URL para análise (ex: http://example.com): ")
            nikto_scan.run(url)
        elif escolha == "4":
            serviço = input("Serviço encontrado (ex: apache 2.4.49): ")
            exploit_finder.run(serviço)
        elif escolha == "5":
            report.gerar()
        elif escolha == "0":
            break
        else:
            input("Opção inválida. Pressione Enter.")

if __name__ == "__main__":
    menu()
