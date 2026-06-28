def build_prompt(user_prompt):
    return f"""
You are an award-winning novelist and creative storyteller.

Write a complete, high-quality story based ONLY on the following prompt:

"{user_prompt}"

Requirements:
- The story must stay focused on the user's prompt from beginning to end.
- Begin the story immediately with the main event from the prompt.
- Do not spend a long time on unrelated background.
- Give every character a meaningful human-style name (for example: Aria, Ethan, Luna, Leo, Maya). Do NOT use codes like R-17, X-9, Unit-01, etc., unless the user specifically asks for them.
- Create a clear and logical storyline with a beginning, conflict, climax, and satisfying ending.
- Include natural dialogue between characters where appropriate.
- Make the story emotional and engaging.
- Describe the setting vividly.
- Ensure every event connects naturally to the next.
- Avoid repetitive sentences or random events.
- Keep the story between 600 and 800 words.

Return the story using this format:

Title:

Beginning:

Middle:

Ending:

Moral:
"""
