# Análisis de Regla Salarial - Auxilio de Transporte (TRANS)

## 1. Descripción

Se analiza una regla salarial en Odoo 16 encargada de calcular el auxilio de transporte en Colombia. Se identifican errores técnicos y legales que afectan la precisión del cálculo.



## 2. Errores identificados

### Error 1: Valores hardcodeados (SMMLV)

El código utiliza un valor fijo de $1.300.000 para el salario mínimo.

**Problema técnico:** No es dinámico ni mantenible.
**Problema legal:** El SMMLV cambia cada año por decreto.



### Error 2: Auxilio de transporte fijo

Se asigna un valor fijo de $162.000.

**Problema técnico:** No es configurable.
**Problema legal:** Este valor cambia anualmente.



### Error 3: Lógica fuera del condicional

El cálculo proporcional se realiza incluso si no se cumple la condición.

**Impacto:** Puede generar cálculos innecesarios o inconsistentes.



### Error 4: Acceso inseguro a WORK100

Se usa `worked_days.WORK100` directamente.

**Problema:** Puede generar errores si no existe el registro.
**Solución:** Usar `worked_days.get('WORK100')`.



### Error 5: Falta de validación legal

No se valida si el trabajador realmente tiene derecho al auxilio (ej. teletrabajo).



### Error 6: No contempla otros tipos de días

No se consideran vacaciones, incapacidades u otras ausencias que pueden afectar el cálculo.



## 3. Versión corregida

```python


result = 0.0

SMMLV = 1300000
AUXILIO_TRANSPORTE = 162000

salario_basico = payslip.contract_id.wage

if salario_basico <= (2 * SMMLV):

    dias = 30
    work100 = worked_days.get('WORK100')

    if work100:
        dias = work100.number_of_days

    result = AUXILIO_TRANSPORTE * (dias / 30)
```



## 4. Mejoras propuestas

* Parametrizar SMMLV y auxilio desde configuración del sistema
* Validar si el empleado requiere transporte
* Incluir más tipos de días trabajados
* Implementar pruebas unitarias para validar cálculos



## 5. Conclusión

La regla original presenta errores comunes en sistemas heredados: valores fijos, falta de validaciones y manejo inseguro de datos. La versión corregida mejora la mantenibilidad, robustez y cumplimiento legal.
