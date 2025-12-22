import re

# Read the file
with open(r"Cloud Practitioner Practice\AWS CLF-C02 - Practice Exam 04.md", "r", encoding="utf-8") as f:
    content = f.read()

# Split by questions
questions = re.split(r'Câu hỏi (\d+)', content)

formatted_questions = []
formatted_questions.append(questions[0])  # Add the first part (before first question)

# Process each question
for i in range(1, len(questions), 2):
    if i + 1 >= len(questions):
        break
    
    question_num = questions[i]
    question_text = questions[i + 1]
    
    # Remove "Điểm số: 1.00" and "Chọn X đáp án đúng"
    question_text = re.sub(r'Điểm số: \d+\.\d+\n', '', question_text)
    question_text = re.sub(r'Chọn \d+ đáp án đúng\n', '', question_text)
    
    # Fix options format - remove line breaks between letter and text
    question_text = re.sub(r'\n([A-E])\.\n', r'\n\1. ', question_text)
    
    # Add proper spacing after options
    lines = question_text.strip().split('\n')
    formatted_lines = []
    for j, line in enumerate(lines):
        if re.match(r'^[A-E]\.', line):
            formatted_lines.append('')
            formatted_lines.append(line)
        else:
            formatted_lines.append(line)
    
    question_text = '\n'.join(formatted_lines)
    
    # Format the question with header
    formatted_question = f"### Câu {question_num}\n{question_text.strip()}\n\n---\n"
    formatted_questions.append(formatted_question)

# Join all formatted questions
result = '\n'.join(formatted_questions)

# Write back to file
with open(r"Cloud Practitioner Practice\AWS CLF-C02 - Practice Exam 04.md", "w", encoding="utf-8") as f:
    f.write(result)

print("File formatted successfully!")
