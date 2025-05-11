package org.example.lab6;


import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Random;

public class Service {
    private DatabaseRepo repository;
    private DatabaseFriendshipRepo friends_repository;
    private DatabaseRequestsRepo requests_repository;
    private DatabaseChatRepo chat_repository;

    public Service(DatabaseRepo repository, DatabaseFriendshipRepo friends_repository, DatabaseRequestsRepo requests_repository, DatabaseChatRepo chat_repository) {
        this.repository = repository;
        this.friends_repository = friends_repository;
        this.requests_repository = requests_repository;
        this.chat_repository = chat_repository;
    }

    public void store(int id, String name, String gender, int age, String location, String description, String phone) throws Exception {
        User user = new User(id, name, gender, age, location, description, phone);
        repository.save(user);
    }

    public void remove (int id) throws Exception {
        repository.delete(id);
    }

    public Iterable<User> getAll() throws Exception {
        return repository.findAll();
    }

    public Optional<User> search(int id) throws Exception {
        return repository.findOne(id);
    }

    public void addFriend(int id1, int id2) throws Exception {
        Friendship friendship = new Friendship(id1, id2, LocalDateTime.now());
        friends_repository.addFriend(friendship);
    }

    public void removeFriend(int id1, int id2) throws Exception {
        friends_repository.removeFriend(id1, id2);
    }

    public List<User> getFriends(int id) throws Exception {
        return friends_repository.getFriends(id);
    }

    public List<Integer> getFriendsIds(int id) throws Exception {
        return friends_repository.getFriendsIds(id);
    }

    public int friendCount(int id) throws Exception {
        return friends_repository.friendCount(id);
    }

    private void visit(User user, List<Object> visited_users) throws Exception {
        visited_users.add(user);
        List<User> friends = friends_repository.getFriends(user.getId());
        for (User friend : friends) {
            if (!visited_users.contains(friend)) {
                visit(friend, visited_users);
            }
        }
    }

    public int communitiesCount() throws Exception {
        Iterable<User> user_list = repository.findAll();
        List<Object> final_list = new ArrayList<>();
        user_list.forEach(final_list::add);

        int counter = 0;
        List<Object> visited_users = new ArrayList<>();
        for (Object user : final_list) {
            if (!visited_users.contains(user)) {
                visit((User) user, visited_users);
                counter++;
            }
            if (final_list.size() == visited_users.size()) {
                break;
            }
        }
        return counter;
    }

    public List<Object> mostSociable() throws Exception {
        int max_friends = 0;
        Iterable<User> user_list = repository.findAll();
        List<Object> final_list = new ArrayList<>();
        user_list.forEach(final_list::add);

        List<Object> current_list = new ArrayList<>();
        List<Object> result_list = new ArrayList<>();
        List<Object> visited_list = new ArrayList<>();
        List<Object> last_visited_list = new ArrayList<>();

        for (Object o : final_list) {
            if (!visited_list.contains(o)) {
                visit((User) o, visited_list);
                for (Object o2 : visited_list) {
                    if (!last_visited_list.contains(o2)) {
                        current_list.add(o2);
                    }
                }
                if (current_list.size() > max_friends) {
                    max_friends = current_list.size();
                    result_list.addAll(current_list);
                }
                last_visited_list.addAll(current_list);
                current_list.clear();

            }
            if (final_list.size() == visited_list.size()) {
                break;
            }
        }
        return result_list;
    }

    public void requestFriend(int sender_id, String recipient_name) throws Exception {
        User user = repository.findByUsername(recipient_name).orElseThrow();
        int recipient_id = user.getId();
        requests_repository.requestFriend(sender_id, recipient_id);
    }

    public void acceptFriend(int recipient_id, String name) throws Exception {
        User user = repository.findByUsername(name).orElseThrow();
        int sender_id = user.getId();
        requests_repository.updateStatus(sender_id, recipient_id, "ACCEPTED");
        addFriend(sender_id, recipient_id);
    }

    public void rejectFriend(int recipient_id, String name) throws Exception {
        User user = repository.findByUsername(name).orElseThrow();
        int sender_id = user.getId();
        requests_repository.updateStatus(sender_id, recipient_id, "REJECTED");
    }

    public List<Requests> getRequests(int recipient_id) throws Exception {
        return requests_repository.getRequests(recipient_id);
    }

    public void deleteFriend(int user_id, String friend_name) throws Exception {
        User user = repository.findByUsername(friend_name).orElseThrow();
        int friend_id = user.getId();
        removeFriend(friend_id, user_id);
    }

    public void deleteRequest(int user_id, String request_name) throws Exception {
        User user = repository.findByUsername(request_name).orElseThrow();
        int friend_id = user.getId();
        requests_repository.deleteRequest(friend_id, user_id);
    }

    public List<MessageAux> loadChat(int sender_id, int receiver_id) throws Exception {
        return chat_repository.loadChat(sender_id, receiver_id);
    }

    public void sendMessage(int sender_id, int receiver_id, String text) throws Exception {
        Random random = new Random();
        int id = random.nextInt();
        while (chat_repository.MessageIdExists(id)) {
            id = random.nextInt();
        }
        User sender = repository.findOne(sender_id).orElseThrow();
        List<User> receivers = new ArrayList<>();
        User receiver = repository.findOne(receiver_id).orElseThrow();
        receivers.add(receiver);

        Message message = new Message(id, sender, receivers, text, LocalDateTime.now(), null);

        if (!chat_repository.chatExists(sender_id, receiver_id) && !chat_repository.chatExists(receiver_id, sender_id)) {
            chat_repository.sendMessage(message);
        }
        else {
            int reply_id = chat_repository.getLastMessageId(receiver_id, sender_id);
            chat_repository.sendMessage(message);
            int new_reply_id = chat_repository.getLastMessageId(sender_id, receiver_id);
            chat_repository.linkMessages(new_reply_id, reply_id);
        }

    }

    public List<Integer> getPageFriendsIds(int user_id, int current_page) throws Exception {
        return friends_repository.getPageFriendsIds(user_id, current_page);
    }
}
