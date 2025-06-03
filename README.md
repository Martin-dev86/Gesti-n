# Gestión de Correctivos

Esta aplicación es un ejemplo básico para gestionar correos corporativos, clasificarlos por sede y crear correctivos que puedan asignarse a equipos de trabajo.

## Características

- Lectura de correos desde una cuenta IMAP.
- Clasificación automática de correos por sede usando un clasificador sencillo.
- Interfaz web con Flask para visualizar y asignar correctivos a los equipos mediante "arrastrar y soltar".

## Requisitos

- Python 3.12
- Paquetes listados en `requirements.txt`

## Uso rápido

Instalar dependencias:
```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:
```bash
python run.py
```

Esto iniciará un servidor en `http://localhost:5000`.

## Notas

Este repositorio es una demostración inicial y puede ampliarse con funcionalidades como preventivos y gestión de fechas límite.
