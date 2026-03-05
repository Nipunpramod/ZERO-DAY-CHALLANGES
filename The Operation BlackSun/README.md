# 🔐 Operation Black Sun

**Category:** Android Reversing  
**Difficulty:** Hard  
**Author:** ret2root  

---

## 🧩 Challenge Description

Black Sun Nuclear Power Plant was once considered one of the most secure energy facilities in the region.  
Our systems were protected by multiple layers of digital and physical security. Yet, in early 2036, an unknown attacker managed to breach our core control network and manipulate critical reactor parameters.

The attacker used a customized Android application as his primary control tool. Through this app, he gained remote access, injected malicious commands, and slowly took control of essential safety systems. By the time we detected the intrusion, several automated safeguards had already been disabled.

In response to this crisis, we hired the elite cybersecurity investigation team known as **AlienX Security**. Their mission was simple: trace the attacker, analyze his tools, and regain control of the reactor before it was too late.

AlienX researchers successfully recovered the attacker’s Android application from an abandoned server node. However, during analysis, they discovered that the hacker had heavily modified and obfuscated the app. Critical functions were hidden inside encrypted modules and native libraries. Most of the original control paths had been altered, making direct access impossible.

As the investigation continued, the situation inside the reactor worsened:

- Core temperature began to rise.  
- Cooling efficiency dropped.  
- Power output exceeded safe operating limits.  

Emergency alarms echoed through the control room.

If the reactor reaches critical overload, a catastrophic meltdown will occur — a disaster on the scale of Chernobyl. Entire regions would be contaminated, millions of lives put at risk, and the environmental impact would be catastrophic for decades.  

Time is running out.

AlienX analysts are now stuck at a crucial point. They believe the **shutdown override code** and **safety restoration keys** are still hidden inside the attacker’s application — but only someone with exceptional reverse-engineering skills can extract them.

That is where you come in.

You have been granted limited access to the recovered APK. Your mission is to:

1. Analyze the application.  
2. Uncover hidden mechanisms.  
3. Bypass the attacker’s protections.  
4. Restore manual control of the reactor.

Failure is not an option. If the system is not shut down in time, **Black Sun will fall — and humanity will pay the price.**

---

## 📁 Files

The following file is provided for this challenge:

* **OBS.apk** → The recovered and obfuscated Android application.

---

## 🎯 Objective

Reverse engineer the APK to recover:

- The **shutdown override code**  
- The **safety restoration keys**

These secrets are hidden within obfuscated or encrypted modules. Only by analyzing the application thoroughly can the reactor be safely restored.

---

## 🧠 Hint

- Look for **encrypted or obfuscated methods**.  
- Bypass protections carefully — the attacker anticipated casual analysis.

---

## 🚩 Flag Format
``` 0DAY-{MD5} ```


---

## ⚠️ Notes

- The APK is heavily obfuscated.  
- A local server may be running in the background.