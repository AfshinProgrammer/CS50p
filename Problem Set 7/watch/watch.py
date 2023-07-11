# Afshin Masoudi
# CS50p/Problem Set 7/Watch on YouTube
# input : <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
import re

def main():
    print(parse(input("HTML: ")))

def parse(attributes):
    if match := re.search(r'<iframe.*?src="(.*?youtube\.com/embed/(.*?))".*?>', attributes):
        return 'https://youtu.be/' + match.group(2)
    else:
        return None

if __name__ == "__main__":
    main()