from textnode import TextNode, TextType

def main():
  textNode = TextNode("this is some text", TextType.LINK, "https://www.google.se")
  print(textNode)

main()