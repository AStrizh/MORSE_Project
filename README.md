# MORSE_Project

Ready to review


## Directions
   
   The project was built with PyCharm on Windows  
   There should be no issues importing into PyCharm  
   
   When launched Main UI will ask for a file name and a series of dates as per instructions  
   

## Files
   
   Main - Launched the program  
   ReadTrades - Used for first task, returns trade at time with record_at_time() method   
   ReadStats - Used for second task, calculates statistics  with the read_stat_record() method  
   Trade - Object to contain a trade object  
   TestTrade - Tests the Trade object
   TestReadTrade - Tests trade reader
   TestReadStats - Tests stats calculator
   
   samplefile.txt - txt file of sample trades

## Assumptions

It is assumed that all times are in Zulu/UTC  
In its current state it will only process dates and times that either end with "Z" timezone or no timezone at all  

It is assumed that trades are in chronological order  

It it is assumed that some date/time stamps are fault and that those trades should be ignored  


## Build Tools

- Python 3.7
- PyCharm
---

## Author

Aleksandr Strizhevskiy, abstrizhevskiy@gmail.com

---
