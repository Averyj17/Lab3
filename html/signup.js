
function check()
{
    while(true)
    {
        let count = 0;

        let email = document.getElementById("email").value;
        let names = document.getElementById("name").value;
        let pass = document.getElementById("pass").value;
        let bday = document.getElementById("bday").value;



        let tmp = document.createElement("div");
        tmp.classList.add("alert");
        document.body.appendChild(tmp);



        if(email=="" || names=="" || pass=="" || bday == "")
        {
            tmp.appendChild( document.createTextNode( "Left one or more fields blank" ) );
            //alert("Left one or more fields blank");
            count+=1;
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
                tmp.appendChild( document.createTextNode("Invalid email1") );
                //alert("Invalid email1");
                return false;
            }

            if(email[0] == "@" || email[-1] == "@")
            {
                tmp.appendChild( document.createTextNode("Invalid email2") );
                //alert("Invalid email2");
                return false;
            }

            //Age
            let today = Date.now();
            let bdayAsDate = new Date(bday);

            thirteen_ms = 13*365.25*24*60*60*1000;

            if(thirteen_ms > (today - bdayAsDate.getTime()))
            {
                tmp.appendChild( document.createTextNode("Not old enough") );
                //alert("Not old enough");
                return false;
            }
            count+=1;
        }
        break;
    }
    let wel = document.createElement("div");
    wel.classList.add("welcome");
    document.body.appendChild(wel);
    wel.appendChild( document.createTextNode("Welcome") );
    
}