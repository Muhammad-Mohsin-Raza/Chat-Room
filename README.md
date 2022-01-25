# Chat-Room
This is semester project for Computer Networks.
<h1> Implementation Tools</h1>
<ul>
 <li>Python  </li>
  <li>Multi-threading</li>
   <li>sockets </li>
   <li>ports</li>
   <li>file handling </li>
   <li>TCP </li>
</ul>
We basically want to implement a concept that is used in group of WhatsApp app. So, there will be one admin(client) that adds or remove the multiple users (clients) in group. They will only send text messages. The client(user) who is not in group try to connect to server will not be allowed to enter the group.
Like in WhatsApp group if someone message in group its name with its message will show on all user’s device. In our application we will also implement it if someone message all users will receive it and see who sends it?

<h1>Things that will be used:</h1>
For our application, we will use the client-server architecture. This means that we will have multiple clients (the users) and one central server that hosts everything and provides the data for these clients.
Therefore, we will need to write two Python scripts. One will be for starting the server and one will be for the client. We will have to run the server first, so that there is a chat, which the clients can connect to. The clients themselves, are not going to directly communicate to each other but via the central server using TCP.
All the clients connect to same port of server, but they do not have same ports.
<h1> Llist of Users </h1>

To know that a user has rights to enter the group or not. We will fetch a data from a txt file that contain the mail and password of all the members that was added by admin.
Similarly, admin can add user by putting a mail and password of user into txt file. And if he wants to remove someone program will remove that mail and password from that txt file.

<h1> How user login </h1>
First, we run server then clients, clients must enter username and password when they are trying to connect with server to enter group and to communicate with each other. Same for admin but he has some privilege rights.
