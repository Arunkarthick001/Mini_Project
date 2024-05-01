function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        const outputDiv = document.getElementById('output');
        outputDiv.innerHTML = `<pre>${data}</pre>`;
    })
    .catch(error => console.error('Error:', error));
}
