\# 🔐 XorWare



\*\*Category:\*\* Cryptography  

\*\*Difficulty:\*\* Easy  

\*\*Author:\*\* ret2root  



---



\## 🧩 Challenge Description



In the past, the world stopped for a moment.  

Screens went dark. Hospitals froze. Files became prisoners.



A simple algorithm powered the chaos — predictable, yet hidden in time.



This program is a relic recovered from an abandoned malware lab.  

It encrypts using a random key, but the randomness was never truly random.



The developer trusted a single moment in history to seed the chaos.



If you understand the day the world learned the cost of weak randomness,  

the lock will open.



The key was generated \*\*once\*\* — at the moment the world panicked.



🕰️ \*History is your debugger.\*



---



\## 📁 Files



The following files are provided with this challenge: 



* \*\*source.py\*\*
* \*\*masseage.enc\*\*



\## 🎯 Objective



Analyze the program and recover the original \*\*flag\*\*.



The encryption process uses \*\*XOR\*\*, but the key generation has a critical flaw.  

If you identify how the key was generated, you can reproduce it and decrypt the flag.



---



\## 🧠 Hint



Think about a \*\*global cyber incident\*\* where ransomware spread rapidly and affected hospitals, companies, and governments worldwide.



The panic happened in \*\*a specific moment in time\*\*.



---



\## 🚩 Flag Format



``` 0DAY{fake\_flag} ```



