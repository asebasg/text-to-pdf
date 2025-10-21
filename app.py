from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_pdf():
    text = request.form.get('text', '')
    
    # Crear PDF en memoria
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Configurar fuente y posición
    c.setFont("Helvetica", 12)
    y = height - 40  # Empezar desde la parte superior

    # Dividir el texto en líneas para que quepa en el PDF
    lines = text.split('\n')
    for line in lines:
        # Si la línea es muy larga, podrías dividirla más (opcional)
        c.drawString(40, y, line[:100])  # Limitar a 100 caracteres por línea
        y -= 15
        if y < 40:  # Nueva página si es necesario (opcional, aquí no se implementa)
            break

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