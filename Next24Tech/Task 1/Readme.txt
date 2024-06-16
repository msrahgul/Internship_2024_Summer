Task 1: 

Simple Registration Form Using Tkinter in Python
This is a simple GUI-based registration form application built using Python's Tkinter library. The form collects user details such as full name, email ID, gender, country, and programming languages known. Once the user submits the form, their details are displayed in a message box for confirmation, and if confirmed, the details are saved to a local file named registration_details.txt.

Features
* User-friendly graphical interface.
* Fields for full name, email ID, gender, country, and programming languages.
* Data validation and confirmation before saving.
* Saves user details to a local file.

How It Works
1. GUI Layout:
o The main window is created with a title "Registration Form" and a fixed size of 600x400 pixels.
o Labels and input widgets (Entry, Radiobutton, Combobox, Checkbutton) are arranged in a grid layout to collect user details.
2. Widgets and Variables:
o StringVar is used to hold the values entered by the user for full name, email ID, gender, country, and programming languages.
o Entry widgets are used for text input for full name and email ID.
o Radiobutton widgets are used for selecting the gender.
o Combobox widget is used for selecting the country from a predefined list.
o Checkbutton widgets are used for selecting the programming languages known.
3. Submit Button:
o A Button widget is provided to submit the form.
o The submit function is called when the submit button is clicked.
4. Submit Function:
o The submit function gathers all the user input and formats it into a string.
o It checks which programming languages are selected and includes them in the string.
o A message box (askyesno) is displayed with the collected information for the user to confirm.
o If the user confirms, the information is appended to a local file named registration_details.txt.
o A success message is displayed, and the application window is closed.
