package org.example.lab6;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DatabaseFriendshipRepo {

    private final String url;
    private final String username;
    private final String password;

    public DatabaseFriendshipRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    private Connection connect() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }

    public int friendCount(int id) {
        String query = "SELECT COUNT(*) FROM friendships WHERE user_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            return resultSet.next() ? resultSet.getInt(1) : 0;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public List<User> getFriends(int id) {
        List<User> friends = new ArrayList<>();
        String query = "SELECT * FROM friendships WHERE user_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                //friends.add(createUserFromResultSet(resultSet));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return friends;
    }

    public List<Integer> getFriendsIds(int id) {
        List<Integer> friends = new ArrayList<>();
        String query = "SELECT friend_id FROM friendships WHERE user_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                friends.add(resultSet.getInt(1));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return friends;
    }

    public void addFriend(Friendship friendship) {
        String query = "INSERT INTO friendships(user_id, friend_id, friends_from) VALUES(?, ?, ?)";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, friendship.getUser_id());
            preparedStatement.setInt(2, friendship.getFriend_id());
            String str_friends_from = String.valueOf(friendship.getFriends_from());
            preparedStatement.setString(3, str_friends_from);
            preparedStatement.executeUpdate();
            preparedStatement.setInt(1, friendship.getFriend_id());
            preparedStatement.setInt(2, friendship.getUser_id());
            preparedStatement.setString(3, str_friends_from);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }


    public void removeFriend(int id1, int id2) {
        String query = "DELETE FROM friendships WHERE user_id = ? AND friend_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id1);
            preparedStatement.setInt(2, id2);
            preparedStatement.executeUpdate();
            preparedStatement.setInt(1, id2);
            preparedStatement.setInt(2, id1);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public List<Integer> getPageFriendsIds(int user_id, int current_page) throws SQLException {
        List<Integer> friends = new ArrayList<>();
        String query = "SELECT friend_id FROM friendships WHERE user_id = ? ORDER BY friend_id LIMIT ? OFFSET ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, user_id);
            preparedStatement.setInt(2, 5);
            preparedStatement.setInt(3, (current_page - 1) * 5);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                friends.add(resultSet.getInt(1));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return friends;
    }

}


