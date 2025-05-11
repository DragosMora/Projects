package org.example.lab6;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.List;
import java.util.Objects;

public class AppController {
    private Service service;
    private int user_id;

    public void setService(Service service) {
        this.service = service;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    @FXML
    public Label usernameLabel;

    @FXML
    public ListView<User> friendsListView;

    @FXML
    public ListView<RequestsDTO> requestsListView;

    @FXML
    public Label requestsNotification;

    @FXML
    public void initView() throws Exception {
        User user = service.search(user_id).orElseThrow();
        usernameLabel.setText("Welcome, " + user.getName() + "!");

        initPageableFriends();
        /*
        List<Integer> friends_ids = service.getFriendsIds(user_id);
        ObservableList<User> friends = FXCollections.observableArrayList();
        for (Integer friend_id : friends_ids) {
            friends.add(service.search(friend_id).orElseThrow());
        }
        friendsListView.setItems(friends);
         */
        int pending_requests_counter = 0;
        List<Requests> requests_list = service.getRequests(user_id);
        ObservableList<RequestsDTO> requests = FXCollections.observableArrayList();
        for (Requests request : requests_list) {
            User request_user = service.search(request.getSender_id()).orElseThrow();
            String name = request_user.getName();
            String status = request.getStatus();
            String date = request.getCreated_at();
            if (Objects.equals(status, "PENDING")) pending_requests_counter++;
            requests.add(new RequestsDTO(name, status, date));
        }
        requestsListView.setItems(requests);
        requestsNotification.setText(String.valueOf(pending_requests_counter));
    }

    private int current_page = 0;
    private int total_pages;

    @FXML
    public Label pagesLabel;

    @FXML
    public void initPageableFriends() throws Exception {
        int friend_count = service.friendCount(user_id);
        total_pages = friend_count / 5;
        if (friend_count % 5 != 0) {
            total_pages++;
        }
        if (current_page == 0) {
            current_page = 1;
        }
        if (current_page > total_pages) {
            current_page = total_pages;
        }
        String pagination = current_page + "/" + total_pages;
        pagesLabel.setText(pagination);

        List<Integer> friends_ids = service.getPageFriendsIds(user_id, current_page);
        ObservableList<User> friends = FXCollections.observableArrayList();
        for (Integer friend_id : friends_ids) {
            friends.add(service.search(friend_id).orElseThrow());
        }
        friendsListView.setItems(friends);
    }

    @FXML
    public void nextPage() throws Exception {
        if (current_page == total_pages) throw new Exception();
        current_page++;
        initPageableFriends();
    }

    @FXML
    public void previousPage() throws Exception {
        if (current_page == 1) throw new Exception();
        current_page--;
        initPageableFriends();
    }

    @FXML
    public TextField userSearchField;

    @FXML
    public void requestFriend() throws Exception {
        String name = userSearchField.getText();
        service.requestFriend(user_id, name);
    }

    @FXML
    public void deleteFromList() throws Exception {
        if (friendsListView.getSelectionModel().getSelectedItem() != null) {
            String selected_name1 = friendsListView.getSelectionModel().getSelectedItem().getName();
            service.deleteFriend(user_id, selected_name1);
        }
        else {
            String selected_name2 = requestsListView.getSelectionModel().getSelectedItem().getName();
            service.deleteRequest(user_id, selected_name2);
        }
        initView();
    }

    @FXML
    public void acceptFriend() throws Exception {
        String selected_name = requestsListView.getSelectionModel().getSelectedItem().getName();
        service.acceptFriend(user_id, selected_name);
        initView();
    }

    @FXML
    public void rejectFriend() throws Exception {
        String selected_name = requestsListView.getSelectionModel().getSelectedItem().getName();
        service.rejectFriend(user_id, selected_name);
        initView();
    }

    @FXML
    public Button logOutButton;

    @FXML
    public void switchToLoginScene() throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("hello-view.fxml"));
        Parent root = fxmlLoader.load();

        HelloController controller = fxmlLoader.getController();
        controller.setService(service);

        Stage stage = (Stage) logOutButton.getScene().getWindow();
        Scene scene = new Scene(root, 300, 300);
        stage.setTitle("Login");
        stage.setScene(scene);
    }

    @FXML
    public void switchToChatScene() throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("chat-view.fxml"));
        Parent root = fxmlLoader.load();

        ChatController controller = fxmlLoader.getController();
        controller.setService(service);

        Stage stage = (Stage) logOutButton.getScene().getWindow();
        Scene scene = new Scene(root, 600, 400);
        stage.setTitle("Chat");
        stage.setScene(scene);

        controller.setUser_id(user_id);
        controller.setFriend_id(friendsListView.getSelectionModel().getSelectedItem().getId());
        controller.initView();
        controller.reloadChat();
    }

}
