from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '').lower()  # convert to lowercase

        # Keyword-based predefined responses
        predefined_keywords = {
            # Greetings
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
            "name": "Nice Name! How can I assist you today?",
            "ok": "Alright! Feel free to ask more about our company or services.",
            "okay": "Alright! Feel free to ask more about our company or services.",

            # About One Aim IT Solutions
            "one aim": """One Aim is a modern IT solutions company that helps businesses grow digitally with services like web development, app development, AI tools, and cloud solutions. We focus on delivering custom, scalable, and innovative technology.<br><br>
                          🌐 <a href='https://theoneaim.in' target='_blank'>Visit our website for more details →</a>""",
            "oneaim": """One Aim is a modern IT solutions company that helps businesses grow digitally with services like web development, app development, AI tools, and cloud solutions. We focus on delivering custom, scalable, and innovative technology.<br><br>
                          🌐 <a href='https://theoneaim.in' target='_blank'>Visit our website for more details →</a>""",
            "one aim it solutions": """One Aim is a modern IT solutions company that helps businesses grow digitally with services like web development, app development, AI tools, and cloud solutions. We focus on delivering custom, scalable, and innovative technology.<br><br>
                          🌐 <a href='https://theoneaim.in' target='_blank'>Visit our website for more details →</a>""",
            "oneaimitsolutions": """One Aim is a modern IT solutions company that helps businesses grow digitally with services like web development, app development, AI tools, and cloud solutions. We focus on delivering custom, scalable, and innovative technology.<br><br>
                          🌐 <a href='https://theoneaim.in' target='_blank'>Visit our website for more details →</a>""",
            "one aim it solution": """One Aim is a modern IT solutions company that helps businesses grow digitally with services like web development, app development, AI tools, and cloud solutions. We focus on delivering custom, scalable, and innovative technology.<br><br>
                          🌐 <a href='https://theoneaim.in' target='_blank'>Visit our website for more details →</a>""",
            
            "company": """We’re One Aim IT Solutions – experts in tech-driven business transformation. We help businesses grow with websites, apps, AI tools, and digital services.<br><br>
                          Learn more at 👉 <a href='https://theoneaim.in' target='_blank'>theoneaim.in</a>""",
            "organization": """We’re One Aim IT Solutions – experts in tech-driven business transformation. We help businesses grow with websites, apps, AI tools, and digital services.<br><br>
                          Learn more at 👉 <a href='https://theoneaim.in' target='_blank'>theoneaim.in</a>""",


            #services
            "services": """Absolutely! ONE AIM provides a wide range of modern IT services designed to drive innovation and growth.<br>
                          ☁️ Cloud Services<br>
                          💻 Web Development<br>
                          🤖 AI/ML<br>
                          📈 Digital Marketing<br><br>
                          ✨ <a href='https://theoneaim.in' target='_blank'>Discover how our services can transform your business →</a>""",
            "service": """Absolutely! ONE AIM provides a wide range of modern IT services designed to drive innovation and growth.<br>
                          ☁️ Cloud Services<br>
                          💻 Web Development<br>
                          🤖 AI/ML<br>
                          📈 Digital Marketing<br><br>
                          ✨ <a href='https://theoneaim.in' target='_blank'>Discover how our services can transform your business →</a>""",
           
            # Cloud Services
            "cloud services": """☁️ <b>Cloud Services</b><br>
                                 We help businesses scale with secure, cost-effective cloud solutions.<br><br>
                                 - Cloud Migration<br>
                                 - DevOps & Automation<br>
                                 - Infrastructure Management<br>
                                 - Cloud Security<br><br>
                                🔗 <a href='https://theoneaim.in/cloud-services' target='_blank'>Explore</a>""",

            "cloud service": """☁️ <b>Cloud Services</b><br>
                                We help businesses scale with secure, cost-effective cloud solutions.<br><br>
                                - Cloud Migration<br>
                                - DevOps & Automation<br>
                                - Infrastructure Management<br>
                                - Cloud Security<br><br>
                               🔗 <a href='https://theoneaim.in/cloud-services' target='_blank'>Explore</a>""",
            "cloud ": """☁️ <b>Cloud Services</b><br>
                               We help businesses scale with secure, cost-effective cloud solutions.<br><br>
                               - Cloud Migration<br>
                               - DevOps & Automation<br>
                               - Infrastructure Management<br>
                               - Cloud Security<br><br>
                              🔗 <a href='https://theoneaim.in/cloud-services' target='_blank'>Explore</a>""",

            "aws cloud": """☁️ <b>Cloud Services</b><br>
                                We help businesses scale with secure, cost-effective cloud solutions.<br><br>
                               - Cloud Migration<br>
                               - DevOps & Automation<br>
                               - Infrastructure Management<br>
                               - Cloud Security<br><br>
                              🔗 <a href='https://theoneaim.in/cloud-services' target='_blank'>Explore</a>""",

            # Web Development
            "web development": """💻 <b>Web Development</b><br>
                                   ONE AIM builds high-performance, scalable websites and platforms tailored to your business needs.<br><br>
                                  - Responsive Web Applications<br>
                                  - Custom Web Solutions<br>
                                  - UI/UX Design<br>
                                  - E-Commerce Development<br>
                                  - API Integration & Backend Services<br><br>
                                  🔗 <a href='https://theoneaim.in/development-services' target='_blank'>Explore Web Development</a>""",
            "web dev": """💻 <b>Web Development</b><br>
                                   ONE AIM builds high-performance, scalable websites and platforms tailored to your business needs.<br><br>
                                  - Responsive Web Applications<br>
                                  - Custom Web Solutions<br>
                                  - UI/UX Design<br>
                                  - E-Commerce Development<br>
                                  - API Integration & Backend Services<br><br>
                                  🔗 <a href='https://theoneaim.in/development-services' target='_blank'>Explore Web Development</a>""",
            "website": """💻 <b>Web Development</b><br>
                                   ONE AIM builds high-performance, scalable websites and platforms tailored to your business needs.<br><br>
                                  - Responsive Web Applications<br>
                                  - Custom Web Solutions<br>
                                  - UI/UX Design<br>
                                  - E-Commerce Development<br>
                                  - API Integration & Backend Services<br><br>
                                  🔗 <a href='https://theoneaim.in/development-services' target='_blank'>Explore Web Development</a>""",
            "web application": """💻 <b>Web Development</b><br>
                                   ONE AIM builds high-performance, scalable websites and platforms tailored to your business needs.<br><br>
                                  - Responsive Web Applications<br>
                                  - Custom Web Solutions<br>
                                  - UI/UX Design<br>
                                  - E-Commerce Development<br>
                                  - API Integration & Backend Services<br><br>
                                  🔗 <a href='https://theoneaim.in/development-services' target='_blank'>Explore Web Development</a>""",
            "web": """💻 <b>Web Development</b><br>
                                   ONE AIM builds high-performance, scalable websites and platforms tailored to your business needs.<br><br>
                                  - Responsive Web Applications<br>
                                  - Custom Web Solutions<br>
                                  - UI/UX Design<br>
                                  - E-Commerce Development<br>
                                  - API Integration & Backend Services<br><br>
                                  🔗 <a href='https://theoneaim.in/development-services' target='_blank'>Explore Web Development</a>""",

            # AI/ML Services
            "ai/ml": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "ai": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "ml": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "ai and ml": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "ai & ml": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "ai/ml": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "automation": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",
            "machine learning": """🤖 <b>AI/ML Services</b><br>
                        ONE AIM delivers intelligent, data-driven solutions that enhance automation, decision-making, and customer experience using Artificial Intelligence and Machine Learning technologies.<br><br>
                        🔍 AI Consultation<br>
                        🧠 ML Model Development<br>
                        🛠️ Data Engineering & Preprocessing<br>
                        📊 Predictive Analytics & Business Intelligence<br>
                        🤖 AI Chatbots & Virtual Assistants<br>
                        🔄 Workflow Automation & Smart Integration<br><br>
                        🔗 <a href='https://theoneaim.in/ai-ml-services' target='_blank'>Explore AI/ML Services</a>""",

            # Digital Marketing
            "digital marketing": """📈 <b>Digital Marketing</b><br>
                                    Grow your brand online with ONE AIM's data-driven digital marketing strategies that maximize reach, engagement, and ROI.<br><br>
                                    🔍 SEO Optimization (On-page & Off-page)<br>
                                    📱 Social Media Marketing (Instagram, Facebook, LinkedIn)<br>
                                    🎯 Performance Campaigns (Google Ads, Meta Ads)<br>
                                    📝 Content Strategy & Blogging<br>
                                    📧 Email Marketing & Lead Nurturing<br>
                                    📈 Analytics & Conversion Tracking<br><br>
                                    🔗 <a href='https://theoneaim.in/digital-marketing' target='_blank'>Explore Digital Marketing</a>""",
            "digital": """📈 <b>Digital Marketing</b><br>
                                    Grow your brand online with ONE AIM's data-driven digital marketing strategies that maximize reach, engagement, and ROI.<br><br>
                                    🔍 SEO Optimization (On-page & Off-page)<br>
                                    📱 Social Media Marketing (Instagram, Facebook, LinkedIn)<br>
                                    🎯 Performance Campaigns (Google Ads, Meta Ads)<br>
                                    📝 Content Strategy & Blogging<br>
                                    📧 Email Marketing & Lead Nurturing<br>
                                    📈 Analytics & Conversion Tracking<br><br>
                                    🔗 <a href='https://theoneaim.in/digital-marketing' target='_blank'>Explore Digital Marketing</a>""",
           
            # about us
            #  🐦 <a href='https://twitter.com/OneAimIT' target='_blank'>Twitter</a><br>  ( ye abhi nahi hai hamari website me to baad me hoga tab integrate karna hai)
            "know more": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",
            "social media": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",
            "instagram": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",
            "youtube": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",
            "facebook": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",
            "linkedin": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",
            "twitter": """🏢 <b>Know more about our organization</b><br>
                            We’d love to connect with you on social media! Find us on your favorite platforms:<br><br>
                            🔗 <a href='https://www.linkedin.com/company/oneaim-it-solutions/posts/?feedView=all' target='_blank'>LinkedIn</a><br>
                            📸 <a href='https://www.instagram.com/oneaimitsolutions/' target='_blank'>Instagram</a><br>
                            📘 <a href='https://www.facebook.com/profile.php?id=61575261976224' target='_blank'>Facebook</a><br>
                            ▶️ <a href='https://www.youtube.com/@OneAimITSolutions' target='_blank'>YouTube</a>""",

            # Industry-specific
            "industries": """🌐 <b>Industries We Are In</b><br>
                              We provide industry-specific technology solutions. Choose your industry of interest:<br><br>
                             🚗 <a href='https://theoneaim.in/automobile' target='_blank'>Automobile</a><br>
                             📞 <a href='https://theoneaim.in/telecommunication' target='_blank'>Telecommunications</a><br>
                             🏥 <a href='https://theoneaim.in/healthcare' target='_blank'>Healthcare</a><br>
                             🛒 <a href='https://theoneaim.in/e-commerce' target='_blank'>E-Commerce</a><br>
                             💰 <a href='https://theoneaim.in/finance-&-banking' target='_blank'>Finance & Banking</a><br>
                             🎓 <a href='https://theoneaim.in/education' target='_blank'>Education</a><br>
                             🛡️ <a href='https://theoneaim.in/government-&-defense' target='_blank'>Government & Defense</a>""",
            "industry": """🌐 <b>Industries We Are In</b><br>
                              We provide industry-specific technology solutions. Choose your industry of interest:<br><br>
                             🚗 <a href='https://theoneaim.in/automobile' target='_blank'>Automobile</a><br>
                             📞 <a href='https://theoneaim.in/telecommunication' target='_blank'>Telecommunications</a><br>
                             🏥 <a href='https://theoneaim.in/healthcare' target='_blank'>Healthcare</a><br>
                             🛒 <a href='https://theoneaim.in/e-commerce' target='_blank'>E-Commerce</a><br>
                             💰 <a href='https://theoneaim.in/finance-&-banking' target='_blank'>Finance & Banking</a><br>
                             🎓 <a href='https://theoneaim.in/education' target='_blank'>Education</a><br>
                             🛡️ <a href='https://theoneaim.in/government-&-defense' target='_blank'>Government & Defense</a>""",

            #location
            "address": "📍 <strong>Office Address:</strong><br>Office No-123, Omega<br>Anukampa, Near Sanskrit College<br>Bhankrota, Jaipur, India<br><br>We also serve clients across the globe!",
            "located": "📍 <strong>Office Address:</strong><br>Office No-123, Omega<br>Anukampa, Near Sanskrit College<br>Bhankrota, Jaipur, India<br><br>We also serve clients across the globe!",
            "location": "📍 <strong>Office Address:</strong><br>Office No-123, Omega<br>Anukampa, Near Sanskrit College<br>Bhankrota, Jaipur, India<br><br>We also serve clients across the globe!",
            "map": "📍 <strong>Office Address:</strong><br>Office No-123, Omega<br>Anukampa, Near Sanskrit College<br>Bhankrota, Jaipur, India<br><br>We also serve clients across the globe!",        
            "rasta": "📍 <strong>Office Address:</strong><br>Office No-123, Omega<br>Anukampa, Near Sanskrit College<br>Bhankrota, Jaipur, India<br><br>We also serve clients across the globe!",
            "location": "📍 <strong>Office Address:</strong><br>Office No-123, Omega<br>Anukampa, Near Sanskrit College<br>Bhankrota, Jaipur, India<br><br>We also serve clients across the globe!",
            #contact
            "call": "You can contact us through the following ways:<br><br>📞 <strong>Phone:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;+91 89552 49714<br>&nbsp;&nbsp;&nbsp;&nbsp;+91 74269 95879<br>&nbsp;&nbsp;&nbsp;&nbsp;+1 (925) 389-4120<br><br>✉️ <strong>Email:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;info@theoneaim.co.in<br><br>🌐 <strong>Website:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;<a href='https://theoneaim.in/contact' target='_blank'>Visit our Contact Us page</a><br><br>We’re here to help you anytime!",
            "contact": "You can contact us through the following ways:<br><br>📞 <strong>Phone:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;+91 89552 49714<br>&nbsp;&nbsp;&nbsp;&nbsp;+91 74269 95879<br>&nbsp;&nbsp;&nbsp;&nbsp;+1 (925) 389-4120<br><br>✉️ <strong>Email:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;info@theoneaim.co.in<br><br>🌐 <strong>Website:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;<a href='https://theoneaim.in/contact' target='_blank'>Visit our Contact Us page</a><br><br>We’re here to help you anytime!",
            "connect": "You can contact us through the following ways:<br><br>📞 <strong>Phone:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;+91 89552 49714<br>&nbsp;&nbsp;&nbsp;&nbsp;+91 74269 95879<br>&nbsp;&nbsp;&nbsp;&nbsp;+1 (925) 389-4120<br><br>✉️ <strong>Email:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;info@theoneaim.co.in<br><br>🌐 <strong>Website:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;<a href='https://theoneaim.in/contact' target='_blank'>Visit our Contact Us page</a><br><br>We’re here to help you anytime!",
            "calling": "You can contact us through the following ways:<br><br>📞 <strong>Phone:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;+91 89552 49714<br>&nbsp;&nbsp;&nbsp;&nbsp;+91 74269 95879<br>&nbsp;&nbsp;&nbsp;&nbsp;+1 (925) 389-4120<br><br>✉️ <strong>Email:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;info@theoneaim.co.in<br><br>🌐 <strong>Website:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;<a href='https://theoneaim.in/contact' target='_blank'>Visit our Contact Us page</a><br><br>We’re here to help you anytime!",
 
        }

        # Matching logic — check if any keyword is in the user message
        matched = False
        for keyword, answer in predefined_keywords.items():
            if keyword in user_message:
                bot_reply = answer
                matched = True
                break

        # Fallback if nothing matched
        if not matched:
            bot_reply = "Something went wrong. Please only ask about One Aim IT Solutions."

        # ✅ Save to database
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_reply)

        return JsonResponse({'reply': bot_reply})
    
    return JsonResponse({'reply': 'Invalid request method.'}, status=400)
