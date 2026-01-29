# LPC Engine

## Life Process Computation (LPC)

LPC Engine es un motor de simulación basado en ciclos de vida, presión del entorno,
toma de decisiones adaptativas y reproducción de entidades.

El motor permite modelar sistemas complejos donde:
- Las entidades consumen recursos
- El entorno ejerce presión
- Las decisiones afectan la supervivencia
- Las poblaciones evolucionan o colapsan

## Filosofía LPC

LPC es un motor abstracto de dinámica de vida.
No está limitado a un solo dominio y puede adaptarse mediante presets semánticos.

Ejemplos de dominios:
- Business Units
- Finanzas
- Salud
- Organizaciones
- Sistemas empresariales

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

