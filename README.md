# catbox.moe
a CLI tool use to upload stuff to catbox &amp; litterbox

- [What is this](#what-is-this)
- [Quick Start](#quick-start)
- [How To use this?](#how-to-use-this)
- [Screenshots](#screenshot)

> The spinning donut.py is a local LLM generated code. it was made to test my local LLM and i added it for fun, feel free to delete the file if you dont need it :)

*This script is not tested on Windows, only on linux, please open an issue if you run into some errors.*
### What is this??
A simple CLI tool Used for uploading stuffs to catbox.moe and litterbox.catbox.moe

Current features in this program, there is more upcoming features, please [see this list](#more-to-come)
- Uploading to catbox.moe (with & without an account)
    - with link
    - upload files directly (Place them in the `upload` folder)
- Upload to litterbox.catbox.moe
    - upload files directly (Place them in the `upload` folder)
    - Customize how long you want the file to stay up.

# Quick Start
1. Firstly, clone this repo.
    ```bash
    git clone https://github.com/Andrewgxgx/catbox.moe.git
    ```
    Then cd into it
    ```bash
    cd catbox.moe
    ```

2. Create a venv

    Windows 
    ```
    python -m venv venv
    ```
    Unix (MacOS/ Linux)
    ```bash
    python3 -m venv venv
    ```

3. Activate the venv
    Windows (command prompt)
    ```
    venv\Scripts\activate.bat
    ```
    Unix (MacOS/ Linux)
    ```bash
    source ./venv/bin/activate
    ```
4. Install requirements 
    ```
    pip install requirements.txt
    ```

5. Run the program 
    Windows 
    ```
    python main.py
    ```
    Unix (MacOS/ Linux)
    ```
    python3 main.py
    ```

# How to use This?
1. when you first run the program the program will ask for your os, choose 1 if you're on windows and choose 2 if you're on Linux & macos 

2. Then everything is very self explanatory, you can upload by link to catbox and only upload files to litterbox

# Screenshot
![alt text](<upload/Screenshot from 2025-03-13 17-34-45.png>)
![alt text](<upload/Screenshot from 2025-03-13 17-35-18.png>)
![alt text](<upload/Screenshot from 2025-03-14 18-10-33.png>)
![alt text](<upload/Screenshot from 2025-03-14 18-11-13.png>)
![alt text](<upload/Screenshot from 2025-03-14 18-11-56.png>)


# More to come
**I AM WORKING ON THESE FEATURES, Please pull a PR if you have already wrote the code**
- Bulk Link upload
    - upload with link but in bulks, eg put lots of links in a file and upload to catbox or litterbox
- Albums 
- Deleting stuff
- Fixing errors 
