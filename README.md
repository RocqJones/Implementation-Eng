# Implementation-Eng
“Implementation Engineer Interview Questions Response”

## Section A.
### 1. Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one.
* [Integration Protocols](https://en.wikipedia.org/wiki/System_integration): In software engineering, integration protocol is the aggregation of bringing together different sub-systems components into one system with the aim of delivering the overarching functionality while ensuring that they function interoperably.
#### Information Technology (IT) integration vs continuous integration (CI).
**IT integration, or systems integration**, is the connection of *data, applications, APIs, and devices* across your IT organization to be more *efficient, productive, and [agile](https://www.atlassian.com/agile/scrum)*. Integration is key when discussing business transformation—fundamental changes in how you conduct business to adapt as the market shifts—as it makes everything in IT work together.
* IT integration isn’t the same as **continuous integration (CI)**, which is a developer practice where working copies of code are merged into a shared central repository multiple times a day. The goal of CI is to automate build and verifications so problems can be detected earlier—leading to faster development.
![cicd](https://github.com/RocqJones/Implementation-Eng/imgs/continuous-integration-vs-delivery.png)

#### Examples of Integration Protocols.
##### a) Application Programming Interface (API).
##### b) WEBHOOKS / HTTP callbacks.
##### c) ORCHESTRATION.

#### a) Application Programming Interface (API).
* An API uses a common code language to specify functionality and set protocols which gives your applications the ability to transfer data.

#### b) WEBHOOKS / HTTP callbacks.
* For webhooks, implementation is often *not code-based*. They often have modules that are programmable within a web application. Instead of being request-based, **webhooks are event-based**. *They only trigger when specific events occur within a third-party service*.

#### C) ORCHESTRATION.
* The most **automated integration option** is *orchestrations*. 
* Orchestration refers to the process of *automating multiple systems and services together*. Teams will often use software configuration management tools such as [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) to build orchestrations. **Software configuration management tools offers** various methods such as *snap-ins or hosting APIs* to connect with applications to manage the automation workflow.

### 2. Give a walk-through of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and  configurations you will use to manage load and asynchronous services.

### 3. Give examples of different encryption/hashing methods you have come across (one way and two way) and give example scripts in python 3 on how to achieve each one.

## Section B.
### 1. Create a login and a success page in Django. A mockup of the created pages should also be submitted. The mockups should have been created by using advanced design wireframe tools thus showcasing prowess in usage of the tools and use of production server deployments on uwsgi/nginx. Ensure that the sessions are well and securely managed.
