# PDF Editor - Convertidor de Texto a PDF

## 📋 Descripción

Una aplicación web simple y elegante que permite a los usuarios convertir texto plano en documentos PDF. Desarrollada con Flask como backend y una interfaz moderna usando HTML, CSS y Bootstrap. Utiliza ReportLab para la generación de PDFs de alta calidad.

## ✨ Características

- **Conversión de Texto a PDF**: Transforma cualquier texto en un documento PDF descargable.
- **Interfaz Moderna**: Diseño responsivo con efecto glassmorphism y tipografía Poppins.
- **Validación de Datos**: Verifica que se proporcione texto antes de generar el PDF.
- **Manejo de Texto Multilínea**: Soporta saltos de línea y ajuste automático de texto.
- **Configuración Personalizable**: Fácil modificación de fuentes, márgenes y tamaños de página.
- **Generación en Memoria**: Los PDFs se crean en memoria para mayor eficiencia.

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Generación de PDF**: ReportLab
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Fuentes**: Google Fonts (Poppins)
- **Iconos**: Bootstrap Icons

## 📋 Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd pdf-editor
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
python -m venv venv
```

**Activar entorno virtual:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:

```bash
pip install flask reportlab
```

## 📁 Estructura del Proyecto

```
pdf-editor/
│
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
│
└── templates/
    ├── index.html        # Plantilla principal
    └── index.css         # Estilos CSS personalizados
```

## ▶️ Uso

### Ejecutar la Aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://127.0.0.1:5000`

### Cómo Usar

1. Abre tu navegador y visita `http://127.0.0.1:5000`
2. Ingresa el texto que deseas convertir en el área de texto
3. Haz clic en "📄 Descargar PDF"
4. El archivo PDF se descargará automáticamente

## ⚙️ Configuración del PDF

En `app.py`, puedes modificar los siguientes parámetros en la función `download_pdf()`:

```python
# Tamaño de página
pagesize=letter

# Fuente y tamaño
c.setFont("Helvetica", 12)

# Márgenes
max_width = width - 100  # 50px a cada lado

# Posición inicial
y = height - 50
```

## 🔧 Personalización

### Modificar Estilos

Edita `templates/index.css` para cambiar la apariencia visual.

### Cambiar la Interfaz

Modifica `templates/index.html` para alterar la estructura HTML.

## 🐛 Solución de Problemas

### Error: "No module named flask"
```bash
pip install flask
```

### Error: "No module named reportlab"
```bash
pip install reportlab
```

### Error: "TemplateNotFound"
Verifica que `templates/index.html` exista.

### La aplicación no se actualiza
- Detén la aplicación con `Ctrl+C`
- Reinicia con `python app.py`

## 🤝 Contribución

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Sebastian Ospina**
- **Juan Garcia**
- **Ricardo Vega**

---

**Grupo 1 - Universidad** 🐧 Hazlo por Mort
