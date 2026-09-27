"""
AI Career Navigator using Prompt Engineering
Author: Thallapaka Jagadiswar
Course: GenAI & LLMs
Project Type: Prompt Engineering / Rule-based LLM Simulation

This project demonstrates:
1. Role prompting
2. Instruction prompting
3. Few-shot prompting
4. Prompt assembly
5. Query classification
6. Structured career responses
7. Basic testing
"""

ROLE_PROMPT = """
You are CareerNavigator, a professional and practical career mentor.
Give concise, structured, beginner-friendly guidance.
Use only information supported by the project knowledge.
Avoid invented facts.
Prefer: Goal -> Skills -> Roadmap -> Project -> Next Step.
"""

INSTRUCTION_PROMPT = """
Response rules:
- Understand the user's career intent.
- Identify the most relevant career track.
- Give a short roadmap.
- Recommend practical skills and one project.
- Use bullet points.
- Keep the answer actionable.
"""

FEW_SHOT_EXAMPLES = """
Example 1
User: I want to become a data analyst.
Assistant:
Track: Data Analytics
- Learn Python, SQL and spreadsheets
- Practice data cleaning and visualization
- Build a dashboard project
- Publish the project with documentation

Example 2
User: I want to enter cybersecurity.
Assistant:
Track: Cybersecurity
- Learn networking and Linux basics
- Study security fundamentals
- Practice in legal training environments
- Document small security-learning projects
"""

def build_prompt(user_question: str) -> str:
    """Assemble the layered prompt used by the project."""
    return (
        ROLE_PROMPT.strip()
        + "\n\n"
        + INSTRUCTION_PROMPT.strip()
        + "\n\n"
        + FEW_SHOT_EXAMPLES.strip()
        + f"\n\nUser: {user_question}\nAssistant:"
    )

def career_response(user_text: str) -> str:
    """
    Lightweight local response engine used for demonstration.
    It simulates the behavior expected from the layered prompt.
    """
    user = user_text.lower().strip()

    if any(k in user for k in ["data analyst", "data analysis", "analytics"]):
        return """Track: Data Analytics
- Learn Python, SQL and spreadsheet fundamentals
- Practice data cleaning and visualization
- Build a sales/college-data dashboard
- Publish the project on GitHub
Next step: complete one small dataset project this week."""

    if any(k in user for k in ["ai", "machine learning", "ml", "artificial intelligence"]):
        return """Track: AI / Machine Learning
- Strengthen Python, NumPy and Pandas
- Learn regression, classification and clustering
- Practice with scikit-learn
- Build a prediction or classification project
Next step: choose one dataset and complete an end-to-end mini project."""

    if any(k in user for k in ["cyber", "security", "ethical hacking"]):
        return """Track: Cybersecurity
- Learn networking and Linux fundamentals
- Study security concepts and safe testing practices
- Practice in authorized training labs
- Build a small security-awareness or log-analysis project
Next step: create a weekly networking + Linux practice plan."""

    if any(k in user for k in ["web", "frontend", "backend", "developer", "software"]):
        return """Track: Software Development
- Learn one programming language deeply
- Practice Git, problem solving and basic databases
- Build small web applications
- Document projects with README files
Next step: build one useful CRUD-style application."""

    if any(k in user for k in ["resume", "cv", "portfolio"]):
        return """Track: Resume & Portfolio
- Keep the resume concise and project-focused
- Highlight technical skills with evidence
- Add 1–2 meaningful projects with links
- Use action verbs such as Built, Designed and Implemented
Next step: update one project description today."""

    if any(k in user for k in ["ece", "mechanical", "commerce", "non it", "switch to it"]):
        return """Track: Transition to IT
- Start with Python and SQL fundamentals
- Choose one entry path: Development, Data or Testing
- Build 1–2 beginner projects
- Create a clear portfolio and resume
Next step: choose one track and follow it for 30 days."""

    return """Track: General Career Planning
- Identify one target role
- Learn the core skills for that role
- Build a small practical project
- Improve your resume and communication
- Apply for internships or trainee opportunities
Next step: tell CareerNavigator your target role for a more focused roadmap."""

def career_navigator(user_question: str) -> str:
    """Public function used by the notebook and command line."""
    _prompt = build_prompt(user_question)
    return career_response(user_question)

def run_tests():
    """Simple functional tests for the project."""
    cases = {
        "I want to become a data analyst": "Data Analytics",
        "How can I start machine learning?": "AI / Machine Learning",
        "I want to learn cybersecurity": "Cybersecurity",
        "How do I improve my resume?": "Resume & Portfolio",
        "I want to become a software developer": "Software Development",
    }
    results = []
    for query, expected in cases.items():
        actual = career_navigator(query)
        passed = expected in actual
        results.append((query, expected, passed))
    return results

if __name__ == "__main__":
    print("=" * 60)
    print("AI CAREER NAVIGATOR — THALLAPAKA JAGADISWAR")
    print("=" * 60)
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Career question: ").strip()
        if question.lower() == "exit":
            print("Thank you for using CareerNavigator.")
            break
        print("\n" + career_navigator(question) + "\n")
