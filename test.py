from compver import compver
def test_answer():
        ans = compver("1.1","1.2")
	assert ans == '"1.2" greater than "1.1"'
def test_answer1():
	ans1 = compver('1.2.1.2','1.1.1.2')
	assert ans1 == '"1.2.1.2" greater than "1.1.1.2"'

def test_answer2():
	ans2 = compver('0.0.1.2','0.0.2.2')
        assert ans2 == '"0.0.2.2" greater than "0.0.1.2"'

