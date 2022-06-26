console.log('axios started')
// const axios = require('axios');
const token = document.getElementsByName("csrfmiddlewaretoken")[0]



axios({
    headers: {
        "Content-Type": "application/json",
        "X-CRFToken": token,
    },
    xsrfHeaderName: "X-CRFToken",
    method: 'GET',
    url: '/event_retrieve',
    
}).then(function (response){
    console.log(response.data);
}); 



