import subprocess

def run(url, worldlist):
    print(f"[+] Executando Gobuster em {url}com wordlist {worldlist}...")
    comando = f"gobuster dir -u {url} -w {worldlist} -q"
    resultado = subprocess.getoutput(comando)
    
    with open("output/resultado.txt", "a") as f:
        f.write("\n\n--- Gobuster ---\n")
        f.write(resultado)
        
        print(resultado)
        input("\n[+] Enumeracao concluida. Pressione Enter para continuar...")
        