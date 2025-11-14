# 3.1節の動作確認用コード
from chapter3.chap3_1_generate_questions_OpenAI import generate_questions

if __name__ == "__main__":
    qa_pairs = generate_questions('A1', 3, ['apple', 'orange'])
    print("\nqa_pairs:\n", qa_pairs)