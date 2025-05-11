package org.example.lab6;

import java.sql.*;
import java.util.*;

public class DatabaseRepo implements Repository <Integer, User> {

    private final String url;
    private final String username;
    private final String password;
    private final IValidator<User> validator;

    public DatabaseRepo(String url, String username, String password, IValidator<User> validator) {
        this.url = url;
        this.username = username;
        this.password = password;
        this.validator = validator;
    }

    private Connection connect() throws SQLException {
        return DriverManager.getConnection(url, username, password);
    }

    @Override
    public Optional<User> findOne(Integer id) {
        if (id == null) throw new IllegalArgumentException("Id cannot be null!");
        String query = "SELECT * FROM users WHERE id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                User user = createUserFromResultSet(resultSet);
                return Optional.of(user);
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return Optional.empty();
    }

    public Optional<User> findByUsername(String username) {
        if (username == null) throw new IllegalArgumentException("Username cannot be null!");
        String query = "SELECT * FROM users WHERE name = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, username);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                User user = createUserFromResultSet(resultSet);
                return Optional.of(user);
            }

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return Optional.empty();
    }

    @Override
    public Iterable<User> findAll() {
        List<User> users = new ArrayList<>();
        String query = "SELECT * FROM users";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query); ResultSet resultSet = preparedStatement.executeQuery()) {
            while (resultSet.next()) {
                users.add(createUserFromResultSet(resultSet));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return users;
    }

    @Override
    public Optional<User> save(User user) throws Exception {
        if (user == null) throw new IllegalArgumentException("User cannot be null!");
        validator.validate(user);
        String query = "INSERT INTO users (id, name, gender, age, location, description, phone) VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, user.getId());
            preparedStatement.setString(2, user.getName());
            preparedStatement.setString(3, user.getGender());
            preparedStatement.setInt(4, user.getAge());
            preparedStatement.setString(5, user.getLocation());
            preparedStatement.setString(6, user.getDescription());
            preparedStatement.setString(7, user.getPhone());
            preparedStatement.executeUpdate();
            return Optional.empty();
        } catch (SQLException e) {
            return Optional.of(user);
        }
    }

    @Override
    public Optional<User> delete(Integer id) {
        if (id == null) throw new IllegalArgumentException("Id cannot be null!");
        Optional<User> userToDelete = findOne(id);
        if (userToDelete.isPresent()) {
            String query = "DELETE FROM users WHERE id = ?";
            try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
                preparedStatement.setInt(1, id);
                preparedStatement.executeUpdate();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        return userToDelete;
    }

    @Override
    public Optional<User> update(User user) throws Exception {
        if (user == null) throw new IllegalArgumentException("User cannot be null!");
        validator.validate(user);
        String query = "UPDATE users SET name = ?, gender = ?, age = ?, location = ?, description = ?, phone = ? WHERE id = ?";
        try (Connection connection = connect(); PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, user.getName());
            preparedStatement.setString(2, user.getGender());
            preparedStatement.setInt(3, user.getAge());
            preparedStatement.setString(4, user.getLocation());
            preparedStatement.setString(5, user.getDescription());
            preparedStatement.setString(6, user.getPhone());
            preparedStatement.setInt(7, user.getId());
            int affectedRows = preparedStatement.executeUpdate();
            if (affectedRows > 0) {
                return Optional.empty();
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return Optional.of(user);
    }

    private User createUserFromResultSet(ResultSet resultSet) throws SQLException {
        int id = resultSet.getInt("id");
        String name = resultSet.getString("name");
        String gender = resultSet.getString("gender");
        int age = resultSet.getInt("age");
        String location = resultSet.getString("location");
        String description = resultSet.getString("description");
        String phone = resultSet.getString("phone");
        return new User(id, name, gender, age, location, description, phone);
    }
}

