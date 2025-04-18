import os

BLOG_DIR="blogs"

def save_blog(title,content) :
    if not os.path.exists(BLOG_DIR):
        os.makedirs(BLOG_DIR)
    filename=os.path.join(BLOG_DIR,f"{title}.txt")
    with open(filename,'w') as file :
        file.write(content)
    print("Content is saved at {title}.txt")

def view_blog():
    if not os.path.exists(BLOG_DIR) or not os.listdir(BLOG_DIR):
        print("No blogs found..")
    else :
        print("Available blogs")
        for file in os.listdir(BLOG_DIR):
            print(f"{file[:-4]}")

def preview_blog(title):
    try:
        filename=os.path.join(BLOG_DIR,f"{title}.txt")
        with open(filename,'r') as file :
            print(f"{file.read()}")
    except FileNotFoundError :
        print("File not found...")



def main():
    print("Blog Post Generator")
    while True :
        print("1.Create Blog")
        print("2.view blogs")
        print("3.preview blogs")
        print("4.exit")
        choice=int(input("Enter the option : "))
        if choice == 1 :
            title=input("Enter the title : ")
            content = input("Enter the content")
            save_blog(title,content)
            print("Blog created..")

        elif choice == 2 :
            view_blog()
        elif choice == 3 :
            title =input("Enter the title : ")
            preview_blog(title)

        elif choice == 4 :
            print("bye....")
            break
        else :
            print("Invalid")

if __name__ == "__main__":
    main()

