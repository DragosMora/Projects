package org.example.lab6;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DatabaseChatRepo {
    private final String url;
    private final String username;
    private final String password;

    public DatabaseChatRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    private Connection connect() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }

    public List<MessageAux> loadChat(int sender_id, int receiver_id) throws SQLException {
        List<MessageAux> messages = new ArrayList<>();
        String query = "SELECT * FROM chats WHERE (sender_id = ? AND receiver_id = ?) OR (receiver_id = ? AND sender_id = ?)";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, sender_id);
            preparedStatement.setInt(2, receiver_id);
            preparedStatement.setInt(3, sender_id);
            preparedStatement.setInt(4, receiver_id);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                messages.add(createMessageAuxFromResultSet(resultSet));
            }
        } catch (SQLException e) {
            throw new SQLException(e);
        }
        return messages;
    }

    public boolean MessageIdExists(int id) throws SQLException {
        String query = "SELECT * FROM chats WHERE id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.isBeforeFirst()) {
                return true;
            }
        } catch (SQLException e) {
            throw new SQLException(e);
        }
        return false;
    }

    public boolean chatExists(int sender_id, int receiver_id) throws SQLException {
        String query = "SELECT * FROM chats WHERE sender_id = ? AND receiver_id = ? AND reply_id = 0";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, sender_id);
            preparedStatement.setInt(2, receiver_id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.isBeforeFirst()) {
                return true;
            }
        } catch (SQLException e) {
            throw new SQLException(e);
        }
        return false;
    }

    //creaza procedura getFirstMessageID pentru SELECT * FROM chats WHERE sender_id = ? AND receiver_id = ? AND reply_id != 0

    public int getLastMessageId(int sender_id, int receiver_id) throws SQLException {
        String query = "SELECT id FROM chats WHERE sender_id = ? AND receiver_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query, ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE)) {
            preparedStatement.setInt(1, sender_id);
            preparedStatement.setInt(2, receiver_id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.last()) {
                return resultSet.getInt("id");
            }
        } catch (SQLException e) {
            throw new SQLException(e);
        }
        return 0;
    }

    public int getMessageId(int sender_id, int receiver_id) throws SQLException {
        String query = "SELECT id FROM chats WHERE sender_id = ? AND receiver_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, sender_id);
            preparedStatement.setInt(2, receiver_id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getInt("id");
            }
        } catch (SQLException e) {
            throw new SQLException(e);
        }
        return 0;
    }

    public void linkMessages(int new_message_id, int reply_id) throws SQLException {
        String query = "UPDATE chats SET reply_id = ? WHERE id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, reply_id);
            preparedStatement.setInt(2, new_message_id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException(e);
        }
    }

    public void sendMessage(Message message) throws SQLException {
        int id = message.getId();
        int sender_id = message.getFrom().getId();
        int receiver_id = message.getTo().getFirst().getId();
        String message_aux = message.getMessage();
        String date = String.valueOf(message.getDate());
        int reply_id = 0;

        String query = "INSERT INTO chats(id, sender_id, receiver_id, message, date, reply_id) VALUES (?, ?, ?, ?, ?, ?)";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            preparedStatement.setInt(2, sender_id);
            preparedStatement.setInt(3, receiver_id);
            preparedStatement.setString(4, message_aux);
            preparedStatement.setString(5, date);
            preparedStatement.setInt(6, reply_id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException(e);
        }
    }

    public MessageAux createMessageAuxFromResultSet(ResultSet resultSet) throws SQLException {
        int id = resultSet.getInt("id");
        int sender_id = resultSet.getInt("sender_id");
        int receiver_id = resultSet.getInt("receiver_id");
        String message = resultSet.getString("message");
        String date = resultSet.getString("date");
        int reply_id = resultSet.getInt("reply_id");
        return new MessageAux(id, sender_id, receiver_id, message, date, reply_id);
    }
}
