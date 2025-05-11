package org.example.lab6;

public class UserValidator implements IValidator<User> {
    @Override
    public boolean validate(User user) throws ValidationException {
        String exceptions = "";
        if (user.getId() <= 0) exceptions += "Invalid user id!\n";
        if (user.getName().isEmpty()) exceptions += "Invalid user name!\n";
        if (user.getGender().isEmpty()) exceptions += "Invalid user gender!\n";
        if (user.getAge() < 0) exceptions += "Invalid user age!\n";
        if (user.getLocation().isEmpty()) exceptions += "Invalid user location!\n";
        if (user.getDescription().isEmpty()) exceptions += "Invalid user description!\n";
        if (user.getPhone().isEmpty()) exceptions += "Invalid user phone!\n";
        if (!exceptions.isEmpty()) throw new ValidationException(exceptions);
        return true;
    }
}
