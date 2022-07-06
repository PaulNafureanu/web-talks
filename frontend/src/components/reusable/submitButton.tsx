import * as React from "react";

interface SubmitButtonProps {
  id: string;
  value: string;
}

const SubmitButton: React.FunctionComponent<SubmitButtonProps> = ({
  id,
  value,
}) => {
  return (
    <div className="submit-button">
      <label htmlFor={id}></label>
      <input type="submit" id={id} value={value}></input>
    </div>
  );
};

export default SubmitButton;
