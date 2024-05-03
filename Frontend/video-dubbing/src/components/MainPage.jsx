import Navbar from "./Navbar";
import OptionCard from "./OptionCard";
import VideoUpload from "./VideoUpload";

const MainPage = () => {
  return (
    <div>
      <Navbar />
      <div className="flex space-x-12 m-24">
        <VideoUpload/>
      </div>

      <OptionCard title ="Video to Audio" />
      <OptionCard title ="Video Subtitles" />
      <OptionCard title ="Translated Subtitles" />
      <OptionCard title ="Dub a Video" />
    </div>
  );
};

export default MainPage;
