# TL;DR
- The process of completing a golf ballot form and checking game results manually is time-consuming and prone to errors.
- Automating these tasks using Selenium in Python can save time and enhance scalability.
- The automation script includes functions to fill the form and send messages via Telegram.
- Hosting the script on a server, Dockerizing Selenium, and using cronjobs are part of the solution.
- Challenges include website updates and code resiliency, which require ongoing maintenance.
- Overall, the project has provided valuable learning experiences and sparked enthusiasm for similar endeavors.

# High-level Overview

Here's a quick description of the manual tasks that need to be completed in order for us to play some golf:
1. Task #1 Complete the ballot form between 8am and 3pm on Fridays. This involves accessing the website, clicking three buttons, and filling out 8-10 fields with text input and radio buttons.

2. Task #2 Check the game results on Friday night at 7pm to determine if you have been selected. If you wish to cancel the games, do it by Monday for Saturday games and by Tuesday for Sunday games. This allows for two days over the weekend to coordinate with buddies and confirm four players for each game.

The cumulative time for these tasks increases significantly, especially when I have to do them for multiple members. Automating these tasks would greatly enhance scalability and save a substantial amount of time.

### More about Task #1:

When completing the form for multiple members, it takes approximately 5 minutes per member. The process includes accessing the site, clicking three buttons to access the form, and filling out 8-10 fields with text input and radio buttons.

### More about Task #2:

Checking the game results is slightly quicker, taking about 2 minutes per member. However, it becomes cumbersome as it involves manually reviewing a PDF with around 50 rows. Additionally, details such as tee time, course name, day, and date need to be copied from the PDF and pasted into a message for coordinating and scheduling players with golf buddies.

### The pain points:

There are several challenges and pain points associated with the process:

1. Forgetting to book due to the difficulty of completing the form between 8am and 3pm on Fridays, despite setting pop-up reminders.
2. The inconvenience of manually extracting details from a 50-row PDF while out for dinner and drinks on a Friday night, particularly at 7pm, which is peak dinner time.
3. Failing to complete the necessary steps results in no golf games, leading to disappointment as golf is an important hobby for relaxation and stress relief.

# My solution 

### Mission Statement / Goal:

Our mission is to leverage the Selenium package in Python to develop a powerful automation script that can efficiently handle tasks #1 and #2 on a larger scale, eliminating the need for manual intervention or triggering.

#### The first part of the mission statement of "automation script that can efficiently handle tasks #1 and #2 on a larger scale". To accomplish this, it involves the implementation of the following functions:

1. `fill_form(name, member, email, phone, course, session)`: This function is designed to handle the various permutations of the ballot form based on the provided arguments. It offers easy customization, allowing for booking on behalf of specific members, selecting between two courses, and choosing preferred session times (AM or PM).

2. `send_telegram(stored_messages)`: This function facilitates the sending of messages via Telegram using pre-stored messages as input. The format of the message is as follows:

![image](https://github.com/jameskohjunwei/golf-booking-automation/assets/60392496/6307cbc5-e5bc-4a17-842a-df6f345dc73a)

3. `send_telegram_error(e)`: In the event of any exceptions during the automation process, this function takes charge of sending error messages through Telegram. A sample error message is as follows:
![image](https://github.com/jameskohjunwei/golf-booking-automation/assets/60392496/509c8a8a-2cfc-40f0-8e82-ed4bc0c74b80)

Due to complications with email, such as messages being marked as spam, I have deprecated the following email functions:

4. `send_error_email(e)`: This function was previously responsible for sending error emails in case of exceptions encountered during the automation process.

5. `send_success_email(stored_messages)`: This function is no longer in use since transitioning to Telegram for messaging purposes.

#### Second part of the mission that is "eliminating the need for manual intervention or triggering". To accomplish this, it involves:

1. Hosting the scripts on a server: I had to decide between hosting it on a cloud solution like Linode, but ended up building my own home server instead because I wanted to learn the ins and outs of self-hosting. So I installed proxmox bare metal on a laptop that was bound for the bin. Spun up a Ubuntu server VM and installed all the dependencies required to run my scripts.
Read more about my self hosting journey here : https://medium.com/@jameskohjunwei/i-built-a-server-with-my-old-laptop-heres-how-it-went-ccce5d3cd27e

![image](https://github.com/jameskohjunwei/golf-booking-automation/assets/60392496/0305c792-5979-44e8-be1f-fca557eb67d3)


3. Dockerise remote Selenium Chrome solution: Part of the conundrum that I had to tackle was "how do I get a chrome session running on my remote PC for the script to do its tasks?". After much research, I found Selenium Grid! I self-hosted it on my server on the same VM using Docker and Portainer and pointed my script to that remote chrome session whenever the cronjob triggers... speaking of cronjob...
![image](https://github.com/jameskohjunwei/golf-booking-automation/assets/60392496/7d49ab4a-c123-4f10-a506-ddb12c6165b2)

4. Cronjobs: The cron syntax took quite a while to figure out but once it was done it worked like clockwork!
![image](https://github.com/jameskohjunwei/golf-booking-automation/assets/60392496/39940ca1-6a8d-4a6b-8164-9e912c5dda0b)

### Comments on Functional Coding Style
I chose to implement it in functional coding style as it didn't require additional complexity. Additionally, when I created this script, I was relatively new to Python and coding in general.

### Code Resiliency 
Initially, my code encountered difficulties when the club removed certain radio buttons or text fields from the ballot form. This usually happens when the course is booked for corporate events, competitions, or maintenance, making it unavailable for regular golfers. To address this issue, I had to incorporate multiple fail-safe code blocks using solutions like try-except-else functions and various conditional statements.

# Room for Improvement
Interacting with the website's frontend for this project poses challenges due to frequent updates, requiring constant script adjustments. Maintaining code resiliency has been a top priority since implementation, with ongoing efforts to minimize the need for frequent hot fixes. These efforts include testing xpaths versus CSS selectors, updating outdated xpaths, and exploring more resilient methods of frontend interaction. It's an ongoing work in progress to ensure long-term stability and reduce maintenance requirements.

# Closing thoughts
I have gained valuable knowledge and skills throughout my journey, starting from a position of zero coding and infrastructure management knowledge. It has been incredibly rewarding to witness the successful development of Python automation scripts and the establishment of an end-to-end self-hosted infrastructure. This achievement has further ignited my enthusiasm for undertaking similar projects that directly align with my daily activities.
