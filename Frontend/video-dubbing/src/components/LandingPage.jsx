import React from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "./Navbar";
import heroStartImg from "../assests/heroStart.png";
import playButton from "../assests/playButton.png"

const LandingPage = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate("/main");
  };

  return (
    <div className="bg-violet-600">
      <Navbar />
      <div>
        <h1 className="m-2 landingHeading font-bold"> DUB YOUR VIDEOS </h1>
      </div>
      <div
        className="text-center text-white text-[28px] font-bold 
       leading-[42px] mb-2"
      >
        Unlock Voices, Amplify Stories: Your Trusted Video Dubbing Hub.
      </div>
      <div className="justify-end items-center m-6 overflow-hidden ">
        <div className=" flex justify-center">
        <button onClick={handleGetStarted} className="text-center rounded-xl w-80 h-14 bg-zinc-800 shadow-inner text-white font-bold font-myFont m-4 ">
          Get started
        </button>
        </div>
        <div className="flex justify-center">
        <img className="w-[700px] h-[420px] m-6" src={heroStartImg} />
        <div className="place-items-center left-30  mt-60 absolute">

        <img src={playButton} className="w-[80px] h-[80px]  "/>
        </div>
        </div>
        

      
      </div>
    </div>
  );
};

export default LandingPage;
