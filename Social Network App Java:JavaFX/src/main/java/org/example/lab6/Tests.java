package org.example.lab6;

import java.util.List;
import java.util.Optional;

public class Tests {

    private void domain_tests() throws Exception {
        User user1 = new User(1001, "Alexandru Pop", "M", 22, "Bucharest, Romania", "I love cooking!", "+40711925301");
        assert user1.getId() == 1001;
        assert user1.getName().equals("Alexandru Pop");
        assert user1.getGender().equals("M");
        assert user1.getAge() == 22;
        assert user1.getLocation().equals("Bucharest, Romania");
        assert user1.getDescription().equals("I love cooking!");
        assert user1.getPhone().equals("+40711925301");
        assert user1.toString() != null;
    }

    private void validation_tests() throws Exception {
        User user_invalid = new User(-100, "", "", -100, "", "", "");
        UserValidator validator = new UserValidator();
        try {
            validator.validate(user_invalid);
        }
        catch (Exception e) {
            assert true;
        }
        User user1 = new User(1001, "Alexandru Pop", "M", 22, "Bucharest, Romania", "I love cooking!", "+40711925301");
        assert validator.validate(user1);
    }

    private void repo_tests() throws Exception {
        UserValidator validator = new UserValidator();
        InMemoryRepo<Integer, User> repo1 = new InMemoryRepo<>(validator);
        User user1 = new User(1001, "Alexandru Pop", "M", 22, "Bucharest, Romania", "I love cooking!", "+40711925301");
        User user2 = new User(1002, "Mihai Pop", "M", 46, "Bucharest, Romania", "I love music!", "+40782900122");
        repo1.save(user1);
        repo1.save(user2);
        assert repo1.size() == 2;
        repo1.delete(user1.getId());
        repo1.delete(user2.getId());
        assert repo1.size() == 0;

        repo1.save(user1);
        assert repo1.save(user1).orElseThrow().equals(user1);

        repo1.delete(user1.getId());
        assert repo1.delete(user1.getId()).isEmpty();

        repo1.save(user1);
        Optional<User> optionalUser = repo1.findOne(user1.getId());
        User newUser = optionalUser.orElseThrow();
        assert newUser.getName().equals("Alexandru Pop");

        newUser.setName("Mihai Pop");
        newUser.setGender("M");
        newUser.setAge(23);
        newUser.setLocation("Barcelona, Spain");
        newUser.setDescription("I love music!");
        newUser.setPhone("+34710029377");
        Optional<User> optionalUser2 = repo1.update(newUser);
        assert optionalUser2.isEmpty();
    }

    public void service_tests() throws Exception {
        UserValidator validator = new UserValidator();
        DatabaseRepo repo = new DatabaseRepo("jdbc:postgresql://localhost:5432/SocialNetwork", "postgres", "MyStrongPassword123$", validator);
        DatabaseFriendshipRepo friendship_repo = new DatabaseFriendshipRepo("jdbc:postgresql://localhost:5432/SocialNetwork", "postgres", "MyStrongPassword123$");
        DatabaseRequestsRepo requests_repo = new DatabaseRequestsRepo("jdbc:postgresql://localhost:5432/SocialNetwork", "postgres", "MyStrongPassword123$");
        DatabaseChatRepo chat_repo = new DatabaseChatRepo("jdbc:postgresql://localhost:5432/SocialNetwork", "postgres", "MyStrongPassword123$");
        Service service = new Service(repo, friendship_repo, requests_repo, chat_repo);
        service.store(1001, "Alexandru Pop", "M", 22, "Bucharest, Romania", "I love cooking!", "+40711925301");
        //assert service.size() == 1;
        service.remove(1001);
        //assert service.size() == 0;
        service.store(1001, "Alexandru Pop", "M", 22, "Bucharest, Romania", "I love cooking!", "+40711925301");
        service.store(1002, "Mihai Pop", "M", 46, "Bucharest, Romania", "I love music!", "+40782900122");
        //assert service.size() == 2;
        service.addFriend(1001, 1002);
        Optional<User> optionalUser = repo.findOne(1001);
        User user1 = optionalUser.orElseThrow();
        assert service.friendCount(user1.getId()) == 1;
        Optional<User> optionalUser2 = repo.findOne(1002);
        User user2 = optionalUser2.orElseThrow();
        assert service.friendCount(user1.getId()) == 1;

        List<User> friends = service.getFriends(user1.getId());
        assert friends.size() == 1;

        service.removeFriend(user1.getId(), user2.getId());
        assert service.friendCount(user1.getId()) == 0;
        assert service.friendCount(user2.getId()) == 0;

        service.addFriend(user1.getId(), user2.getId());
        assert service.communitiesCount() == 1;
        assert service.mostSociable().size() == 2;
    }

    public void run_all_tests() throws Exception {
        domain_tests();
        validation_tests();
        repo_tests();
        service_tests();

    }

}
