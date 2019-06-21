# Okta---Legacy-Events

<b>Retrieve from an organization the SysLog legacy type of events. Examples include:</b>
<i> 
- app.user_management.grouppush.mapping.created;
- app.user_management.grouppush.updated;
- app.admin.sso.login.success;
- core.user.factor.attempt_success;
- core.user_auth.login_failed;
- app.generic.import.started;
- app.office365.api.sync.heartbeat.sent;<br>
And so on...
</i><br>
You can retrieve those only by having an API token and then specifying the:<br>

- dubdomain;
- domain;
- timeframe;
- type of legacy.events;
- nr. of events retrieved.<br><br>


<b> Note: </b> <br>
:warning: This is NOT an official Okta Dev-vetted product / script, but rather a personal project. This does not qualify for any Okta support. Anyone who chooses to use this must ensure that their implementation meets any applicable legal obligations including any Okta terms and conditions. :warning:
