import nltk
import ssl

# Contourner la vérification SSL pour les téléchargements NLTK
ssl._create_default_https_context = ssl._create_unverified_context

# Télécharger les ressources NLTK
nltk.download('stopwords')
nltk.download('punkt')

# Restaurer le paramètre de vérification SSL par défaut
ssl._create_default_https_context = ssl._create_default_https_context

# Continuer avec le reste de votre code
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Créer un nouveau robot de discussion nommé Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

# Ajouter des exemples de dialogues supplémentaires
trainer.train([
    "Bonjour!",
    "Salut, comment puis-je vous aider aujourd'hui?",
    "Quels sont les types de vols disponibles?",
    "Nous proposons des vols réguliers et des vols charter vers diverses destinations.",
    "Comment puis-je annuler ma réservation?",
    "Pour annuler une réservation, veuillez nous contacter par téléphone ou par e-mail.",
    "Quelles sont les informations nécessaires pour réserver un vol?",
    "Nous aurons besoin de votre nom complet, de vos dates de voyage et des détails de paiement.",
    "Pouvez-vous m'aider avec des informations sur les hôtels à destination?",
    "Bien sûr, je peux vous fournir des recommandations d'hôtels une fois votre destination confirmée.",
    "Merci beaucoup!",
    "De rien! Si vous avez d'autres questions, n'hésitez pas à demander.",
    "Au revoir!",
    "Au revoir! Prenez soin de vous."
])

# Interaction avec l'utilisateur
print("Bonjour! Je suis Charlie, votre assistant virtuel. Comment puis-je vous aider aujourd'hui?")
while True:
    user_input = input("Vous: ")

    if user_input.lower() in ['exit', 'quit', 'bye', 'au revoir']:
        print("Charlie: Au revoir! N'hésitez pas à revenir si vous avez d'autres questions.")
        break

    # Obtenir une réponse basée sur l'entrée de l'utilisateur
    response = chatbot.get_response(user_input)
    print("Charlie:", response)