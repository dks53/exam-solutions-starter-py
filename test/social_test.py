from solutions.social import question_a, tweets

def test_qa():
    result = question_a(tweets)
    assert result == "sandwhoa"
