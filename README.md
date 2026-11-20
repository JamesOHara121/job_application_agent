# Job application helper

This is a simple script that prompts Google Gemini to produce personalised answers to written job application form questions, based on your own experiences, the job advert and any additional company information you choose to give it.

## How to use:

1) Get a Google Gemini API key, copy and paste it into ".env"
2) Install requirements
3) Add your own skills and experiences to "experiences.md" - a template has been provided
4) Copy and paste the job advert into "job_advert.md"
5) Add any additional company context, such as values, mission, recent projects/news into "additional_context.md"
6) Copy and paste the application question into the "question" variable in main() within app.py
7) Run the script