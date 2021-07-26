import React, { CSSProperties } from "react";

interface Props {
  backgroundImg: string;
}

const Header: React.FC<Props> = ({ backgroundImg }) => {
  return (
    <header>
      <div
        className="w-full bg-center bg-cover h-128"
        style={{ backgroundImage: `url(${backgroundImg})` }}
      >
        <div className="flex items-center justify-center w-full h-full bg-gray-900 bg-opacity-50">
          <div className="text-center">
            <h1 className="text-2xl font-semibold text-white lg:text-3xl">
              Post on confession page{" "}
              <span className="text-red-400 underline">Anonymously</span>
            </h1>
            <button className="w-full px-4 py-2 mt-4 text-sm font-medium text-white uppercase transition-colors duration-200 transform bg-blue-600 rounded-md lg:w-auto hover:bg-blue-500 focus:outline-none focus:bg-blue-500">
              Start posting
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
