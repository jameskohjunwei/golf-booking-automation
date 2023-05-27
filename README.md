## High-Level Overview

To ensure a smooth process and avoid issues, follow the steps below:

**Task #1**: Complete the ballot form between 8am and 3pm on Fridays. This involves accessing the website, clicking buttons, and filling out fields with text input and radio buttons.

**Task #2**: Check the game results on Friday night at 7pm to determine if you've been selected. If you want to cancel the games, do so by Monday for Saturday games and by Tuesday for Sunday games. This allows time to coordinate players.

The cumulative time for these tasks increases significantly when done for multiple members. Automating these tasks enhances scalability and saves time.

## More about Task #1

Completing the form for multiple members takes around 5 minutes per member. The process includes accessing the site, clicking buttons to access the form, and filling out fields with text input and radio buttons.

## More about Task #2

Checking the game results takes about 2 minutes per member. However, it becomes cumbersome as it involves manually reviewing a 50-row PDF. Details like tee time, course name, day, and date need to be copied and pasted into a message for coordination.

# Pain Points

The process has several challenges and pain points:

1. Forgetting to book due to the difficulty of completing the form between 8am and 3pm on Fridays, despite setting reminders.
2. Inconvenience of manually extracting details from a 50-row PDF on a Friday night during dinner hours.
3. Failure to complete the necessary steps resulting in no golf games, leading to disappointment.

## My Solution

### Mission Statement / Goal

Our mission is to leverage Python's Selenium package to develop an automation script that handles tasks #1 and #2 efficiently, eliminating manual intervention.

#### Functions Implemented

1. `fill_form(name, member, email, phone, course, session)`: Handles various permutations of the ballot form based on the provided arguments, allowing customization.
2. `send_telegram(stored_messages)`: Facilitates sending messages via Telegram using pre-stored messages.
3. `send_telegram_error(e)`: Sends error messages through Telegram in case of exceptions during the automation process.

Email functions have been deprecated due to complications such as messages being marked as spam.

#### Eliminating Manual Intervention

To eliminate manual intervention, the following steps were taken:

1. Hosting the scripts on a server: A home server was built using proxmox bare metal on a laptop. An Ubuntu server VM was created with all the required dependencies.
2. Dockerizing remote Selenium Chrome solution: Selenium grid was self-hosted on the server using Docker and Portainer. The script points to the remote Chrome session triggered by cronjobs.

### Comments on Functional Coding Style

Functional coding style was chosen for simplicity, considering the project's requirements and the author's experience level with Python and coding.

### Code Resiliency

To ensure code resiliency, multiple fail-safe code blocks were incorporated. When the club removes certain elements from the ballot form, the code adapts using try-except-else functions and conditional statements.

## Room for Improvement

Interacting with the website's frontend poses challenges due to frequent updates, necessitating constant script adjustments. Maintaining code resiliency is a top priority, with ongoing efforts to minimize the need for hot fixes. This includes testing xpaths versus CSS selectors, updating outdated xpaths, and exploring more resilient methods of frontend interaction.

## Closing Thoughts

The journey from zero coding and infrastructure management knowledge to developing Python automation scripts and an end-to-end self-hosted infrastructure has been rewarding. This achievement has sparked enthusiasm for similar projects aligned with daily activities.
