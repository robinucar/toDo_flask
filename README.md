# ToDo_App_flask
This repo has been updated to work with Python 3.9.12 and up.

## User Stories

As a user,
So that I can remember my notes,
I would like to create a note.

As a user,
So that I can remember my notes,
I would like to see my notes.

As a user,
So that I can change my note,
I would like to update my note.

As a user,
So that I do not want to keep the note I do not need,
I would like to delete my note.

## How To Run 
1. Install `virtualenv:`

   `$ pip install virtualenv`

2. Open a terminal in the project root directory and run:

   `$ virtualenv env`
 
3. Then run the command:

   `$ .\env\Scripts\activate`
    
4. Then install the dependencies:

    `$ (env) pip install -r requirements.txt`
    
5. Finally start the web server:

   `$ (env) python app.py` 
   
   This server will start on port 5000 by default. You can change this in app.py by changing the following line to this:
   
   `if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)`