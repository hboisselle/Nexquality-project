function ConfirmAndRedirect(string url, string confirmMessage)
{
	if(confirm(confirmMessage))
	{
		location.replace(url);
	}
}