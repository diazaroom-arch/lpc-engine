# LPC Engine

## Life Process Computation (LPC)

LPC Engine es un motor de simulación basado en ciclos de vida, presión del entorno,
toma de decisiones adaptativas y reproducción de entidades.

El motor permite modelar sistemas complejos donde:
- Las entidades consumen recursos
- El entorno ejerce presión
- Las decisiones afectan la supervivencia
- Las poblaciones evolucionan o colapsan

LPC no es una aplicación cerrada, sino un core de simulación reutilizable
y configurable para múltiples dominios.

## Contexto del proyecto

LPC Engine nace como la evolución de experimentos previos sobre agentes,
comportamiento y persistencia de estados, con el objetivo de construir
un **motor base ordenado, modular y extensible**, y no prototipos aislados.

El enfoque del proyecto está en el **diseño del core**, la separación clara
de responsabilidades y la capacidad de adaptación a distintos escenarios,
más que en interfaces gráficas o productos finales en esta etapa.

## Objetivo general

Construir un **motor de simulación flexible y genérico** que permita
modelar entidades autónomas, su interacción con el entorno y su evolución
temporal bajo reglas configurables.

## Objetivos específicos

- Definir un **core de entidades** con estado interno y rasgos (traits).
- Separar claramente:
  - entidades
  - entorno
  - toma de decisiones
  - memoria y métricas
- Permitir configuración por parámetros, no por código rígido.
- Facilitar la creación de **escenarios reutilizables**.
- Servir como base para agentes, simulaciones estratégicas o investigación.

## Filosofía LPC

LPC es un motor abstracto de dinámica de vida.
No está limitado a un solo dominio y puede adaptarse mediante
**presets semánticos**, manteniendo siempre el mismo core.

Ejemplos de dominios:
- Business Units
- Finanzas
- Salud
- Organizaciones
- Sistemas empresariales

## Alcance actual del proyecto (versión base)

En su estado actual, LPC Engine incluye:

- Un motor funcional basado en ciclos de simulación.
- Entidades con:
  - estado
  - rasgos
  - memoria básica
  - toma de decisiones
- Un entorno (world) que influye sobre las entidades.
- Configuración centralizada (`config.py`).
- Escenarios base y presets.
- Un punto de entrada (`run.py`) para ejecutar simulaciones simples.

## Estructura del proyecto

```
lpc-engine/
│
├── lpc/
│   ├── __init__.py
│   ├── config.py
│   ├── entity.py
│   ├── traits.py
│   ├── memory.py
│   ├── decision.py
│   ├── population.py
│   ├── world.py
│   ├── metrics.py
│   └── scenarios.py
│
├── presets/
│   ├── lpc_presets.py
│   └── visualization.py
│
├── simulation.py
├── run.py
├── pyproject.toml
└── LICENSE
```

## Ejecución básica

Ejecuta el archivo principal:

```
python run.py
```

## Licencia

Este proyecto utiliza la licencia MIT.
Consulta el archivo LICENSE para más información.


