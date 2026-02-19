from vanna_calls import (generate_questions_cached)

def test_generate_questions_cached():
    questions = generate_questions_cached()
    assert questions is not None
    assert isinstance(questions, list)
    assert len(questions) > 0

def main():
    test_generate_questions_cached()
    print("test_generate_questions_cached: Test passed!")

if __name__ == "__main__":
    main()
    print("All tests passed!")