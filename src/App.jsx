import ProjectCard from "./components/ProjectCard";
import AutoScrolling from "./components/AutoScrolling";
import "./App.css";
import { programmings, volunteers, studyingLogs } from "./data";
import MeA from "./assets/img/MeA.webp";
import MeB from "./assets/img/MeB.webp";
import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, Pagination } from "swiper/modules";
import "swiper/css";
import "swiper/css/pagination";

function App() {
  return (
    <div className="max-w-7xl mx-auto px-2 py-4">
      <div className="flex w-full pt-[10px]" id="Home">
        <div className="px-[10px] w-full">
          <div className="flex items-center">
            <h1 className="text-4xl sm:text-3xl md:text-4xl lg:text-6xl font-bold">Hi!</h1>
            <h1 className="ml-8 text-4xl sm:text-3xl md:text-4xl lg:text-6xl font-bold">
              I am <span className="--text-shadow-black">Derek</span> !
            </h1>
          </div>
          <section className="py-[10px] mt-[10px]">
            <div>
              <h2 className="text-2xl sm:text-3xl md:text-4xl lg:text-4xl font-bold mb-6 py-[20px] px-[10px] flex items-center">
                <span className="w-1 h-8 bg-gradient-to-t from-blue-600 to-blue-400 mr-4"></span>
                <span className="--text-shadow-black-one">About Me</span>
              </h2>

              <div className="text-xl border-2 border-[#E6E6E9] rounded p-4">
                I am a self-taught programmer. I am a student in Hong Kong
                currently. The website is totally built by myself.
              </div>
            </div>
          </section>
        </div>
      </div>
      <section className="py-[10px] mt-[10px] w-full flex justify-center">
        <Swiper
          spaceBetween={10}
          slidesPerView={1} // 每次完整显示 1 张图片
          autoplay={{ delay: 3000, disableOnInteraction: false }} // 自动播放，3秒间隔
          pagination={{ clickable: true }} // 指示器可点击
          modules={[Autoplay, Pagination]} // 引入模块
          className="w-full h-auto max-w-[1200px] max-h-[620px]" 
        >
          <SwiperSlide className="flex justify-center items-center w-[1200px] h-[620px]">
            <img
              src={MeA}
              className="w-full h-full object-cover rounded"
            />
          </SwiperSlide>
          <SwiperSlide className="flex justify-center items-center w-[1200px] h-[620px]">
            <img
              src={MeB}
              className="w-full h-full object-cover rounded"
            />
          </SwiperSlide>
        </Swiper>
      </section>

      <section className="py-[10px] px-[10px] mt-[10px]">
        <h2
          id="CodingProject"
          className="text-2xl sm:text-3xl md:text-4xl lg:text-4xl font-bold mb-6 py-[20px] px-[10px] flex items-center"
        >
          <span className="w-1 h-8 bg-gradient-to-t from-blue-600 to-blue-400 mr-4"></span>
          <span className="--text-shadow-black-one">Coding Project</span>
        </h2>
        <AutoScrolling
          content={programmings.concat(programmings).map((project, index) => (
            <div key={index} className="w-86 flex-shrink-0">
              <ProjectCard {...project} />
            </div>
          ))}
        />
      </section>

      <section className="py-[10px] px-[10px] mt-[10px]">
        <h2
          id="VolunteerProgram"
          className="text-2xl sm:text-3xl md:text-4xl lg:text-4xl font-bold mb-6 py-[20px] px-[10px] flex items-center"
        >
          <span className="w-1 h-8 bg-gradient-to-t from-blue-600 to-blue-400 mr-4"></span>
          <span className="--text-shadow-black-one">Volunteer Program</span>
        </h2>

        <AutoScrolling
          content={volunteers
            .concat(volunteers)
            .concat(volunteers)
            .concat(volunteers)
            .map((project, index) => (
              <div key={index} className="w-86 flex-shrink-0">
                <ProjectCard {...project} />
              </div>
            ))}
        />
      </section>

      <section className="py-[10px] px-[10px] mt-[10px]">
        <h2
          id="StudyingLog"
          className="text-2xl sm:text-3xl md:text-4xl lg:text-4xl font-bold mb-6 py-[20px] px-[10px] flex items-center"
        >
          <span className="w-1 h-8 bg-gradient-to-t from-blue-600 to-blue-400 mr-4"></span>
          <span className="--text-shadow-black-one">Studying Log</span>
        </h2>
        <AutoScrolling
          content={studyingLogs
            .concat(studyingLogs)
            .concat(studyingLogs)
            .map((project, index) => (
              <div key={index} className="w-86 flex-shrink-0">
                <ProjectCard {...project} />
              </div>
            ))}
        />
      </section>
    </div>
  );
}

export default App;
