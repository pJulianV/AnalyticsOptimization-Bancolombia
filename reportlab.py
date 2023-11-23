from reportlab.pdfgen import canvas

def generate_report(data):
    pdf = canvas.Canvas("report.pdf")

    # Define el formato del informe
    pdf.setFont("Helvetica-Bold", 16)

    # Encabezado del informe
    pdf.drawString(50, 750, "Analítica Tool Report")

    # Encabezado de la tabla
    pdf.setFont("Helvetica", 12)
    y = 700
    pdf.drawString(50, y, "User ID")
    pdf.drawString(100, y, "Query")
    pdf.drawString(150, y, "Date")
    pdf.drawString(200, y, "Consumption")

    # Dibujar la tabla con los datos
    for row in data:
        pdf.drawString(50, y, row[0])
        pdf.drawString(100, y, row[1])
        pdf.drawString(150, y, row[2])
        pdf.drawString(200, y, row[3])
        y -= 15

    # Cerrar el documento
    pdf.save()