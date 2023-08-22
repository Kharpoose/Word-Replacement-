def replace_word():

    str = input("Write what you want: ")
   # str = 'Hi guys, I am Çağrı and hi hi hi hi'
    word_to_replace = input("Enter to word replace: ") 
    word_replacement = input("Enter to word replacement: ")
    print(str.replace(word_to_replace, word_replacement))


replace_word()