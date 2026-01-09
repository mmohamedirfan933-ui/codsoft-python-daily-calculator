# Daily Quiz Game

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
        "answer": "A"
    }
]

score = 0

print("--- DAILY QUIZ GAME ---\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    ans = input("Enter your answer (A/B/C/D): ").upper()
    
    if ans == q["answer"]:
        print("Correct ✅\n")
        score += 1
    else:
        print(f"Wrong ❌. Correct answer: {q['answer']}\n")

print(f"Your total score: {score}/{len(questions)}")
print("Quiz completed! Keep learning 💡")