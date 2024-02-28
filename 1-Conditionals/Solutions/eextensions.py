A = input("What's the name of the file? ")
if str(A).endswith(".gif"):
    print("gif/gif (pronounced with soft g)")
elif str(A).endswith(".jpg"):
    print("image/jpeg")
elif str(A).endswith(".jpeg"):
    print("image/jpeg")
elif str(A).endswith(".png"):
    print("image/png")
elif str(A).endswith(".pdf"):
    print("application/pdf")
elif str(A).endswith(".txt"):
    print("application/txt")
elif str(A).endswith(".zip"):
    print("file/zip")
else:
    print("application/octet-stream")
