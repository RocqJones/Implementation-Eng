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
#### Below is a demonstration of a REST API with Python3. For the methods and endpoints I will be using [my own API (click on this link to view project for more endpoints)](https://github.com/RocqJones/Undergraduate-Project-2020):
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
In Python, we are lucky to have an excellent HTTP library: *Kenneth Reitz’* `requests`. It’s one of the few projects worth treating as if it is part of the standard library:
```SHELL
$ pip3 install requests
```
#### Step 2: Get a list of action items from REST API endpoint.
* REST API endpoint: `https://rocqjones.pythonanywhere.com/api/products/all` for this example.
#### Step 3: Import 'requests'.
```Python
import requests
```
#### Step 4: Check the server response status.
If the reponse is `OK` which is equivalent to `200` it means the server is responding and you can print the json data. Here is the python code:
```Python
import requests

def fetchData(url):
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise ApiError('GET /products/all/ {}'.format(resp.status_code))
    else:
        for items in resp.json():
            print(items)

if __name__ == '__main__':
    base_url = "https://rocqjones.pythonanywhere.com/api/products/all"
    fetchData(base_url)
```

**Note:** *Unless otherwise noted, all actions return 200 on success; those referencing a task ID return 404 if the ID is not found. The response body is empty unless specified otherwise. All non-empty response bodies are JSON. All actions that take a request body are JSON (not form-encoded).*

#### b) WEBHOOKS / HTTP callbacks.
* For webhooks, implementation is often *not code-based*. They often have modules that are programmable within a web application. Instead of being request-based, **webhooks are event-based**. *They only trigger when specific events occur within a third-party service*.
* In simple terms **Webhooks** are *automated messages sent from apps when something happens*. They have a *message or payload and are sent to a unique URL* essentially the app's phone number or email address. Webhooks are much like SMS notifications. I have interacted with webhooks through Google Firebase API which are all done with webhooks.
<a href="url"><img src="https://github.com/RocqJones/Implementation-Eng/blob/main/imgs/webhooks.png" height="350" width="100%" ></a>

##### Webhooks python flask.
Webhooks run a large portion of the "magic" that happens between applications. They are sometimes called reverse APIs, callbacks, and even notifications. Many services, such as SendGrid, Stripe, Slack, and GitHub use events to send webhooks as part of their API. This allows your application to listen for events and perform actions when they happen.
##### There are a few consistencies across webhook implementations.
**a.** They are normally `POST` requests.<br>
**b** They receive `JSON` data.<br>
**c** They need to respond quickly.<br>

##### Requirements: 1. Install Flask
```Shell
$ python3 -m pip install Flask
```

##### 2. Receive a webhook with Flask.
Imports the Flask class along with the `request` and Response objects. Then instantiates it with a name of `__name__` before assigning it to the `app` variable. This naming scheme is convention in the Flask documentation.
```Python
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)
```

##### Receive a webhook with Django.
##### a. Install django.
As a more traditional Model-View-Controller (MVC) framework, Django scaffolds out the main parts of the project for you.
`python3 -m pip install Django`
* CREATING VIRTUAL ENVIRONMENT
```
$ python3 -m venv myvenv
```
* SWITCHING TO VENV
```
$ source myvenv/bin/activate 
```
or 
```
$ . myvenv/bin/activate 
```
* START A PROJECT
```Shell
$ django-admin startproject webhooks.
```
##### b. Open the file webhooks/views.py. Here we will write the logic for handling a route.
```Python
from django.http import HttpResponse
from django.views.decorators.http import require_POST

@require_POST
def example(request):
	return HttpResponse('Hello, world. This is the webhook response.')
```
* This code does the following:
- It imports the `HttpResponse` object that will be used to send a response.
- It imports a special decorator to limit the request method. In Django, routes accept all HTTP methods by default and let the views manage which methods they respond to.
- Calls the decorator to limit the function that follows to only the `POST` method.
- Defines a function, named example that takes the request as an argument and returns a response.

* Next, create webhooks/urls.py if it doesn't already exist. This is where we organize routes within this sub-app of our project.
```Python
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhooks/', include('webhooks.urls'))
]
```
* CREATING DATABASE (sqlite3)
```
$ python3 manage.py migrate
```
* RUN SERVER
```
$ python3 manage.py runserver
```
* CREATING SUPERUSER
This is done after configuring admin section inside the app.
```
$ python3 manage.py createsuperuser
```
`[admin, admin@admin.com, p@$$w0rd]`

#### C) ORCHESTRATION.
* The most **automated integration option** is *orchestrations*. 
* Orchestration refers to the process of *automating multiple systems and services together*. Teams will often use software configuration management tools such as [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1) to build orchestrations. **Software configuration management tools offers** various methods such as *snap-ins or hosting APIs* to connect with applications to manage the automation workflow.
##### Cloud-orchestration Vs Automation.
<a href="url"><img src="https://github.com/RocqJones/Implementation-Eng/blob/main/imgs/cloud-orchestration-vs-automation-2.jpg" height="400" width="100%" ></a>
    
### 2. Give a walk-through of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and configurations you will use to manage load and asynchronous services.
**Push notifications** are short popup messages sent by a web-based application server to the client application.
* They’re a great tool to improve your app’s engagement level and website traffic. 
* To understand the definition of push notifications, we need to clear our concept of the client-server communication.
* The server is any computer/program that sends information over a network to the client, which is the receiving computer/program. 
* In a typical client-server exchange, the client asks for data and the server sends the requested information. 
* We use “push notification” when the server sends the information to the client without the client asking for it. So, the information is “pushed” by the server to the client.
* All brands that use push notifications as a marketing strategy, use them as a part of a larger campaign, and not only to push traffic to their content.
* There are plenty of examples of best practices about how one may use push notifications. The truth is that push notifications are powerful for both websites and mobile apps.
* Brands like National Geographic and Ford have successfully leveraged the power of push notifications to get customers engaged with their content.
#### Push Notification Terms
**a.** *Notification* – a message displayed to the user outside of the app's normal UI (i.e., the browser).<br>
**b.** *Push Message* – a message sent from the server to the client.<br>
**c.** *Push Notification* – a notification created in response to a push message.<br>
**d.** *Notifications API* – an interface used to configure and display notifications to the user.<br>
**e** *Push API* – an interface used to subscribe your app to a push service and receive push messages in the service worker.<br>
**f** *Web Push* – an informal term referring to the process or components involved in the process of pushing messages from a server to a client on the web.<br>
**g** *Push Service* – a system for routing push messages from a server to a client. Each browser implements its own push service.<br>
**h** *Web Push Protocol* – describes how an application server or user agent interacts with a push service.<br>
#### Technologies and configurations you will use to manage load and asynchronous services.
##### Request permission
Before we can create a notification we need to get permission from the user. Below is the code to prompt the user to allow notifications. This goes in the app's main JavaScript file.
* `JavaScript`
main.js
```JavaScript
Notification.requestPermission(function(status) {
    console.log('Notification permission status:', status);
});
```
We call the `requestPermission` method on the global Notification object. This displays a pop-up message from the browser requesting permission to allow notifications. The user's response is stored along with your app, so calling this again returns the user's last choice. Once the user grants permission, the app can display notifications.
#### Display a notification
* We can show a notification from the app's main script with the `showNotification` method (the "Invocation API"). Here is an example:<br>
main.js
```JavaScript
function displayNotification() {
  if (Notification.permission == 'granted') {
    navigator.serviceWorker.getRegistration().then(function(reg) {
      reg.showNotification('Hello world!');
    });
  }
}
```
#### Add notification options
The showNotification method has an optional second argument for configuring the notification. The following example code demonstrates some of the available options. See the showNotification reference on MDN for a complete explanation of each option.<br>
main.js
```JavaScript
function displayNotification() {
  if (Notification.permission == 'granted') {
    navigator.serviceWorker.getRegistration().then(function(reg) {
      var options = {
        body: 'Here is a notification body!',
        icon: 'images/example.png',
        vibrate: [100, 50, 100],
        data: {
          dateOfArrival: Date.now(),
          primaryKey: 1
        }
      };
      reg.showNotification('Hello world!', options);
    });
  }
}
```
* The **body** option adds a main description to the notification. It should give the user enough information to decide how to act on it.
* The **icon** option attaches an image to make the notification more visually appealing, but also more relevant to the user. For example, if it's a message from their friend you might include an image of the sender's avatar.
* The **vibrate** option specifies a vibration pattern for a phone receiving the notification. In our example, a phone would vibrate for 100 milliseconds, pause for 50 milliseconds, and then vibrate again for 100 milliseconds.
* The **data** option attaches custom data to the notification, so that the service worker can retrieve it when the user interacts with the notification. For instance, adding a unique "id" or "key" option to the data allows us to determine which notification was clicked when the service worker handles the click event.
#### Listen for events
* Displaying a notification was the first step. Now we need to handle user interactions in the service worker (using the "Interaction API"). Once the user has seen your notification they can either dismiss it or act on it.
#### The notificationclose event
* If the user dismisses the notification through a direct action on the notification (such as a swipe in Android), it raises a notificationclose event inside the service worker.
* This event is important because it tells you how the user is interacting with your notifications. You might, for example, log the event to your analytics database. Or, you might use the event to synchronize your database and avoid re-notifying the user of the same event.
* Here is an example of a `notificationclose` event listener in the service worker:
serviceworker.js
```JavaScript
self.addEventListener('notificationclose', function(e) {
  var notification = e.notification;
  var primaryKey = notification.data.primaryKey;

  console.log('Closed notification: ' + primaryKey);
});
```

### 3. Give examples of different encryption/hashing methods you have come across (one way and two way) and give example scripts in python 3 on how to achieve each one.
**Encryption** is a two-way function; what is encrypted can be decrypted with the proper key.<br>
* Encryption is the practice of scrambling information in a way that only someone with a corresponding key can unscramble and read it. Encryption is a two-way function. When you encrypt something, you’re doing so with the intention of decrypting it later.
##### Common forms of encryption are:
**1. Asymmetric Encryption** – This is the Public Key example we just gave. One key encrypts, the other key decrypts. The encryption only goes one way. This is the concept that forms the foundation for PKI (public key infrastructure), which is the trust model that undergirds SSL/TLS.<br>
**2. Symmetric Encryption** – This is closer to a form of private key encryption. Each party has its own key that can both encrypt and decrypt. As we discussed in the example above, after the asymmetric encryption that occurs in the SSL handshake, the browser and server communicate using the symmetric session key that is passed along.
<a href="url"><img src="https://github.com/RocqJones/Implementation-Eng/blob/main/imgs/encription.png" height="250" width="100%" ></a>

**Hashing**, however, is a one-way function that scrambles plain text to produce a unique message digest. With a properly designed algorithm, there is no way to reverse the hashing process to reveal the original password.
<a href="url"><img src="https://github.com/RocqJones/Implementation-Eng/blob/main/imgs/hashing.png" height="250" width="100%" ></a>
##### Common Hashing Algorithms.
Just like we did with encryption, let’s take a look at some of the most common hashing algorithms in use today.
**MD4** – MD4 is a self-loathing hash algorithm, created in 1990, even its creator, Ronald Rivest, admits it has security problems. The 128-bit hashing algorithm made an impact though, it’s influence can be felt in more recent algorithms like WMD5, WRIPEMD and the WHSA family.<br>
**MD5** – MD5 is another hashing algorithm made by Ray Rivest that is known to suffer vulnerabilities. It was created in 1992 as the successor to MD4. Currently MD6 is in the works, but as of 2009 Rivest had removed it from NIST consideration for SHA-3.<br>
**SHA** – SHA stands for Security Hashing Algorithm and it’s probably best known as the hashing algorithm used in most SSL/TLS cipher suites. A cipher suite is a collection of ciphers and algorithms that are used for SSL/TLS connections. SHA handles the hashing aspects. SHA-1, as we mentioned earlier, is now deprecated. SHA-2 is now mandatory. SHA-2 is sometimes known has SHA-256, though variants with longer bit lengths are also available.<br>

## Section B.
### 1. Create a login and a success page in Django. A mockup of the created pages should also be submitted. The mockups should have been created by using advanced design wireframe tools thus showcasing prowess in usage of the tools and use of production server deployments on uwsgi/nginx. Ensure that the sessions are well and securely managed.
