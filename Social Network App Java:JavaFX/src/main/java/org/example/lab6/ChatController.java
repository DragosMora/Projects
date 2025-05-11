package org.example.lab6;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextField;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.scene.text.TextFlow;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class ChatController {
    private Service service;
    private int user_id;
    private int friend_id;

    public void setService(Service service) {
        this.service = service;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public void setFriend_id(int friend_id) {
        this.friend_id = friend_id;
    }

    @FXML
    public Label friendUsernameLabel;

    @FXML
    public ScrollPane chatScrollPane;

    @FXML
    public void initView() throws Exception {
        User friend = service.search(friend_id).orElseThrow();
        friendUsernameLabel.setText(friend.getName());
    }

    @FXML
    public void reloadChat() throws Exception {
        VBox vbox = new VBox();
        vbox.setSpacing(10);
        vbox.setPadding(new Insets(10));

        List<MessageAux> messages = service.loadChat(user_id, friend_id);
        for (MessageAux message : messages) {
            Text text = new Text(message.getMessage());
            text.setFont(new Font("Apple Braile", 16));
            TextFlow textFlow = new TextFlow();

            HBox hbox = new HBox();
            hbox.setSpacing(10);
            hbox.setPadding(new Insets(10));
            if (message.getSender_id() == user_id) {
                text.setFill(Color.WHITE);
                textFlow.getChildren().add(text);
                hbox.setAlignment(Pos.TOP_RIGHT);
                textFlow.setStyle("-fx-background-color: #00a1ff; -fx-background-radius: 15px; -fx-padding: 10px;");
            }
            else {
                text.setFill(Color.BLACK);
                textFlow.getChildren().add(text);
                hbox.setAlignment(Pos.TOP_LEFT);
                textFlow.setStyle("-fx-background-color: #d7d7d7; -fx-background-radius: 15px; -fx-padding: 10px;");
            }
            textFlow.setMaxWidth(300);
            hbox.getChildren().add(textFlow);
            vbox.getChildren().add(hbox);
        }
        chatScrollPane.setFitToWidth(true);
        chatScrollPane.setContent(vbox);
    }

    @FXML
    public TextField messageTextField;

    @FXML
    public void sendMessage() throws Exception {
        String message = messageTextField.getText();
        service.sendMessage(user_id, friend_id, message);
        reloadChat();
    }

    @FXML
    public void switchToMainScene() throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("app-view.fxml"));
        Parent root = fxmlLoader.load();

        AppController controller = fxmlLoader.getController();
        controller.setService(service);

        Stage stage = (Stage) friendUsernameLabel.getScene().getWindow();
        Scene scene = new Scene(root, 600, 415);
        stage.setTitle("App");
        stage.setScene(scene);

        controller.setUser_id(user_id);
        controller.initView();
    }
}
