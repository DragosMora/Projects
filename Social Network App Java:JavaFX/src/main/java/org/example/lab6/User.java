package org.example.lab6;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class User extends Entity<Integer> {

    private String name;
    private String gender;
    private int age;
    private String location;
    private String description;
    private String phone;
    //private List<User> friends = new ArrayList<>();

    public User(int id, String name, String gender, int age, String location, String description, String phone) {
        super(id);
        this.name = name;
        this.gender = gender;
        this.age = age;
        this.location = location;
        this.description = description;
        this.phone = phone;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    @Override
    public String toString() {
        return name + " " + gender + " " + age + " " + location + " " + description + " " + phone;
    }
}
