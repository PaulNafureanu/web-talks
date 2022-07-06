import * as React from "react";
import { Component } from "react";
import CheckBox from "./checkBox";
import Input from "./input";
import SubmitButton from "./submitButton";

interface FormProps {}

interface FormState {}

class Form extends React.Component<FormProps, FormState> {
  renderInput(label: string, id: string, type: string = "text") {
    return <Input label={label} id={id} type={type} />;
  }

  renderCheckBox(label: string, id: string) {
    return <CheckBox label={label} id={id} />;
  }

  renderSubmitButton(value: string, id: string) {
    return <SubmitButton value={value} id={id} />;
  }
}

export default Form;
