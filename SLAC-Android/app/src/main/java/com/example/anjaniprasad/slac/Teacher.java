package com.example.anjaniprasad.slac;

public class Teacher{
    public String name,pass,mail,num;

    public Teacher()
    {

    }

    public String getName() {
        return name;
    }

    public String getnum() {
        return num;
    }

    public String getPass() {
        return pass;
    }

    public String getMail() {
        return mail;
    }


    public Teacher(String name, String mail ,String pass, String num) {
        this.name = name;
        this.pass = pass;
        this.mail= mail;
        this.num=num;
    }
}
