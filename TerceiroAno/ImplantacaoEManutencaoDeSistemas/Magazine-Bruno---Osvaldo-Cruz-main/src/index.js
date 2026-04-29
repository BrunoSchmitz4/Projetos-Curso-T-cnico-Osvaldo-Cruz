import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import Header from "./components/Header";
import Card from "./components/Card";
import ConteudoPrincipal from "./components/ConteudoPrincipal";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Header />
    <ConteudoPrincipal />
  </React.StrictMode>,
);
