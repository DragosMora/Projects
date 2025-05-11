namespace motoProjectCSharp.network;

[Serializable]
public class Request
{
    public string MethodName { get; set; }
    public object[] Params { get; set; }

    public Request(string methodName, object[] parameters)
    {
        MethodName = methodName;
        Params = parameters;
    }

    public Request()
    {
    }
}