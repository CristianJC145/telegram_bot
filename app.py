# -*- coding: utf-8 -*-
'''
Bot para telegram
'''
import random
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)
from models import models

# [Opcional] Recomendable poner un log con los errores que apareceran por pantalla.
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Bienvenido, para ver la lista de comandos escribe /help", parse_mode=ParseMode.HTML)

	# Podemos llamar a otros comandos, sin que se haya activado en el chat (/help).

def registro_gasto(update, context):
	context.bot.send_message(update.message.chat_id,"Hola, por favor escribenos en numeros sin espacios ni comas el monto que deseas ingresar")
	valorGasto = int(context.args[0])
	fecha = context.args[1]
	nombreGasto=context.args[2]
	models.monto(valorGasto, fecha, nombreGasto)


def reportes(update, context):
	''' Lista de Reportes '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, """Lista de reportes disponibles:
	 1. /grafico_torta: Grafico de torta, porcentaje de ingresos y gastos entre fechas especificas.
	 2. /grafico_barra: Grafico de barras (Trimestre, semestre o anual) .
	 3. /descargar_reporte : Reporte excel o pdf con los ingresos o gastos de una fecha especifica.""", parse_mode=ParseMode.HTML)

	# Podemos llamar a otros comandos, sin que se haya activado en el chat (/help).

def help(update, context):
	''' HELP '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, """Esta es la lista de comandos para el funcionamiento del bot:
	1. /Registro_Gasto : aqui debes ingresar algun gasto realizado en una fecha especifica.
	2. /Registro_Ingreso : aqui debes ingresa algun ingreso que hayas realizado con una fecha especifica.
	3. /Reportes : aqui se mostraran una lista de reportes de tu interes.
	
	""", parse_mode=ParseMode.HTML)

	# Podemos llamar a otros comandos, sin que se haya activado en el chat (/help).

def main():
	TOKEN="5377368149:AAFCOwoMpyKlKb4zdKJ10vOM2UXwstORxNE"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	# /comandos
	dp.add_handler(CommandHandler('help',	help))
	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('reportes',	reportes))
	dp.add_handler(CommandHandler('registro_gasto',	registro_gasto))

	dp.add_error_handler(error_callback)
    # Comienza el bot
	updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	print(('[Nombre del bot] Start...'))
	main()