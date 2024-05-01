const express = require('express');
const multer = require('multer');
const fs = require('fs');
const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static('public'));

app.post('/upload', upload.single('file'), (req, res) => {
    const uploadedFile = req.file;
    const filePath = uploadedFile.path;

    // Your backend processing logic here
    // For example, read the file, process it, and send back the output
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const processedOutput = `Processed Content: ${fileContent}`;

    // Remove the uploaded file after processing
    fs.unlinkSync(filePath);

    res.send(processedOutput);
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
