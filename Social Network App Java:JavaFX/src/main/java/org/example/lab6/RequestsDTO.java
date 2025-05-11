package org.example.lab6;

public class RequestsDTO {
    private String name;
    private String status;
    private String date;

    public RequestsDTO(String name, String status, String date) {
        this.name = name;
        this.status = status;
        this.date = date;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    @Override
    public String toString() {
        return name + " " + status + " " + date;
    }
}
