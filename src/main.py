def main(request):
    import os

    out = os.getenv('TESTVAR')
    print(out)
    return "Hello World!"
