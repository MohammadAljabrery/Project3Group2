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
        
class LoggerFrame(Frame):
    def __init__(self, parent, previous_window, logger):
        super().__init__(parent, bg="lightblue")
        self.parent = parent
        self.previous_window = previous_window
        self.logger = logger

        # Frame for the Logger Table
        tableFrame = Frame(self, bg="lightgrey")
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
        self.logTable = ttk.Treeview(
            tableFrame, columns=("time", "user", "action"), show="headings", height=15
        )
        self.logTable.pack(fill="both", expand=True)

        # Define Table Columns
        self.logTable.heading("time", text="Time")
        self.logTable.heading("user", text="User")
        self.logTable.heading("action", text="Action Description")

        self.logTable.column("time", anchor="center", width=300)
        self.logTable.column("user", anchor="center", width=200)
        self.logTable.column("action", anchor="w", width=700)

        # Logger Alternative Row Colors
        self.logTable.tag_configure("odd", background="lightgrey")
        self.logTable.tag_configure("even", background="white")
        # Add Scrollbar
        scrollbar = ttk.Scrollbar(tableFrame, orient="vertical", command=self.logTable.yview)
        self.logTable.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Button to Reload Logs
        reloadButton = Button(
            self,
            text="Reload Logs",
            command=self.loadLogsToTable,
            font=("Consolas", 12),
            bg="lightblue",
        )
        reloadButton.pack(pady=10)

        # Search Frame
        searchFrame = Frame(self, bg="lightblue")
        searchFrame.pack(anchor="center", pady=10)

        # Search by User
        searchUserLabel = Label(searchFrame, text="Search by User:", font=("Consolas", 12), bg="lightblue")
        searchUserLabel.grid(row=0, column=0, padx=5, pady=5)
        self.searchUserEntry = Entry(searchFrame, font=("Consolas", 12))
        self.searchUserEntry.grid(row=0, column=1, padx=5, pady=5)
        searchUserButton = Button(searchFrame, text="Search by User", font=("Consolas", 12), bg="lightblue", command=lambda: self.searchLogs("user"))
        searchUserButton.grid(row=0, column=2, padx=5, pady=5)

        # Search by Action
        searchActionLabel = Label(searchFrame, text="Search by Action:", font=("Consolas", 12), bg="lightblue")
        searchActionLabel.grid(row=1, column=0, padx=5, pady=5)
        self.searchActionEntry = Entry(searchFrame, font=("Consolas", 12))
        self.searchActionEntry.grid(row=1, column=1, padx=5, pady=5)
        searchActionButton = Button(searchFrame, text="Search by Action", font=("Consolas", 12), bg="lightblue", command=lambda: self.searchLogs("action"))
        searchActionButton.grid(row=1, column=2, padx=5, pady=5)

        # Back Button
        backButton = Button(
            self,
            text="Back",
            command=self.goBack,
            font=("Consolas", 12),
            bg="lightblue",
        )
        backButton.pack(pady=10)

        # Initial Load of Logs
        self.loadLogsToTable()

    def loadLogsToTable(self):
        """Load logs from the logs.txt file and runtime logs into the Treeview table with alternating row colors."""
        # Clear the table first
        for item in self.logTable.get_children():
            self.logTable.delete(item)

        # Get logs and populate the table
        logs = self.logger.getLogs()

        if logs == "No Logs Available.":
            self.logTable.insert("", "end", values=("No Logs Available", "", ""))
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
                    self.logTable.insert("", "end", values=(timestamp, user, action), tags=(row_tag,))
                except IndexError:
                    print(f"Skipping malformed log entry: {log}")

    def searchLogs(self, criteria):
        """Filter logs based on the selected criteria (user or action)."""
        searchTerm = ""
        if criteria == "user":
            searchTerm = self.searchUserEntry.get().strip().lower()
        elif criteria == "action":
            searchTerm = self.searchActionEntry.get().strip().lower()

        if not searchTerm:
            self.logTable.insert("", "end", values=("Please enter a search term", "", ""))
            return

        # Clear the table first
        for item in self.logTable.get_children():
            self.logTable.delete(item)

        # Get logs and filter them
        logs = self.logger.getLogs().split("\n")  # Ensure logs are in list format
        if logs == "No Logs Available.":
            self.logTable.insert("", "end", values=("No Logs Available", "", ""))
            return

        for log in logs:
            if "USER:" in log and "ACTION:" in log:
                # Split the log entry
                timestamp = log.split("]")[0][1:]  # Extract timestamp without brackets
                user = log.split("USER: ")[1].split(" | ACTION:")[0].lower()  # Extract user
                action = log.split("ACTION: ")[1].lower()  # Extract action description

                # Check criteria match
                if (criteria == "user" and searchTerm in user) or (criteria == "action" and searchTerm in action):
                    self.logTable.insert("", "end", values=(timestamp, user, action))

    def goBack(self):
        """Go back to the previous window."""
        self.parent.destroy()  # Destroy the current logger window
        self.previous_window.deiconify()  # Show the previous window


# Run the Logger Frame
def run_logger_frame(parent, previous_window, logger):
    frame = LoggerFrame(parent, previous_window, logger)
    frame.pack(fill=BOTH, expand=True)
