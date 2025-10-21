from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_pdf():
    text = request.form.get('text_content', '')
    
    if not text.strip():
        return "No se proporcionó texto", 400
    
    # Crear PDF en memoria
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Configurar fuente y posición
    c.setFont("Helvetica", 12)
    y = height - 50
    max_width = width - 100  # Margen de 50px a cada lado

    # Dividir el texto en líneas y ajustar al ancho
    lines = text.split('\n')
    for line in lines:
        # Dividir líneas largas
        wrapped_lines = simpleSplit(line, "Helvetica", 12, max_width)
        for wrapped_line in wrapped_lines:
            if y < 50:
                c.showPage()
                y = height - 50
            c.drawString(50, y, wrapped_line)
            y -= 20

    c.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name='texto.pdf',
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)