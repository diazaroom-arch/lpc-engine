PRESETS = {

    # ------------------------
    # PRESET BASE (NEUTRO)
    # ------------------------
    "CORE": {
        "metrics": {
            "energy": "energy",
            "wear": "wear",
            "age": "age",
            "alive": "alive"
        },
        "actions": {
            "REST": "REST",
            "EXPLORE": "EXPLORE",
            "EXERT": "EXERT"
        },
        "world": {
            "pressure": "pressure",
            "CRISIS": "CRISIS",
            "COLLAPSE": "COLLAPSE"
        }
    },

    # ---------------------------
    # PRESET SALUD + FINANZAS 
    # ---------------------------
    "HEALTH_FINANCE": {
        "metrics": {
            "energy": "liquidez",
            "wear": "costos_fijos",
            "age": "ciclos_operativos",
            "alive": "solvente"
        },
        "actions": {
            "REST": "congelar_gastos",
            "EXPLORE": "captar_pacientes",
            "EXERT": "invertir_expandir"
        },
        "world": {
            "pressure": "presion_economica_sanitaria",
            "CRISIS": "saturacion_sanitaria",
            "COLLAPSE": "insolvencia"
        }
    },

    # -----------------------------------------
    # PRESET BUSINESS UNIT LIFE CYCLE (BULCS)
    # -----------------------------------------
    "BUSINESS_UNIT": {
        "metrics": {
            "energy": "flujo_caja",
            "wear": "carga_operativa",
            "age": "ciclos_negocio",
            "alive": "unidad_activa"
        },
        "actions": {
            "REST": "optimizar_costos",
            "EXPLORE": "explorar_mercado",
            "EXERT": "escalar_operaciones"
        },
        "world": {
            "pressure": "presion_mercado",
            "CRISIS": "recesion",
            "COLLAPSE": "mercado_colapsado"
        }
    }
}
