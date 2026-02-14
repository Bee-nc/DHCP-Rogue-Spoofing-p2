# Práctica P2 - Rogue DHCP
Viensy Pérez 
**Matrícula:** 20241203  

## Descripción
Repositorio individual para la práctica P2: ataque Rogue DHCP en la asignatura Seguridad de Redes.  
Este ataque se basa en levantar un servidor DHCP falso que responde más rápido que el servidor legítimo, asignando direcciones IP incorrectas y redirigiendo el tráfico hacia un atacante.

## Archivos incluidos
- `Viensy_20241203_RogueDHCP_P2.py` → Script en Python para el ataque.
- `Viensy_20241203_Informe_P2.pdf` → Informe con explicación, capturas y resultados.
- `capturas/` → Evidencias gráficas del ataque.
- `Viensy_20241203_P2.zip` → Paquete final con todos los entregables.

## Direccionamiento IP
El laboratorio utiliza direccionamiento basado en la matrícula:
- Red: `192.168.120.0/24`
- Router (R1): `192.168.120.1`
- Kali (servidor DHCP falso): `192.168.120.99`
- VPCS (PC1): recibe IP falsa (ej. `192.168.120.200`)
## 🎥 Video
👉 [Ver demostración en YouTube](https://www.youtube.com/playlist?list=PLLg_Q-fL0LdJKLXCK0P90yAFpeDc8ml5L)

## Ejecución del script
En Kali:
```bash
python3 Viensy_20241203_RogueDHCP_P2.py
