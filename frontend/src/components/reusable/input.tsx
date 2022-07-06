import * as React from "react";

interface InputProps {
  label: string;
  id: string;
  type: string;
}

const Input: React.FunctionComponent<InputProps> = ({ label, id, type }) => {
  return (
    <div className="input-container">
      <span>{label}</span>
      <div className="input-box">
        <label htmlFor={id}></label>
        <input type={type} id={id} />
      </div>
    </div>
  );
};

export default Input;
