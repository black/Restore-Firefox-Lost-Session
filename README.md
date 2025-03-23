# Restore-Firefox-Lost-Session


Use the link below to open your session file in JSON format.
# https://www.jeffersonscher.com/res/scrounger.html



# https://support.mozilla.org/bm/questions/1364802

I went full desperation mode and did some manual editing of the sessionstore.jsonlz4 using https://github.com/jusw85/mozlz4

Extract the JSON from previous.jsonlz4

Download mozlz4 (I downloaded for Windows). For convenience I renamed the downloaded file to mozlz4.exe.
Place the exe in the folder with your backed up copy of sessionstore-backups
Open a terminal in this folder
Run mozlz4 --extract "previous.jsonlz4" > previous-extracted.json
Use a text editor to format the extracted JSON and replace the "windows" element with the contents of "_closedWindows".

Open https://vscode.dev/ or open VS Code or equivalent text editor that can format JSON. (The next few steps assume VS Code.)
Open previous-extracted.json in the text editor (can drag and drop into https://vscode.dev)
Top left menu > View > Command Palette (or press F1)
Type "language" and then select "Change Language Mode". Type "json" and select the "JSON" option.
Open command palette again (F1). Type "format doc" and then select the "Format document" option (or press Shift + Alt + F).
Open command palette again (F1). Type "fold all" and then select "Fold All".
Now expand the root node (click arrow in left margin of editor).
Expand "windows" and "_closedWindows" twice to see their inner items like "tabs", "selected", "_closedTabs", etc.
Copy the line from "windows" that says: "_shouldRestore": true,
Paste this line into the "_closedWindows" section just below "title".
Copy the entire "_closedWindows" section by selecting everything from its opening bracket "[" to the closing bracket "]".
Select the entire "windows" section, starting from its opening bracket "[" to its closing bracket "]" and then paste the "_closedWindows" section that you just copied.
Save this file as previous-extracted-modified.json. Save it with mozlz4 in the session-backup folder.
Re-compress your modified sessionstore.jsonlz4 and place it into your Firefox profile to restore the closed windows.

In the terminal window, and run: mozlz4 --compress "previous-extracted-modified.json" > sessionstore.jsonlz4
Open your Firefox profile folder (about:support > Open Profile folder).
Close Firefox so that the sessionstore.jsonlz4 file will be present in the profile folder.
Delete, move or rename sessionstore.jsonlz4 in the base profile folder and all the files in the sessionstore-backups folder.
Paste your modified sessionstore.jsonlz4 into the base profile folder.
Open Firefox and the closed window will be restored.

# https://www.reddit.com/r/firefox/comments/gyxr85/how_to_restore_lost_firefox_session/#:~:text=Check%20%22Recently%20Closed%20Windows%22%20as,file%20that%20you%20just%20renamed.


# https://www.reddit.com/r/firefox/comments/56sevb/how_to_restore_a_browsing_session_from_backup/