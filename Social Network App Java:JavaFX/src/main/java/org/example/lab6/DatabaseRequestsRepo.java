package org.example.lab6;

import java.sql.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class DatabaseRequestsRepo {

    private final String url;
    private final String username;
    private final String password;

    public DatabaseRequestsRepo(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    private Connection connect() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }

    public void requestFriend(int sender_id, int recipient_id) throws SQLException {
        String query = "INSERT INTO requests (sender_id, recipient_id, status, created_at) VALUES (?, ?, ?, ?)";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, sender_id);
            preparedStatement.setInt(2, recipient_id);
            preparedStatement.setString(3, "PENDING");
            LocalDateTime time = LocalDateTime.now();
            preparedStatement.setString(4, String.valueOf(time));
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException(e);
        }
    }

    public void deleteRequest(int sender_id, int recipient_id) throws SQLException {
        String query = "DELETE FROM requests WHERE sender_id = ? AND recipient_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, sender_id);
            preparedStatement.setInt(2, recipient_id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException(e);
        }
    }

    public void updateStatus(int sender_id, int recipient_id, String status) throws SQLException {
        String query = "UPDATE requests SET status = ? WHERE sender_id = ? AND recipient_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, status);
            preparedStatement.setInt(2, sender_id);
            preparedStatement.setInt(3, recipient_id);
            preparedStatement.executeUpdate();
        } catch (SQLException e) {
            throw new SQLException(e);
        }
    }

    public List<Requests> getRequests(int recipient_id) throws SQLException {
        List<Requests> requests = new ArrayList<>();
        String query = "SELECT * FROM requests WHERE recipient_id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, recipient_id);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                Requests request = createRequestFromResultSet(resultSet);
                requests.add(request);
            }
        } catch (SQLException e) {
            throw new SQLException(e);
        }
        return requests;
    }

    private Requests createRequestFromResultSet(ResultSet resultSet) throws SQLException {
        int id = resultSet.getInt("id");
        int sender_id = resultSet.getInt("sender_id");
        int recipient_id = resultSet.getInt("recipient_id");
        String status = resultSet.getString("status");
        String created_at = resultSet.getString("created_at");
        return new Requests(id, sender_id, recipient_id, status, created_at);
    }


}
