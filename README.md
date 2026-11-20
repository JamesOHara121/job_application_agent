# Job application helper

This is a simple script that prompts Google Gemini to produce personalised answers to written job application form questions, based on your own experiences, the job advert and any additional company information you choose to give it.

## How to use:

### Initial setup

1) Get a Google Gemini API key, copy and paste it into ".env"
2) Install requirements.txt
3) Add your own skills and experiences to "experiences.md" - a template has been provided
4) Add some examples of your writing style at the bottom of "style_guide.md"

### For each different company / question:

1) Copy and paste the job advert into "job_advert.md"
2) Add any additional company context, such as values, mission, recent projects/news into "additional_context.md"
3) Copy and paste the application question into the "question" variable in main() within app.py
4) Run the script