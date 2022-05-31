from config.database import db

def monto(valorGasto, fecha, nombreGasto):
    cursor = db.cursor()
    cursor.execute("""insert into gastos 
    (nombre_gasto, 
    valor, 
    fecha
    ) values (%s,%s,%s)""", (nombreGasto, valorGasto, fecha,))
    db.commit()