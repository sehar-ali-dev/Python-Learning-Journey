comment=input("Enter your coment")
if "stupid" in comment or "hate" in comment or "idiot" in comment:
   print("comment block")
elif ".com" in comment or "www." in comment:
   print("Comment Blocked: Please use respectful language.")
elif comment == "":
   print("Error: Cannot post an empty comment.")
elif len() > 50 in comment:
   print("Too Long: Please short your comment.")
else:
   print("Success: Comment posted successfully!")

