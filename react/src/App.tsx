import React from "react";
import ReactDOM from "react-dom";

import Editor from "@monaco-editor/react";

export default function App() {
  return (
    <>
      <button>Button</button>
      <button>run</button>
      <div className="p-1">
        <Editor
          defaultLanguage="python"
          theme="vs-dark"
          height="90vh"
          width="50vw"
          defaultValue="# some comment"
        />
      </div>
      <h1 className="text-6xl font-bold underline">Hello world!</h1>
    </>
  );
}
