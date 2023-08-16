# Purpose: To Create a Bug Tracking Menu for Developers to Keep Note About Bugs Encountered During Development
# Author: Lorenz Wilkins
# Resources: Geeks for Geeks, Python Library
# Date Modified: August 15th, 2023


# Importing packages
import os
from datetime import datetime
import json
import pytz

# Creating a new file called bugs
bugsDirectory = "bugs"

# Creating the json file with the id # and data
def createBugFile (bugID, bugData):
    fileName = f"{bugsDirectory}/bug-{bugID}.json"
    with open(fileName, "w") as f:
        json.dump(bugData, f, indent=4)

# Retrieving bugID # when option 2 is selected
def getFileName(bugID):
    return f"{bugsDirectory}/bug-{bugID}.json"

# Loading the Data
def loadData(bugID):
    fileName = getFileName(bugID)
    if os.path.exists(fileName):
        with open(fileName, "r") as f:
            return json.load(f)
    return bugID

# Updating status of a bug
def updateStatus(bugID, newStatus):
    bugData = loadData(bugID)
    if bugData:
        bugData["Status"] = newStatus
        bugData["Last Updated"] = datetime.now(pytz.timezone('US/Pacific'))
        with open(getFileName(bugID), "w") as f:
            json.dump(bugData, f, indent=4, default=str)
        print("Bug status updated.")
    else:
        print("Bug not found.")

# Menu Function
def main():
    if not os.path.exists(bugsDirectory):
        os.makedirs(bugsDirectory)
        
    while True:
        print("***************")
        print("Bug Tracker")
        print("***************\n")
        print("1. File a new bug\n")
        print("2. Update bug status\n")
        print("3. Exit")
        choice = input("\nEnter your choice: ")
            
        if choice == "1":
            bugID = len(os.listdir(bugsDirectory))
            print("\n***************")
            print("File A Bug")
            print("***************\n")
            name = input("Enter Developer's name: ")
            bugType = input("Enter type of bug: ")
            priority = input("Enter priority of bug: ")
            bugDescription = input("Enter bug description: ")
            status = "Open"
            lastUpdated = datetime.now(pytz.timezone('US/Pacific'))
                
            bugData = {
                "name": name,
                "Bug Type": bugType,
                "Priority": priority,
                "Description": bugDescription,
                "Status": status,
                "Last Updated": lastUpdated.isoformat()
                }
                
            createBugFile(bugID, bugData)
            print ("Bug File Added.")
                
        elif choice == "2":
            print("\n***************")
            print("Update Bug Status")
            print("***************\n")
            bugID = input("Enter Bug ID: ")
            newStatus = input("Enter New Status (Open, In Progress, Resolved): ")
            updateStatus(int(bugID), newStatus)
            
        elif choice == "3":
            break
        
if __name__ == "__main__":
    main()