from agents.logical_tutor import get_logical_explanation
from agents.visual_tutor import get_visual_explanation
from agents.story_tutor import get_story_explanation
from agents.quiz_tutor import get_quiz_questions

def route_to_agent(topic, style):
    # Handle single styles
    if style == "logical":
        return get_logical_explanation(topic)
    elif style == "visual":
        return get_visual_explanation(topic)
    elif style == "story":
        return get_story_explanation(topic)
    elif style == "quiz":
        return get_quiz_questions(topic)
    # Handle combined styles
    elif style == "story_quiz":
        story = get_story_explanation(topic)
        quiz = get_quiz_questions(topic)
        return f"{story}\n\n---\n\n**Test Your Knowledge:**\n{quiz}"
    elif style == "visual_quiz":
        visual = get_visual_explanation(topic)
        quiz = get_quiz_questions(topic)
        return f"{visual}\n\n---\n\n**Test Your Knowledge:**\n{quiz}"
    elif style == "visual_story":
        visual = get_visual_explanation(topic)
        story = get_story_explanation(topic)
        return f"{visual}\n\n---\n\n**Learn Through Story:**\n{story}"
    else:
        return "Invalid style. Choose: logical, visual, story, quiz, story_quiz, visual_quiz, or visual_story." 