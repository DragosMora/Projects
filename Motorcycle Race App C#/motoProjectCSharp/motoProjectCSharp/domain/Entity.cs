namespace motoProjectCSharp.domain;

[Serializable]
public class Entity<T>
{
    public T Id { get; }

    public Entity(T entityId)
    {
        Id = entityId;
    }

    public override string ToString()
    {
        return Id.ToString();
    }
}
