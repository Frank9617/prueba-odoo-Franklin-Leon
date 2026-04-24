# Prueba Técnica Odoo — Franklin León

##  Descripción

Este repositorio contiene la solución a la prueba técnica basada en Odoo 16. Incluye:

* Desarrollo de un módulo personalizado
* Análisis de regla salarial colombiana
* Propuestas de solución a casos empresariales reales

---

##  Estructura del proyecto

```
prueba-odoo-franklin-leon/
│
├──it_inventory_insumos/ 
├── __init__.py 
├── __manifest__.py 
├── models/ 
  └── insumo.py
  └── _init_.py  
├── views/
  └── insumo_views.xml 
├── security/
  └── ir.model.access.csv
│
├── analisis_nomina.md        # Ejercicio 2
├── propuestas_solucion.md    # Ejercicio 3
└── README.md
```

---

##  Ejercicio 1 — Módulo IT Inventory Insumos

Se desarrolló un módulo en Odoo 16 que permite:

* Registrar insumos de IT (tóner, cables, repuestos, etc.)
* Asociar proveedor (res.partner)
* Controlar stock por sede
* Generar alerta cuando el stock está por debajo del mínimo

###  Lógica clave

El campo `alerta_stock` se calcula automáticamente:

```python
record.alerta_stock = record.cantidad_stock < record.cantidad_minima
```

---

##  Ejercicio 2 — Análisis de Nómina

Se analizó una regla salarial con errores en:

* Valores hardcodeados (SMMLV y auxilio)
* Manejo inseguro de datos
* Falta de validaciones legales

Se propuso una versión corregida con mejores prácticas y mayor mantenibilidad.

---

##  Ejercicio 3 — Propuestas de solución

Se plantearon soluciones para 5 casos reales usando:

* Configuración estándar de Odoo
* Desarrollo backend (Python)
* Desarrollo frontend (POS en JS)
* Buenas prácticas de arquitectura

---

##  Consideraciones

* El módulo fue desarrollado siguiendo la estructura estándar de Odoo
* No se incluye entorno Odoo instalado localmente
* Se priorizó claridad, buenas prácticas y mantenibilidad

---

## Autor

Franklin León
