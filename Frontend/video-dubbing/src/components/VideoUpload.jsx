import React, { useState } from 'react';

function VideoUpload() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    try {
      if (!selectedFile) {
        alert('Please select a video file.');
        return;
      }
  
      const formData = new FormData();
      formData.append('video', selectedFile);
  
      // Update the URL to match your Flask server's endpoint
      const response = await fetch('http://localhost:5000/upload/hindi', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        alert('Video uploaded successfully.');
      } else {
        alert('Failed to upload video.');
      }
    } catch (error) {
      console.error('Error uploading video:', error);
    }
  };
  

  return (
    <div>
      <h2>Upload a Video</h2>
      <input type="file" accept="video/*" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default VideoUpload;
