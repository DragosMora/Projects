package org.example.lab6;

public class Requests {
    private int id;
    private int sender_id;
    private int recipient_id;
    private String status;
    private String created_at;

    public Requests(int id, int sender_id, int recipient_id, String status, String created_at) {
        this.id = id;
        this.sender_id = sender_id;
        this.recipient_id = recipient_id;
        this.status = status;
        this.created_at = created_at;
    }

    public int getId() {
        return id;
    }

    public int getSender_id() {
        return sender_id;
    }

    public void setSender_id(int sender_id) {
        this.sender_id = sender_id;
    }

    public int getRecipient_id() {
        return recipient_id;
    }

    public void setRecipient_id(int recipient_id) {
        this.recipient_id = recipient_id;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }

}
