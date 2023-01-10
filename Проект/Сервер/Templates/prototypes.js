


document.querySelector("#submit").onclick = function(){
    
    const formData = new FormData();
    const fileField = document.querySelector('input[type="file"]');

    formData.append('username', 'abc123');
    formData.append('avatar', fileField.files[0]);

    fetch('http://127.0.0.1:8000/post_photo', {
    method: 'POST',
    body: formData,
    
    headers: {
        'login': 'Ignacio'
    }
    })
        .then((response) => response.json())
        .then((result) => {
            console.log('Success:', result);
        })
        .catch((error) => {
            console.error('Error:', error);
    });

    // fetch('http://localhost:8000/')
    //     .then(response => response.json())
    //     .then(info => console.log(info));

}

