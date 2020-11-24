# Monterrey's Mexican Grill Virtual Waitlist
COMP426 Final Documentation

# Motivation
COVID-19 calls for companies to adapt and take extra safety precautions for customers and employees. At Monterrey's there can be overcrowding in peak times while customers are waiting to be seated. Customers are unable to social distance themselves putting everyone at risk. Our solution is a virtual waiting list customers can join without entering the restaurant until their table is ready.

# Customer tutorial:
A customer will first go to www.monterreywaitlist.xyz where they will see the home page with three simple step listed. The customer will first register or login. After logging in, the customer will be taken to a page that asks them to select the monterrey location and party size they will have. Next they are taken to the in list page which displays a progress bar so the customers can see how many people are ahead of them. This page also has directions to the restaurant as well as information about the restaurant. On this page the customer has the option to leave the waitlist. When their table is ready, the customer will see a table ready page that gives them a few social distancing guidlines and tells them they have 10 minutes to meet the host at the host stand and claim their table.

# Admin tutorial:
The hostess/staff manage the waitlist by logging into www.monterreywaitlist.xyx/admin and then clicking on waitlist tickets. Waitlist tickets shows everyone on the list, their party size, and the time they entered the list. By default, waitlist tickets are sorted by customer arrival time. It is possible to filter by location and add aditional sorting parameters such as party size. Two important columns to note are _table is ready_ and _customer is served_. When the staff selects _table is ready_ for a customer, this alerts the waiting customer that their table is ready. From here, once the customer is seated, the staff will then select _customer is served_. 

It is important that the staff checks the _customer is served_ box, as this is the only way the system will know to remove the customer from the waitlist and end the transaction. In the event the customer does not show up in a timely manner after being called, the staff is able to remove them from the waitlist by using the _delete waitlist ticket_ action.

Admin are also able to manually add someone to the list if a customer does not have a smart device. In order to do this, the staff simply needs to click _add waitlist ticket_ at the top right corner of the waitlist ticket view. When entering the customer details, the admin must use his/her own username to fill the form.

# File structure and organization
We followed standard django structure by separating concerns into apps and concentrating all html in a single templates folder.

# Technologies used in the frontend
Bulma was used to provide website aesthetics. User interface design made for customers with various technical backgrounds. Simple three step process to enter into waiting list. Responsive web design for various devices.

# Technologies used in the backend
Implemented using the Django framework. HTTPS get/post requests and dynamic content are handled by Django templates and views. PostgreSQL is the DBMS used for user data and dynamic content storage. For deployment we used: digital ocean to host an Ubuntu server, Gunicorn, and Nginx.
