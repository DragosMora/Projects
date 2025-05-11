package org.example.lab6;


@FunctionalInterface
public interface IValidator<E> {
    boolean validate(E entity) throws ValidationException;
}
