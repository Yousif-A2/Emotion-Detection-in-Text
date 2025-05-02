# utils/recommendations_utils.py

def get_emotion_recommendations(emotion):
    """
    Returns personalized recommendations based on the detected emotion.
    
    Args:
        emotion (str): The detected emotion (e.g., 'happy', 'sad', 'anger')
    
    Returns:
        dict: A dictionary containing recommendations and strategies
    """
    # Define recommendations for each emotion
    recommendations = {
        "anger": {
            "title": "Managing Anger",
            "description": "It seems you're expressing anger. Here are some helpful strategies to manage these feelings.",
            "strategies": [
                "Take deep breaths and count to ten before responding",
                "Step away from the situation temporarily if possible",
                "Try physical exercise to release tension",
                "Write down your thoughts to gain perspective",
                "Consider speaking with someone you trust about your feelings"
            ],
            "quote": "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured."
        },
        "disgust": {
            "title": "Processing Disgust",
            "description": "Your text shows elements of disgust. Here are ways to process this emotion constructively.",
            "strategies": [
                "Identify the specific trigger for your feelings",
                "Consider if your reaction is proportionate to the situation",
                "Practice acceptance of things outside your control",
                "Focus on aspects you find positive or pleasant",
                "Use mindfulness techniques to observe without judgment"
            ],
            "quote": "Understanding the root of disgust helps us respond rather than react."
        },
        "fear": {
            "title": "Addressing Fear",
            "description": "I've detected fear in your text. These strategies might help you cope with anxious feelings.",
            "strategies": [
                "Name your fear specifically to reduce its power",
                "Challenge catastrophic thinking with evidence",
                "Practice grounding techniques (5-4-3-2-1 method)",
                "Try progressive muscle relaxation",
                "Consider what you've successfully overcome in the past"
            ],
            "quote": "Fear is a reaction. Courage is a decision."
        },
        "happy": {
            "title": "Nurturing Happiness",
            "description": "Your text expresses happiness. Here are ways to cultivate and extend these positive feelings.",
            "strategies": [
                "Share your positive feelings with others",
                "Practice gratitude by noting specific things you appreciate",
                "Savor the moment through mindful awareness",
                "Plan activities that reliably bring you joy",
                "Use this positive energy for creative pursuits"
            ],
            "quote": "Happiness is not something ready-made. It comes from your own actions."
        },
        "joy": {
            "title": "Embracing Joy",
            "description": "Your text shows joy! Here's how to celebrate and enhance this wonderful emotion.",
            "strategies": [
                "Express your joy through creative outlets",
                "Document this moment in a journal to revisit later",
                "Use this emotional state to connect with others",
                "Set intentions while in this positive mindset",
                "Practice kindness as a way to spread your joy"
            ],
            "quote": "Joy is the simplest form of gratitude."
        },
        "neutral": {
            "title": "Emotional Balance",
            "description": "Your text appears emotionally neutral. This could be an opportunity for reflection.",
            "strategies": [
                "Check in with yourself about how you're truly feeling",
                "Use this balanced state for decision-making",
                "Practice mindfulness to enhance awareness",
                "Consider what would add positive emotion to your day",
                "Reflect on your recent emotional patterns"
            ],
            "quote": "Emotional neutrality can be the canvas for intentional living."
        },
        "sad": {
            "title": "Navigating Sadness",
            "description": "I've detected sadness in your text. These approaches might help you process these feelings.",
            "strategies": [
                "Allow yourself to feel without judgment",
                "Connect with a supportive friend or family member",
                "Engage in gentle physical movement like walking",
                "Practice self-compassion and speak kindly to yourself",
                "Consider activities that have lifted your mood before"
            ],
            "quote": "Sadness is but a wall between two gardens."
        },
        "sadness": {
            "title": "Navigating Sadness",
            "description": "I've detected sadness in your text. These approaches might help you process these feelings.",
            "strategies": [
                "Allow yourself to feel without judgment",
                "Connect with a supportive friend or family member",
                "Engage in gentle physical movement like walking",
                "Practice self-compassion and speak kindly to yourself",
                "Consider activities that have lifted your mood before"
            ],
            "quote": "Sadness is but a wall between two gardens."
        },
        "shame": {
            "title": "Healing from Shame",
            "description": "Your text contains elements of shame. Here are some ways to address these difficult feelings.",
            "strategies": [
                "Distinguish between guilt (behavior-focused) and shame (self-focused)",
                "Practice vulnerability with trusted people",
                "Replace self-criticism with self-compassion",
                "Remember that mistakes are universal human experiences",
                "Consider journaling to explore the roots of these feelings"
            ],
            "quote": "Shame corrodes the very part of us that believes we are capable of change."
        },
        "surprise": {
            "title": "Processing Surprise",
            "description": "I've detected surprise in your text. Here's how to navigate unexpected situations.",
            "strategies": [
                "Take a moment to pause and process what happened",
                "Accept the unexpected as part of life's journey",
                "Look for opportunities within the unexpected",
                "Reflect on how this surprise challenges your assumptions",
                "Share your experience with others for perspective"
            ],
            "quote": "Life is a series of natural and spontaneous changes. Don't resist them; that only creates sorrow."
        }
    }
    
    # Return the recommendations for this emotion (default to neutral if not found)
    return recommendations.get(emotion.lower(), recommendations["neutral"])