# Slack Timezoner

If you use slack, it's sometimes useful to get an idea of the geographic distribution of members.

And because we're online, while geographic distance is important to know it's often the timezone that's more relevant for working out when might be sensible to contact someone, or see how a commmunity is distributed.

This is what slack timezoner does. It prints out count of members in your community, by timezone.


## Usage


1. Create an app for a single slack group
2. Get a Web API token - https://api.slack.com/web#authentication
3. Checkout this code
4. Install dependencies
5. Either use the code programatically, or run it this as a server, to see the JSON output


### Create an app

You need to create an app for a single team. See below for more

https://slack.dev/python-slackclient/auth.html#

You can create an app at the link below:

https://api.slack.com/apps

### Get a web api token

This is detailed in slack's extensive documentation. You need a Web API token

https://api.slack.com/web#authentication

If it helps it should be visible at a link that looks like the pattern below, and it will be called `OAuth Access Token` in the web UI:

https://api.slack.com/apps/YOUR_APP_ID/oauth


### Check out this code

This isn't packaged up as a file you can run yet from a pip install. Sorry about that - (if you can help do this, I'd be veeery grateful)

### Install dependencies

See above. This shouldn't be necessary once it's packaged up properly.

### Use the code programatically, or run the server

This project includes a minimal, single-file Django app, to serve the summary as JSON, to display using some charting or tabular renderer.

```
python ./minimal.py runserver
```

Alternatively, you can also import the library and use it programatically in python code:


```
import group_by_timezones

tzc = group_by_timezones.TimeZoneCounter()

# returns a Counter datastructure
res = tzc.summary()


```


### Next steps

This was thrown together in a hurry, and I'd like to adapt this to allow running the same kind of summaries for any public channel in slack workspace.

You can list all the channels in workspace with this API call:
https://api.slack.com/methods/conversations.list


Once you have that, you can get a list of the members like so:
https://api.slack.com/methods/conversations.members

This returns a list of member ids like so:

```
{
    "ok": true,
    "members": [
        "U023BECGF",
        "U061F7AUR",
        "W012A3CDE"
    ],
    "response_metadata": {
        "next_cursor": "e3VzZXJfaWQ6IFcxMjM0NTY3fQ=="
    }
}
```

You can then look up the timezones, with this call to recontruct a datastructure similar to the one used in the TimeZoneCounter already.

https://slack.dev/python-slackclient/basic_usage.html#listing-team-members



### Contributing

This is currently used in the ClimateAction.tech slack. If you're interested in helping out, please file an issue, or join the slack there.



You can join the link below:

https://climateaction.tech/#join




