![Icon](https://media.discordapp.net/attachments/1175270205388226630/1175516912894099526/Capture-removebg-preview.png?ex=656b8470&is=65590f70&hm=4b23a97a1c6b9f278be8c5dbbbc7627fcdad1685de885dab9a2811d50c971ad2&=&width=651&height=598)

---
Recycling is pivotal in our battle against pollution and climate change. It reduces greenhouse gas emissions, saves energy and conserves rare resources. Recycling a ton of paper can save **17 trees, 1400 liters of oil, 3.3 cubic yards of landfill space and 26500 liters of water**! That's enough to hydrate the inhabitants of a small village for an entire year! 

---
### Instructions
Our webapp helps people figure out if their trash is recyclable or compostable. All you need is your phone camera and something you want to throw away!

**Installation Instructions**
1. Clone the repository
2. Run the bash script "./run.sh" to setup the virtual environment in conda and install dependencies.
3. Change directory to the first EcoSnap directory
Option 1: Local Serving Machine
4. Run the bash command python manage.py runserver
5.  Open Browser at 127.0.0.1:8000/
Option 2: Connect from Android Mobile Device to Host Machine
4.  Enable chrome://flags/#unsafely-treat-insecure-origin-as-secure on the phone browser by registering the IP address of the Host Machine.
5. Run the bash command python manage.py runserver 0.0.0.0:8000
6. Open Chrome on the Mobile device and connect to the [registered_IP_address]:8000/
Eg. 192.168.0.1:8000/

**3 Easy Steps**
> 1. Take a picture of something you will throw away, and submit the picture for analysis
> 2. The app will tell you what type of material your object is made of and where to throw it.
> 3. Watch your stats and level go up in Game and Insights tabs.
You just helped the planet!

---
### Creation Process

**Inspiration:**

As students, a frequent challenge we encounter after eating lunch in the cafeteria is the confusion surrounding proper trash disposal as waste disposal posters often lack clarity. Additionally, there's minimal incentive to sort trash accurately, as it's often more convenient to dispose of everything in the general garbage bin. Our app aims to address these concerns by transforming trash sorting into a gamified experience. By simply taking a picture, the app guides you to the appropriate disposal bin and rewards you with points. It also provides a means to track the positive environmental impact you contribute to the Earth.

**Building:**
We incorporated several key technologies to elevate our project. Leveraging PyTorch for machine learning, we successfully implemented trash type identification. This significantly improved our ability to accurately classify items as recyclable or compostable. Additionally, the Django web framework played a pivotal role in streamlining the development process, enabling us to create a user-friendly website with minimal challenges.

**Challenges and what we learned:**
Communication and time management were one of the hardest aspects of this project. One of the major things we learned is that good planning can save a lot of time and headaches.  

---
### The Future

Based on the feedback and reception of our project, we are considering the possibility of launching it as a mobile application for your convenience. Additionally, we plan to enhance the accuracy of our machine learning model and focus on improving overall accessibility, including options for sound and an enhanced user experience (UX). Our future plans also involve integration for iOS devices. Furthermore, we aim to elevate the gaming experience by implementing features such as leaderboards and milestones to enhance the gamification aspect of the project.

Make sure to leave us a like if you want to support this project!
