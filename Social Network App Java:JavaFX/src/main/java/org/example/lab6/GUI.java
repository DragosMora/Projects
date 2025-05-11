package org.example.lab6;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class GUI extends Application {

    @Override
    public void start(Stage stage) throws Exception {
        Tests tests = new Tests();
        tests.run_all_tests();

        UserValidator validator = new UserValidator();
        String url = "jdbc:postgresql://localhost:5432/SocialNetwork";
        String user = "postgres";
        String password = "MyStrongPassword123$";
        DatabaseRepo repo = new DatabaseRepo(url, user, password, validator);
        DatabaseFriendshipRepo friendship_repo = new DatabaseFriendshipRepo(url, user, password);
        DatabaseRequestsRepo requests_repo = new DatabaseRequestsRepo(url, user, password);
        DatabaseChatRepo chat_repo = new DatabaseChatRepo(url, user, password);
        Service service = new Service(repo, friendship_repo, requests_repo, chat_repo);

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("hello-view.fxml"));
        Parent root = fxmlLoader.load();

        HelloController login_controller = fxmlLoader.getController();
        login_controller.setService(service);

        Scene scene = new Scene(root, 300, 300);
        stage.setTitle("Login");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}