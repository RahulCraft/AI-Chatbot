from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import os
from dotenv import load_dotenv
from openai import OpenAI  # ✅ new import

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)  # ✅ new client object

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')

        predefined = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hi there! Need any help?",
            "hey": "Hey! How can I help you?",
            "good morning": "Good morning! Hope you have a productive day!",
            "good afternoon": "Good afternoon! How can I assist you?",
            "good evening": "Good evening! What can I do for you?",
            "how are you": "I'm just a bot, but I'm functioning perfectly! How can I assist you?",
            "what can you do": "I can help you with your queries, just ask me something!",
            "who are you": "I'm your virtual assistant, here to help you out!",
            "help": "Sure, I'm here to help. Please tell me your question.",
            "support": "You can ask your question here, and I'll do my best to assist you.",
            "thanks": "You're welcome!",
            "thank you": "Glad I could help!",
            "bye": "Goodbye! Have a nice day!",
            "goodbye": "See you later! Stay safe!",
            #Company & About
            "what is one aim": "One Aim is an IT solutions company that helps businesses grow through modern digital services.",
            "tell me about your company": "We are One Aim IT Solutions, offering web, app, and AI development services.",
            "what do you guys do": "We help businesses go digital with websites, apps, AI tools, and cloud services.",
            "who are you": "We’re One Aim IT Solutions – experts in tech-driven business transformation.",
            "what does your company specialize in": "We specialize in building websites, apps, AI solutions, and providing digital growth services.",
            #Web & App Development
            "do you build websites": "Yes! We design and develop fast, responsive, and modern websites.",
            "i want a website for my business": "Sure! We create custom websites based on your business needs.",
            "can you make an e-commerce website": "Yes, we develop full-featured e-commerce websites with payment gateways and inventory.",
            "can you make mobile apps": "Yes, we build Android and iOS apps for all kinds of businesses.",
            "i need an app for my startup": "We can help! We specialize in building startup-friendly mobile applications.",
            #AI/ML & Automation
            "do you provide ai services": "Yes, we offer AI/ML solutions like chatbots, automation, and prediction tools.",
            "can you create a chatbot": "Yes! We build smart chatbots for websites, support, and automation.",
            "i want ai for my business": "We can build AI tools that automate tasks and improve your workflow.",
            "do you offer machine learning solutions": "Yes, we create ML models for data analysis, predictions, and automation.",
            #Cloud & Digital Solutions
            "do you work with cloud": "Yes, we offer cloud integration, hosting, and deployment services.", 
            "can you help me go online": "Absolutely! We help with websites, apps, cloud hosting, and digital marketing.",
            "do you provide digital solutions": "Yes, from cloud platforms to automation tools, we offer full digital support.",
            #Consulting & Industries
            "what industries do you serve": "We work with healthcare, education, retail, logistics, and more.",
            "which type of companies do you help": "Startups, SMEs, and enterprises looking for tech growth solutions.",
            "do you offer tech consulting": "Yes, we guide businesses on how to use tech to grow and save costs.",
            #Location & Contact
            "how can i contact you": "You can visit our Contact Us page on the website to reach out.",
            "where are you based": "We are based in India and serve clients worldwide.",
            "how to reach your team": "Use the form on our website or email us directly.",
            #Why Choose One Aim
            "why should i choose one aim": "We deliver tailored, scalable, and high-quality tech solutions with full support.",
            "what makes you different": "We combine innovation with business understanding to build the best digital products.",
            "do you offer custom solutions": "Yes, everything we build is tailored to your business needs.",

        }

        if user_message.lower() in predefined:
            bot_reply = predefined[user_message.lower()]
        else:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=[{"role": "user", "content": user_message}]
                )
                bot_reply = response.choices[0].message.content
            except Exception as e:
                bot_reply = f"Sorry, something went wrong: {str(e)}"

        ChatMessage.objects.create(user_message=user_message, bot_response=bot_reply)

        return JsonResponse({'reply': bot_reply})
