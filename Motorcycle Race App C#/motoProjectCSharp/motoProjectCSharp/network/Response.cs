namespace motoProjectCSharp.network;

[Serializable]
public class Response
{
    public bool Success { get; set; }
    public object Data { get; set; }
    public string ErrorMessage { get; set; }

    public Response(bool success, object data, string errorMessage)
    {
        Success = success;
        Data = data;
        ErrorMessage = errorMessage;
    }

    public static Response Ok(object data)
    {
        return new Response(true, data, null);
    }

    public static Response Error(string errorMessage)
    {
        return new Response(false, null, errorMessage);
    }
}