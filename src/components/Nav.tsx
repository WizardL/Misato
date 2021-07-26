import React, { useState } from "react";
import { Link } from "react-router-dom";
import MisatoConfig from "../misato.conf";

const Nav = () => {
  const [mobileMenuState, toggleMobileMenu] = useState<boolean>(false);
  const mobileMenuClick = () => {
    toggleMobileMenu(!mobileMenuState);
  };

  const links = [
    { text: "Home", to: "/" },
    { text: "About", to: "/about" },
  ];

  return (
    <nav className="bg-white shadow dark:bg-gray-800">
      <div className="container px-6 py-4 mx-auto">
        <div className="lg:flex lg:items-center lg:justify-between">
          <div className="flex items-center justify-between">
            <div className="text-xl font-semibold text-gray-700">
              <a
                className="text-2xl font-bold text-gray-800 dark:text-white lg:text-3xl hover:text-gray-700 dark:hover:text-gray-300"
                href="#"
              >
                {MisatoConfig.name}
              </a>
            </div>

            {/* <!-- Mobile menu button --> */}
            <div className="flex lg:hidden">
              <button
                type="button"
                className="text-gray-500 dark:text-gray-200 hover:text-gray-600 dark:hover:text-gray-400 focus:outline-none focus:text-gray-600 dark:focus:text-gray-400"
                onClick={mobileMenuClick}
                aria-label="toggle menu"
              >
                <svg viewBox="0 0 24 24" className="w-6 h-6 fill-current">
                  <path
                    fillRule="evenodd"
                    d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"
                  ></path>
                </svg>
              </button>
            </div>
          </div>

          {/* <!-- Mobile Menu open: "block", Menu closed: "hidden" --> */}
          <div
            className={`${
              mobileMenuState ? "block" : "hidden"
            } -mx-4 lg:flex lg:items-center`}
          >
            {links.map((link, i) => (
              <Link
                key={link.text}
                to={link.to}
                className={`block mx-4 mt-2 text-sm text-gray-700 capitalize lg:mt-0 dark:text-gray-200 hover:text-blue-600 dark:hover:text-indigo-400`}
              >
                {link.text}
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Nav;
