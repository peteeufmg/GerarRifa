from reportlab.pdfgen.canvas import Canvas
A4Size = (597, 842.4)
NumeroDePaginas = 24
index = 1
canvas = Canvas("Rifa.pdf", pagesize=A4Size)


ImageWitdh = 298
ImageHeight = 99

OFFSETNUMERO1X = 275
OFFSETNUMERO2X = 50
OFFSETNUMERO1Y = 84
OFFSETNUMERO2Y = 14

for j in range(NumeroDePaginas):
  x = 0
  y = 0
  for i in range(8):
    canvas.setFont("Helvetica",5)
    canvas.drawImage("RIFA.png",x,y,ImageWitdh,ImageHeight)
    canvas.drawImage("RIFA.png",x+ImageWitdh,y,ImageWitdh,ImageHeight)

    canvas.drawString(x+OFFSETNUMERO1X, y+OFFSETNUMERO1Y, str(index).zfill(3))
    canvas.drawString(x+OFFSETNUMERO2X, y+OFFSETNUMERO2Y, str(index).zfill(3))
    index += 1
    canvas.drawString(x+OFFSETNUMERO1X+ImageWitdh, y+OFFSETNUMERO1Y, str(index).zfill(3))
    canvas.drawString(x+OFFSETNUMERO2X+ImageWitdh, y+OFFSETNUMERO2Y, str(index).zfill(3))
    index += 1
    y += ImageHeight
  canvas.showPage()

canvas.save()