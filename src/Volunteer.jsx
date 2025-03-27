import { useLocation, useNavigate } from "react-router-dom";
import { volunteers } from "./data/index";
import Volunteerbanner from "./assets/img/Volunteerbanner.jpg";
import ScrollToTop from "./components/ScrollToTop.jsx";

const Volunteers = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const title = searchParams.get("title");
  const currentVolunteers = volunteers.find((item) => item.title === title);
  const otherItems = volunteers.filter((item) => item.title !== title);

  const goToPage = (type, title) => {
    navigate(`/${type}?title=${title}`);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <ScrollToTop />
      <h2 className="text-2xl sm:text-3xl md:text-4xl lg:text-4xl font-bold mb-6 py-[20px] px-[10px] flex items-center">
        <span className="w-1 h-8 bg-gradient-to-t from-blue-600 to-blue-400 mr-4"></span>
        <span className="--text-shadow-black-one">Volunteer Program</span>
      </h2>

      {/* Banner部分 */}
      <div className="relative w-full aspect-w-16 aspect-h-9">
        <div className="absolute bottom-4 left-4 z-10 flex gap-2 flex-wrap">
          {currentVolunteers.technologies.map((tech) => (
            <span
              key={tech}
              className="px-3 py-1.5 bg-sky-400 backdrop-blur-sm text-white text-sm font-medium rounded-lg shadow-lg"
            >
              {tech}
            </span>
          ))}
        </div>
        <div className="h-full w-full overflow-hidden rounded-xl shadow-md">
          <img src={Volunteerbanner} className="w-full h-full object-cover" />
        </div>
      </div>

      {/* 主内容和侧边栏部分 */}
      <div className="mt-8 grid grid-cols-1 lg:grid-cols-4 gap-4">
        {/* 主内容 */}
        <div className="col-span-1 lg:col-span-3">
          <div className="p-6 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl flex-1">
            <div className="mb-6 flex items-center justify-center gap-3">
              <h1 className="text-2xl sm:text-3xl md:text-3xl lg:text-3xl font-bold text-gray-800 dark:text-white">
                {currentVolunteers.title}
              </h1>
            </div>
            <p className="text-xl leading-relaxed text-gray-600 dark:text-gray-300 whitespace-pre-line">
              {currentVolunteers.text}
            </p>
            <div className="col-span-1 border-t border-gray-200 p-2 mt-4">
              <img
                src={currentVolunteers.firstImg}
                className="w-full object-cover rounded"
                alt={currentVolunteers.title}
              />
            </div>
          </div>
        </div>

        {/* 侧边栏 - 其他项目 */}
        <div className="col-span-1 p-6 bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl py-4 overflow-auto">
          <h2 className="text-2xl sm:text-3xl md:text-3xl lg:text-3xl font-bold mb-4">Other Projects</h2>
          {otherItems.map((item) => (
            <div
              key={item.title}
              className="mt-5 p-2 rounded border-blue-100 border-2 cursor-pointer hover:bg-gray-100 transition-all"
              onClick={() => {
                goToPage("volunteers", item.title);
              }}
            >
              <div className="text-lg">{item.title}</div>
              <div>
                <img
                  className="h-20 object-cover w-full rounded transform transition-transform duration-300 ease-in-out hover:scale-105"
                  src={item.firstImg}
                  alt={item.title}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Volunteers;
