
function check()
{
    while(true)
    {
    let email = document.getElementById("email").value;
    let names = document.getElementById("name").value;
    let pass = document.getElementById("pass").value;
    let bday = document.getElementById("bday").value;
    //Blank?
    if(email=="" || names=="" || pass=="" || bday == "")
    {
        alert("Left one or more fields blank");
        return false;
    }
    else
    {
        count_at = 0;
        //Email 
        for(i=0; i< email.length; i++)
        {
            if(email[i]=="@")
            {
                count_at++;
            }
        }
        if(count_at != 1)
        {
            alert("Invalid email1");
            return false;
        }

        if(email[0] == "@" || email[-1] == "@")
        {
            alert("Invalid email2");
            return false;
        }

        //Age
        let today = Date.now();
        let bdayAsDate = new Date(bday);

        thirteen_ms = 13*365.25*24*60*60*1000;

        if(thirteen_ms > (today - bdayAsDate.getTime()))
        {
            alert("Not old enough");
            return false;
        }
    }
}
}