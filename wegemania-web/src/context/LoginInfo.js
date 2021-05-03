import React, { useState, useEffect, createContext } from "react";
import { Redirect } from "react-router";
const LoginInfo = createContext();
/*
const useStateWithLocalStorage = localStorageKey => {
  /*
  var temp;
  console.log("TEST");
  console.log(localStorage.getItem(localStorageKey));
  if (
    localStorage.getItem(localStorageKey) == null ||
    localStorage.getItem(localStorageKey) == undefined
  ) {
    localStorage.removeItem(localStorageKey);
  } else {
    temp = localStorage.getItem(localStorageKey);
  }
  const [userInfo, setUserInfo] = useState(temp);
  useEffect(() => {
    if (temp) {
      localStorage.setItem(localStorageKey, userInfo);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [userInfo]);

  return [userInfo, setUserInfo];
  var temp;
  if (localStorage.getItem(localStorageKey) !== undefined) {
    temp = localStorage.getItem(localStorageKey);
  } else {
    localStorage.removeItem(localStorageKey);
  }
  const [userInfo, setUserInfo] = useState(temp);
  localStorage.setItem(localStorageKey, userInfo);
  return [userInfo, setUserInfo];
};
*/

export const LoginInfoProvider = (props) => {
  let tempInfo;
  //https://veggiesapp.herokuapp.com/
  // const Api = "http://veggies.ddns.net:8181";
  const Api = "http://10.5.0.5:8000";

  const [isOpen, setIsOpen] = useState(false);
  const openPanel = (val) => {
    setIsOpen(val);
  };
  if (localStorage.getItem("loginState")) {
    tempInfo = JSON.parse(localStorage.getItem("loginState"));
  } else {
    tempInfo = undefined;
  }
  const [userInfo, setUserInfo] = useState(tempInfo);
  const [isStaff, setIsStaff] = useState(false);
  const setStaff = (val) => {
    setIsStaff(val);
  };
  console.log("-------");
  console.log(userInfo);
  const login = (info) => {
    localStorage.setItem("loginState", JSON.stringify(info));
    setUserInfo(info);
  };
  const logout = () => {
    localStorage.removeItem("loginState");
    setUserInfo(undefined);
  };
  const { children } = props;
  return (
    <LoginInfo.Provider
      value={{
        isOpen: isOpen,
        openPanel: openPanel,
        login: login,
        isStaff: isStaff,
        setStaff: setStaff,
        logout: logout,
        userInfo: userInfo,
        Api: Api,
      }}
    >
      {children}
    </LoginInfo.Provider>
  );
};
export const LoginInfoConsumer = LoginInfo.Consumer;
export const NewLoginInfo = LoginInfo;
