import { Dispatch } from "react";
import { BackendResponse } from "../../types/BackendResponse";
import UserManagementService from "../../services/UserManagementService";
import { setUser } from "../../store/slices/userSlice";
import { UnknownAction } from "@reduxjs/toolkit";
import { LoginOrRegister } from "../../generic/LoginOrRegister";
import { PAGE_TYPE } from "../../types/enums";
import axios, { AxiosError } from "axios";



export const Login = () => {

    async function loginProcess(
        email:string,
        password:string,
        dispatch:Dispatch<UnknownAction>,
        setUser:Function,
        setLoginError:Function,
        setLoginErrorColour:Function,
        navigate:Function
    ) {
        UserManagementService.login(
            email,
            password
        ).then(
            (res) => {
                dispatch(setUser(res.data.ss_user));
                navigate("/my-clubs")
            }
        ).catch(
            (err:Error|AxiosError) => {
                if (axios.isAxiosError(err))  {
                    // Access to config, request, and response
                    const a = 1;
                } else {
                    // Just a stock error
                    const b = 1;
                }
                setLoginErrorColour("red");
                // setLoginError(res.data.message);
          }
        )
    }

    async function handleLogin(
        setButtonDisabled:Function,
        dispatch:Dispatch<UnknownAction>,
        setEmailError:Function,
        setPasswordError:Function,
        email:string,
        password:string,
        setLoginErrorColour:Function,
        setLoginError:Function,
        navigate:Function
    ) {
        setButtonDisabled(true);
        setEmailError("");
        setPasswordError("");
        var email_ok = true;
        if (email.length === 0) {
            setEmailError(
                "Please provide your email"
            );
            email_ok = false;
        }
        var password_ok = true;
        if (password.length === 0) {
            setPasswordError(
                "Please provide your password"
            )
            password_ok = false;
        }
        if (email_ok && password_ok) {
            setLoginErrorColour("black");
            setLoginError("Loading..");
            await loginProcess(
                email,
                password,
                dispatch,
                setUser,
                setLoginError,
                setLoginErrorColour,
                navigate
            );            
        }
        setButtonDisabled(false);
    }

    return (
        <LoginOrRegister
            pageType={PAGE_TYPE.LOGIN}
            handleSubmitButton={handleLogin}
        />
    );
};