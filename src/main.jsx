import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router";
import "./index.css";
import Layout from "./Layout.jsx";
import App from "./App.jsx";
import Programming from "./Programming.jsx";
import StudyingLog from "./StudyingLog.jsx";
import Volunteer from "./Volunteer.jsx";


createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<App />} />
        <Route path="programmings" element={<Programming />} />
        <Route path="studyingLogs" element={<StudyingLog />} />
        <Route path="volunteers" element={<Volunteer />} />
      </Route>
    </Routes>
  </BrowserRouter>
);
