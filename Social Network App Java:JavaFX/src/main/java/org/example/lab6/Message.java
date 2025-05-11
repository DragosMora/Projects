package org.example.lab6;

import java.time.LocalDateTime;
import java.util.List;

public class Message {
    private final int id;
    private User from;
    private List<User> to;
    private String message;
    private LocalDateTime date;
    private Message reply;

    public Message(int id, User from, List<User> to, String message, LocalDateTime date, Object reply) {
        this.id = id;
        this.from = from;
        this.to = to;
        this.message = message;
        this.date = date;
        this.reply = null;
    }

    public int getId() {
        return id;
    }

    public User getFrom() {
        return from;
    }

    public void setFrom(User from) {
        this.from = from;
    }

    public List<User> getTo() {
        return to;
    }

    public void setTo(List<User> to) {
        this.to = to;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public LocalDateTime getDate() {
        return date;
    }

    public void setDate(LocalDateTime date) {
        this.date = date;
    }

    public Message getReply() {
        return reply;
    }

    public void setReply(Message reply) {
        this.reply = reply;
    }
}
