var url = "js/response/";

fetch(url, {
    "method": "GET",
    "headers": {
        "Content-Type": "application/json",
    },
})
.then(function(resp){
    console.log(resp);

    return resp.json();
})
.then((data) => {
    console.log(data);
});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken);

fetch("js/post/", {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
    },
    "body": JSON.stringify({  // Json --> String
        "title": "NEW TITLE2",
        "text": "Hello world",
    })
})
.then((resp) => {
    console.log(resp);
    return resp.json();
})
.then(function(data){
    console.log(data);
})

