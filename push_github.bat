"C:\Program Files\Git\cmd\git.exe" config user.email "admin@localhost"
"C:\Program Files\Git\cmd\git.exe" config user.name "admin"
"C:\Program Files\Git\cmd\git.exe" add .
"C:\Program Files\Git\cmd\git.exe" commit -m "Initialize HealthOrganizer project"
"C:\Program Files\Git\cmd\git.exe" branch -M main
"C:\Program Files\Git\cmd\git.exe" remote remove origin
"C:\Program Files\Git\cmd\git.exe" remote add origin https://github.com/Bharathvaj10/ReportCollection.git
"C:\Program Files\Git\cmd\git.exe" push -u origin main
