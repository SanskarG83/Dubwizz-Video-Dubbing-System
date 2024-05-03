import React, { useState } from 'react';

function FileInput() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = () => {
    if (selectedFile) {
      // You can implement your dubbing logic here
      alert(`Uploading and dubbing file: ${selectedFile.name}`);
    } else {
      alert('Please select a file to upload.');
    }
  };

  return (
    <div >
      <input 
        className="myFont"
        type="file"
        accept="video/*"
        onChange={handleFileChange}
        style={{ display: 'none' }}
        ref={(fileInput) => (this.fileInput = fileInput)}
      />
      <button className="myFont buttonStyle bg-gradient-to-r from-violet-500 to-indigo-500" onClick={() => this.fileInput.click()}>Choose File</button>
      {selectedFile && (
        <div>
          <p className="myFont" >Selected Video: {selectedFile.name}</p>
          <p className="myFont" >File Type: {selectedFile.type}</p>
          <button onClick={handleUpload}>Start Dubbing</button>
        </div>
      )}
    </div>
  );
}

export default FileInput;

