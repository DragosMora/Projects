package org.example.lab6;

public class MessageAux {
    private final int id;
    private int sender_id;
    private int receiver_id;
    private String message;
    private String date;
    private int reply_id;

    public MessageAux(int id, int sender_id, int receiver_id, String message, String date, int reply_id) {
        this.id = id;
        this.sender_id = sender_id;
        this.receiver_id = receiver_id;
        this.message = message;
        this.date = date;
        this.reply_id = reply_id;
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

    public int getReceiver_id() {
        return receiver_id;
    }

    public void setReceiver_id(int receiver_id) {
        this.receiver_id = receiver_id;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public int getReply_id() {
        return reply_id;
    }

    public void setReply_id(int reply_id) {
        this.reply_id = reply_id;
    }
}
