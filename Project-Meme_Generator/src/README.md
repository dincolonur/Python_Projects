### `Meme Generator`

Meme Generator project is designed to generate Meme's for in project or custom images.
The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. 

With this project;

- You can interact with a variety of complex filetypes.
- Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
- Load, manipulate, and save images.
- Accept dynamic user input through a command-line tool and a web service.

In this project design, we tried to focus on;

- Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don’t repeat yourself) principles of class and method design.
- Working with modules and packages in Python.

In this project, All methods and classes are documented by using docstrings and comments which are 
regarding on PEP 8 Standards.

#### `Project Setup`

Before running the project, Setup steps have to be completed.

- (Optional) Create a virtual environment in your machine and activate;
    python3 -m venv venv
    source venv/bin/activate
    
- Install all dependent modules by using requirements.txt file;
    pip install -r requirements.txt
    
- Project Dependencies;

certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
lxml==4.6.3
MarkupSafe==1.1.1
numpy==1.19.5
pandas==1.1.5
Pillow==8.2.0
python-dateutil==2.8.1
python-docx==0.8.10
pytz==2021.1
requests==2.25.1
six==1.15.0
urllib3==1.26.4
Werkzeug==1.0.1 
    
Now Project is ready to run.

 
#### `Project Structure`


##### `Python Module Structure (Directory Tree)`

|____ `__init__.py`  
|____ `app.py`  
|____ `meme.py`  
|____ `Engines/`  
| |____ `__init__.py`  
| |____ `IngestorEngine/`  
| | |____  `__init__.py`  
| | |____  `CSVIngestor.py`   
| | |____  `DocxIngestor.py`   
| | |____  `PDFIngestor.py`  
| | |____  `TextIngestor.py`  
| | |____  `Ingestor.py`   
| | |____  `IngestorInterface.py`  
| |____ `MemeEngine/`  
| | |____  `__init__.py`  
| | |____  `MemEngine.py`  
| |____ `QuoteEngine/`  
| | |____  `__init__.py`   
| | |____  `QuoteModel.py`  


**_Engines Module:_** 
Main module which has all engines modules.

**_IngestorEngine Module:_** 
Ingest operations module including CSV, TXT, PDF and DOCX file format ingest processes.
To use this module import Ingestor class and call parse method.

**_MemeEngine Module:_** 
Meme Generator operations module which has MemEngine class. In MemEngine there are fundamental methods of the process
resize_image, add_caption and make_meme. To understand method usages, please check doctrings.

**_QuoteEngine Module:_** 
QuoteModel object model is in this module. QuoteModel object is used to create structured Quotes.


##### `Other Packages`

- _data folder: Default photos and files(docx, txt, pdf, csv) are in this folder.
This folder data is used for RANDOM Mem Generator usage
- fonts folder: Mem Generator font Types folder.(ttf files)
- templates folder: Web Pages source code folder.(html files)
- tmp folder: temporary images files folder. Used by meme.py.(CLI Run)
- static folder: temporary images and result files folder. Used by app.py.(Web Run)


#### `Running Project`

We can run project in 2 ways.By using Command Line Interface(CLI) or via Web Interface(Flask):

##### `CLI Run`

To run project via CLI, main script is meme.py.

_$ python3 meme.py -h_

usage: Meme Generator Arguments [-h] [--path PATH] [--body BODY]
                                [--author AUTHOR]

optional arguments:  
  -h, --help       show this help message and exit  
  --path PATH      Image Path  
  --body BODY      Meme Quote  
  --author AUTHOR  Meme Quote Author  
  
  
 Running meme.py without optional arguments will print random Quote 
 and random Image from inputs from __data_ folder.
 
 
##### `Web Interface Run`
 
To run project via Web Interface, first we need to run Web Application Server or deploy the project into an existing Application Server.
Running in our local Application Server by using Flask framework run this command;

_$ flask run --host 0.0.0.0 --port 3000 --reload

You will see this result;

`* Serving Flask app "app.py" (lazy loading)`  
` * Environment: production `  
   `WARNING: This is a development server. Do not use it in a production deployment.`  
   `Use a production WSGI server instead.`  
 `* Debug mode: off`  
 `* Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)`  
 `* Restarting with stat`  
 
Open page  _http://0.0.0.0:3000/_


On the screen there are 2 buttons for 2 usages;
 
**1 - RANDOM:**
Random button will use files and photos inside the _data folder and generate random memes.

**2 - CREATE:**
Create button will open a form.   
In this form User needs to enter manually _Image URL_ of the photo(it can be any format, jpg, png etc...),
 _Quote Body_ which is manually entered quote text and _Quote Author_ Author of the Quote.  
 
After entering all these fields and clicking _Create Meme!_ button, you will see new created Meme on the screen.


Really cool project. Please Enjoy.

_OD_




