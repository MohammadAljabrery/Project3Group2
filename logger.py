import random 
import datetime
from tkinter import *
from tkinter import ttk
import os


class LoggerSystem:
    def __init__(self, logFileName="logs.txt"):
        self.logs = []
        self.logFileName = logFileName
    
    def logAction(self, userID: str, action: str):
        logTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logEntry = {
            "userID": userID,
            "action": action,
            "logTime": logTime
        }
        self.logs.append(logEntry)
        print(f"[{logTime}] USER: {userID} | ACTION: {action}")
        
        
    def getLogs(self):
        fileLogs = []
        if os.path.exists(self.logFileName):
            with open(self.logFileName, "r") as file:
                fileLogs = file.readlines()
    
        runtimeLogs = [
            f"[{entry['logTime']}] USER: {entry['userID']} | ACTION: {entry['action']}"
            for entry in self.logs
        ]
    
        combinedLogs = runtimeLogs + [log.strip() for log in fileLogs]
        if not combinedLogs:
            return "No Logs Available."
    
        # Return logs as a single string
        return "\n".join(combinedLogs)

    
    def saveLogs(self):
        # Read existing logs from the file to avoid duplicates
        existingLogs = []
        if os.path.exists(self.logFileName):
            with open(self.logFileName, "r") as file:
                existingLogs = file.readlines()

        # Format new logs
        newLogs = [
            f"[{entry['logTime']}] USER: {entry['userID']} | ACTION: {entry['action']}\n"
            for entry in self.logs
        ]
    
        # Combine existing logs with new logs
        combinedLogs = list(set(existingLogs + newLogs))  # Remove duplicates
        combinedLogs.sort(reverse=True)  # Sort by most recent first

        # Save all logs back to the file
        with open(self.logFileName, "w") as file:
            file.writelines(combinedLogs)

        print(f"Logs saved to {self.logFileName}")
        
def LoggerGui():
    
    def loadLogsToTable():
        """Load logs from the logs.txt file and runtime logs into the Treeview table with alternating row colors."""
        # Clear the table first
        for item in logTable.get_children():
            logTable.delete(item)

        # Get logs and populate the table
        logs = logger.getLogs()

        if logs == "No Logs Available.":
            logTable.insert("", "end", values=("No Logs Available", "", ""))
            return

        # Split logs into individual lines and parse each
        logEntries = logs.split("\n")
        for index, log in enumerate(logEntries):
            if "USER:" in log and "ACTION:" in log:
                try:
                    # Extract log components
                    timestamp = log[log.find("[") + 1: log.find("]")]
                    user = log.split("USER: ")[1].split(" | ")[0].strip()
                    action = log.split("ACTION: ")[1].strip()

                    # Determine the row tag for alternating colors
                    row_tag = "odd" if index % 2 == 0 else "even"

                    # Insert into the table with the appropriate tag
                    logTable.insert("", "end", values=(timestamp, user, action), tags=(row_tag,))
                except IndexError:
                    print(f"Skipping malformed log entry: {log}")
    
    def searchLogs(criteria):
        """Filter logs based on the selected criteria (user or action)."""
        searchTerm = ""
        if criteria == "user":
            searchTerm = searchUserEntry.get().strip().lower()
        elif criteria == "action":
            searchTerm = searchActionEntry.get().strip().lower()

        if not searchTerm:
            logTable.insert("", "end", values=("Please enter a search term", "", ""))
            return

        # Clear the table first
        for item in logTable.get_children():
            logTable.delete(item)

        # Get logs and filter them
        logs = logger.getLogs().split("\n")  # Ensure logs are in list format
        if logs == "No Logs Available.":
            logTable.insert("", "end", values=("No Logs Available", "", ""))
            return

        for log in logs:
            if "USER:" in log and "ACTION:" in log:
                # Split the log entry
                timestamp = log.split("]")[0][1:]  # Extract timestamp without brackets
                user = log.split("USER: ")[1].split(" | ACTION:")[0].lower()  # Extract user
                action = log.split("ACTION: ")[1].lower()  # Extract action description

                # Check criteria match
                if (criteria == "user" and searchTerm in user) or (criteria == "action" and searchTerm in action):
                    logTable.insert("", "end", values=(timestamp, user, action))



    
    window = Tk()
    window.title("Logger System")
    window.geometry("1920x1080")
    window.configure(bg="lightblue")

    # Frame for the Logger Table
    tableFrame = Frame(window, bg="lightgrey")
    tableFrame.pack(anchor="center", pady=20, padx=20, fill="both", expand=True)

    # Table Title
    tableTitleLabel = Label(
        tableFrame, text="Action Logs", font=("Consolas", 14), bg="lightgrey"
    )
    tableTitleLabel.pack(anchor="n", pady=10)

    # Logger Table
    style = ttk.Style()
    style.configure("Treeview", font=("Consolas", 12))
    style.configure("Treeview.Heading", font=("Consolas", 14, "bold"))
    logTable = ttk.Treeview(
        tableFrame, columns=("time", "user", "action"), show="headings", height=15
    )
    logTable.pack(fill="both", expand=True)

    # Define Table Columns
    logTable.heading("time", text="Time")
    logTable.heading("user", text="User")
    logTable.heading("action", text="Action Description")

    logTable.column("time", anchor="center", width=300)
    logTable.column("user", anchor="center", width=200)
    logTable.column("action", anchor="w", width=700)

    # LOGGER ALTERNATIVE ROW COLOURS
    logTable.tag_configure("odd", background="lightgrey")
    logTable.tag_configure("even", background="white")
    # Add Scrollbar
    scrollbar = ttk.Scrollbar(tableFrame, orient="vertical", command=logTable.yview)
    logTable.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Button to Reload Logs
    reloadButton = Button(
        window,
        text="Reload Logs",
        command=lambda: loadLogsToTable(),
        font=("Consolas", 12),
        bg="lightblue",
    )
    reloadButton.pack(pady=10)
    
    
    searchFrame = Frame(window, bg="lightblue")
    searchFrame.pack(anchor="center", pady=10)

    # Search by User
    searchUserLabel = Label(searchFrame, text="Search by User:", font=("Consolas", 12), bg="lightblue")
    searchUserLabel.grid(row=0, column=0, padx=5, pady=5)
    searchUserEntry = Entry(searchFrame, font=("Consolas", 12))
    searchUserEntry.grid(row=0, column=1, padx=5, pady=5)
    searchUserButton = Button(searchFrame, text="Search by User", font=("Consolas", 12), bg="lightblue", command=lambda: searchLogs("user"))
    searchUserButton.grid(row=0, column=2, padx=5, pady=5)

    # Search by Action
    searchActionLabel = Label(searchFrame, text="Search by Action:", font=("Consolas", 12), bg="lightblue")
    searchActionLabel.grid(row=1, column=0, padx=5, pady=5)
    searchActionEntry = Entry(searchFrame, font=("Consolas", 12))
    searchActionEntry.grid(row=1, column=1, padx=5, pady=5)
    searchActionButton = Button(searchFrame, text="Search by Action", font=("Consolas", 12), bg="lightblue", command=lambda: searchLogs("action"))
    searchActionButton.grid(row=1, column=2, padx=5, pady=5)

    # Initial Load of Logs
    loadLogsToTable()

    window.mainloop()

        
logger = LoggerSystem()
'''
logger.logAction("Mohammad", "do this doing that")
logger.logAction("Nikhil", "Being Silly")
logger.logAction("Henil", "Securing the security system")
logger.logAction("Meera", "checking the envirnment, exploring nature and shit")'''

def run_logger_gui():
    LoggerGui()

    print("\nALL LOGS:")
    print(logger.getLogs())
    logger.saveLogs()
