from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import config

def chouin(update: Update, context: CallbackContext) -> None:
    # Vérifiez si le message est une réponse
    if update.message.reply_to_message:
        original_text = update.message.reply_to_message.text
        # Modifiez le texte
        modified_text = ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(original_text))
        # Envoyez le message modifié
        update.message.reply_text(modified_text)
    else:
        update.message.reply_text("Veuillez répondre à un message avec /chouin.")

def main():
    # Utilisez le token du bot à partir du fichier de configuration
    updater = Updater(config.TOKEN)

    dp = updater.dispatcher

    # Ajoutez un gestionnaire pour la commande /chouin
    dp.add_handler(CommandHandler('chouin', chouin))

    # Démarrez le bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()