

def build_prompt(user_prompt):
    return f"""
You are an award-winning novelist and creative storyteller.

Write a complete, engaging, and high-quality story based ONLY on the following prompt:

"{user_prompt}"

Instructions:
- The story MUST stay focused on the user's prompt.
- Start the story immediately from the given prompt.
- Use meaningful character names that suit the story.
- Do NOT use robot IDs like R-17, X-9, Unit-01 unless the user specifically requests them.
- The storyline must be logical, emotional, and connected.
- Every page must continue naturally from the previous page.
- Include dialogue where appropriate.
- Do not add unrelated events.
- Use descriptive but simple English.

The story MUST follow EXACTLY this format:

Story Title:
<Write the story title>

Page 1:
<Write only 1-2 concise lines>

Page 2:
<Write only 1-2 concise lines>

Page 3:
<Write only 1-2 concise lines>

Continue the same pattern for all remaining pages.

Requirements:
- Create exactly 10 pages.
- Each page must contain ONLY 1-2 concise lines.
- Number every page correctly.
- Do NOT combine pages.
- Do NOT write long paragraphs.
- Do NOT use headings such as Beginning, Middle, or Ending.
- Finish the story naturally on Page 10.
- After Page 10, write:

Moral:
<One meaningful sentence>

Return ONLY the story in the exact format above.
"""
