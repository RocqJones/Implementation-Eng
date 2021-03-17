# Implementation-Eng
“Implementation Engineer Interview Questions Response”

## Section A.
### 1. Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one.
* [Integration Protocols](https://en.wikipedia.org/wiki/System_integration): In software engineering, integration protocol is the aggregation of bringing together different sub-systems components into one system with the aim of delivering the overarching functionality while ensuring that they function interoperably.
#### Information Technology (IT) integration vs continuous integration (CI).
**IT integration, or systems integration**, is the connection of *data, applications, APIs, and devices* across your IT organization to be more *efficient, productive, and [agile](https://www.atlassian.com/agile/scrum)*. Integration is key when discussing business transformation—fundamental changes in how you conduct business to adapt as the market shifts—as it makes everything in IT work together.
* IT integration isn’t the same as **continuous integration (CI)**, which is a developer practice where working copies of code are merged into a shared central repository multiple times a day. The goal of CI is to automate build and verifications so problems can be detected earlier—leading to faster development.<br>
![cicd](https://github.com/RocqJones/Implementation-Eng/blob/main/imgs/continuous-integration-vs-delivery.png)<br>
  (CICD Collaboration against value illustration)

#### Examples of Integration Protocols.
**a) Application Programming Interface (API).**<br>
**b) WEBHOOKS / HTTP callbacks.**<br>
**c) ORCHESTRATION.**<br>

#### a) Application Programming Interface (API).
A computing interface that defines interactions between multiple software applications or mixed hardware-software intermediaries. It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used,and the conventions to follow.
* An API uses a common code language to specify functionality and set protocols which gives your applications the ability to transfer data.<br>
**Below is a demonstration of a REST API with Python3. For the methods and endpoints I will be using [my own API from this project](https://github.com/RocqJones/Undergraduate-Project-2020):**<br>
#### API JSON Format.
```JSON
[
    {
      "demand": 14, 
      "id": 1, 
      "product_name": "Passion"
    }, 
    {
      "demand": 12, 
      "id": 2, 
      "product_name": "Mangoes"
    }
]
```
#### Key Methods.
* **GET:** HTTP GET method is used to request data from a specified resource.
* **PUT:** HTTP PUT Used to modify a singular resource which is already a part of resources collection.
* **POST:** HTTP POST methd is used to send data to a server to create or update a resource.
* **DELETE:** HTTP DELETE method is used to delete a resource from the server. Although, sending a message body on a DELETE request might cause some servers to reject the request.

#### Step 1: Install Python3 'Requests'.
In Python, we are lucky to have an excellent HTTP library: Kenneth Reitz’ `requests`. It’s one of the few projects worth treating as if it is part of the standard library:
```SHELL
$ pip3 install requests
```
#### Step 2: Get a list of action items from REST API endpoint.
* REST API endpoint: `https://rocqjones.pythonanywhere.com/api/products/all` for this example.
The python code will be as follows
```Python
import requests

base_url = "https://rocqjones.pythonanywhere.com/api/products/all"

resp = requests.get(base_url)

if resp.status_code != 200:
    raise ApiError('GET /products/all/ {}'.format(resp.status_code))

else:
    for items in resp.json():
        print(items)
```

**Note:** *Unless otherwise noted, all actions return 200 on success; those referencing a task ID return 404 if the ID is not found. The response body is empty unless specified otherwise. All non-empty response bodies are JSON. All actions that take a request body are JSON (not form-encoded).*

#### b) WEBHOOKS / HTTP callbacks.
* For webhooks, implementation is often *not code-based*. They often have modules that are programmable within a web application. Instead of being request-based, **webhooks are event-based**. *They only trigger when specific events occur within a third-party service*.

#### C) ORCHESTRATION.
* The most **automated integration option** is *orchestrations*. 
* Orchestration refers to the process of *automating multiple systems and services together*. Teams will often use software configuration management tools such as [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) to build orchestrations. **Software configuration management tools offers** various methods such as *snap-ins or hosting APIs* to connect with applications to manage the automation workflow.

### 2. Give a walk-through of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and  configurations you will use to manage load and asynchronous services.

### 3. Give examples of different encryption/hashing methods you have come across (one way and two way) and give example scripts in python 3 on how to achieve each one.

## Section B.
### 1. Create a login and a success page in Django. A mockup of the created pages should also be submitted. The mockups should have been created by using advanced design wireframe tools thus showcasing prowess in usage of the tools and use of production server deployments on uwsgi/nginx. Ensure that the sessions are well and securely managed.
