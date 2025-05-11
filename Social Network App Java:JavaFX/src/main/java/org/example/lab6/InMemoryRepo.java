package org.example.lab6;


import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class InMemoryRepo<ID, E extends Entity<ID>> implements Repository<ID, E> {
    private Map<ID, E> storage = new HashMap<>();
    private final IValidator<E> validator;

    public InMemoryRepo(IValidator<E> validator) {
        this.validator = validator;
    }

    @Override
    public Optional<E> findOne(ID id) {
        if (id == null) throw new IllegalArgumentException("Id cannot be null!");
        return Optional.ofNullable(storage.get(id));
    }

    @Override
    public Iterable<E> findAll() {
        return storage.values();
    }

    @Override
    public Optional<E> save(E entity) throws Exception {
        if (entity == null) throw new IllegalArgumentException("Entity cannot be null!");
        validator.validate(entity);
        return Optional.ofNullable(storage.putIfAbsent(entity.getId(), entity));
    }

    @Override
    public Optional<E> delete(ID id) {
        if (id == null) throw new IllegalArgumentException("Id cannot be null!");
        return Optional.ofNullable(storage.remove(id));
    }

    @Override
    public Optional<E> update(E entity) throws Exception {
        if (entity == null) throw new IllegalArgumentException("Entity cannot be null!");
        validator.validate(entity);
        if (!storage.containsKey(entity.getId())) {
            return Optional.of(entity);
        }
        storage.put(entity.getId(), entity);
        return Optional.empty();
    }

    public Integer size() {
        return storage.size();
    }
}
