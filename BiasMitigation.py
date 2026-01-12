from google import genai
from google.genai import types
import config

client = genai.Client(api_key=config.GEMINI_API_KEY)

def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""
    try:
        contents = [
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=prompt)]
            )
        ]
        config_params = types.GenerateContentConfig(
            temperature=temperature
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config=config_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")

    prompt = input(
        "Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): "
    )
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}")

    modified_prompt = input(
        "\nModify the prompt to make it more neutral "
        "(e.g., 'Describe the qualities of a doctor'): "
    )
    modified_response = generate_response(modified_prompt)
    print(f"\nModified AI Response (Neutral):\n{modified_response}")


def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")

    long_prompt = input(
        "Enter a long prompt (300+ words, e.g., a detailed story): "
    )
    long_response = generate_response(long_prompt)
    print(f"\nResponse to Long Prompt (truncated):\n{long_response[:500]}...\n")

    short_prompt = input(
        "Now, condense the prompt to be more concise: "
    )
    short_response = generate_response(short_prompt)
    print(f"\nResponse to Condensed Prompt:\n{short_response}")


def run_activity():
    print("\n=== AI Learning Activity ===\n")

    activity_choice = input(
        "Which activity would you like to run?\n"
        "1: Bias Mitigation\n"
        "2: Token Limits\n"
        "Enter choice (1 or 2): "
    )

    if activity_choice == "1":
        bias_mitigation_activity()
    elif activity_choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose either 1 or 2.")


if __name__ == "__main__":
    run_activity()
