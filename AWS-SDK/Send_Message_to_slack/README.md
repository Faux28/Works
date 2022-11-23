# Steps to generate Webhook URL in slack


1.Open slack app

2.Create/open the workspace(you have to be the administrator of the workspace)

3.Open the workspace dropdown

4.Go to settings and administration > Manage apps > Build

5.Click Create New App' > From scratch

6.Enter the app name and pick a workspace in the dropdown list and click create app

7.Open the created app

8.Under 'Add features and functionality' click incoming webhooks

9.Activate the incoming webhooks

10.Click 'Add New Webhook to Workspace'

11.Select a channel in dropdown and click allow


Create a environmental variable `Webhook_URL` for the program.

Set the webhook url of the created slack app as the value for the variable
