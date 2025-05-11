using System.Net.Sockets;
using System.Text.Json;
using Avalonia.Data;
using motoProjectCSharp.domain;
using motoProjectCSharp.services;

namespace motoProjectCSharp.network;

public class TeamServiceProxy : ITeamService
{
    private readonly string host;
    private readonly int port;

    public TeamServiceProxy(string host, int port)
    {
        this.host = host;
        this.port = port;
    }

    public void SaveTeam(Team team)
    {
        SendRequest(new Request("SaveTeam", new object[] { team }));
    }

    public Team? FindById(long id)
    {
        try
        {
            using (var client = new TcpClient(host, port))
            using (var stream = client.GetStream())
            using (var writer = new StreamWriter(stream) { AutoFlush = true })
            using (var reader = new StreamReader(stream))
            {
                Console.WriteLine("[Proxy] Connected to server.");

                var request = new Request("FindTeamById", new object[] { id });  // make sure method name matches server
                var requestJson = JsonSerializer.Serialize(request);
                Console.WriteLine("[Proxy] Sending request JSON: " + requestJson);
                writer.WriteLine(requestJson);  // send with newline
                writer.Flush();

                var responseJson = reader.ReadLine();  // wait for newline
                Console.WriteLine("[Proxy] Response JSON received: " + responseJson);

                if (!string.IsNullOrEmpty(responseJson))
                {
                    var response = JsonSerializer.Deserialize<Response>(responseJson);
                    if (response != null && response.Success)
                    {
                        Console.WriteLine($"[Proxy] Success. Data: {response.Data}");
                        var team = JsonSerializer.Deserialize<Team>(response.Data?.ToString());
                        return team;
                    }
                }

                Console.WriteLine("[Proxy] Response was null or unsuccessful.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Proxy] Exception: {ex.Message}");
        }

        return null;
    }

    public List<Team> FindAll()
    {
        try
        {
            using (var client = new TcpClient(host, port))
            using (var stream = client.GetStream())
            using (var writer = new StreamWriter(stream) { AutoFlush = true })
            using (var reader = new StreamReader(stream))
            {
                Console.WriteLine("[Proxy] Connected to server.");

                var request = new Request("FindAllTeams", new object[] { });  // make sure method name matches server
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
                        var teams = JsonSerializer.Deserialize<List<Team>>(response.Data?.ToString());
                        return teams;
                    }
                }

                Console.WriteLine("[Proxy] Response was null or unsuccessful.");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[Proxy] Exception: {ex.Message}");
        }
        
        return new List<Team>();
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