# Text-to-PDF

## Descripción general

Esta aplicación web permite a los usuarios convertir texto en archivos PDF. Está construida con Flask como framework backend y utiliza ReportLab para generar documentos PDF. La interfaz está desarrollada con HTML, CSS y Bootstrap.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

1. **Python 3.7 o superior**

   - Verifica tu versión ejecutando:
     ```bash
     python --version
     ```

2. **pip** (gestor de paquetes de Python)
   - Normalmente viene incluido con Python, verifica con:
     ```bash
     pip --version
     ```

## Instalación del proyecto

### 1. Clonar o descargar el repositorio

Si usas git:

```bash
git clone <url-del-repositorio>
cd pdf-editor
```

O descarga y extrae el archivo ZIP del proyecto en una carpeta local.

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
```

Activar el entorno virtual:

En Windows:

```bash
venv\Scripts\activate
```

En macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

El proyecto requiere las siguientes librerías:

- Flask
- ReportLab

Instala todas las dependencias ejecutando:

```bash
pip install flask reportlab
```

## Estructura del proyecto

```
pdf-editor/
│
├── app.py              # Aplicación principal Flask
├── templates/
│   └── index.html      # Plantilla HTML principal
└── static/
    └── index.css       # Archivo CSS personalizado (si existe)
```

## Ejecutar la aplicación

Una vez instaladas las dependencias, puedes iniciar la aplicación con:

```bash
python app.py
```

Por defecto, la aplicación se ejecutará en `http://127.0.0.1:5000/`.

Verás una salida similar a:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

## Uso de la aplicación

1. Abre tu navegador web y visita `http://127.0.0.1:5000`
2. Verás la interfaz con un campo de texto
3. Ingresa el texto que deseas convertir a PDF
4. Haz clic en el botón "📄 Descargar PDF"
5. El navegador iniciará la descarga del archivo PDF generado

## Funcionalidades principales

### Generación de PDF

- Convierte texto plano en documentos PDF
- Manejo automático de saltos de línea y páginas
- Fuente Helvetica tamaño 12
- Márgenes de 50px en todos los lados
- Soporte para texto multilínea

### Validaciones

- Verificación de contenido vacío
- Respuesta de error si no se proporciona texto

### Interfaz de usuario

- Diseño responsivo usando Bootstrap 5.3
- Fondo con efecto de desenfoque (glassmorphism)
- Tipografía moderna con fuente Poppins
- Botones y elementos con sombras para mejor apariencia

## Personalización

### Modificar estilos

Puedes editar el archivo `static/index.css` para cambiar los estilos visuales.

### Cambiar configuración del PDF

En [app.py](file://c:\Users\ultra\Universidad\Septimo%20trimestre\Data%20science\pdf-editor\app.py), dentro de la función [download_pdf()](file://c:\Users\ultra\Universidad\Septimo%20trimestre\Data%20science\pdf-editor\app.py#L13-L49), puedes modificar:

- Tamaño de página: `pagesize=letter`
- Fuente: `c.setFont("Helvetica", 12)`
- Márgenes: `max_width = width - 100`
- Posición inicial: `y = height - 50`

## Solución de problemas comunes

### ImportError: No module named flask

Asegúrate de haber instalado Flask:

```bash
pip install flask
```

### ImportError: No module named reportlab

Asegúrate de haber instalado ReportLab:

```bash
pip install reportlab
```

### TemplateNotFound: index.html

Verifica que el archivo [index.html](file://c:\Users\ultra\Universidad\Septimo%20trimestre\Data%20science\pdf-editor\templates\index.html) exista en la carpeta `templates/`.

### La aplicación no se actualiza después de hacer cambios

Detén la aplicación (Ctrl+C) y reiníciala:

```bash
python app.py
```

## Desactivar el entorno virtual

Cuando termines de trabajar, desactiva el entorno virtual:

```bash
deactivate
```
