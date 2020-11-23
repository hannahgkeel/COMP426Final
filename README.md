# COMP426Final
COMP426 Final Documentation

# A brief description of the project
COVID-19 calls for companies to adapt and take extra safety precautions for customers and employees. At Monterrey's there can be overcrowding in peak times while customers are waiting to be seated. Customers are unable to social distance themselves putting everyone at risk. Our solution is a virtual waiting list customers can join without entering the restaurant until their table is ready.

# Customer tutorial:
A customer will first go to www.monterreywaitlist.xyz where they will see the home page with three simple step listed. The customer will first register or login. After loging in, the customer will be taken to a page that asks them to select the monterrey location and party size they will have. Next they are taken to the in list page which displays a progress bar so the customers can see how many people are ahead of them. This page also has directions to the restaurant as well as information about the restaurant. On this page the customer has the option to leave the waitlist. When their table is ready, the customer will see a table ready page that gives them a few social distancing guidlines and tells them they have 10 minutes to meet the host at the host stand and claim their table.

# Admin tutorial:
The hostess/staff manage the waitlist by loging into www.monterreywaitlist.xyx/admin and then clicking on waitlist tickets. Waitlist tickets shows everyone on the list, their party size, and the time they entered the list. Two important columns to note are table ready and customer is served. When the staff selects table is ready for a customer this alerts the customer that their table is ready. From here, once the customer is seated, the staff will then select customer is served. The waitlist ticket feature can be filtered by location and is sorted by customer arrival time. Admin are also able to manually add someone to the list if a customer does not have a smart device.

# File structure and organization

# Technologies used in the frontend
Bulma was used to provide website aesthetics. User interface design made for customers with various technical backgrounds. Simple three step process to enter into waiting list. Responsive web design for various devices.

# Technologies used in the backend
Implemented using the Django framework. PostgreSQL is the DBMS used for user data and dynamic content storage. For deployment we used: digital ocean to host an ubuntu server, Gunicorn, and Nginx.
