# Project Title:
CURD opearation using Firebase and PyQt5 
# Objectives :
The objective of this project is used to designed for user to create, read, update and delete their data effectively. This project also  integrated with the Firestore Database for data storage. 
# CURD Opearations:
### 1_ Create Opearation:
- User Inputs:
User need to  input their name, age, phone number and email.
- Database: 
Save the validated data as a new document in the Firestore user collection.
- Feedback:
It also display a confirmation message with document ID of the new created record.
### 2_ Read Opeartion:
- Input:
User enter the document ID they want to retrieve.
- Database: 
Retrieve the document data from the firestore user collection.
- Feedback: 
Display the retrieved data in a readable format. If the document ID does not exist, it shows an error message to user.
### 3_ Update Operation:
- Input: 
Firstly enter the ID they want to update, along with the new data for name, age, phone number, and email.
- Database:
It is used to update the existing document in the Firestore Database user collection with the new data.
- Feedback: 
It display a confirmation message the data update successful. If the document ID does not exist, show an error message.
### 4_Delete Operation:
- Input: 
Enter the ID they want to delete.
- Database:
When user enter ID and press ok the Document that they saved it has been deleted from the Firestore user collection.
- Feedback: 
After deleted document ID it show a confirmation message of delete document successful. 

# Overview:
In this project used PyQt5 to create graphical user interface. Used Firebase Admin SDK for interacting with firestore and also used NoSQL database for storing user data. In Firestore collections named user will store documents with fields like name, age, phone, and email.
