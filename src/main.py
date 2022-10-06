def main(request):
    import os

    out = os.getenv('tetsvar')
    print(out)
    return "Hello World!"
