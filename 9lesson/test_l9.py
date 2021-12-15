import l9

class Test_Fibonacci():
    def test_fibonaci_0(self):
        assert l9.fibonacci(0)==0
    def test_fibonaci_30(self):
        assert l9.fibonacci(30)==832040
    def test_fibonaci_9(self):
        assert l9.fibonacci(9)==34
class Test_XorCipher():
    def test_xorCipher_1(self):
        assert l9.xorCipher('Hello',17)=='Yt}}~'
    def test_xorCipher_2(self):
        assert l9.xorCipher('Yt}}~',17)=='Hello'
    def test_xorCipher_4(self):
        assert l9.xorCipher('',86)==''