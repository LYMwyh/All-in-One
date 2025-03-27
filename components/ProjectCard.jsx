import PropTypes from "prop-types";
import { useNavigate } from "react-router-dom";

function ProjectCard({ type, title, technologies, firstImg }) {
  const navigate = useNavigate();

  const goToPage = (type, title) => {
    navigate(`/${type}?title=${title}`);
  };

  return (
    <div
      onClick={() => {
        goToPage(type, title);
      }}
      className="bg-gray-50 p-4 rounded-lg w-full cursor-pointer 
             hover:shadow-lg hover:scale-105
             transition-all duration-300 ease-in-out"
    >
      <h3 className="text-xl font-bold mb-2 truncate">{title}</h3>
      <div className="flex flex-wrap gap-2 mb-2">
        {technologies.map((tech, index) => (
          <span
            key={index}
            className="px-2 py-1 text-sm text-white bg-gray-700 rounded"
          >
            {tech}
          </span>
        ))}
      </div>
      <img
        src={firstImg}
        className="rounded w-full h-35 object-cover"
        loading="lazy"
      />
    </div>
  );
}

ProjectCard.propTypes = {
  type: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  technologies: PropTypes.arrayOf(PropTypes.string).isRequired,
  firstImg: PropTypes.string.isRequired,
};

export default ProjectCard;
