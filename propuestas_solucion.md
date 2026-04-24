# Propuestas de Solución — Odoo 16

## Caso 1 — Alertas de consecutivos y vencimientos de facturación electrónica

### Solución propuesta

Se puede resolver con una combinación de configuración estándar y desarrollo personalizado.

### Modelos involucrados

* `account.move` (facturas)
* `ir.sequence` (consecutivos)
* Modelo de resolución DIAN (custom si no existe)

### Desarrollo requerido

Sí, desarrollo personalizado para:

* Control de rango de consecutivos
* Control de fecha de vencimiento de resolución

### Implementación

1. Crear campos personalizados en `ir.sequence`:

   * rango_final
   * rango_actual
   * fecha_vencimiento_resolucion

2. Crear un método programado (cron job):

   * Se ejecute diariamente
   * Calcule si el consecutivo está cerca del límite:

     * Ej: si faltan menos de 50 números

3. Crear alerta cuando:

   * El consecutivo esté al 90% del rango
   * Falten menos de 15 días para vencimiento

4. Tipos de alerta:

   * Actividad automática (`mail.activity`)
   * Correo electrónico
   * Notificación interna

### Justificación

Odoo no maneja por defecto control de resolución DIAN, por lo que se requiere extensión del modelo.

---

## Caso 2 — Topes de facturación en POS

### Solución propuesta

Requiere desarrollo en frontend (JavaScript) del POS.

### Módulos involucrados

* `point_of_sale`

### Desarrollo requerido

Sí, validación en frontend JS

### Implementación

1. Extender modelo del POS (`Orderline` y `Order`)

2. Definir parámetros:

   * valor_maximo_linea
   * valor_maximo_orden

3. Implementar validación en JS:

   * Antes de agregar producto
   * Antes de pagar la orden

4. Mostrar mensaje de error:

   * "El valor ingresado supera el máximo permitido"

### Alternativa backend

Se podría usar `@api.constrains`, pero no es recomendable porque el POS funciona offline.

### Justificación

El POS de Odoo es altamente dependiente de JS, por lo que las validaciones deben hacerse en frontend.

---

## Caso 3 — Flujo logístico entre bodegas

### Solución propuesta

Se puede resolver con configuración estándar de inventario (multi-almacén).

### Módulos involucrados

* `stock`
* `sale_management`
* `account`

### Desarrollo requerido

No obligatorio (solo configuración)

### Implementación

1. Activar multi-almacén en Inventario

2. Crear almacenes:

   * CEDI Sede 2
   * CEDI Sede Norte

3. Configurar ubicaciones internas

4. Crear rutas:

   * Ruta de transferencia interna entre bodegas

5. Configurar reglas:

   * Pull rule: desde CEDI Sede Norte toma de CEDI Sede 2

6. Flujo:

   * Pedido de venta
   * Genera transferencia interna
   * Luego entrega final
   * Finalmente factura

### Reportes y seguimiento

* Picking (transferencias)
* Órdenes de entrega
* Estado del pedido de venta

### Justificación

Odoo ya soporta este flujo con rutas y reglas de inventario.

---

## Caso 4 — Carga masiva de PDFs a contactos

### Solución propuesta

Se puede resolver con desarrollo utilizando `ir.attachment`.

### Módulos involucrados

* `base`
* `documents` (opcional)

### Desarrollo requerido

Sí (wizard o script)

### Implementación

1. Diseñar un proceso de carga:

   * Wizard en Odoo o script Python

2. Identificación del contacto:

   * Por NIT (campo VAT en `res.partner`)

3. Carga del archivo:

   * Crear registros en `ir.attachment`

4. Relación:

   * `res_model = 'res.partner'`
   * `res_id = ID del contacto`

5. Alternativa:

   * Usar módulo `documents` para organización por carpetas

### Riesgos

* Alto volumen de archivos → impacto en rendimiento
* Tamaño de base de datos
* Errores de asociación si el NIT no coincide

### Justificación

`ir.attachment` es el mecanismo nativo para archivos en Odoo.

---

## Caso 5 — Odoo.sh y Scrum

### Parte 1 — Problema en rama Development

### Plan de acción (primeros 5 días)

Día 1:

* Revisar logs de error en build
* Identificar módulo `Pedido_peso`

Día 2:

* Aislar el módulo en entorno local
* Detectar error (dependencias, sintaxis, manifest)

Día 3:

* Corregir errores
* Validar instalación

Día 4:

* Crear nueva rama desde Development
* Probar build limpio

Día 5:

* Hacer merge controlado
* Validar en Staging antes de producción

### Justificación

Trabajar directamente en Staging es mala práctica y genera riesgo en producción.

---

### Parte 2 — Gestión de Sprint

### Situación

Una historia no se puede completar en el tiempo estimado

### Acción

1. Comunicar inmediatamente al Director IT

2. Explicar:

   * Motivo técnico
   * Impacto
   * Nueva estimación

3. Replanificar sprint:

   * Priorizar historias
   * Dividir la historia compleja

4. Opciones:

   * Mover historia al siguiente sprint
   * Entregar parcialmente

### Justificación

Transparencia y gestión de expectativas son claves en Scrum.

---

## Conclusión

Las soluciones propuestas combinan configuración estándar de Odoo con desarrollo personalizado cuando es necesario, priorizando mantenibilidad, escalabilidad y buenas prácticas.
