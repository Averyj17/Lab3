
function submit()
{
    let title = document.getElementById("name").value;
    let picfiles = document.getElementById("profilepic").files;


    

    let fdata = new FormData();
    fdata.append("name", title );
    fdata.append("profilepic", picfiles[0]);

    console.log(fdata[2]);

    fetch( "/do_update", {
        method: "POST",
        body: fdata
    }).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);
        }).catch( (err) => {
            console.log("JSON error:",err);
        })
        document.location = "http://localhost:8080/";
    }).catch( (err) => {
        console.log("Error:",err);
    });

    if( picfiles.length === 0 ){
        alert(err);
        return;
    }
    if( title == "")
    {
        alert(err);
        return;
    }

}
    
function updatethumb(){
    let picfiles = document.getElementById("profilepic").files;
    if(picfiles.length > 0 ){
        let u = URL.createObjectURL(picfiles[0]);
        let th = document.getElementById("thumbnail");
        th.onload = () => {
            URL.revokeObjectURL(u);
        };
        th.src = u;
    }
}

