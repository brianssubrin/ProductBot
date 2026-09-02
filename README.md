# Brian's Product Requirements Builder

An AI-powered product-management prototype built with Python, Streamlit, and the OpenAI API.

## Purpose

This application demonstrates how generative AI can help a Product Owner transform an ambiguous business objective into a structured starting point for product discovery.

The current example asks the application to identify potential improvements to the PrePass fleet-customer enrollment experience. Because the application does not have access to internal PrePass information, all company-specific recommendations are treated as hypotheses requiring validation.

## Current Capabilities

* Accepts product-management questions through a conversational interface
* Maintains conversation history during the current browser session
* Generates product ideas, user stories, and success measures
* Encourages evidence-based product discovery
* Separates assumptions from confirmed information
* Limits example responses to reduce unnecessary API usage

## Example Prompt

> Suggest five ways PrePass could improve enrollment for fleet customers.
>
> For each idea, provide:
>
> * The customer problem
> * The proposed improvement
> * One user story
> * One success metric
>
> Treat all PrePass-specific details as assumptions requiring validation. Keep the entire response under 500 words.

## Product Principles

The application is designed around several core principles:

* Begin with the customer problem rather than a predetermined solution
* Ground recommendations in facts, evidence, and measurable outcomes
* Clearly identify assumptions requiring validation
* Treat AI-generated requirements as discovery inputs, not approved requirements
* Keep people and customer outcomes ahead of processes and tools

## Technology

* Python
* Streamlit
* OpenAI Responses API
* Git and GitHub

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/brianssubrin/ProductBot.git
cd ProductBot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Install the required packages

```bash
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Configure the OpenAI API key

On Windows PowerShell:

```powershell
setx OPENAI_API_KEY "your-api-key"
```

Close and reopen PowerShell after saving the environment variable.

Never place an API key directly in the application code or commit it to GitHub.

### 5. Launch the application

```bash
.venv\Scripts\python.exe -m streamlit run app.py
```

The application should open at:

```text
http://localhost:8501
```

## Current Limitations

* The application does not have access to internal company data
* It does not independently validate its assumptions
* It does not currently search the live internet
* Conversation history is limited to the current session
* API usage incurs separate OpenAI API charges
* AI-generated recommendations require human review

## Potential Enhancements

* Structured product-discovery input fields
* Document upload and analysis
* Requirements export
* Permanent project knowledge bases
* Authentication and usage controls
* Response-length and cost controls
* Public cloud deployment
* Automated evaluation of output quality

## Disclaimer

This is an independent portfolio and learning project created by Brian Subrin. It is not affiliated with, endorsed by, or connected to PrePass. No proprietary PrePass information is included. References to PrePass are used solely as a hypothetical product-management example.
