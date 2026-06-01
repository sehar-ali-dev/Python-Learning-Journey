#mini projec: Emoji converter
#convert text-based emotions into emojis
covert_emojis= input("enter your message")
covert_emojis=covert_emojis.replace(":)","😀")
covert_emojis= covert_emojis.replace(":(","😞")
covert_emojis= covert_emojis.replace(":D","😁")
covert_emojis= covert_emojis.replace(":/","😕")
print(covert_emojis)


