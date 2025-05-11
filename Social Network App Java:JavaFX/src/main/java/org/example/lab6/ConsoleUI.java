package org.example.lab6;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Scanner;

public class ConsoleUI {
    private final Service service;

    public ConsoleUI(Service service) {
        this.service = service;
    }

    public void run() throws Exception {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("> ");
            String input = scanner.nextLine();
            if (input.equals("exit")) {
                scanner.close();
                return;
            }
            try {
                String[] parts = input.split(" ");
                if (parts[0].equals("help")) {
                    System.out.println("commands: help, store, remove, list, search, befriend, unfriend, friends, friend_number, communities, most_sociable, exit");
                }
                if (parts[0].equals("store")) {
                    int id = Integer.parseInt(parts[1]);
                    String name = parts[2];
                    String gender = parts[3];
                    int age = Integer.parseInt(parts[4]);
                    String location = parts[5];
                    String description = parts[6];
                    String phone = parts[7];
                    service.store(id, name, gender, age, location, description, phone);
                    System.out.println("User stored successfully!");
                }
                if (parts[0].equals("remove")) {
                    int id = Integer.parseInt(parts[1]);
                    service.remove(id);
                    System.out.println("User deleted successfully!");
                }
                if (parts[0].equals("list")) {
                    Iterable<User> optional_list = service.getAll();
                    List<Object> list = new ArrayList<>();
                    optional_list.forEach(list::add);
                    System.out.println("User list:");
                    list.forEach(System.out::println);
                }
                if (parts[0].equals("search")) {
                    int id = Integer.parseInt(parts[1]);
                    Optional<User> optional_user = service.search(id);
                    User user = optional_user.orElseThrow();
                    System.out.println(user);
                }
                if (parts[0].equals("befriend")) {
                    int id1 = Integer.parseInt(parts[1]);
                    int id2 = Integer.parseInt(parts[2]);
                    service.addFriend(id1, id2);
                    System.out.println("Friend added successfully!");
                }
                if (parts[0].equals("unfriend")) {
                    int id1 = Integer.parseInt(parts[1]);
                    int id2 = Integer.parseInt(parts[2]);
                    service.removeFriend(id1, id2);
                    System.out.println("Friend removed successfully!");
                }
                if (parts[0].equals("friends")) {
                    int id1 = Integer.parseInt(parts[1]);
                    List<User> friends = service.getFriends(id1);
                    System.out.println("Friend list:");
                    friends.forEach(System.out::println);
                }
                if (parts[0].equals("friend_number")) {
                    int id1 = Integer.parseInt(parts[1]);
                    int nr = service.friendCount(id1);
                    System.out.println("Number of friends: " + nr);
                }
                if (parts[0].equals("communities")) {
                    int c = service.communitiesCount();
                    System.out.println("Number of communities: " + c);
                }
                if (parts[0].equals("most_sociable")) {
                    List<Object> friends = service.mostSociable();
                    System.out.println("Most sociable list:");
                    friends.forEach(System.out::println);
                }
            }
            catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Not enough arguments!");
            }
            catch (NullPointerException e) {
                System.out.println("Invalid arguments!");
            }
            catch (RepoException | ValidationException | FriendException | RuntimeException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
