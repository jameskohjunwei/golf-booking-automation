# High level overview:

To ensure a smooth process and avoid any issues, the following steps need to be followed:

Task #1: Complete the ballot form between 8am and 3pm on Fridays. This involves accessing the website, clicking three buttons, and filling out 8-10 fields with text input and radio buttons.

Task #2: Check the game results on Friday night at 7pm to determine if you have been selected. If you wish to cancel the games, do it by Monday for Saturday games and by Tuesday for Sunday games. This allows for two days over the weekend to coordinate with buddies and confirm four players for each game.

The cumulative time for these tasks increases significantly, especially when I have to do them for multiple members. Automating these tasks would greatly enhance scalability and save a substantial amount of time.

### More about no.1:

When completing the form for multiple members, it takes approximately 5 minutes per member. The process includes accessing the site, clicking three buttons to access the form, and filling out 8-10 fields with text input and radio buttons.

### More about no.2:

Checking the game results is slightly quicker, taking about 2 minutes per member. However, it becomes cumbersome as it involves manually reviewing a PDF with around 50 rows. Additionally, details such as tee time, course name, day, and date need to be copied from the PDF and pasted into a message for coordinating and scheduling players with golf buddies.

### The pain points:

There are several challenges and pain points associated with the process:

1. Forgetting to book due to the difficulty of completing the form between 8am and 3pm on Fridays, despite setting pop-up reminders.
2. The inconvenience of manually extracting details from a 50-row PDF while out for dinner and drinks on a Friday night, particularly at 7pm, which is peak dinner time.
3. Failing to complete the necessary steps results in no golf games, leading to disappointment as golf is an important hobby for relaxation and stress relief.

# My solution 

### Mission Statement / Goal:

Our mission is to leverage the Selenium package in Python to develop a powerful automation script that can efficiently handle tasks #1 and #2 on a larger scale, eliminating the need for manual intervention or triggering.

#### The first part of the mission statement of : "automation script that can efficiently handle tasks #1 and #2 on a larger scale". To accomplish this, it involves the implementation of the following functions:

1. `fill_form(name, member, email, phone, course, session)`: This function is designed to handle the various permutations of the ballot form based on the provided arguments. It offers easy customization, allowing for booking on behalf of specific members, selecting between two courses, and choosing preferred session times (AM or PM).

2. `send_telegram(stored_messages)`: This function facilitates the sending of messages via Telegram using pre-stored messages as input. The format of the message is as follows:

3. `send_telegram_error(e)`: In the event of any exceptions during the automation process, this function takes charge of sending error messages through Telegram. A sample error message is as follows:

Due to complications with email, such as messages being marked as spam, I have deprecated the following email functions:

4. `send_error_email(e)`: This function was previously responsible for sending error emails in case of exceptions encountered during the automation process.

5. `send_success_email(stored_messages)`: This function is no longer in use since transitioning to Telegram for messaging purposes.

#### Second part of the mission that is "eliminating the need for manual intervention or triggering". To accomplish this, it involves:

1. Hosting the scripts on a server: I had to decide between hosting it on a cloud solution like Linode, but ended up building my own home server instead because I wanted to learn the ins and outs of self-hosting. So I installed proxmox bare metal on a laptop that was bound for the bin. Spun up a ubuntu server vm and installed all the dependencies required to run my scripts.
2. Dockerise remote selenium chrome solution: Part of the conumdrum that I had to tackle was "how do I get a chrome session running on my remote pc for the script to do its tasks?". After much research, I found selenium grid! I self-hosted it on my server on the same vm using docker and portainer and pointed my script to that remote chrome session whenever the cronjob triggers... speaking of cronjob...
2. Cronjobs: The cron syntax took quite a while to figure out but once it was done it worked like clockwork!

### comments on functional coding style
I chose to implement it in functional coding style, as it didn't require additional complexity. Additionally, when I created this script, I was relatively new to Python and coding in general.

### code resiliency 
Initially, my code encounters difficulties when the club removes certain radio buttons or text fields from the ballot form. This usually happens when the course is booked for corporate events, competitions, or maintenance, making it unavailable for regular golfers. To address this issue, I had to incorporate multiple fail-safe code blocks using solutions like try-except-else functions and various conditional statements.

# room for improvement
Interacting with the website's frontend for this project poses challenges due to frequent updates, requiring constant script adjustments. Maintaining code resiliency has been a top priority since implementation, with ongoing efforts to minimize the need for frequent hot fixes. These efforts include testing xpaths versus CSS selectors, updating outdated xpaths, and exploring more resilient methods of frontend interaction. It's an ongoing work in progress to ensure long-term stability and reduce maintenance requirements.

# Closing thoughts
I have gained valuable knowledge and skills throughout my journey, starting from a position of zero coding and infrastructure management knowledge. It has been incredibly rewarding to witness the successful development of Python automation scripts and the establishment of an end-to-end self-hosted infrastructure. This achievement has further ignited my enthusiasm for undertaking similar projects that directly align with my daily activities.

