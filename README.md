## Birth
At first, my purpose of creating this project was to practice web scrapping.
I was looking for a challenge which is a good idea to practice and I found the idea of this program.
So I started to write the codes and when I finished programming, I decided to put it in GitHub.

## Introduction
This is a program to extract the headings of the wikipedia pages.
You should just give the url of a page as input and then see the result.
The web page language can be in different languages such as English, Arabic, Persian, etc.

## How to run

#### In developer mode
You can see the steps to run the code below:
1. Install `python3` on your system.
2. Clone the project repository:
```bash
git clone https://github.com/mm-ansarian/Wikipedia_Reader.git
``` 
or 
```bash
git clone git@github.com:mm-ansarian/Wikipedia_Reader.git
```
3. Open the project folder.
4. Install the required Python packages(`PyQt6`, `beautifulsoup4` and `requests`). You can do this by using the `requirements.txt`:
```bash
pip install -r requirements.txt
```
5. Run `app.py`.

#### An executable file
To run the project as an executable file, You can use pyinstaller or other gadgets.
If you are using another gadget, reading the guid can be helpful for you.
But if you are using pyinstaller, here is the guid to convert `app.py` to an executable file:
1. Open the project folder in your command prompt.
2. Install required packages on the python of your system(I offer you to not use a virtual environment, becaus it can make a problem when you run the executable file) using this command:
```bash
pip install -r requirements.txt
```
3. Install `pyinstaller` on the python of your system(or you can even use `auto-py-to-exe`):
```bash
pip install pyinstaller
```
or 
```bash
pip install auto-py-to-exe
```
4. Run the command below to create the executable file:
```bash
pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --name "Wikipedia Reader" --add-data "icon.ico;." --add-data "icons;icons/"  "app.py"
```
5. Run `Wikipedia Reader.exe`.

## Used tools
- **Programming language**: Python
    - PyQt6
    - beautifulsoup4
    - requests
- **GUI**: Qt 

## TODO
- [x] Make a graphical user interface.
- [ ] Add dark mode to the user interface.
- [ ] Improve the performance.
