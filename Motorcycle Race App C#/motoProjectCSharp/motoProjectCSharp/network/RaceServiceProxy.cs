using System.Net.Sockets;
using System.Text.Json;
using Avalonia.Data;
using motoProjectCSharp.domain;
using motoProjectCSharp.services;

namespace motoProjectCSharp.network;

public class RaceServiceProxy : IRaceService
{
    private readonly string host;
    private readonly int port;

    public RaceServiceProxy(string host, int port)
    {
        this.host = host;
        this.port = port;
    }

    public void SaveRace(Race race)
    {
        SendRequest(new Request("SaveRace", new object[] { race }));
    }

    public Race? FindById(long id)
    {
        var response = SendRequest(new Request("FindRaceById", new object[] { id }));
        if (response?.Success == true && response.Data is JsonElement element)
        {
            var race = JsonSerializer.Deserialize<Race>(element.GetRawText());
            return race;
        }

        return null;
    }

    public List<Race> FindAll()
    {
        try
        {
            using (var client = new TcpClient(host, port))
            using (var stream = client.GetStream())
            using (var writer = new StreamWriter(stream) { AutoFlush = true })
            using (var reader = new StreamReader(stream))
            {
                Console.WriteLine("[Proxy] Connected to server.");

                var request = new Request("FindAllRaces", new object[] { });  // make sure method name matches server
                var requestJson = JsonSerializer.Serialize(request);
                Console.WriteLine("[Proxy] Sending request JSON: " + requestJson);
                writer.WriteLine(requestJson);  // send with newline
                writer.Flush();

                var responseJson = reader.ReadLine();  // wait for newline
                Console.WriteLine("[Proxy] Response JSON received: " + responseJson);

                if (!string.IsNullOrEmpty(responseJson))
                {
                    var response = JsonSerializer.Deserialize<Response>(responseJson);
                    if (response?.Success == true)
                    {
                        var races = JsonSerializer.Deserialize<List<Race>>(response.Data?.ToString());
                        return races;
                    }
                }

                Console.WriteLine("[Proxy] Response was null or unsuccessful.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Proxy] Exception: {ex.Message}");
        }
        
        return new List<Race>();
    }
    
    //la fel ca mai sus si pentru celelalte din Teams si cele de aici care au ramas

    public void SignUpParticipant(Participant participant, long raceId, long participantTeamId)
    {
        try
        {
            using (var client = new TcpClient(host, port))
            using (var stream = client.GetStream())
            using (var writer = new StreamWriter(stream) { AutoFlush = true })
            using (var reader = new StreamReader(stream))
            {
                Console.WriteLine("[Proxy] Connected to server.");

                var request = new Request("SignUpParticipant", new object[] { participant, raceId, participantTeamId });  // make sure method name matches server
                var requestJson = JsonSerializer.Serialize(request);
                Console.WriteLine("[Proxy] Sending request JSON: " + requestJson);
                writer.WriteLine(requestJson);  // send with newline
                writer.Flush();

                var responseJson = reader.ReadLine();  // wait for newline
                Console.WriteLine("[Proxy] Response JSON received: " + responseJson);

                if (!string.IsNullOrEmpty(responseJson))
                {
                    var response = JsonSerializer.Deserialize<Response>(responseJson);
                    if (response?.Success == true)
                    {
                        Console.WriteLine("[Proxy] Response was successful.");
                    }
                }

                Console.WriteLine("[Proxy] Response was null or unsuccessful.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Proxy] Exception: {ex.Message}");
        }
    }

    private Response? SendRequest(Request request)
    {
        try
        {
            using var client = new TcpClient(host, port);
            using var stream = client.GetStream();

            JsonSerializer.Serialize(stream, request);
            return JsonSerializer.Deserialize<Response>(stream);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
            return null;
        }
    }
}