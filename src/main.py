from textnode import TextNode

def main():
    node = TextNode("This is a text", "italic", "https://www.boot.dev")
    print(repr(node))

main()