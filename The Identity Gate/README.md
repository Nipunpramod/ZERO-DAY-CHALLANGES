# 🔐 The Identity Gate

**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Author:** ret2root  

---

## 🧩 Challenge Description

My friend was working late on a research project about process identity in Linux.  
He believed that who you are depends on what the system tells you — not who you really are.

One night, he sent me a strange message:

> “I built a program that only trusts someone with the right identity.  
> Not root. Not admin.  
> Someone who can convince the program they are someone else.”

The next morning, his laptop was gone.

All that remains is this compiled binary.

- It doesn’t ask for passwords.  
- It doesn’t read input.  
- It doesn’t care who you really are.

It only cares about the story the system tells it.

Your task is to recover the secret he protected.

**Remember:**  
Sometimes, breaking the rules isn’t enough.  
You must change the narrative.

---

## 📁 Files

The following file is provided for this challenge:

* **challange** → Compiled binary.

---

## 🎯 Objective

Analyze the binary and recover the secret.  

The program checks the **process identity** reported by the system.  
It does not rely on passwords or input.  
You may need to **manipulate system calls or environment** to trick it.

---

## 🧠 Hint

- Think about **Linux process identity**: UID, EUID, GID.  
- Check how a process can **pretend to be someone else**.  
- Sometimes the system's story differs from reality.

---

## 🚩 Flag Format
 ``` 0DAY{fake_flag} ```


---

## ⚠️ Notes

- The binary is **self-contained**.  
- You don’t need root permissions to solve it.  
- Reverse engineering skills and knowledge of **Linux process attributes** will help.