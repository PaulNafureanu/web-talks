import { throws } from "assert";
import * as React from "react";
import { Component } from "react";
import "../css/register.css";
import Form from "./reusable/form";

interface RegisterFormProps {}

interface RegisterFormState {}

class RegisterForm extends Form {
  render() {
    return (
      <div className="registerForm">
        <form>
          <h3>Sign Up</h3>
          {this.renderInput("First name", "first_name")}
          {this.renderInput("Last name", "last_name")}
          {this.renderInput("Username*", "username")}
          {this.renderInput("Email*", "email")}
          {this.renderInput("Password*", "password", "password")}
          {this.renderInput("Repeat Password*", "repeat_password", "password")}
          {this.renderCheckBox("Accept Terms and Conditions", "terms")}
          {this.renderSubmitButton("Register", "submit-register-form")}
        </form>
      </div>
    );
  }
}

export default RegisterForm;
