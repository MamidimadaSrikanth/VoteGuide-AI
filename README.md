VoteGuide AI:-
VoteGuide AI is an interactive web assistant that helps users understand the election process in India — including eligibility, registration steps, timelines, and voting guidance — in a simple and user-friendly way.

Live Demo:-
https://voteguide-ai-szzt.onrender.com
https://voteguide-ai.onrender.com             
https://voteguide-ai.onrender.com/

Project Overview:-
This project is designed to simplify the election process for citizens by providing:
* Smart chatbot assistance
* Step-by-step voting guidance
* Eligibility checker
* Election timeline visualization
* Voice input support
* Clean and modern UI

Features:-
* Interactive Chat Assistant
* Answers questions like:
  * “How do I vote?”
  * “What documents are required?”
  * “Am I eligible?”

Eligibility Checker:-
  * Checks voting eligibility based on:
  * Age
  * Citizenship

Election Timeline:-
* Displays key election phases:
  * Registration
  * Campaign
  * Voting
  * Counting

Voice Input:-
* Users can speak instead of typing (browser-supported)

Polling Booth Finder:-
* Integrated Google Maps to locate nearby polling booths

Tech Stack:-
        
        * Backend
             1) Python
             2) Flask

        *) Frontend
             1) HTML
             2) CSS
             3) JavaScript

Deployment:-
        Render


Project Structure:-

VoteGuide-AI/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── utils/
│   ├── eligibility.py
│   └── timeline.py
```


Installation & Setup:-
   1️⃣ Clone the repository
            git clone https://github.com/MamidimadaSrikanth/VoteGuide-AI.git
            cd VoteGuide-AI
   2️⃣ Install dependencies
             pip install -r requirements.txt
   3️⃣ Run the application
            python app.py
   4️⃣ Open in browser
             http://127.0.0.1:8080


Deployment:-
      This project is deployed using **Render**.
      Steps:
            * Push code to GitHub
            * Connect repository to Render
            * Set:
                  * Build command: `pip install -r requirements.txt`
                  * Start command: `gunicorn app:app`

How It Works:-
* User interacts through chat or UI
* Requests are sent to Flask backend
* Backend processes logic via:
  * `chatbot.py`
  * `eligibility.py`
  * `timeline.py`
* Response is returned and displayed dynamically

Testing:-
Run:
pytest

Security:-
- Input validation implemented
- Safe JSON parsing
- Error handling

Google Services:-
- Integrated Google Maps for polling booth discovery

Assumptions:-
* User is interacting for Indian elections
* Internet connection is available
* Voice input works only in supported browsers

Security Considerations:-
* No sensitive user data is stored
* Input is handled safely via backend routes
* No external API keys exposed

Testing:-
* Tested locally using Flask server
* Verified all endpoints:
  * `/chat`
  * `/eligibility`
  * `/timeline`

Future Enhancements:-
      * 🌐 Multi-language support (Telugu / Hindi)
      * 🤖 AI integration (Gemini / GPT)
      * 📡 Real-time election data APIs
      * 🔐 User authentication system
      * 📊 Analytics dashboard

Author:-
Mamidimada Srikanth
mamidimadasrikanth143@gmail.com (mailto:mamidimadasrikanth143@gmail.com)
🔗 https://www.linkedin.com/in/mamidimada-srikanth-68aa20289

Project Post Link:-
https://www.linkedin.com/posts/mamidimada-srikanth-68aa20289_github-mamidimadasrikanthvoteguide-ai-activity-7456710925107257344-cxKZ?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEYYrcoBHq0S6h2ctz10s-GH4UShWC8Wkdo

