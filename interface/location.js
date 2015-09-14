//location.js
//var x=document.getElementById("demo");
    function getLocation()
    {
        if (navigator.geolocation)
        {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        }
        else
        {
            
            //x.innerHTML="Geolocation is not supported by this browser.";
        }
    }
    function showError(error) {
        
        var location_error ="";
        switch(error.code) {
            case error.PERMISSION_DENIED:
                location_error ="User denied the request for Geolocation.";
                break;
            case error.POSITION_UNAVAILABLE:
                location_error ="Location information is unavailable.";
                break;
            case error.TIMEOUT:
                location_error ="The request to get user location timed out.";
                break;
            case error.UNKNOWN_ERROR:
                location_error ="An unknown error occurred.";
                break;
        }
        var l=[];
        //l['location_error']=location_error;
        l="&location_error="+location_error+"&key3="+"value3"

        console.log(l);

        $.post('index.php', l  );
    }
    function showPosition(position)
    {
        $.post('index.php', position.coords);
    }
    getLocation();
