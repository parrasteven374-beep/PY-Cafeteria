# Sistema de Gestión de Cafetería en Python ☕🍔

Aplicación interactiva de consola desarrollada en Python que simula el punto de venta (POS) y la administración de inventario de una cafetería.

## 📋 Características Principales

### 🎓 Módulo de Estudiante / Cliente
- **Consulta de Menú:** Muestra productos ordenados por categoría, precio y disponibilidad de stock.
- **Procesamiento de Pedidos:** Selección dinámica de hasta 5 productos por pedido con validación inmediata de inventario.
- **Descuentos Automáticos:** Aplica un **10% de descuento** en compras que superen los $20.000.
- **Generación de Factura:** Desglose detallado del subtotal, descuento aplicado y total a pagar.

### 🛠️ Módulo de Administración (Admin)
- **Cierre y Resumen Diario:** Cálculo acumulado de los ingresos en caja durante la jornada.
- **Métricas de Venta:** Identificación del producto más vendido del día.
- **Control de Inventario Crítico:** Sistema de alertas para productos con stock bajo (menos de 3 unidades disponibles).

## 🏗️ Estructura Técnica
- **Control de Datos:** Uso de listas y diccionarios para simular la base de datos de productos y transacciones.
- **Manejo de Errores:** Implementación de bloques `try-except` para validar las entradas numéricas del usuario y prevenir fallos en ejecución.
- **Navegación:** Menú interactivo basado en bucles condicionales anidados con roles diferenciados (`estudiante` / `admin`).

## 🛠️ Tecnologías
- **Lenguaje:** Python 3.x
- **Entorno:** Consola / Terminal
