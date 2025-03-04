def format_recommendations(recommendations):
    formatted = "\n".join(f"- {rec}" for rec in recommendations)
    return formatted

def validate_input(user_input):
    if not user_input.strip():
        raise ValueError("Input cannot be empty.")
    return user_input.strip()