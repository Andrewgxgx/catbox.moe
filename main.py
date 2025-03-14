import os
import requests
from datetime import datetime

credits="""
This program is made and maintained by Andrew
This program is open source and free to use
MIT @ 2025 
Support me by Starring the project & following me on Github:
- https://github.com/Andrewgxgx/catbox.moe
- https://github.com/Andrewgxgx
"""
api = "https://catbox.moe/user/api.php"
api_litter="https://litterbox.catbox.moe/resources/internals/api.php"
os_unix="/"
os_windows="\\" #i hate windows, they make everything difficult 
control=0

start=0
def get_user_preferences():
    global user_os, control
    # Get preferences from user
    print("""Please choose your OS:
          1. Windows
          2. Unix (Linux, MacOS)
          3. Temple OS 
          4. Other
          Type the number of your choice.
           """)
    Preferences =input("Enter a number 1 to 4: ")
    if Preferences=="1":
        user_os=os_windows
    elif Preferences=="2":
        user_os=os_unix
    elif Preferences=="3":
        print("Hello Terry Davis, We currently, don't support Temple OS")
        print("Exiting...")
        control= control+1
        exit()
    else:
        print("Type 1, 2 or 3")
        get_user_preferences()



def format():
    global formatting
    print("""
          How would you like to format your links?
          1. <file path>: <link>
          2. <link>
          3. <numbered list>. <link>
          4. <Timestamp (hh:mm:ss)> : <File path> : <Link>
          5. <custom string (user input)> : <link> 
          """)
    formatting = int(input("Enter a number 1 to 5: "))


def catbox_no_acc():
    linkornot= input("Do you want to upload via link (Y/N) ?: ")
    if linkornot.upper() == "Y" or linkornot.upper()=="YE" or linkornot.upper()=="YES":
        asking_links=0
        while asking_links == 0: 
            text = """
                  if you are done with the uploading links, you can type `done` 
                  """
            enter_links = input("Enter Links: ")
            if enter_links.lower() == "done":
                asking_links=2
            else: 
                
                data = {
                    "reqtype": "urlupload",
                    "url": enter_links
                    }
                response = requests.post(api, data=data) 
                if response.status_code == 200:
                    print(f"Uploaded: {enter_links} \n Catbox Link: {response.text}")
                
                else:
                    print("Failed to upload")
    else:
        folder_path = f".{user_os}upload"  
        def scan():
            print("Scanning")
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(file_path)
        scan()  
        ask=input("Are these all of the files you want to upload? (Y/N): ")
        if ask == "Y" or ask=="y" or ask == "yes" or ask=="YES" or ask=="YE" or ask =="ye" or ask =="yeah" or ask =="YEAH":
            print("Uploading!...")
            format()

    ######################################
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(f"uploading {file_path}")
                    with open( file_path, "rb") as item:
                        files = {
                            "fileToUpload": item  
                        }
                        
                        data = {
                            "reqtype": "fileupload"  
                        }
                        response = requests.post(api, data=data, files=files)  
                        print("status code:",response.status_code) 
                    if response.status_code == 200:
                        if formatting == 1: # FILE PATH : LINK 
                            formatting_write=f""" \"{file_path}\" : {response.text} \n """
                        elif formatting == 2:  # LINK
                            formatting_write=f""" {response.text} \n """ 
                        elif formatting== 3:  # NUMBER. LINK
                            start = start + 1
                            formatting_write =f"""{start}. {response.text}"""
                        elif formatting==4: # TIME STAMP : FILE PATH : LINK
                            current_time = datetime.now().strftime("%H:%M:%S")
                            formatting_write = f"[{current_time}]: {file_path} : {response.text}"
                        elif formatting == 5: # CUSTOM TEXT : LINK 
                            write = input("Put something infront of the link, (TEXT) : (Link) \n ")
                            formatting_write = f"{write} : {response.text}"
                        # SAVE THE LINKS
                        createfile = open(f"uploaded_links.txt", "a")
                        createfile.write(formatting_write)
                        createfile.close()
                        print(f"File \"{file_path}\" Uploaded")
                    else:
                        print("Failed to upload")  
        elif ask == "N" or ask == "n" or ask.upper() =="NO":
            print("Rescanning...")
            scan()
###############################################
def catbox_with_acc():
    account = input("Enter your account hash: ")
    linkornot= input("Do you want to upload via link (Y/N) ?: ")
    if linkornot.upper() == "Y" or linkornot.upper()=="YE" or linkornot.upper()=="YES":
        asking_links=0
        while asking_links == 0: 
            text = """
                  if you are done with the uploading links, you can type `done` 
                  """
            enter_links = input("Enter Links: ")
            if enter_links.lower() == "done":
                asking_links=2
            else: 
                print() ### NOT DONE 
                data = {
                    "reqtype": "urlupload",
                    "userhash" : account,
                    "url": enter_links
                    }
                response = requests.post(api, data=data) 
                if response.status_code == 200:
                    print(f"Uploaded: {enter_links} \n Catbox Link: {response.text}")
                
                else:
                    print("Failed to upload")
    else:
        folder_path = f".{user_os}upload"  
        def scan():
            print("Scanning")
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(file_path)
        scan()  
        ask=input("Are these all of the files you want to upload? (Y/N): ")
        if ask == "Y" or ask=="y" or ask == "yes" or ask=="YES" or ask=="YE" or ask =="ye" or ask =="yeah" or ask =="YEAH":
            print("Uploading!...")
            format()

    ######################################
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    print(f"uploading {file_path}")
                    with open( file_path, "rb") as item:
                        files = {
                            "fileToUpload": item  
                        }
                        
                        data = {
                            "reqtype": "fileupload",
                            "userhash":account,
                        }
                        response = requests.post(api, data=data, files=files)  
                        print("status code:",response.status_code) 
                    if response.status_code == 200:
                        if formatting == 1: # FILE PATH : LINK 
                            formatting_write=f""" \"{file_path}\" : {response.text} \n """
                        elif formatting == 2:  # LINK
                            formatting_write=f""" {response.text} \n """ 
                        elif formatting== 3:  # NUMBER. LINK
                            start = start + 1
                            formatting_write =f"""{start}. {response.text}"""
                        elif formatting==4: # TIME STAMP : FILE PATH : LINK
                            current_time = datetime.now().strftime("%H:%M:%S")
                            formatting_write = f"[{current_time}]: {file_path} : {response.text}"
                        elif formatting == 5: # CUSTOM TEXT : LINK 
                            write = input("Put something infront of the link, (TEXT) : (Link) \n ")
                            formatting_write = f"{write} : {response.text}"
                        # SAVE THE LINKS
                        createfile = open(f"uploaded_links.txt", "a")
                        createfile.write(formatting_write)
                        createfile.close()
                        print(f"File \"{file_path}\" Uploaded")
                    else:
                        print("Failed to upload")  
        elif ask == "N" or ask == "n" or ask.upper() =="NO":
            print("Rescanning...")
            scan()

def litterbox():
    folder_path = f".{user_os}upload"  
    def scan():
        print("Scanning")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
    scan()  
    ask=input("Are these all of the files you want to upload? (Y/N): ")
    if ask == "Y" or ask=="y" or ask == "yes" or ask=="YES" or ask=="YE" or ask =="ye" or ask =="yeah" or ask =="YEAH":
        time=input("How long do you want the file to be uploaded for? (1h, 12h, 24h, 72h): ")
        if time=="1h" or time=="12h" or time=="24h" or time=="72h":
            print("Uploading!...")
            format()
        else:
            print("Invalid time, enter 1h, 12h, 24h, 72h only, not other values, you must enter the h also. For example, you need to type 12h if you want to upload for 12 hour.")
            litterbox()
######################################
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"uploading {file_path}")
                with open( file_path, "rb") as item:
                    files = {
                        "fileToUpload": item  
                    }
                    
                    data = {
                        "reqtype": "fileupload",
                        "time":time,
                    }
                    response = requests.post(api_litter, data=data, files=files)  
                    print("status code:",response.status_code) 
                if response.status_code == 200:
                    if formatting == 1: # FILE PATH : LINK 
                        formatting_write=f""" \"{file_path}\" : {response.text} \n """
                    elif formatting == 2:  # LINK
                        formatting_write=f""" {response.text} \n """ 
                    elif formatting== 3:  # NUMBER. LINK
                        start = start + 1
                        formatting_write =f"""{start}. {response.text}"""
                    elif formatting==4: # TIME STAMP : FILE PATH : LINK
                        current_time = datetime.now().strftime("%H:%M:%S")
                        formatting_write = f"[{current_time}]: {file_path} : {response.text}"
                    elif formatting == 5: # CUSTOM TEXT : LINK 
                        write = input("Put something infront of the link, (TEXT) : (Link) \n ")
                        formatting_write = f"{write} : {response.text}"
                    # SAVE THE LINKS
                    createfile = open(f"uploaded_links.txt", "a")
                    createfile.write(formatting_write)
                    createfile.close()
                    print(f"File \"{file_path}\" Uploaded")
                else:
                    print("Failed to upload")  
    elif ask == "N" or ask == "n" or ask.upper() =="NO":
        print("Rescanning...")
        scan()
    


def menu():
    print(f"""
{credits}
=========
Welcome to CATBOX & Litterbox Uploader!
Where you can bulk upload stuff to catbox and litterbox.
Choose your options! 
1. Upload to Catbox.moe (No account)
2. Upload to Catbox.moe (with account)
3. Upload to Litterbox
4. Exit / Stop program
====
Deleting files, Creating, editing, adding, removing files to albums is coming soon!
""")
    opt=int(input("Type 1,2,3 or 4: "))
    if opt==1:
       print("Catbox - no account")
       catbox_no_acc()
    elif opt==2:
        print("Catbox - with account")
        catbox_with_acc()
    elif opt==3:
        print("Upload to LitterBox")
        litterbox()
    elif opt==4:
        print("Exiting...")
        control = 1
        exit()

#================================================================
print(credits)
print("Welcome to the Catbox Uploader")
print("Please choose your OS First, before getting started")
get_user_preferences()
while control==0:
    menu()

print(credits)
print("Thank you for using the Catbox Uploader")
print("Exiting...")
exit()






