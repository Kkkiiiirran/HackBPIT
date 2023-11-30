# GymSo Fitness 💪
![Uploading WorkoutGymGIF.gif…]()



Welcome to GymSo Fitness – Your Virtual Gym Experience!

## Overview

GymSo Fitness is a revolutionary project that brings the gym experience to the comfort of your home, combining technology, gamification, and fitness. Our goal is to provide users with an engaging and effective way to stay fit and healthy.

## Features

### Virtual Fitness Experiences

Immerse yourself in a variety of virtual fitness experiences, ranging from VR workouts to gamified exercises. Explore different realms of exercise, each designed to make your fitness journey exciting and enjoyable.

#### VR Fitness Experiences

- **Curls Exercise**
  - Embark on a journey with VR Curls Challenge, an immersive virtual reality workout designed to enhance arm strength and endurance.

- **Shoulder Exercise**
  - Immerse yourself in the tranquility of VR Yoga Sessions, blending technology and mindfulness to promote a healthier lifestyle.

- **Pushups Exercise**
  - Dance your way to fitness with VR Zumba Fusion, a high-energy virtual reality dance workout that adds a fun and rhythmic twist to your exercise routine.

### Personalized Dieting Options

Tailor your diet to achieve specific muscle gains with personalized dieting options. Whether you're focusing on building shoulder strength, improving endurance, or working on core muscles, we've got you covered.

### Gamified Gym Experience

Transform your workout routine into a fun and interactive experience. Earn rewards, track your progress, and compete with friends in fitness challenges. Our gamification approach makes exercising at home enjoyable and motivating.
## Pages

### 1. [Homepage](#homepage)

Provide an overview of GymSo Fitness, its features, and how users can get started.

### 2. [Exercises Page](#exercises-page)

Explore the different exercises and virtual fitness experiences available in GymSo Fitness.

### 3. [Calorie Page](#calorie-page)

Learn about personalized dieting options and how GymSo Fitness helps you achieve your fitness goals.

### 4. [ML Models](#ml-models)

Discover the machine learning models used in GymSo Fitness to enhance the user experience.

# 1- LLM Chatbot

Sure, here's a basic README file for your Python script and the command to run it:

### Overview:
This project utilizes the LangChain library to create a language model chain that generates specific answers to questions related to exercise, workout, health, and fitness. The chain is built using Hugging Face's model from the repository "tiiuae/falcon-7b-instruct."

### Dependencies:
- Python 3.6 or higher
- Install dependencies using: `pip install langchain chainlit`

### Usage:
1. Set up your Hugging Face API token:
   - Get your Hugging Face API token from [Hugging Face](https://huggingface.co/settings/token).
   - Replace `'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'` with your actual API token in the `LLM.py` script.

2. Run the script:
   ```bash
   chainlit run LLM.py
   ```

# 2 - Posture CV
## Project Title: Bicep Curls Counter with Pose Detection

### Overview:
This project uses the MediaPipe library for pose detection to count bicep curls based on the movement of the left and right arms. The script captures webcam input, detects key landmarks on the user's body, and calculates the angle between the shoulder, elbow, and wrist to determine a bicep curl. The counts for left and right bicep curls are displayed on the screen.

### Dependencies:
- Python 3.6 or higher
- OpenCV (`cv2`)
- NumPy (`numpy`)
- MediaPipe (`mediapipe`)

Install dependencies using:
```bash
pip install opencv-python numpy mediapipe
```

### Usage:
1. Clone the repository:
   ```bash
   git clone https://github.com/prtm1908/Gymso-VR-Fitness.git
   cd your-repo
   ```

2. Run the script:
   ```bash
   python app.py
   ```

### Instructions:
- The script captures webcam input and uses the MediaPipe pose detection model to identify key landmarks on the body.
- The angle between the shoulder, elbow, and wrist is calculated to determine a bicep curl.
- Counts for left and right bicep curls are displayed on the screen.
- Press 'r' to reset the bicep curl counters.
- Press 'Esc' to exit the application.

### Additional Notes:
- Ensure you have a webcam connected and accessible.
- This script assumes that the left and right bicep curls are performed independently.
- Adjust the angle thresholds in the script based on your specific exercise form.

### Model Information:
- The script uses the MediaPipe pose detection model for landmark identification.
- Additionally, a model for shoulder and chest detection is used (provide details on the model and how to obtain it).

Feel free to customize the README file based on your specific project details and requirements.

### Input:
The script expects input questions related to health, fitness, exercise, and workout. It generates specific answers with references to exercises in an academic style suitable for an audience aged 18-25.

### Output:
The script outputs a paragraph-length response based on the provided question.

### Example Usage:
```bash
python app.py
```

### Additional Notes:
- Ensure you have proper permissions and access to the specified Hugging Face model repository.
- The script uses the `cl` and `langchain` libraries for chat-based language model chaining. Make sure they are installed using the provided `pip install` command.

## Getting Started

To start your virtual fitness journey with GymSo Fitness, follow these steps:

1. Clone the repository:
   ```bash
   git clone https:/github.com/prtm1908/Gymso-VR-Fitness.git
