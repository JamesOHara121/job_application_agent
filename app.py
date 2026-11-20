from dotenv import load_dotenv
from google import genai
from google.genai import types


def generate_application_answer(job_advert, question, additional_context):

    load_dotenv()
    client = genai.Client()

    with open("style_guide.md", "r") as f:
        style_guide = f.read()

    with open("experiences.md", "r") as f:
        experiences = f.read()

    prompt = f"""
You are an exceptional, highly articulate candidate applying for a competitive graduate scheme. Your task is to write a highly tailored, authentic, and compelling response to a job application question. 

You will be provided with: a strict style guide; your factual CV, motivations and STAR-format experiences; the job advert; and additional company context. You must synthesise this information to answer the application question perfectly.

<style_guide>
{style_guide}
</style_guide>

<experiences>
{experiences}
</experiences>

<job_advert>
{job_advert}
</job_advert>

<company_context>
{additional_context}
</company_context>

<application_question>
{question}
</application_question>

CRITICAL INSTRUCTIONS (READ CAREFULLY):
1. STRICT STYLE ADHERENCE: You must perfectly emulate the tone, voice, and writing rules defined in the <style_guide>. 
2. ZERO HALLUCINATION: You are strictly forbidden from making up, assuming, or exaggerating any experiences, skills, metrics, or qualifications. You must ONLY draw from the factual information provided in the <experiences> section. Map your existing STAR examples to the question.
3. STRATEGIC ALIGNMENT: Seamlessly weave in relevant keywords, core values, and mission statements from the <job_advert> and <company_context> to show deep alignment with the company.
4. WORD COUNT: You must strictly adhere to any word count or character limits specified in the <application_question>. 
5. NO CONVERSATIONAL FLUFF: Output *only* the exact final text to be copy-pasted into the application form. Do not include introductory phrases like "Certainly! Here is your answer:" or concluding remarks. Do not include markdown formatting unless permitted by the style guide. Output plain text only.

Write the response now:
"""

    # Generate response
    response = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.3)
    )
    
    return response.text


def main():
    with open("job_advert.md", "r") as f:
        job_advert = f.read()

    with open("additional_context.md", "r") as f:
        additional_context = f.read()

    question = "[Sample Question]"
    
    print(generate_application_answer(job_advert, question, additional_context))


if __name__ == "__main__":
    main()