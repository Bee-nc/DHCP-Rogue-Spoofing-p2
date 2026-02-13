# Práctica P2 - Rogue DHCP
** Viensy Pérez 
**Matrícula:** 20241203  

## Descripción
Repositorio individual para la práctica P2: ataque Rogue DHCP en la asignatura Seguridad de Redes.

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

## Ejecución del script
En Kali:
```bash
python3 Viensy_20241203_RogueDHCP_P2.py
