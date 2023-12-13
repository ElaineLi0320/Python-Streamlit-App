'''
Yini Li
CS 5001, Fall 2023
Final Project

This is the quiz page for the museum app
'''
import streamlit as st


def check_answers(user_answers, answers):
    """
    Compares user answers with correct answers and calculates the score.

    Args:
        user_answers (dict): A dictionary containing user's answers, with question as keys.
        answers (dict): A dictionary containing the correct answers, with question as keys.

    Returns:
        int: The total score

    Raises:
        TypeError: If either 'user_answers' or 'answers' is not a dictionary.
        ValueError: If 'user_answers' contains keys not present in 'answers'.
    """
    if not isinstance(user_answers, dict) or not isinstance(answers, dict):
        raise TypeError("Both user_answers and answers must be dictionaries.")

    for question in user_answers:
        if question not in answers:
            raise ValueError(f"The question '{question}' in user_answers is not present in answers.")

    score = 0
    for question, answer in user_answers.items():
        if answers.get(question) == answer:
            score += 1
    return score


def display_quiz_page():
    """
    Displays a quiz page in a Streamlit application.

    Args:
        Nothing

    Returns:
        Nothing
    """
    st.title('Take a quick Quiz!')

    # Revised Questions and Answers
    questions = {
        "Who created the sculpture 'The Thinker'?": ["Auguste Rodin", "Michelangelo", "Henry Moore", "Donatello"],
        "Where can you find the famous painting 'The Starry Night'?": ["The Museum of Modern Art, New York", "The Louvre, Paris", "Tate Modern, London", "Rijksmuseum, Amsterdam"],
        "What is the Sistine Chapel ceiling famous for?": ["Its large size", "Michelangelo's frescoes", "Modern art installations", "Ancient Egyptian artifacts"],
        "What is 'Guernica' by Pablo Picasso known for?": ["Its abstract style", "Depicting a war scene", "Being a self-portrait", "Bright colors"],
        "Where is The Metropolitan Museum of Art located?": ["Amsterdam", "Paris", "New York", "London"]
    }
    answers = {
        "Who created the sculpture 'The Thinker'?": "Auguste Rodin",
        "Where can you find the famous painting 'The Starry Night'?": "The Museum of Modern Art, New York",
        "What is the Sistine Chapel ceiling famous for?": "Michelangelo's frescoes",
        "What is 'Guernica' by Pablo Picasso known for?": "Depicting a war scene",
        "Where is The Metropolitan Museum of Art located?": "New York"
    }

    # Collecting user answers
    user_answers = {}
    for question, options in questions.items():
        user_answers[question] = st.radio(question, options)

    # submit button
    if st.button('Submit'):
        score = check_answers(user_answers, answers)
        st.write(f'Your score is {score} out of {len(questions)}')
