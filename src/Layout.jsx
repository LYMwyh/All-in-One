import { Outlet } from 'react-router-dom';
import { useState } from 'react';
import { useLocation,useNavigate } from'react-router-dom';


const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();
  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);

  const goToTarget = (targetId) => {
    const goToId = () => {
      const target = document.getElementById(targetId);
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 100,
          behavior:'smooth',
        });
      }
    }
    if (location.pathname !== '/') {
      navigate(`/`);
      setTimeout(() => {
        goToId();
      },250)
    } else {
      goToId();
    }
    if (isMenuOpen) {
      setIsMenuOpen(false);
    }
    
  }


  return (
    <div className="sticky top-0 left-0 w-full border-b-2 border-[#E6E6E9] flex justify-between min-h-[40px] py-[20px] z-50 bg-white">
      <div className="flex items-center">
        <a
          className="py-[5px] px-[10px] cursor-pointer"
          onClick={() => {goToTarget('Home')}}
        >
          <h2 className='text-3xl font-bold'>HelloWorld-er</h2>
        </a>
        <div className="ml-20 space-x-6 hidden md:flex">
          <a className="text-[#333] hover:text-[#0073e6] text-lg font-bold cursor-pointer" onClick={() => {goToTarget('Home')}}>Home</a>
          <a className="text-[#333] hover:text-[#0073e6] text-lg font-bold cursor-pointer" onClick={() => {goToTarget("CodingProject")}}>Coding Project</a>
          <a className="text-[#333] hover:text-[#0073e6] text-lg font-bold cursor-pointer" onClick={() => {goToTarget("VolunteerProgram")}}>Volunteer Program</a>
          <a className="text-[#333] hover:text-[#0073e6] text-lg font-bold cursor-pointer" onClick={() => {goToTarget("StudyingLog")}}>Studying Log</a>
        </div>
        {/* Mobile menu button */}
        <button
          className="md:hidden p-2"
          onClick={toggleMenu}
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              fill="currentColor"
              d="M3 6H21M3 12H21M3 18H21"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </button>
      </div>

      <a href="https://github.com/HelloWorld-er">
        <svg viewBox="0 0 16 16" aria-hidden="true" width="32" height="32">
          <path
            fill="currentColor"
            d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"
          ></path>
        </svg>
      </a>

      {/* Mobile menu dropdown */}
      <div
        className={`absolute top-0 left-0 w-full bg-white shadow-lg p-4 md:hidden transform transition-all duration-300 ease-in-out ${isMenuOpen ? 'translate-x-0 opacity-100 visible' : '-translate-x-full opacity-0 invisible'}`}
      >
        <a className="block text-[#333] hover:text-[#0073e6] text-lg font-bold" onClick={() => {goToTarget('Home')}}>Home</a>
        <a className="block text-[#333] hover:text-[#0073e6] text-lg font-bold" onClick={() => {goToTarget("CodingProject")}}>Coding Project</a>
        <a className="block text-[#333] hover:text-[#0073e6] text-lg font-bold" onClick={() => {goToTarget("VolunteerProgram")}}>Volunteer Program</a>
        <a className="block text-[#333] hover:text-[#0073e6] text-lg font-bold" onClick={() => {goToTarget("StudyingLog")}}>Studying Log</a>
        {/* Close button for mobile menu */}
        <button
          className="absolute top-4 right-4 text-[#333] hover:text-[#0073e6]"
          onClick={toggleMenu}
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              fill="currentColor"
              d="M6 18L18 6M6 6L18 18"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </button>
      </div>
    </div>
  );
};

// Footer.js

const Footer = () => {
  return (
    <footer className="bg-gray-700 text-white py-4 rounded">
      <div className="container mx-auto text-center">
        <p className="text-sm">
          &copy; {new Date().getFullYear()} HelloWorld-er. All rights reserved.
        </p>
      </div>
    </footer>
  );
};



const Layout = () => {
  return (
    <div className="max-w-7xl mx-auto px-2 py-4">
      <Header />
      <main className="flex-grow">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}

export default Layout;
