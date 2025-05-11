package org.example.lab6;

import java.time.LocalDateTime;

public class Friendship {
    private int user_id;
    private int friend_id;
    LocalDateTime friends_from;

    public Friendship(int user_id, int friend_id, LocalDateTime friends_from) {
        this.user_id = user_id;
        this.friend_id = friend_id;
        this.friends_from = friends_from;
    }

    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public int getFriend_id() {
        return friend_id;
    }

    public void setFriend_id(int friend_id) {
        this.friend_id = friend_id;
    }

    public LocalDateTime getFriends_from() {
        return friends_from;
    }

    public void setFriends_from(LocalDateTime friends_from) {
        this.friends_from = friends_from;
    }
}
