import * as React from "react";

interface CheckBoxProps {
  label: string;
  id: string;
}

const CheckBox: React.FunctionComponent<CheckBoxProps> = ({ label, id }) => {
  return (
    <label htmlFor={id}>
      <input type="checkbox" id={id} />
      <p>{label}</p>
    </label>
  );
};

export default CheckBox;
