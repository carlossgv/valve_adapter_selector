Hello!

My name is Carlos González, I am a Venezuelan living in Santiago de Chile, Chile. My CS50 Final Project on the Web Development path is called "Valve Adapter Selector".

First of all let me tell you that CS50 has been a really nice experience and have open my eyes on what I could do with coding. Really grateful!

The website I've created is a "simple" site that automates one of the more tedious process I have at work. I say "simple" because it looks like it since it only has one page, but in the background it is a little bit more complex.

I am Mechanical Engineer who works in Technical Sales, specialized in industrial valves. When we need to quote valves with some kind of special operator (besides a regular handle), we need to check beforehand if the valve can be mounted on the operator (actually called actuator); and if is so, we need to check what adapter is required for the installation.

Although it sounds simple, there are a lot of steps and files we have to check to do this, something like this:

1.	Look in the valves catalogue for the adapter type each valve uses depending on the size of the valve, of course there is a catalogue for each type of valve.
2.	Look in the actuators catalogue (also multiple catalogues depending on the type of the actuator) to see if it’s possible to adapt the actuator to the valve.
3.	If so, we take a look at the “base code” of the adapter and write it down.
4.	With the base code we have to find the actual part number of the adapter which is what we need.

With this website I automate this process using the following tools:

•	SQL: I created a database with multiple tables (VALVES, ACTUATORS, ADAPTERS AND KITS), which have the information required to link the valve information to the actuators and finally the kit or adapter required.
•	Flask: The backend portion of the website is mostly made on Flask using to files, the primary app.py for most of the coding and helpers.py for the functions. Used libraries like WTForms, sqlite3 and jsonify for this.
•	HTML and CSS: For the frontend of the website, used most CSS from Bootstrap for styling and some additional CSS for responsiveness.
•	JavaScript: I wanted to make the website to be as much as an application as possible, so I followed some tutorials to make the dropdowns of the site to be dependent from themselves in real time so some of them will be updated as soon as changes on other dropdowns are detected. 

An that is basically it! There is a lot to improve on the website, there are some bugs here and there and there is a lot of improvement (I am planning to have the prices also shown with the results and maybe some log of what has been done).

Hope you like it, and again thanks for all, bye!
