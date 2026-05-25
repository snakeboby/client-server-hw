console.log('[Client] Sending request to server...');

fetch('http://localhost:3000/api/ping')
    .then(response => response.json())
    .then(data => {
        console.log('[Client] Response received:');
        console.log(data);
    })
    .catch(error => console.error('[Client] Error:', error));