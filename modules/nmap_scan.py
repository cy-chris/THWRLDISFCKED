import subprocess

def run(target):
    print(f"[+] Executando Nmap em {target}...")
    comando = f"nmap -sV -T4 -p- {target}"
    resultado = subprocess.getoutput(comando)
    
    
    with open("output/resultados.txt", "a") as f:
        f.write("\n\n--- Nmap Scan ---\n")
        f.write(resultado)
        
    print(resultado)
    input("\n[+] Scan concluido. Pressione Enter para continuar...")