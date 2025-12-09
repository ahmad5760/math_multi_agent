import google.generativeai as genai
from google.api_core.exceptions import GoogleAPICallError, ResourceExhausted

class MathAgent:
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def _generate(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except ResourceExhausted as exc:
            return (
                "The request exceeded the current Gemini API quota. "
                "Please wait and retry or increase the quota. "
                f"Details: {exc}"
            )
        except GoogleAPICallError as exc:
            return f"Gemini API error: {exc}"
        except Exception as exc:
            return f"Unexpected error while generating a response: {exc}"

    def solve(self, problem):
        """Base method to be overridden by specific agents"""
        raise NotImplementedError("Subclasses must implement solve()")

class SchoolAgent(MathAgent):
    def solve(self, problem):
        # Prompt Engineering for Level 1
        system_prompt = (
            "You are a Level 1 Math Tutor for elementary school students. "
            "Your goals: "
            "1. Solve problems in very simple steps. "
            "2. Use real-world examples like apples, toys, or money. "
            "3. Use emojis and encouraging language. "
            "4. AVOID complex jargon or algebra variables like 'x' and 'y' unless absolutely necessary. "
            f"Problem: {problem}"
        )
        return self._generate(system_prompt)

class CollegeAgent(MathAgent):
    def solve(self, problem):
        # Prompt Engineering for Level 2
        system_prompt = (
            "You are a Level 2 Math Tutor for High School and College students. "
            "Your goals: "
            "1. Solve problems with detailed, logical steps. "
            "2. Use standard mathematical notation (e.g., f(x), ^2). "
            "3. Provide a short 'Hint' or 'Key Concept' box at the end. "
            "4. Tone should be educational and structured. "
            f"Problem: {problem}"
        )
        return self._generate(system_prompt)

class UniversityAgent(MathAgent):
    def solve(self, problem):
        # Prompt Engineering for Level 3
        system_prompt = (
            "You are a Level 3 Professor for University students. "
            "Your goals: "
            "1. Solve problems with high rigor and formal proofs if applicable. "
            "2. Use LaTeX style formatting or formal notation. "
            "3. Briefly mention real-world engineering or scientific applications of this concept. "
            "4. Skip basic arithmetic explanations; assume the student knows the basics. "
            f"Problem: {problem}"
        )
        return self._generate(system_prompt)
