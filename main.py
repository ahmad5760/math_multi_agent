import os
import google.generativeai as genai
from dotenv import load_dotenv
from router import AgentRouter
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Load Environment Variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
PREFERRED_MODEL = os.getenv("GEMINI_MODEL")

if not API_KEY:
    print(Fore.RED + "Error: API Key not found. Please check your .env file.")
    raise SystemExit(1)

# Configure Gemini
genai.configure(api_key=API_KEY)


def init_model():
    """
    Try to initialize a supported Gemini model, falling back through a short list.
    Older API keys may not have access to every model name.
    """
    candidates = []
    if PREFERRED_MODEL:
        candidates.append(PREFERRED_MODEL)
    # Put newer, broadly available models first.
    candidates.extend(
        [
            "models/gemini-2.0-flash",
            "models/gemini-1.5-flash",
            "models/gemini-pro",
        ]
    )

    last_error = None
    for name in candidates:
        try:
            model = genai.GenerativeModel(name)
            # Quick probe to ensure the model is reachable.
            model.count_tokens("ping")
            return model, name
        except Exception as exc:
            last_error = exc
            continue

    print(
        Fore.RED
        + "Error: Could not initialize any Gemini model. "
        + "Check your API key permissions or set GEMINI_MODEL to a supported model."
    )
    if last_error:
        print(Fore.RED + f"Last error: {last_error}")
    raise SystemExit(1)


model, active_model_name = init_model()


def print_separator():
    print(Fore.CYAN + "-" * 80)


def run_demo():
    router = AgentRouter(model)

    print(Fore.GREEN + Style.BRIGHT + "Multi-Agent Math System Initialized\n")
    print(Fore.GREEN + f"Using model: {active_model_name}\n")

    # --- TEST CASES ---
    test_cases = [
        # Level 1 Tests
        ("School", "What is 5 times 4?"),
        ("School", "If I have 10 candies and eat 3, how many are left?"),
        ("School", "What is half of 20?"),
        # Level 2 Tests
        ("College", "Solve for x: 2x + 5 = 15"),
        ("College", "Find the derivative of x^2 + 4x"),
        ("College", "What is the probability of rolling a 6 on a fair die?"),
        # Level 3 Tests
        ("University", "Solve the differential equation dy/dx = y"),
        ("University", "Explain the concept of Eigenvalues in Linear Algebra"),
        ("University", "Optimize the function f(x) = x^3 - 3x using derivatives"),
    ]

    for level, problem in test_cases:
        print_separator()
        print(f"Input Level: {level}")
        print(f"Problem: {problem}")

        # Route the problem
        agent, solution = router.route_problem(level, problem)

        print(f"Agent Assigned: {agent.name}")
        print(f"Solution:\n{solution}")
        print("\n")


if __name__ == "__main__":
    run_demo()
