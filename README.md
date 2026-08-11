# HealthSense AI 

## Your AI-Powered Health & Wellness Companion

HealthSense AI is a polished Streamlit application that helps users explore health and wellness topics through an AI-assisted consultation flow, a wellness dashboard, smart calculators, and exportable consultation reports.

It is designed for educational use only and does not replace professional medical advice, diagnosis, or treatment.

<img width="1264" height="940" alt="Screenshot 2026-08-07 124531" src="https://github.com/user-attachments/assets/3992941a-4442-466f-92d9-9133170c3bb0" />


## What You Can Do

- Ask health and wellness questions through an AI consultation flow
- Answer follow-up questions for more structured guidance
- Track daily wellness metrics in a live dashboard
- Use calculators for BMI, water intake, sleep, and exercise guidance
- Generate and export consultation reports
- Navigate through a clean, modern Streamlit interface

## Project Structure

| Folder | Purpose |
|---|---|
| `app.py` | Main Streamlit application entry point |
| `backend/` | AI, configuration, formatting, exporting, and consultation logic |
| `calculators/` | Health calculators for BMI, water, sleep, and exercise |
| `frontend/` | UI pages, navigation, theme, dashboard, and visual components |
| `assets/` | Styling and visual assets |
| `key-vault/` | Stores the Groq API key used by the app |
| `exports/` | Saved consultation reports |

## Requirements

- Python 3.10 or newer
- A valid Groq API key
- Internet access for AI responses

## Installation

1. Open the project in VS Code or your terminal.
2. Go to the project root folder: HealthSense-AI.
3. Create a virtual environment.

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

5. Install the dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Add Your Own Groq API Key

HealthSense AI reads the API key from the key vault folder.

1. Open the folder [key-vault](key-vault).
2. Create a file named [groq-api.key](key-vault/groq-api.key).
3. Paste your own Groq API key into that file.
4. Save the file.

The app expects the key at this exact location:

```text
HealthSense-AI/key-vault/groq-api.key
```

If the file is missing or empty, the AI consultation feature will not work.

## How To Run The Project

1. Make sure your virtual environment is active.
2. Confirm that [key-vault/groq-api.key](key-vault/groq-api.key) exists and contains your Groq API key.
3. Start the Streamlit app.

   ```bash
   streamlit run app.py
   ```

4. Open the local URL shown in the terminal.
5. Use the sidebar to move between Home, AI Consultation, Wellness Dashboard, Health Calculators, Export Report, and About.

## Step-by-Step Usage Guide

### 1. Open the Home page

The home page introduces the app and gives you quick access to the main sections.

### 2. Start an AI consultation

Open AI Consultation, enter your health question, and click the start button. The app may ask follow-up questions to make the response more useful and structured.

### 3. Read the AI response

After the follow-up flow, the app shows an educational response generated through Groq.

### 4. Generate a report

If you want to keep the result, go to Export Report and preview the consultation report. Exported markdown files are saved in the [exports](exports) folder.

### 5. Track your wellness

Open the Wellness Dashboard to monitor:

- Water intake
- Sleep hours
- Exercise minutes
- BMI
- Daily healthy habits

Each checked habit updates the wellness score and completion count.

### 6. Use the calculators

The calculators help you quickly estimate:

- BMI
- Recommended daily water intake
- Sleep guidance by age
- Exercise-related wellness progress

## Configuration Check

If you want to verify that the Groq key is detected correctly, run:

```bash
python backend/config.py
```

This prints the API key file path and the default model name.

## Troubleshooting

If the app does not start:

- Check that the virtual environment is active.
- Make sure all packages from [requirements.txt](requirements.txt) are installed.
- Confirm that [key-vault/groq-api.key](key-vault/groq-api.key) exists and contains a valid Groq API key.
- Make sure you launch the app from the project root using [app.py](app.py).

## Medical Disclaimer

HealthSense AI is intended for educational purposes only.

It does not diagnose diseases, prescribe medication, or replace professional medical advice.

If you have serious or urgent symptoms, contact a qualified healthcare professional or emergency services immediately.

## Tech Stack

- Streamlit
- Groq Python SDK
- Pandas
- Plotly
- Markdown

## Why This Project Is Useful

HealthSense AI brings together AI consultation, wellness tracking, practical calculators, and report export in one place. It is simple to use, visually clean, and built to support daily health awareness.
