def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text
def main():
    message = input()
    result = convert(message)
    print(result)
main()
