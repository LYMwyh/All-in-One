import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const ScrollToTop = () => {
  const location = useLocation();

  useEffect(() => {
    // 重置页面滚动位置
    window.scrollTo(0, 0);
  }, [location]);

  return null;
};

export default ScrollToTop;
